weekly_temps = [24, 28, 33, 31, 27, 35, 29]
days = ["Monday","Tuesday","Wednesday", "Thrusday","Friday", "Saturday", "Sunday"]

# Heatwave day if temp over 30 and use zip to combine the lists
heatwave_days = [(day,temp) for (day,temp) in zip(days,weekly_temps) if temp > 30]

print("Temperatures this week:", weekly_temps)
print("Heatwave Temperatures:", heatwave_days)

