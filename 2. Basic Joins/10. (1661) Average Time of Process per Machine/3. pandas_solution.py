--Schema
data = [[0, 0, 'start', 0.712], [0, 0, 'end', 1.52], [0, 1, 'start', 3.14], [0, 1, 'end', 4.12], [1, 0, 'start', 0.55], [1, 0, 'end', 1.55], [1, 1, 'start', 0.43], [1, 1, 'end', 1.42], [2, 0, 'start', 4.1], [2, 0, 'end', 4.512], [2, 1, 'start', 2.5], [2, 1, 'end', 5]]
activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp']).astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})

--Solution
import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity_end = activity[activity['activity_type'] == 'end']
    activity_filtered = activity[activity['activity_type'] != 'end']
    result = pd.merge(activity_end, activity_filtered, how='inner', on=['machine_id', 'process_id'])
    result['processing_time'] = result['timestamp_x'] - result['timestamp_y']
    result = (result.groupby('machine_id')['processing_time'].mean().reset_index())
    result['processing_time'] = result['processing_time'].round(3)
    return result

