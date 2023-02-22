import csv

#Set up variables to store financial data
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
change_profit_loss = 0
greatest_increase = ['', 0]
greatest_decrease = ['', 999999999999]

#Open the CSV file containing the financial data
with open('budget_data.csv', 'r')as file:
    reader = csv.reader(file)

    #Skip the header row
    header = next(reader)

    #Loop through each row in the CSV file
    for row in reader:

        #Increment the total number of months
        total_months += 1

#Add the current profit/loss to the total
total_profit_loss += int(row[1])

#Calculate the change in profit/loss from the previous month
if total_months > 1:
    change_profit_loss = int(row[1]) - prev_profit_loss

#Update the previous profit/loss to the current one
prev_profit_loss = int(row[1])

#Check if this change is the greatest increase or decrease
if change_profit_loss > greatest_increase[1]:
    greatest_increase[0] = row[0]
    greatest_increase[1] = change_profit_loss

if change_profit_loss < greatest_decrease[1]:
    greatest_decrease[0] = row[0]
    greatest_decrease[1] = change_profit_loss

#Calculate the average change in profit/loss
average_change = round((total_profit_loss / total_months), 2)

#Print out the financial analysis
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
