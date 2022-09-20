# import csv
#
# with open("weather_data.csv") as wFile:
#     dataList = csv.reader(wFile)
#     temperatures = []
#     for row in dataList:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# ddir = data.to_dict()
# all_temps = data['temp'].to_list()
#
# #avg
# print(sum(all_temps)/len(all_temps))
#
# #max temp
# max_temp_rec = data[data.temp == data.temp.max()]
# print(max_temp_rec['temp'])

#datafram from dir

# data_dir = {
#     'studs': ['J', 'S', 'K'],
#     'mks': [10, 20, 30]
# }
#
# data_frame = pandas.DataFrame(data_dir)
#
# print(data_frame)

#squirell data
#X,Y,Unique Squirrel ID,Hectare,Shift,Date,Hectare Squirrel Number,Age,Primary Fur Color,Highlight Fur Color,Combination of Primary and Highlight Color,Color notes,Location,Above Ground Sighter Measurement,Specific Location,Running,Chasing,Climbing,Eating,Foraging,Other Activities,Kuks,Quaas,Moans,Tail flags,Tail twitches,Approaches,Indifferent,Runs from,Other Interactions,Lat/Long
squirrel_dataframe = pandas.read_csv('squirell_data.csv')
#grey squirrel count
print(len(squirrel_dataframe[squirrel_dataframe['Primary Fur Color'] == 'Gray']))