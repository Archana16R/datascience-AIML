import csv
with open(r"C:\Users\archana\OneDrive\Documents\Company_Data.xlsx", mode="r")as file:
    csv_file=csv.reader(file)
    for lines in csv_file:
        print(lines)