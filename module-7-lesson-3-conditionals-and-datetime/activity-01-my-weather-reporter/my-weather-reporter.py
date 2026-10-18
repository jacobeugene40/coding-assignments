import datetime
import calendar

# Step 2: Collect user input
city = input("Enter the city name: ")
temp = float(input("Enter today's temperature in Celsius: "))

# Step 3: if statement - hot warning only when needed
if temp > 35:
    print("Warning: It is extremely hot! Stay hydrated and avoid the midday sun.")

# Step 4: if-else - choose between two messages
if temp > 25:
    print("Great day to go outside!")
else:
    print("Grab a jacket before you go out!")

# Step 5: if-elif-else - pick the right weather label
if temp > 35:
    print("Weather label: Scorching Hot")
elif temp > 25:
    print("Weather label: Warm and Sunny")
elif temp > 15:
    print("Weather label: Cool and Breezy")
else:
    print("Weather label: Cold")

# Step 6: datetime and calendar modules
now = datetime.datetime.now()
print("\nWeather report for", city)
print("Date and time:", now)

print("\nCalendar for", now.year)
print(calendar.calendar(now.year))