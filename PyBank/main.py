# PyBank Challenge - Financial Analysis Script
 
# Import necessary modules
import os
import csv
 
# Define paths for input and output files
# Using the specific file path provided
file_csv = "/Users/nkd/Documents/Data_Science_Class/Starter_Code-4/PyBank/Resources/budget_data.csv"
# Define output file path relative to the script location
output_file = os.path.join(os.path.dirname(__file__), "Analysis", "financial_analysis.txt", encoding="UTF-8")
 
# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
profit_loss_changes = []
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}
 
# Open and read the CSV file
try:
    with open(budget_csv, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
 
        # Skip the header row
        next(csv_reader)
 
        # Iterate through each row in the CSV
        for row in csv_reader:
            date = row[0]
            profit_loss = int(row[1])
 
            # Count total months
            total_months += 1
 
            # Calculate net total
            net_total += profit_loss
 
            # Calculate profit/loss change
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                profit_loss_changes.append(change)
 
                # Check for greatest increase
                if change > greatest_increase["amount"]:
                    greatest_increase["date"] = date
                    greatest_increase["amount"] = change
 
                # Check for greatest decrease
                if change < greatest_decrease["amount"]:
                    greatest_decrease["date"] = date
                    greatest_decrease["amount"] = change
 
            # Update previous profit/loss for next iteration
            previous_profit_loss = profit_loss
 
    # Calculate average change
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)
 
    # Prepare the analysis results
    analysis_results = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})
Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})
"""
 
    # Print results to terminal
    print(analysis_results)
 
    # Write results to output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as file:
        file.write(analysis_results)
 
    print(f"Analysis has been saved to {output_file}")
 
except FileNotFoundError:
    print(f"Error: The file {budget_csv} was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


