import requests
import pandas as import pd


#Weather API - DMI
#User link https://dmiapi.govcloud.dk/?session_state=3a0a28b6-cef5-45ce-91dd-c1d8a0250039&code=299a4443-bb5f-4318-b74a-c5bfee0308a0.3a0a28b6-cef5-45ce-91dd-c1d8a0250039.8a59ec03-4512-4167-b602-7052c700f7c2#!/user

weather_url = "https://dmigw.govcloud.dk/metObs/v1/observation"
weather_apikey = "1e8ba0a3-e4f3-4646-aaea-3923370e52bc"
weather_params = {
    "api-key": weather_apikey,
    "stationId": "06174", #30414
    "limit": 10
}

def get_weather(url, params):
    r = requests.get(url, params=params)
    df = pd.DataFrame(r.json())
    df['time'] = pd.to_datetime(df['timeObserved'], unit='us')
    df = df.drop(['_id', 'timeCreated', 'timeObserved'], axis=1)
    df.index = df['parameterId']
    return df

df = get_weather(weather_url, weather_params)
print(df)