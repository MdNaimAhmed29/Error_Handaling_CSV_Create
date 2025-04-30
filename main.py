"""
file create -> open()
w for write
r for read
use (with) -> it will automatically colse the  file after read or write

file rename or delete -> import os
os.rename()
CSV file create,read, write
JSON

#import os

#with open("new folder/demo.text","w") as file:
    #file.write("Hello World")
    #print("Success")

#with open("new folder/demo.text","r") as file:
    #print(file.read())


#os.rename("demo.text","R-W-Re-De.text")
#os.remove("new folder/demo.text")



os.mkdir("new folder")
os.listdir(".")
#os.rename("new folder","New Folder")
#os.rmdir("new folder")
os.listdir("new folder")
"""

"""import csv


myResults = [
    ['Name', 'Subject', 'Group', 'Language'],
    ['Naim', 'CSE', 'Science', 'Bangla'],
    ['Naim', 'CSE', 'Science', 'Bangla'],
    ['Naim', 'CSE', 'Science', 'Bangla'],
    ['Naim', 'CSE', 'Science', 'Bangla'],
    ['Naim', 'CSE', 'Science', 'Bangla'],
    ['Naim', 'CSE', 'Science', 'Bangla']
]

with open("report.csv",'w') as file:
    writer = csv.writer(file)
    writer.writerows(myResults)
    print("Completed")


results = []
with open("report.csv",'r') as file:
    reader = csv.reader(file)
    for row in reader:
        results.append(row)
print(results)




person = {
    "Name": "Naim",
    "Age": 34,
    "Subject": "CSE",
    "Group": "Science",
    "Language": "English",
    "Titles": ["C","Python","Django"]
}

#personjson = json.dumps(person,indent=4)
#print(personjson)

#with open("report.json","w") as file:
    #json.dump(person,file,indent=4)
    #print("Completed")

"""

import json

try:
    with open("report.json", "r") as file:
        person = json.load(file)
        print(person)

        print(personjson)

except Exception as Error:
    print(Error)

finally:
    print("Completed....")

#import zipfile


#with zipfile.ZipFile("report.zip","w") as myzip:
    #myzip.write("report.csv")
    #myzip.write("report.json")


#with zipfile.ZipFile("report.zip","r") as myzip:
    #myzip.extractall()
    #extracted_file = myzip.namelist()

#import shutil

#shutil.make_archive("new folder", "zip", "new folder")
