import requests
import json


    

def main():
    print("Hello Mister!")
    city = input("Enter City (I.E) London ")
    print("City you chosen" , city);
    url1 = 'http://api.weatherapi.com/v1/current.json?key=baf9c1228bc647b19ab161704210710&q='
    url2 = '&aqi=no'
    url = url1  + city + url2
    print(url)
    x = requests.get(url)
    print("Loaded Json" , "Result" , x.text)
    x = x.text
    x = json.loads(x)
    print("hello here is the wheater for London n' stuff" , x)

if __name__ == "__main__":
    main()

