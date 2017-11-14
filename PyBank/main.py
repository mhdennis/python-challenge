#Import dependencies 
import os
import csv
import pandas as pd 

#Bring in CSV file
budget_data = os.path.join("budget_data_1.csv")
csv_path = "raw_data/budget_data_1.csv"

#Create dataframe
pd.read_csv(csv_path)
budget_df = pd.read_csv(csv_path)

#Find total month count
month_counts = budget_df["Date"].value_counts()
total_months = month_counts.sum() 

#Find total revenue
revenue_count = budget_df["Revenue"].sum()

#Find min and max dates and revenues
max_value = budget_df["Revenue"].max()
max_date = budget_df["Date"].max()
min_value = budget_df["Revenue"].max()
min_date = budget_df["Date"].min()

#Find avg change
average_change = int((revenue_count)/(total_months))

#Print Results

print("Financial Analysis")
print("-------------------------")
print("Total Months: "+ str(total_months))
print("Total Revenue: $" +str(revenue_count))
print("Average Revenue Change: $"  + str(average_change))
print("Greatest Increase in Revenue: " 
	+str(max_date) + " ($" + str(max_value)+ ")")
print("Greatest Decrease in Revenue: " 
	+str(min_date) + " ($" + str(min_value)+")")






