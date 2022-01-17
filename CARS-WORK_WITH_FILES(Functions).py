import csv
import json


def cou(country):
    list_car = []
    list_car_2 = []
    with open('cars.csv', 'r', encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=";")

        for i in csv_reader:
            list_car.append(i)

        for line in list_car:
            if country in line:
                list_car_2.append(line)
                list_car_2.sort(key=lambda x:x[0])
    return list_car_2


def save_file(save_format, country, lst):
    with open(f'cars-model_{country}.{save_format}', 'w', encoding='utf-8') as file:
        for car in lst:
            car_tuple = tuple(car)
            if save_format == "txt":
                car = " ".join(car) + "\n"
                txt_file = file.write(car)
            elif save_format == "csv":
                csv_file = csv.writer(file, dialect="excel")
                csv_file.writerow(car_tuple)
            elif save_format == "json":
                json_file = json.dump(lst, file, indent=4)


country_to_enter = input('Enter country :Japan, US, Europe: ')

save_format = input('Enter format: txt; csv; json: ')

save_file(save_format, country_to_enter, cou(country_to_enter))

