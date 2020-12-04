import os
import csv

employee_csv = os.path.join('Resources', 'employee_data_final.csv')

with open('employee_csv_HW', 'w', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# field names
fields  = ['Employee ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

# data rows of csv file
rows =[['232', 'John', 'Mathews','02/24/1991','***.**.9165','ND'],
       ['533', 'Natasha','Moore','11/19/1978','***.**.7469','ME'],
       ['', 'Amanada', 'Douglas','01/08/1990','***.**.6971','ID'],
       ['189', 'Heather','Andrews','08/11/1976','***.**.1797','VT'],
       ['284', 'Daniel', 'Hernandez','07/22/1976','***.**.7473','CO'],
       ['512', 'Danny', 'Pena','01/31/1978','***.**.9878','MN'],
       ['126', 'Gary', 'Knight','03/08/1994','***.**.1242','AR'],
       ['556', 'Robin', 'Carroll','10/14/1972','***.**.7194','CA'],
       ['595', 'Michelle','Dickerson','02/08/1984','***.**.2817','TN'],
       ['191', 'Kimberly','Gallegos','08/05/1972','***.**.7563','OR'],
       ['55', 'Morgan', 'Parker','01/30/1986','***.**.4320','TN'],
       ['623', 'Mason', 'Rhodes','01/28/1977','***.**.4767','MD'],
       ['426', 'Amy', 'Griffin','02/18/1973','***.**.1946','MA'],
       ['535', 'Danielle', 'House','04/16/1975','***.**.9308','ME'],
       ['399', 'Charles', 'Greene','11/28/1992','***.**.2935','KY'],
       ['33', 'Nicholas', 'Martinez','04/5/1979','***.**.1689','LA'],
       ['302', 'Tracey', 'Meadows','01/12/1988','***.**.6175','RI'],
       ['325', 'Joseph', 'Estrada','03/29/1984','***.**.2571','PA'],
       
    ]



with open("employee_csv",'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)


print("completed")
    
        
