# File Name : main.py
# Student Name: David Becker & Nikki Carfora
# email:  beckerd8@mail.uc.edu  carfornc@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Using python to clean the data in a csv file (fix missing values, truncate numbers, delete duplicate rows)

# Brief Description of what this module does. calls the functions from the other modules and executes them. 
# Citations: 

# Anything else that's relevant:

from dataProcessing.dataProcessing import *

if __name__ == "__main__":
    processor = DataProcessor("./csvData/fuelPurchaseData.csv")
    processor.clean_data()

