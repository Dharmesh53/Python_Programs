import csv
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[1] != "temp":
            temp.append(int(row[1]))

    print(temp)

import pandas as pd
# data = pd.read_csv('weather_data.csv')
# print(data.to_dict())
# print(data["temp"])
#
# print(type(data))
# print(type(data["temp"]))
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(data["temp"].mean())
# print(data.temp.max())
# print(data.temp.min())
#
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

data_dict = {
    'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'},
    'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24},
    'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
}

data = pd.DataFrame(data_dict)
data.to_html("weather_data.html")