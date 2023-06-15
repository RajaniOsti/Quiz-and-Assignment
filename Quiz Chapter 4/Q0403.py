"""
Enter the temperature in celsius, and convert the temperature to fahrenheit. Finally, 
display different fever levels of the user.

fahrenheit = 1.6*celsius + 32

Conditions:
Temperature	Remarks
below 96F	Low Temperature
96F to 98F	Normal Temperature
99F to 101F	Normal Fever
102F to 104F	High Fever
above 104F	Critical
"""
temp = float(input("enter temperature"))
temp_fah = temp * 9/5 + 32
if temp_fah <=  96:
    print("Low Temperature")
elif temp_fah <= 98:
    print("Normal Temperature")
elif temp_fah <= 101:
    print("Normal Fever")
elif temp_fah <= 104:
    print("High Fever")
else:
    print("Critical")