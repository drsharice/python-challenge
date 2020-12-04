import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')



total_months = 0
previous_row_pl = 0
num_changes = 0
list_change = []
list_month = []
total_profit_losses = 0
row_index_profit_loss = 1

#Open and read csv
with open(budget_csv) as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter=",")
    csv_reader_object = csv.reader(csv_file)
    if csv.Sniffer().has_header:
        next(csv_reader_object)
    for row in csv_reader_object:
        total_months +=1
        float_profit_losses = float(row[row_index_profit_loss])
        total_profit_losses += float_profit_losses
        change_pl = int(row[1]) - int(previous_row_pl)
        list_change.append(change_pl)
        previous_row_pl = row [1]
        list_month.append(row[0])
        num_changes += 1

print("Financial Analysis")
print("------------------")
    
str_total_months = str(total_months)
print("Total Months: " +str_total_months)

str_total_profit_losses = str(total_profit_losses)
print("Total: $" +str_total_profit_losses)


average_change = (sum(list_change)/num_changes)
str_average_change = str(average_change)
print("Just Average $"+str_average_change)

increase_change =(max(list_change))
index_change = list_change.index(increase_change)
greatest_month = list_month [index_change]
str_increase_change = str(increase_change)

decrease_change =(min(list_change))
l_index_change = list_change.index(decrease_change)
least_month = list_month[l_index_change]
str_decrease_change = str(decrease_change)
print("Greatest Increase in Profits:" +greatest_month+" $" +str_increase_change)
print("Greatest Decrease in Profits:" +least_month+" $"+str_decrease_change)
                


