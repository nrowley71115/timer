#!/bin/bash

# Function to countdown and then log to CSV
countdown() {
    secs=$1
	workType=${2:-w} # Default to 'w' if no second argument is given
	startTime=$(date '+%Y-%m-%d %H:%M:%S')
	duration=$secs

	while [ $secs -gt 0 ]; do
		echo -ne "$secs\033[0K\r"
		sleep 1
		: $((secs--))
	done
													    
	echo "Timer done!"
	say "Completed"
																    
	# Logging to CSV
	echo "$(date '+%Y-%m-%d'),$startTime,$duration,$workType" >> timer.csv
}

# Call countdown with provided arguments
countdown "$1" "$2"
