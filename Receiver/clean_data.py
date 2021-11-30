#!/usr/bin/python3
import datetime
import pytz
def Clean():
  Data=[]

  with open("./raw_data.txt","r") as file:
    datos = file.readlines()
    for info in datos:
      x=info.split(',')
      try:
        float(x[0])
      except ValueError:
        pass
      else:
        Data.append(x)
  not_duplicates_plates=[]
  not_duplicates_data=[]
  for i in range(len(Data)):
    if Data[i][2] not in not_duplicates_plates:
      not_duplicates_plates.append(Data[i][2])
      not_duplicates_data.append(Data[i])

  #Delete raw_data content
  erase=open("./raw_data.txt","w")
  erase.close()
  timezone = pytz.timezone('America/Bogota') 
  today=datetime.datetime.now(timezone).strftime("%d%m%y")
  file_name=f'./data{today}.txt'
  with open(file_name,"a") as file:
    for pos in not_duplicates_data:
      string = str(pos).replace('[','').replace(']','').replace('\'','')
      string = string.replace('\\', '').replace('n', '')
      file.write(string+"\n")

if __name__=='__main__':
  Clean()