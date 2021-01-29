import requests
import json


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
import django
django.setup()

from weather.models import Weather


apikey = "52fe4829cee35ef947d9a0119feda4de"
city = "Seoul"

# 앞으로 5일 동안의 3시간 간격 일기예보
api = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}"

k2c = lambda k: k-273.15

url = api.format(city=city, key=apikey)
r = requests.get(url)
data = json.loads(r.text)
print(len(data["list"]))

a =[]
b =[]
c =[]
d =[]
e =[]
f =[]
g =[]
h =[]
for i in range(0,40):
    a.append(data["list"][i]["dt_txt"])
    b.append(data["list"][i]["weather"][0]["description"])
    c.append(k2c(data["list"][i]["main"]["temp_min"]))
    d.append(k2c(data["list"][i]["main"]["temp_max"]))
    e.append(data["list"][i]["main"]["humidity"])
    f.append(data["list"][i]["main"]["pressure"])
    g.append(data["list"][i]["wind"]["deg"])
    h.append(data["list"][i]["wind"]["speed"])

for item in zip(a, b, c, d, e, f, g, h):
    Weather(
        date=item[0],
        desc=item[1],
        temp_min=item[2],
        temp_max=item[3],
        humidity=item[4],
        pressure=item[5],
        deg=item[6],
        speed=item[7]
    ).save()



for i in range(0,40):
    print("+ 도시 =", data["city"]["name"])
    print("| 날짜 =", data["list"][i]["dt_txt"])
    print("| 날씨 =", data["list"][i]["weather"][0]["description"])
    print("| 최저 기온 =", k2c(data["list"][i]["main"]["temp_min"]))
    print("| 최고 기온 =", k2c(data["list"][i]["main"]["temp_max"]))
    print("| 습도 =", data["list"][i]["main"]["humidity"])
    print("| 기압 =", data["list"][i]["main"]["pressure"])
    print("| 풍향 =", data["list"][i]["wind"]["deg"])
    print("| 풍속 =", data["list"][i]["wind"]["speed"])
    print("")




