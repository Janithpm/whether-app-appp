import requests


    

def main():
    print("Hello Mister!")
    x = requests.get('http://api.weatherapi.com/v1/current.json?key=baf9c1228bc647b19ab161704210710&q=London&aqi=no')
    print("hello here is the wheater for London n' stuff" , x.text)

if __name__ == "__main__":
    main()

