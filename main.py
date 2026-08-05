import requests

r = requests.get("https://countries.dev/countries")
countries = r.json()

name = input("Enter a country: ")

for c in countries:
    print(c["name"], c["population"], c["region"])
