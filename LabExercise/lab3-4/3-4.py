#WAP that reads columns 1,2,3 from emp.csv file and converts them into list of tuples where elements of the tuples are from column 1,2 and 3 respectively
import csv
data=[]
with open('emp.csv', mode='r', newline='') as file:
      reader = csv.reader(file)
      
      for row in reader:
            print(f"{row[0]}, {row[1]},  {row[3]}")

            tuple_data=(row[1], row[2], row[3])
            data.append(tuple_data)

for t in data:
      print(t)