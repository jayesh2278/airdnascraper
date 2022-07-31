import scrapy
import json


class ExampleSpider(scrapy.Spider):
    name = 'example'
    
    start_urls = ['https://api.airdna.co/v1/market/property_list?access_token=NjYwMTgw|a495e9b28dae4f76af7b8c3e2696cdc3&city_id=71282&start_month=5&start_year=2019&number_of_months=36&currency=native&show_regions=true']

    def parse(self, response):
        
        a = json.loads(response.text)

        for data in a["properties"]:

          title = data['title']
          room_type =data['room_type']
          property_type = data["property_type"]
          bedrooms = data["bedrooms"]
          accommodates = data["accommodates"]
          bathrooms = data["bathrooms"]
          reviews = data["reviews"]
          rating = data["rating"]
          days_available = data["days_available"]
          img_cover = data["img_cover"]
          occ = data["occ"]
          revenue = data["revenue"]

          yield{
              'title': title,
              'room_type': room_type,
              'property_type': property_type,
              'bedrooms' : bedrooms,
              'accommodates' : accommodates,
              'bathrooms' :bathrooms,
              'reviews' : reviews,
              'reviews': reviews,
              'rating' : rating,
              'days_available' : days_available,
              'img_cover' : img_cover,
              'occ' : occ,
              'revenue' : revenue,
          }
