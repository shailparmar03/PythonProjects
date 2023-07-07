# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()  # outputs a list of the data
#     print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)  # returns an object
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv('./weather_data.csv')
# print(type(data))
# print(data['temp'])
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
#
# print(data['temp'].max())
#
# print(data[data.day == 'Monday'] )
# print(data[data.temp == data.temp.max()])
#
#
# # create dataframe from scratch
# #
# my_dict={
#     "students" : ['Amy', 'James', 'Angela'],
#     'scores' : [76,56,65]
# }
#
# data=pandas.DataFrame(my_dict)
# print(data)
# data.to_csv('new_data.csv')

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])


print(gray_squirrels_count)
print(cinnamon_squirrels_count)
print(black_squirrels_count)

data_dict={
    'Fur Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count' : [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrels_count.csv')