--Schema
data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})

--Solution
import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather_date_shifted_back = weather.copy()
    weather_date_shifted_back['recordDate'] = weather_date_shifted_back['recordDate'] - pd.Timedelta(days=1)
    result = pd.merge(weather_date_shifted_back, weather, how='left', on='recordDate')
    result = result[result['temperature_x'] > result['temperature_y']]
    return result[['id_x']].rename(columns={'id_x': 'id'})
