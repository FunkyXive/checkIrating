from iracingdataapi.client import irDataClient
from getpass import getpass
import json
import csv
USERNAME = input("Enter your username: ")
PASSWORD = getpass()
membersToUseFormulaRacing = []
iratingsToAverage = []
print('Authenticating...')
idc = irDataClient(username=USERNAME, password=PASSWORD)
print('Authenticated')

print("Reading file")
with open('members.csv', newline='') as csvfile:
    file = csv.reader(csvfile, delimiter=',', quotechar='|')
    print("File read")
    print('Calculating')
    for members in file:
        for member in members:
            currentMemberName = idc.member_profile(
                cust_id=member)['member_info']['display_name']
            for category in idc.member_profile(cust_id=member)['member_info']['licenses']:
                if member in membersToUseFormulaRacing and category['category'] == "formula_car":
                    print(
                        f"{currentMemberName}, your irating in Formula racing is: {category['irating']}")
                    iratingsToAverage.append(int(category['irating']))
                elif category['category'] == "sports_car":
                    print(
                        f"{currentMemberName}, your irating in Sports car is: {category['irating']}")
                    iratingsToAverage.append(int(category['irating']))

        print(f"Counted {len(members)} members with a total of {sum(iratingsToAverage)} irating for an average of {sum(iratingsToAverage)/len(members)}")
        #tester lige noget shit her
