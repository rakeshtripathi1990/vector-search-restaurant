# vector-search-restaurant

It is not advised to use this code base straight into production without first conducting enough testing; it is only meant to be used for demo purposes. Customers can search for nearby eateries in this demo by entering their location. The MongoDB Atlas contains the example data. I have also attached the dataset in JSON format and its already embedded with the help of hugging face API.

Note: The attached dataset (docs.restaurant.json) contains more than 15k records, however due to rate limitation only 1st 300 dataset are embedded.

The sample dataset looks like below:
{"_id":{"$oid":"65a7a8bf31d8e5e3bdfb4aa0"},"searched_zipcode":"EC1A 7EB","searched_category":"London_Center","searched_lat":{"$numberDouble":"51.51808898"},"searched_lng":{"$numberDouble":"-0.09922265"},"loc_number":{"$numberInt":"162699"},"address":{"City":"London","FirstLine":"94 Old Street","Postcode":"EC1V 9AY","Latitude":{"$numberDouble":"51.524631"},"Longitude":{"$numberDouble":"-0.093726"}},"cuisines":[{"Name":"Lebanese","SeoName":"lebanese"},{"Name":"Grill","SeoName":"grill"}],"delivery_fee":{"$numberDouble":"2.49"},"delivery_time_raw":"25-40","delivery_time":{"$numberDouble":"32.5"},"service_fee":{"$numberDouble":"0.0"},"distance":{"$numberDouble":"0.5"},"review_count":{"$numberInt":"11"},"review_rating":{"$numberDouble":"4.73"},"RunDate":"2022-04-25 01:01:19","restaurant_name":"Naar Lebanese takeaway","rest_embedding":[{"$numberDouble":"0.05272199958562851"},{"$numberDouble":"-0.018040137365460396"},{"$numberDouble":"0.015452860854566097"},{"$numberDouble":"-0.03143155947327614"},{"$numberDouble":"0.0021594027057290077"},{"$numberDouble":"0.04670470207929611"},{"$numberDouble":"-0.01380916964262724"},{"$numberDouble":"-0.026966340839862823"},{"$numberDouble":"-0.047650787979364395"},{"$numberDouble":"-0.06812593340873718"},{"$numberDouble":"0.03187422826886177"},{"$numberDouble":"-0.10928595811128616"},{"$numberDouble":"-0.03663641959428787"},{"$numberDouble":"-0.05730269476771355"},{"$numberDouble":"-0.005498598795384169"},{"$numberDouble":"-0.06220139563083649"},{"$numberDouble":"0.008997558616101742"},{"$numberDouble":"-0.05608617514371872"},{"$numberDouble":"0.01650460995733738"},{"$numberDouble":"-0.025891801342368126"},{"$numberDouble":"-0.019711945205926895"},{"$numberDouble":"0.06469666212797165"},{"$numberDouble":"0.010315903462469578"},{"$numberDouble":"-0.019438426941633224"},{"$numberDouble":"-0.04903504624962807"},{"$numberDouble":"0.07461261004209518"}]}

I have reduce the no of dimension to make the example more compact and easy to understand.

How to do the setup?
Prerequisits:
1. Python
2. Hugging face [For embedding]
3. MongoDB Database
4. HTML/CSS
5. Javascript

Step 1: Install Python 
Step 2: Pull The CodeBase
Step 3: Install required python dependencies. Such as [django, folium, geocoder, pymongo, crispy-bootstrap5, django-crispy-forms]
Step 4: run the server = python3 manage.py runserver
