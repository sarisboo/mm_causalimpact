import pyreadr

# Convert weather.rda to .csv for testing 
# Into a dict with one key, weather
result = pyreadr.read_r("data/weather.rda") # also works for RData
weather_df = result['weather']
#weather_df.to_csv('data/weather.csv', index=False)
#print(weather_df.Area.unique())
