# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts
# it into degrees Fahrenheit.
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.
# (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key:((val * 9/5) + 32) for (key,val) in weather_c.items()}

print(weather_f)

