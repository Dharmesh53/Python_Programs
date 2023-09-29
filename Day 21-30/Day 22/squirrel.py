import pandas as pd

data = pd.read_csv("squirrel_data.csv")
gray = len(data[data["Primary Fur Color"] == 'Gray'])
black = len(data[data["Primary Fur Color"] == 'Black'])
red = len(data[data["Primary Fur Color"] == 'Red'])

data_dict = {
    "Fur Color": ['Gray', 'Black', 'Red'],
    "Count": [gray, black, red]
}

df = pd.DataFrame(data_dict)
df.to_json("squirrel_data.json")
