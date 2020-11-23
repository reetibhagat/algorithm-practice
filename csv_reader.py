import csv

filtered_list = []

with open('heart.csv', newline='') as csv_heart:
    csv_data = csv.reader(csv_heart , delimiter=",")
    for row in csv_data:
        if row[13] == "1":
            filtered_list.append(row)
print(filtered_list)

