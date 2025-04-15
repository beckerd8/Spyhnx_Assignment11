# File Name : utilities.py
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

import csv
import requests

class CSVReader:
    def read_CSV_file(self, path):
        with open(path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

class CSVWriter:
    @staticmethod
    def write_CSV_file(path, data):
        if not data:
            print(f"No data to write to {path}")
            return
        with open(path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

class APIHandler:
    API_KEY = "64edf560-1996-11f0-857d-fd139d48e852"

    @staticmethod
    def lookup_zip(city_name):
        try:
            url = f"https://app.zipcodebase.com/api/v1/search?apikey={APIHandler.API_KEY}&city={city_name}&country=US"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if "results" in data and city_name in data["results"]:
                    return data["results"][city_name][0]["postal_code"]
        except Exception as e:
            print(f"API error for {city_name}: {e}")
        return None
