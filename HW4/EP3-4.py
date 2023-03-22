def writedata():
    with open('data.txt','w',encoding='utf-8') as f:
        f.write('hello world')

def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as f:
        f.writelines(text + '\n')

#adddata('See ya')

def readdata():
    with open('add-data.txt',encoding='utf-8') as f:
        #data = f.readlines() #export data to list
        data = f.read()
        print(data)

readdata()