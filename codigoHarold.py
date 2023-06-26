

import pandas as pd
import matplotlib.pyplot as plt

# Load the data (replace 'file_path' with your actual csv file path)
df = pd.read_csv('file_path')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the average volume of calls by year, date, and interval
average_volume = df.groupby([df['Date'].dt.year, df['Date'].dt.date, 'Interval'])['IB Calls', 'IB Handled'].mean().reset_index()

# Filter out the data for January 2023
average_volume_january_2023 = average_volume[average_volume['Date'].dt.month == 1]

# Display the result as a time series
plt.figure(figsize=(12, 6))
plt.plot(average_volume_january_2023['Date'], average_volume_january_2023['IB Calls'], label='IB Calls')
plt.plot(average_volume_january_2023['Date'], average_volume_january_2023['IB Handled'], label='IB Handled')
plt.title('Average Volume of Calls (January 2023)')
plt.xlabel('Date')
plt.ylabel('Average Volume')
plt.legend()
plt.show()

# Calculate the Service Level Compliance
df['Service Level Compliance'] = df['Calls in SL'] / df['IB Calls']

# Display a scatter plot for September 2022
df_september_2022 = df[df['Date'].dt.month == 9]
plt.figure(figsize=(12, 6))
plt.scatter(df_september_2022['Date'], df_september_2022['Service Level Compliance'])
plt.title('Service Level Compliance (September 2022)')
plt.xlabel('Date')
plt.ylabel('Service Level Compliance')
plt.show()

# Display a chart to compare the call volume vs service level for September 2022
plt.figure(figsize=(12, 6))
plt.plot(df_september_2022['Date'], df_september_2022['IB Calls'], label='IB Calls')
plt.plot(df_september_2022['Date'], df_september_2022['Service Level Compliance'], label='Service Level Compliance')
plt.title('Calls Volume vs Service Level (September 2022)')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Calculate the weighted IB AHT per month for 2021
df_2021 = df[df['Date'].dt.year == 2021]
weighted_aht = (df_2021['IB AHT'] * df_2021['IB Calls']).groupby(df_2021['Date'].dt.month).sum() / df_2021.groupby(df_2021['Date'].dt.month)['IB Calls'].sum()
weighted_aht = weighted_aht.reset_index()

# Display the result in a DataFrame
weighted_aht_df = pd.DataFrame(weighted_aht, columns=['Month', 'Weighted IB AHT'])
print(weighted_aht_df)

# Display the result in a chart
plt.figure(figsize=(12, 6))
plt.plot(weighted_aht_df['Month'], weighted_aht_df['Weighted IB AHT'])
plt.title('Weighted IB AHT per Month (2021)')
plt.xlabel('Month')
plt.ylabel('Weighted IB AHT')
plt.show()
