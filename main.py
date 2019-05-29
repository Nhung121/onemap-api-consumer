import requests
import pandas as pd

def get_coordinates_as_svy21(lat, lon):
    url = "https://developers.onemap.sg/commonapi/convert/4326to3414"
    response = requests.request("GET", url, params={"latitude":lat,"longitude":lon})

    return response.json()

# load data
coordinates = pd.read_csv('./data/input_coordinates.csv')

# call onemap api for conversion
for i, coordinate in coordinates.iterrows():
    lat = coordinate['latitude']
    lon = coordinate['longitude']

    result = get_coordinates_as_svy21(lat=lat, lon=lon)

    coordinates.loc[i, 'Y'] = result['Y']
    coordinates.loc[i, 'X'] = result['X']

coordinates.to_csv('./data/output_coordinates.csv', index=False)
