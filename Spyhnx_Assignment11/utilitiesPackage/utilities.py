# File Name : utilities.py
# Student Name: David Becker & Nikki Carfora
# email:  beckerd8@mail.uc.edu  carfornc@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  
# Brief Description of what this module does. calls the functions from the other modules and executes them. 
# Citations:

# Anything else that's relevant:

import csv
import os

class CSVReader:
    def read_CSV_file(self, filepath):
        data = []
        try:
            with open(filepath, mode='r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"File not found: {filepath}")
        return data
