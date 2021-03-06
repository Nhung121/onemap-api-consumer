import time
import requests
import pandas as pd

def get_coordinates_as_svy21(lat, lon):
    try:
        url = "https://developers.onemap.sg/commonapi/convert/4326to3414"
        response = requests.request("GET", url, params={"latitude":lat,"longitude":lon})

        return response.json()    
    except:
        return (0, 0)

# load data
coordinates = pd.read_csv('./data/input_coordinates.csv')

# call onemap api for conversion
for i, coordinate in coordinates.iterrows():
    result = get_coordinates_as_svy21(lat=coordinate['latitude'], lon=coordinate['longitude'])
    print(result)

    coordinates.loc[i, 'Y'] = result['Y']
    coordinates.loc[i, 'X'] = result['X']

    # rate limit
    limit = 250
    if i % limit == 0:
        # UNCOMMENT THE NEXT 3 LINES IF WE NEED TO RATE LIMIT
        # secs_to_sleep = 40
        # print(f'sleep for {secs_to_sleep} secs')
        # time.sleep(secs_to_sleep)

        # save checkpoint 
        _coordinates = coordinates.dropna()
        _coordinates.to_csv(f'./data/output_coordinates-checkpoint-{i}.csv', index=False)
        

coordinates.to_csv(f'./data/output_coordinates-final.csv', index=False)