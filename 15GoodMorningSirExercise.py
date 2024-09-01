# This is quite a typical thing to do.

## NOTA BAAD MEIN KARENGE
# Now we are doing it , since, I understood it .
import time

timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
if hour >= 0 and hour < 12:
  print("Good Morning Sir. \n")
elif hour >= 12 and hour < 16:
  print("Good Afternoon Sir. \n")
elif hour >= 16 and hour < 24:
  print("Good Evening Sir. \n")