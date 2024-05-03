import pandas as pd

# Load data from csv file
df = pd.read_csv('Netflix.csv', sep=';')


# Format the Duration column and Start Time column
df['Duration'] = pd.to_timedelta(df['Duration'])
df['Start Time'] = pd.to_datetime(df['Start Time'])


# Total number of countries

num_unique_countries = df['Country'].nunique()
print(f'There are {num_unique_countries} unique countries in column Country.')
print('Unique countries: ' + '; '.join(df['Country'].unique()))

# Check the average duration of movies and TV shows

average_duration = round(df['Duration'].mean().total_seconds() / 60, 2)
print(f'The average duration of movies and TV shows is {average_duration} minutes.')


# Total watch time in the selected country (DE (Germany))

country = 'DE (Germany)'
data_country = df[df['Country'] == country]  # Filter rows for the selected country
data_country.loc[:, 'Duration'] = pd.to_timedelta(data_country['Duration'])  # Convert duration to timedelta format
total_watch_time = round(data_country['Duration'].sum().total_seconds() / 3600)  # Calculate the sum in hours
print(f'Total watch time in {country}: {total_watch_time} hours.')


# Find the earliest entry

earliest_entry = df['Start Time'].min()
print(f'The first watch was on {earliest_entry}.')


# Find the latest entry

latest_entry = df['Start Time'].max()
print(f'The last watch was on {latest_entry}.')


# Find the most watched show

df['Title'] = df['Title'].str.split(':').str[0]
most_watch_title = df['Title'].value_counts().idxmax()
print(f'The most watched title is "{most_watch_title}".')


# Find the highest watch time movie or series (duration)

df['Total Watch Time'] = df['Duration'].dt.total_seconds() / 3600  # Convert to hours
highest_watch_time = df.groupby('Title')['Total Watch Time'].sum().idxmax()
time = df.groupby('Title')['Total Watch Time'].sum().max()  # Find the highest watch time
print(f'The series or movie which has the highest watch time (duration) is {highest_watch_time}'
      f' with {time} hours.')


# Total number of devices used

num_unique_devices = df['Device Type'].nunique()
print(f'There are {num_unique_devices} unique devices used to watch Netflix.')
# print('Unique devices: ' + '; '.join(data['Device Type'].unique()))


# Filter the data for the COVID-19 pandemic period

start_date = pd.to_datetime('2020-03-11').date()
end_date = pd.to_datetime('2021-10-25').date()
covid_data = df[(df['Start Time'].dt.date >= start_date) & (df['Start Time'].dt.date <= end_date)]

# Number of countries appeared during COVID-19 pandemic

num_unique_countries_during_covid = covid_data.groupby(covid_data['Start Time'].dt.date)['Country'].nunique().max()
unique_countries_during_covid = covid_data['Country'].unique()
countries_str = ', '.join(unique_countries_during_covid)
print(f'Number of countries appeared during COVID-19 pandemic: {num_unique_countries_during_covid}. '
      f'The countries are: {countries_str}.')


# Total watch time per day during the COVID-19 pandemic

# Group the data by date and calculate the total watch time
daily_duration_covid = covid_data.groupby(covid_data['Start Time'].dt.date)['Duration'].sum()
# Convert the duration to hours
daily_duration_covid = daily_duration_covid.dt.total_seconds() / 3600
#print(daily_duration_covid)
