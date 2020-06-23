import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    city = input("Please choose a city. Type 'chicago', 'nyc', or 'washington': \n").lower()
    
    while city not in ['chicago', 'nyc', 'washington']:
        city = input("Please enter a valid string. Type 'chicago', 'nyc', or 'washington': \n").lower()

    month = input("Please choose a month from Jan to June. \n Type full name of chosen month with no caps. \n Or, type 'all' for no filter. \n").lower()

    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while month not in months :
        month = input("Please choose a valid month please or 'all': \n").lower()

    day = input("Please choose a day of week. \n Type full name chosen day with no caps. \n Or, type 'all' for no filter. \n").lower()
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' , 'sunday', 'all']
    while day not in days:
        day = input("Please choose valid day or all: \n").lower()
    
    #separtion and returns 
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
    df = pd.read_csv("{}.csv".format(city))
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['dow'] = df['Start Time'].dt.day_name()
    df["month"] = df['Start Time'].dt.month_name()
    
    df['dow'] = df['dow'].str.lower()
    df["month"] = df['month'].str.lower()
    
    if month != 'all':
        df = df.loc[df['month']== month,:]
    if day != 'all':    
        df = df.loc[df['dow'] == day,:]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
        Input: df. DataFrame that we have filtered 
        Output: Calculates time taken for entire calculation and most common month, day, hour. 
        """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # TO DO: display the most common day of week
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['dow'] = df['Start Time'].dt.day_name()
    df["month"] = df['Start Time'].dt.month_name()
    df['hour'] = df['Start Time'].dt.hour
    
    df['dow'] = df['dow'].str.lower()
    df["month"] = df['month'].str.lower()
    
    modeMonth = df['month'].mode()[0]
    modeDow = df['dow'].mode()[0]
    modeHour = df['hour'].mode()[0]
    print("The most common month within our given frame is:\n", modeMonth )
    print("The most common day within our given frame is:\n", modeDow )
    print("The most common hour within our given frame is:\n", modeHour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Input: df. DataFrame that we have filtered 
    Output: Calculates time taken for entire calculation and most popular start station, end station, and combination. """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    # TO DO: display most commonly used end station
    # TO DO: display most frequent combination of start station and end station trip

    modeStartStation = df['Start Station'].mode()[0]
    modeEndStation = df['End Station'].mode()[0]
    combo = df['Start Station'] + ' to ' + df['End Station']
    modeCombo = combo.mode()[0]

    print("The most popular starting station is: \n" + str(modeStartStation))
    print("The most popular ending station is: \n" + str(modeEndStation))
    print("The most popular combination station is: \n" + str(modeCombo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # TO DO: display mean travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['travelTime'] = df['End Time'] - df['Start Time']
    
    totalTime = df['travelTime'].sum()
    meanTime = df['travelTime'].mean()

    print("The total travel time is: \n" + str(totalTime))
    print("The mean travel time is: \n" + str(meanTime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    userCount = df['User Type'].value_counts()
    print('Count of user types: \n' + str(userCount))

    if city != 'washington':
        genderCount = df['Gender'].value_counts()
        print('Count of genders: \n', genderCount)

        earliestBOY = df['Birth Year'].min()
        print('Earliest Birth Year is: \n', earliestBOY)
        recentBOY = df['Birth Year'].max()
        print('Most recent Birth Year is: \n', recentBOY)
        modeBOY = df['Birth Year'].mode()
        print('Most common Birth Year is: \n', modeBOY)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def rawData(df):
    """
    Display raw data from CSV file. 
    """
    startLoc = 0
    endLoc = 5

    display = input("Do you want to see raw Data? ( y or n) \n").lower()

    if display == 'y':
        while endLoc <= df.shape[0] -1:
            print(df.iloc[startLoc:endLoc,:])
            startLoc += 5
            endLoc += 5

            stopDisplay = input("Do you wish to contiue? ( y or n ) \n").lower()
            if stopDisplay == 'n':
                break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        rawData(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
