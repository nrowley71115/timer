#!/usr/bin/env python3
import csv
import datetime
import sys
import time
import subprocess # used for the 'say' command

# CONSTANTS
CSV_FILE = "timer.csv"

def get_cmd_args():
    """
    Processes command-line arguments.
    Returns:
        seconds (int): Number of seconds to run the timer.
        work_type (str): Type of timer 'w' for work, 'b' for break.
    """
    if len(sys.argv) < 2:
        print("Usage: python timer.py <seconds> [WorkType]")
        sys.exit(1)

    # Required first argument: number of seconds
    seconds = int(sys.argv[1])
    # Optional second argument: work type
    if len(sys.argv) > 2:
        work_type = sys.argv[2]
    else:
        work_type = 'w'

    return seconds, work_type

def start_timer(seconds, work_type):
    """
    Runs a countdown timer for the specified number of seconds, updating the display every second.
    Args:
        seconds (int): Number of seconds to run the timer.
        work_type (str): Type of the timer activity.
    """
    for remaining in range(seconds, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write(f"{remaining} seconds")
        sys.stdout.flush()
        time.sleep(1)

    sys.stdout.write("\rThe timer has completed!                     \n")
    subprocess.run(['say', 'completed!'])

    log_to_csv(seconds, work_type)

def log_to_csv(duration, work_type):
    """
    Logs the timer data to a CSV file.
    Args:
        duration (int): Duration in seconds.
        work_type (str): Type of the timer activity.
    """
    # format date and time 
    time = datetime.datetime.now()
    date_str = time.strftime("%Y-%m-%d")
    time_str = time.strftime("%H:%M:%S")

    with open(CSV_FILE, 'a', newline='\n') as file:
        writer = csv.writer(file)
        writer.writerow([date_str, time_str, duration, work_type])

def main():
    seconds, work_type = get_cmd_args()
    start_timer(seconds, work_type)

if __name__ == "__main__":
    main()
