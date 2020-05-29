import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    error_inputs = "ERROR. Please try again" 
    
 
    while True :
        city_input = input("\nEnter the city to analyze: \nchicago,\nnew york,\nwashington. \n").lower()
        if city_input in ['chicago', 'new york', 'washington']:
            break
        else:
            print(error_inputs)

    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month_input = input("\nenter the month that you are interesting: \njanuary,\nfebruary,\nmarch,"
            "\napril,\nmay,\njune\nto filter by, or \"all\" to apply no month filter\n").lower()
        if month_input in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            print(error_inputs)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day_input = input("\nenter  day of the week that you are interesting: \nmonday,\ntuesday,\nwednesday,\nthursday,"
            "\nfriday,\nsaturday,\nsunday\nof week to filter by, or \"all\" to apply no day filter\n").lower()
        if day_input in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            print(error_inputs)


 
    return city_input, month_input, day_input


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    input_file = CITY_DATA[city] #define input file for city and select from the dictionary the corresponding csv file
    df = pd.read_csv(input_file) #dataframe variable to read the file csv
    
    df["start_time_dt"] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S') # convert the string start time in a data format
    df["month"] = df['start_time_dt'].dt.month # extract the month from the date column
    df["day_of_week"] = df['start_time_dt'].dt.day_name() # extract the day of the week from the date column
    
    if month != 'all': #if you select different from all you have to filter according the different months
        months_map = { "january":1,"february":2,"march":3,"april":4,"may":5,"june":6} #create a map where each month has an associated number
        month_id = months_map[month]
        df = df.loc[df['month'] == month_id] # dataframe becomes filter by month = to month_id
    
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
        
    return df
    



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
   

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(arg = df['Start Time'], format = '%Y-%m-%d %H:%M:%S')

    month = df['Start Time'].dt.month
    weekday_name = df['Start Time'].dt.day_name()
    hour = df['Start Time'].dt.hour

    # TO DO: display the most common month
    most_common_month = month.mode()[0]
    print('The month most frequent is:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day_week = weekday_name.mode()[0]
    print('The day of the week most frequent is:', most_common_day_week)

    # TO DO: display the most common start hour
    most_common_start_hour = hour.mode()[0]
    print('The hour most frequent is:', most_common_start_hour)



def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The start station most frequent is:', df['Start Station'].value_counts().idxmax())

    # TO DO: display most commonly used end station
    print('The end station most frequent is:', df['End Station'].value_counts().idxmax())

    # TO DO: display most frequent combination of start station and end station trip
    start_end_stations = df["Start Station"] + "_" + df["End Station"] #concatenate the start station and end station strings
    common_station = start_end_stations.value_counts().idxmax() # count the start and end station combination
    print('Most frequent start+end stations are:\n{} \nto\n{}'.format(common_station.split("_")[0], common_station.split("_")[1])) # print the most frequent combination

        


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print("Total travel time:\n", total_travel_time)
   


    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print("Mean travel time:\n", mean_travel_time)
    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    typology_of_user = df["User Type"].value_counts()


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_counter = df["Gender"].value_counts()
        print(gender_counter)
    else:
        print("This dataset has no information about gender")


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        earliest_year_of_birth = df["Birth Year"].min()
        most_recent_year_of_birth = df["Birth Year"].max()
        common_year_of_birth = df['Birth Year'].mode()[0]
        print("\nthis is the earliest year of birth: " + str(earliest_year_of_birth))
        print("\nthis is the most recent year of birth: " + str(most_recent_year_of_birth))
        print("\nthis is the most common year of birh: " + str(common_year_of_birth))
    else:
        print("This dataset has no information about birth year")




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
