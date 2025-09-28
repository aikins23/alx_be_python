from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y:%m:%d %H:%M:%S"))
    return current_date  # return the datetime object, not just the string

def calculate_future_date():
    current_date = datetime.now()
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=days)
    print("Future date and time:", future_date.strftime("%Y:%m:%d %H:%M:%S"))

calculate_future_date()
