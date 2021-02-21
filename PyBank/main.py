import os

# Module for reading CSV files
import csv
total_month = 0
total_rev = 0
delta = 0
previous = 0
total_delta = 0
greatest_inc = 0
greatest_inc_mon = ""
greatest_dec = 99999999999
greatest_dec_mon = ""

csvpath = os.path.join('budget_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
      total_month = total_month +1
      total_rev = total_rev + int(row[1])
      current = int(row[1])
      change = current - previous
      previous = int(row[1])
      if total_month > 1:
          total_delta = total_delta + change
          if change > greatest_inc: 
              greatest_inc = change
              greatest_inc_mon = row[0]
          if change < greatest_dec:
              greatest_dec = change
              greatest_dec_mon = row[0]

        

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {total_month}')
print(f'Total: ${total_rev}')
print(f'Average  Change: ${total_delta/(total_month-1):.2f}')
print(f'Greatest Increase in Profits: {greatest_inc_mon} (${greatest_inc})')
print(f'Greatest Decrease in Profits: {greatest_dec_mon} (${greatest_dec})')