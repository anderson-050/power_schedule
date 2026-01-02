from datetime import datetime
import re

# The patterns are defined by the start and end times of "ON" periods.
# Times are represented as (start_hour, start_minute, end_hour, end_minute)

POWER_PATTERNS = {
    # Pattern 1
    1: [
        (5, 0, 9, 0), #5:00 - 9:00
        (13, 0, 17, 0),
        (18, 0, 24, 0),
        (0, 0, 1, 0)
    ],
    # Pattern 2
    2: [
        (5, 0, 6, 0),
        (9, 0, 13, 0),
        (17, 0, 24, 0),
        (0, 0, 3, 0)
    ]
}

SUNDAY_PATTERN = [(9, 0, 24, 0)]

# Reference Date: 28 November 2025
REFERENCE_DATE = datetime(2025, 11, 28)

REFERENCE_PATTERNS = {
    'A': 2,
    'B': 1
}

def parse_time_input(time_str):
    # transform time string into (hour, minute) in 24-hour format

    time_str = time_str.strip().lower().replace(".", "")

    # 12-hour format
    match_12hr = re.match(r'(\d{1,2}):?(\d{2})?\s*(am|pm)', time_str)
    if match_12hr:
        hr = int(match_12hr.group(1))
        min_str = match_12hr.group(2)
        min = int(min_str) if min_str else 0
        ampm = match_12hr.group(3)

        if ampm == 'pm' and hr != 12:
            hr += 12
        elif ampm == 'am' and hr == 12:
            hr = 0

        if 0 <= hr < 24 and 0 <= min < 60:
            return hr, min
        return None
    
    # 24-hour format
    match_24hr = re.match(r'(\d{1,2}):(\d{2})', time_str)
    if match_24hr:
        hr = int(match_24hr.group(1))
        min = int(match_24hr.group(2))
        if 0 <= hr < 24 and 0 <= min < 60:
            return hr, min
        return None
    
    # Simple hour entries(e.g., 5)
    match_simple = re.match(r'(\d{1,2})', time_str)
    if match_simple:
        hr = int(match_simple.group(1))
        if 0 <= hr < 24:
            return hr, 0
        
    return None
    
def get_pattern_for_date(date_input, group_input):

    # Calculate the no of days passed
    date_diff = (date_input - REFERENCE_DATE).days

    # Get the pattern
    ref_pattern = REFERENCE_PATTERNS[group_input]

    # Check if the number of days passed is even or odd
    if date_diff % 2 == 0:
        current_pattern = ref_pattern
    else:
        current_pattern = 3 - ref_pattern #3-1=2 3-2=1
    return current_pattern

def check_power_status(group_input, date_input, time_hm):
    input_hr, input_min = time_hm

    is_sunday = date_input.weekday() == 6
    if is_sunday:
        current_pattern = SUNDAY_PATTERN
    else:
        pattern_num = get_pattern_for_date(date_input, group_input)

        current_pattern = POWER_PATTERNS[pattern_num]
    
    is_on = False

    for start_hr, start_min, end_hr, end_min in current_pattern:
        # convert to min
        input_time_in_min = input_hr * 60 + input_min
        start_time_in_min = start_hr * 60 + start_min
        end_time_in_min = end_hr * 60 + end_min

        if start_time_in_min <= input_time_in_min < end_time_in_min:
            is_on = True
            break

    display_time = f"{input_hr:02d}:{input_min:02d}"

    if is_on:
        status = "ON (Power is available)"
    else:
        status = "OUT (Power is not available)"

    # Get the day of the week for response
    day_of_week = date_input.strftime('%A')

    return (
        f"--- Power Status Result ---\n"
        f"Group: {group_input}\n"
        f"Date: {date_input.strftime('%d %B %Y')}({day_of_week})\n"
        f"Time: {display_time}\n"
        f"Status: {status}"
    )

def main():
    print("\n Welcome to the Power Status Checker")
    print("-"*37)

    # Get Group Input
    while True:
        group_input = input("Enter the Group (A or B): ").strip().upper()
        if group_input in ["A", "B"]:
            break
        print("Invalid input. Please enter 'A' or 'B'.")
    
    # Get Date Input
    while True:
        date_input = input("Enter the Date(dd/mm/yyyy): ")
        try:
            date_input = datetime.strptime(date_input.strip(), '%d/%m/%Y')
            break
        except ValueError:
            print("Invalid date or date format!")

    # Get Time Input
    while True:
        time_input = input("Enter the time(e.g., '14:30', '4:30pm'): ")
        time_hm = parse_time_input(time_input) 
        if time_hm is not None:
            break
        print("Invalid time format. Please try again.")

    # Result
    result = check_power_status(group_input, date_input, time_hm)
    print("\n" + result + "\n")
    

if __name__ == "__main__":
    main()
