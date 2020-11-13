import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = {'chicago', 'new york city', 'washington'}

months = ['January', 'February', 'March', 'April', 'May', 'June']

weekdays = {'Sunday', 'Monday', 'Tuesday', 'Wednesdaay', 'Thursday', 'Friday', 'Saturday'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    day = ''
    
    while(city not in cities):
        city = input("Select one of the following cities: Chicago, New York City or Washington:").lower()
        if city not in cities:
            print("The selected city is not valid.\n")

    # get user input for month (all, january, february, ... , june)
    month = ''
    while(month not in months and month != 'all'):
        month = input("Select one of the following months: Jan, Feb, Mar, Apr, May, Jun or all:").lower()
        if month == 'jan':
            month = 'January'
        elif month == 'feb':
            month = 'February'
        elif month == 'mar':
            month = 'March'
        elif month == 'apr':
            month = 'April'
        elif month == 'may':
            month = 'May'
        elif month == 'jun':
            month = 'June'
        
        if month not in months and month != 'all':
            print("The selected month is not valid.\n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while(day not in weekdays and day != 'all'):
        day = input("Select one of the following months: Sun, Mon, Tue, Wed, Thu, Fri, Sat or all:").lower()
        if day == 'sun':
            day = 'Sunday'
        elif day == 'mon':
            day = 'Monday'
        elif day == 'tue':
            day = 'Tuesday'
        elif day == 'wed':
            day = 'Wednesday'
        elif day == 'thu':
            day = 'Thursday'
        elif day == 'fri':
            day = 'Friday'
        elif day == 'sat':
            day = 'Saturday'
            
        if day not in weekdays and day != 'all':
            print("The selected day is not valid.\n")
    
    print('-'*40)
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
    CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    
    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        (DataFrame) df - DataFrame to extract data
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_mode = df['month'].mode()[0]
    print("The most common month is {}.".format(months[month_mode - 1]))

    # display the most common day of week
    weekday_mode = df['day_of_week'].mode()[0]
    print("The most common day of week is {}.".format(weekday_mode))

    # display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    hour_mode = df['start_hour'].mode()[0]
    print("The most common day of week is {}.".format(hour_mode))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    
    Args:
        (DataFrame) df - DataFrame to extract data
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_mode = df['Start Station'].mode()[0]
    print("The most commonly used start station is {}.".format(start_station_mode))

    # display most commonly used end station
    end_station_mode = df['End Station'].mode()[0]
    print("The most commonly used end station is {}.".format(end_station_mode))

    # display most frequent combination of start station and end station trip
    df['travel'] = "FROM: " + df['Start Station'] + " TO: " + df['End Station']
    travel_mode = df['travel'].mode()[0]
    print("The most frequent combination of start station and end station trip is {}.".format(travel_mode))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    
    Args:
        (DataFrame) df - DataFrame to extract data
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_duration_sum = df['Trip Duration'].sum()
    print("The total travel time is {} seconds.".format(trip_duration_sum))

    # display mean travel time
    trip_duration_mean = df['Trip Duration'].mean()
    print("The mean travel time is {} seconds.".format(trip_duration_mean))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    
    Args:
        (DataFrame) df - DataFrame to extract data
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of each user type
    user_types = df['User Type']
    suscribers_count = user_types[user_types == 'Subscriber'].count()
    customers_count = user_types[user_types == 'Customer'].count()
    print("The amount of subscribers is {}".format(suscribers_count))
    print("The amount of customers is {}".format(customers_count))
    

    # Display counts of each gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].dropna(axis = 0)
        female_count = gender_types[gender_types == 'Female'].count()
        male_count = gender_types[gender_types == 'Male'].count()
        print("The amount of female users is {}".format(female_count))
        print("The amount of male users is {}".format(male_count))
    else:
        print("No gender data available")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_years = df['Birth Year'].dropna(axis = 0)
        print("The older user was born in {}".format(int(birth_years.min())))
        print("The younger user was born in {}".format(int(birth_years.max())))
        print("The most common year of birth is {}".format(int(birth_years.mode()[0])))
    else:
        print("No year of birth data available")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):
    """Displays raw data from de DataFrame.
    
    Args:
        (DataFrame) df - DataFrame to extract data
    """
    display = input('\nIf you want to see raw data, enter yes.\n').lower()
    
    iter = 0
    while display == 'yes':
        # print 5 rows of raw data starting from the iter value
        print(df.iloc[iter:iter+5])
        iter += 5
        display = input('\nIf you want to see more raw data, enter yes.\n').lower()
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
