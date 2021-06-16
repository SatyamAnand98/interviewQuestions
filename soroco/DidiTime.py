from datetime import datetime

departed = datetime.strptime("06:46:00", "%H:%M:%S")
curr = datetime.strptime(datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")
arrived = datetime.strptime("20:23:00", "%H:%S:%M")
print(arrived-departed)
