from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_current_date = current_date.strftime('%Y-%m-%d %H:%M:%S') 
    print(f'Current date and time: {current_date}')
    return current_date    

def calculate_future_date(current_date):
    number_of_days = int(input(f'Enter the number of days to add to the current date: '))
    delta = timedelta(days = number_of_days)
    future_date = current_date + delta
    formatted_future_date = future_date.strftime('%Y-%m-%d %H:%M:%S') 
    print(f'Future date: {formatted_future_date}')

def main():
    current_date = display_current_datetime()
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()