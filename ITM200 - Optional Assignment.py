# 1 - Read the content provided data.csv file and print the contents
import csv             
with open("data.csv", mode = 'r') as fileCSV: 
    fCSV = csv.reader(fileCSV)                 
    for line in fCSV:
        print(line)                       


# 2 - Calculate the total number of vehicles sold in each year starting from 2012 to 2021

import csv

# Initialize a dictionary to store the total number of vehicles sold for each year
totals_by_year = {str(year): 0 for year in range(2012, 2022)}

# Open the CSV file and read the data
with open("data.csv", "r") as fileCSV:
    reader = csv.reader(fileCSV)
    header = next(reader)  # Skip the header row
    for row in reader:
        year = row[0]
        if int(year) < 2022:  # Ignore data for 2022
            for i in range(1, 13):
                totals_by_year[year] += int(row[i])

# Print the total number of vehicles sold for each year
for year, total in totals_by_year.items():
    print(f"Total vehicles sold in {year}: {total}")

with open('stats.txt', 'w') as file:
    file.write(f"Total number of vehicles sold is: {totals_by_year}\n")




# 4 - Calculate the total sales in the first 6 months of 2021

import csv

# Initialize a variable to store the total number of vehicles sold in the first 6 months of 2021
sales_first_half_2021 = 0

# Open the CSV file and read the data
with open("data.csv" , "r") as fileCSV:
    reader = csv.reader(fileCSV)
    header = next(reader)  # Skip the header row
    for row in reader:
        year = row[0]
        if year == '2021':
            for i in range(1, 7):  # Sum data for the first 6 months
                sales_first_half_2021 += int(row[i])

# Print the total number of vehicles sold in the first 6 months of 2021
print(f"Total vehicles sold in the first half of 2021: {sales_first_half_2021}")


# Calculate the total sales in the first 6 months of 2022

import csv

# Initialize a variable to store the total number of vehicles sold in the first 6 months of 2022
sales_first_half_2022 = 0

# Open the CSV file and read the data
with open("data.csv" , "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        year = row[0]
        if year == '2022':
            for i in range(1, 7):  # Sum data for the first 6 months
                sales_first_half_2022 += int(row[i])

# Print the total number of vehicles sold in the first 6 months of 2022
print(f"Total vehicles sold in the first half of 2022: {sales_first_half_2022}")


# Calculate the sales growth rate for the first 6 months of 2022
import csv

# Initialize variables to store the total number of vehicles sold in the first 6 months of 2021 and 2022
sales_first_half_2021 = 0
sales_first_half_2022 = 0

# Open the CSV file and read the data
with open("data.csv" , "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        year = row[0]
        if year == '2021':
            for i in range(1, 7):  # Sum data for the first 6 months of 2021
                sales_first_half_2021 += int(row[i])
        elif year == '2022':
            for i in range(1, 7):  # Sum data for the first 6 months of 2022
                sales_first_half_2022 += int(row[i])

# Calculate the sales growth rate
growth_rate = (sales_first_half_2022 - sales_first_half_2021) / sales_first_half_2022

# Write the sales growth rate to a file
with open('stats.txt', 'w') as file:
    file.write(f"Sales growth rate: {growth_rate}")
print(growth_rate)


estimated_sales = (sales_first_half_2021 + sales_first_half_2021) * (growth_rate)
with open('stats.txt', 'w') as file:
    file.write(f"Estimated sales for 2022 is: {estimated_sales}\n")
    file.write(f"Total number of vehicles sold is: {totals_by_year}\n")


