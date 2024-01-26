# # data = []
# # with open("weather_data.csv", mode='r') as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv", mode='r') as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #
# #     print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# print(data.to_dict())
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
#
# # By series we can calculate mean and max
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Colume from DataFrame
# print(data["condition"])
# print(data.condition)
#
# #Get Data in Row
# print(data[data.day == "Monday"])
#
# #Get max Temp Row
# print(data[data.temp == (data.temp).max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp)
#
# print(monday.temp[0])
# import pandas
#
# #Create a dataframe from scratch
# data_dict = {
#     "students" : ["Devesh", "Abhinesh", "Pranjal"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240125.csv")
grey_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")