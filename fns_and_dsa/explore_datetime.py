# explore_datetime.py
# Objective: Demonstrate usage of Python's datetime module

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()  # get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date


def calculate_future_date(current_date):
    """
    Prompts user for number of days and calculates the future date.
    Displays the future date in the format YYYY-MM-DD
    """
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        future_date = current_date + timedelta(days=number_of_days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
        return future_date
    except ValueError:
        print("Invalid input! Please enter an integer value.")
        return None


if __name__ == "__main__":
    # Part 1: Display current date and time
    current_date = display_current_datetime()

    # Part 2: Calculate future date
    calculate_future_date(current_date)