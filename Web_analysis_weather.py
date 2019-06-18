import requests
city=input("Enter your city name here: ")
country=input("Enter your country name here: ")
text='http://api.openweathermap.org/data/2.5/weather?q='+city+','+country+'&APPID=f0b386f7312adeafd3d32704bba51b24'
r = requests.get(text)
print(r.text.strip())
climate=r.text.find('main')
climate_res=r.text[climate.text()]
print(climate_res)
degree = r.text.find('temp')
degree_res = r.text[degree+6:degree+9]
term = "clouds"
if term in climate_res.lower():
    print("It is cloudy")
    print(str(int(degree_res)-273)+" C")
elif "rain" in climate_res.lower():
    print("It's Raining")
    print(str(int(degree_res)-273)+" C")
elif "haze" in climate_res.lower():
    print("It's haze")
    print(str(int(degree_res)-273)+" C")

else:
    print("It's hot outside")
    print(str(int(degree_res)-273)+" C")
