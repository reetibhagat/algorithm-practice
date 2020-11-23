import json
import csv
from datetime import date, datetime
import datetime as dt


def take_priority(elem):
    return elem[6]


with open('banners.json', 'r') as json_file:
    json_banners_List = json.load(json_file)

print(json_banners_List)

with open('campaigns.csv', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=",")
    fields = next(csv_data)
    # csv_data.sort(key=take_priority, reverse=True)

    campaign_sorted_list = []
    for row in csv_data:
        campaign_sorted_list.append(row)
    campaign_sorted_list.sort(key=take_priority, reverse=True)

    campaign_filtered_list = []
    for row in campaign_sorted_list:
        if len(campaign_filtered_list) > 10:
            break
        end_date_time = datetime.fromisoformat(row[3])
        if row[5] == "1" and end_date_time > datetime.today():
            campaign_filtered_list.append(row)
    print(campaign_filtered_list)
    for campaign in campaign_filtered_list:
        count = 0
        for banner in json_banners_List:
            if count > 1:
                break
            banner_end_date_time = dt.datetime.strptime(banner['endDate'], "%Y/%m/%d")

            if banner['campaignId'] == int(campaign[0]) and banner_end_date_time > datetime.today():
                print('campaignId = ', campaign[0])
                print('bannerId = ', banner['bannerId'])
                count += 1
        print('------------------------')
