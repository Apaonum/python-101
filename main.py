import csv

############################## CSV Files ##################################
def write_csv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def read_csv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

#data = readcsv()
#print(data)
data = ['Caramel-Machiato',105,'09.00 AM.']
write_csv(data)