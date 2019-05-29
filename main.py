import requests


def get_coordinates_as_svy21(lat, lon):
    url = "https://developers.onemap.sg/commonapi/convert/4326to3857"
    response = requests.request("GET", url, params={"latitude":lat,"longitude":lon})
    
    return response.text

result = get_coordinates_as_svy21(lat=1.319728905, lon=103.8421581)
print(result)
