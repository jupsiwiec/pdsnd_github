import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

print('Hello! Let\'s explore some US bikeshare data!')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """


    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    print('Please choose one of three cities: Chicago, New York City, Washington')
    while True:
        city = input("I choose:").lower()
        if city in CITY_DATA:
            print('You have chosen', city)
            break
        else:
            print('You have not chosen one of 3 options. Please select either: Chicago, New York City, or Washington')

    # TO DO: get user input for month (all, january, february, ... , june)
    usermonth = ["january", "february", "march", "april", "may", "june", 'all']
    print('Please pick a month')
    while True:
        month = input("I choose:").lower()
        if month in usermonth:
            print('You have chosen', month)
            break
        else:
            print('The Data only contains the first six months. please select one of the first six months or type "all" for see all six months')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    userday = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    print('Please pick a day')
    while True:
        day = input("I choose:").lower()
        if day in userday:
            print('You have chosen', day)
            break
        else:
            print('you have misspelled or have not selected a valid day')

    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])

    # covert the start time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.lower() == day.lower()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

       # Display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # Display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', common_day_of_week)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

      # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end_station)

    # Display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['Start To End'].mode()[0]
    print('Most Frequent Combination of Start Station and End Station Trip:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nGender Counts:\n', gender_counts)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


 
  def display_raw_data(df):
    """
    Displays 5 lines of raw data at a time upon user request.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
        # Displays 5 lines of raw data at a time upon user request.

        while True:
            raw_data = input("\nWould you like to see 5 lines of raw data? Enter yes or no.\n").lower()
            if raw_data == 'yes':
                print(df.sample(n=5))
            elif raw_data == 'no':
                break
            else:
                print('Please type out yes or no')

def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

