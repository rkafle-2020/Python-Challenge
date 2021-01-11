#PyBank Solution
#Import Dependencies
import os
import csv

# set the path for the csv file
path = "C:/Users/renuk/OneDrive/Documents/DU-HomeWork/Python-Challenge/PyBank"
pybank_csv = os.path.join(path, 'Resources', 'budget_data.csv')

#set the file/path to store our output analysis
pybank_output = os.path.join(path, 'analysis', 'budget_analysis.txt')

#Initialize the required variables
total_months=0
total_net=0
net_change_list=[]
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# read the csv file
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# read the header row
    csv_header = next(csvreader)
    
# Extract first row to avoid appending to net_change_list
    first_row = next(csvreader)

    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    #Initiate for loop to iterate through the data set to calculate the ask
    for row in csvreader:

        #calculate the total number of months in dataset
        total_months+= 1

        #Calculate the net change in profit / loss
        total_net += int(row[1])
        net_change= int(row[1])-prev_net
        prev_net = int(row[1])
        net_change_list+= [net_change]

        # Calculate the greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#calculate the average change in profit/loss over the entire period
average_change = sum(net_change_list)/len(net_change_list)

#print the financial analysis
results = (
    f"financial analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(results)

# Export the results to text file
with open(pybank_output, "w") as txt_file:
    txt_file.write(results)


 





