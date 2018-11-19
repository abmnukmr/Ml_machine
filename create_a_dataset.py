import csv
import random


def create_data_set(file_name, length):
    with open(file_name + '.csv', 'a', newline='') as f:
        writer = csv.writer(f)

        list_of_data = []

        for x in range(length):
            y = random.randint(-10000, 10000)
            tupless = (y, y + 2)
            list_of_data.append(tupless)

        writer.writerows(list_of_data)
        print("successfully created")

create_data_set('test',  5000)
create_data_set('train', 50000)
