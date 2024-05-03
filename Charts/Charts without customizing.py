import matplotlib.pyplot as plt
import pandas as pd

# Load data from csv file
df = pd.read_csv('../Netflix.csv', sep=';')


# Bar plot showing how many entries there are for each country

country_counts = df['Country'].value_counts()  # Get the number of entries for each country

# Plot the results

plt.figure(figsize=(14, 10))
country_counts.plot(kind='bar')
plt.xlabel('Countries')
plt.ylabel('Number of Entries')
plt.title('Number of Entries for Each Country')
plt.show()


# Bar plot for the duration watched each month in 2022

df['Duration'] = pd.to_timedelta(df['Duration'])  # Convert the Duration column to timedelta
df['Start Time'] = pd.to_datetime(df['Start Time'])  # Convert the Start Time column to datetime

data_2022 = df[df['Start Time'].dt.year == 2022]  # Filter the data for 2022

# Group the data by month and calculate the total watch time

monthly_duration_2022 = data_2022.groupby(data_2022['Start Time'].dt.month)['Duration'].sum()
# covert the duration to hours
monthly_duration_2022 = monthly_duration_2022.dt.total_seconds() / 3600

# Plot the results

plt.figure(figsize=(10, 6))
monthly_duration_2022.plot(kind='bar')
plt.xlabel('Months')
plt.ylabel('Duration')
plt.title('Watch Time per Month in 2022')
plt.show()


# Total watch time per day during the COVID-19 pandemic

# Filter the data for the COVID-19 pandemic period
start_date = pd.to_datetime('2020-03-11').date()
end_date = pd.to_datetime('2021-10-25').date()
covid_data = df[(df['Start Time'].dt.date >= start_date) & (df['Start Time'].dt.date <= end_date)]

# Group the data by date and calculate the total watch time
daily_duration_covid = covid_data.groupby(covid_data['Start Time'].dt.date)['Duration'].sum()
# Convert the duration to hours
daily_duration_covid = daily_duration_covid.dt.total_seconds() / 3600

# Line Plot the results
plt.figure(figsize=(14, 10))
daily_duration_covid.plot(kind='line')
plt.xlabel('Date')
plt.ylabel('Duration (hours)')
plt.title('Watch Time per Day During COVID-19 Pandemic')
plt.show()

# Bar Plot the results
plt.figure(figsize=(14, 10))
daily_duration_covid.plot(kind='bar')
plt.xlabel('Date')
plt.ylabel('Duration (hours)')
plt.title('Watch Time per Day During COVID-19 Pandemic')
plt.show()


# Bar plot for the top 10 most watched titles base on watch time

df['Title'] = df['Title'].str.split(':').str[0]  # Remove the episode information from the Title column
df['Total Watch Time'] = df['Duration'].dt.total_seconds() / 60  # Convert the Duration to minutes
top_titles = df.groupby('Title')['Total Watch Time'].sum().nlargest(10)  # Get the top 10 most watched titles

# Plot the results

plt.figure(figsize=(24, 20))
top_titles.plot(kind='bar')
plt.xlabel('Titles')
plt.ylabel('Total Watch Time (minutes)')
plt.title('Top 10 Most Watched Titles')
plt.show()


# Device usage pie chart

device_usage = df['Device Type'].value_counts().nlargest(10)  # Get the number of entries for top 10 devices

# Plot the results

plt.figure(figsize=(14, 14))
device_usage.plot(kind='pie', autopct='%1.1f%%')
plt.title('Device Usage')
plt.show()


