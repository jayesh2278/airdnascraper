import requests
import json

url = "https://api.airdna.co/v1/market/property_list?access_token=NjYwMTgw|a495e9b28dae4f76af7b8c3e2696cdc3&city_id=71282&start_month=5&start_year=2019&number_of_months=36&currency=native&show_regions=true"

payload={}
headers = {
  'authority': 'api.airdna.co',
  'accept': '*/*',
  'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,gu;q=0.7',
  'dnt': '1',
  'origin': 'https://www.airdna.co',
  'referer': 'https://www.airdna.co/',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

a = json.loads(response.text)

for data in a["properties"]:
  print(data['title'])
