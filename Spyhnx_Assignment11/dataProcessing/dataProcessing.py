# File Name : dataProcessing.py
# Student Name: David Becker & Nikki Carfora
# email:  beckerd8@mail.uc.edu  carfornc@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   4/17/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: Using python to clean the data in a csv file (fix missing values, truncate numbers, delete duplicate rows)

# Brief Description of what this module does. Cleans the csv file, accesses an API to fill nul zip codes. 
# Citations:

# Anything else that's relevant:

import os
from utilitiesPackage.utilities import *

class DataProcessor:
    def __init__(self, filepath):
        self.filepath = filepath
        self.cleaned_data = []
        self.anomalies = []
        self.zip_fixes = 0  

    def clean_data(self):
        csv_reader = CSVReader()
        raw_data = csv_reader.read_CSV_file(self.filepath)

        seen = set()  

        for row in raw_data:
            key = tuple(row.items())
            if key in seen:
                continue 
            seen.add(key)

            fuel_type = row.get("Fuel Type", "").strip().lower()
            if "pepsi" in fuel_type:
                self.anomalies.append(row)
                continue

            # Format Gross Price to 2 decimal places
            if "Gross Price" in row:
                try:
                    row["Gross Price"] = "{:.2f}".format(float(row["Gross Price"]))
                except ValueError:
                    row["Gross Price"] = "0.00"

            # Fill in missing Zip using API (limit to 5 lookups)
            if row.get("Zip") == "" and row.get("City") and self.zip_fixes < 5:
                zip_code = APIHandler.lookup_zip(row["City"])
                if zip_code:
                    row["Zip"] = zip_code
                    self.zip_fixes += 1
                else:
                    row["Zip"] = "00000"

            self.cleaned_data.append(row)

        os.makedirs("Data", exist_ok=True)
        CSVWriter.write_CSV_file("Data/cleanedData.csv", self.cleaned_data)
        CSVWriter.write_CSV_file("Data/dataAnomalies.csv", self.anomalies)
        print("Cleaning complete & output saved to the Data folder.")
