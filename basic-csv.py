import csv

def write_csv(datalist):
    with open('data_new.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def read_csv():
    with open('data_new.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

data = read_csv()
print(data)
#data = ['Americano',55,'8.00 น.']
#write_csv(data)