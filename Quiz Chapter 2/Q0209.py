"""
Quiz Q0209
"If the weather is cloudy today and it rained yesterday, it will rain today".

Generate the logical operation for the statement above and evaluate the weather forecast for today.
"""
cloudy_today = True
rained_yesterday = True
rain_today = cloudy_today and rained_yesterday
print(rain_today)