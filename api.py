
import requests
from PIL import Image 
str=input("enter the symbol")
r = requests.get('https://api.polygon.io/v1/open-close/'+str+'/2020-10-14?adjusted=true&apiKey=ABjviIuq_vEeG4G0_Kwi8hAZlX81NiJU')
r1 = requests.get('https://api.polygon.io/v3/reference/tickers/'+str+'?apiKey=ABjviIuq_vEeG4G0_Kwi8hAZlX81NiJU') #info
json_object = r.json()
json_object1 = r1.json()
print(json_object['symbol'],json_object['high'])
# print(json_object1)


#ind.html for image in api