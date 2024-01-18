from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm
import folium
import geocoder
import pymongo
import requests
import json

# credentials hugging face and MongoDB
client = pymongo.MongoClient(
    "mongodb+srv://mongoadmin:passwordone@searchdemo.dgvwz.mongodb.net/")
db = client.docs
collection = db.restaurant

hf_token = "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"
embedding_url = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"

# generate embedding


def generate_embedding(text: str) -> list[float]:
    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": str(text)})

    if response.status_code != 200:
        raise ValueError(
            f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = SearchForm()
    address = Search.objects.all().last()
    print(address)
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    if lat == None or lng == None:
        address.delete()
        return HttpResponse('You address input is invalid')

    # Create Map Object
    m = folium.Map(location=[51.51808898, -0.09922265], zoom_start=12)

    folium.Marker([lat, lng], tooltip='Click for more',
                  popup=address).add_to(m)
    
    results = collection.aggregate([
        {"$vectorSearch": {
            "queryVector": generate_embedding(address),
            "path": "rest_embedding",
            "numCandidates": 300,
            "limit": 4,
            "index": "vector_index",
        }}
    ])

    final_res = []
    for document in results:
        # print(
        #     f'Restaurant Name: {document["restaurant_name"]},\nID: {document["_id"]}\n')
        final_res.append({
            'Restaurant Name': document["restaurant_name"],
            'ID': document["_id"]
        })


    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'list': final_res, 
        'form': form,
    }

    return render(request, 'index.html', context)
