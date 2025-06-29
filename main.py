import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250629.csv")

count_black = len(data[data["Primary Fur Color"] == "Black"])
count_gray = len(data[data["Primary Fur Color"] == "Gray"])
count_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [count_black, count_gray, count_cinnamon]
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
