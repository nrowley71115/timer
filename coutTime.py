#!/usr/bin/env python3
import csv
from datetime import datetime

def read_timer_csv():
    with open('./timer.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        data = []
        for row in reader:
            date = row[0]
            timestamp = row[1]
            duration = row[2]
            category = row[3]
            data.append((date, timestamp, duration, category))    
        return data

def printTerminal(week_hrs, month_hrs, last_month_hrs, year_days):
    print(f"Week hours: {week_hrs}")
    print(f"Month hours: {month_hrs}")
    print(f"Last month hours: {last_month_hrs}")
    print(f"Year days: {year_days}")

def calculate_time():
    data = read_timer_csv()

    # Initialize variables
    week_sec = 0
    month_sec = 0
    year_sec = 0
    last_month_sec = 0

    # Iterate through data form csv
    for date, timestamp, duration, category in data:
        # Convert date to datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        # Convert duration to seconds
        duration = int(duration)

        # Calculate this week
        this_week = datetime.now().isocalendar()[1]
        if category == 'w' and date_obj.isocalendar()[1] == this_week:
            week_sec += duration 

        # Calculate this month
        this_month = datetime.now().month
        if category == 'w' and date_obj.month == this_month:
            month_sec += duration

        # Calculate this year
        this_year = datetime.now().year
        if category == 'w' and date_obj.year == this_year:
            year_sec += duration

        # Calculate last month
        last_month = datetime.now().month - 1 if datetime.now().month != 1 else 12
        if category == 'w' and date_obj.month == last_month:
            last_month_sec += duration

    # Convert seconds to hours and days, round to 2 decimal places
    week_hrs = round(week_sec / 3600, 2)
    month_hrs = round(month_sec / 3600, 2)
    year_days = round(year_sec / 86400, 2)
    last_month_hrs = round(last_month_sec / 3600, 2)

    printTerminal(week_hrs, month_hrs, last_month_hrs, year_days)

if __name__ == "__main__":
    calculate_time()
