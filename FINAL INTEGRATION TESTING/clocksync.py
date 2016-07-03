import time

sys_hours = int(time.strftime("%H"))
sys_mins = int(time.strftime("%M"))
#print (int(sys_time))

print("System time is " + time.strftime("%H:%M"))

#take user time 1

htime1 = input("Please enter time1 (HOURS) : ")
htime1 = int(htime1)
mtime1 = input("Please enter time1 (MINUTES) : ")
mtime1 = int(mtime1)
print("Time1 entered by user is "+str(htime1)+":"+str(mtime1))


htime2 = input("Please enter time2 (HOURS) : ")
htime2 = int(htime2)
mtime2 = input("Please enter time2 (MINUTES) : ")
mtime2 = int(mtime2)
print("Time2 entered by user is "+str(htime2)+":"+str(mtime2))

#sum min
min_sum = sys_mins + mtime1 + mtime2
sys_hours_to_min = sys_hours*60
user1_hours_in_min = htime1*60
user2_hours_in_min = htime2*60

total_mins = min_sum + sys_hours_to_min + user1_hours_in_min + user2_hours_in_min
avg_tolerance_hours = int((total_mins/3)/60)
avg_tolerance_mins = int((total_mins/3)%60)

print("Avg fault tolerance time is "+str(avg_tolerance_hours) + ":" + str(avg_tolerance_mins))

sys_value = None
user1_value = None
user2_value = None

system_correction_in_min = (avg_tolerance_hours*60 + avg_tolerance_mins) - (sys_hours_to_min+sys_mins)
if system_correction_in_min < 0: 
	system_correction_in_min = abs(system_correction_in_min)
	sys_value = "-"
system_correction_hours = int(system_correction_in_min/60)
system_correction_mins = int(system_correction_in_min%60)
if sys_value!="-" :
	sys_value = "+"

user1_correction_in_min = (avg_tolerance_hours*60 + avg_tolerance_mins) - (user1_hours_in_min+mtime1)
if user1_correction_in_min < 0 :
	user1_correction_in_min = abs(user1_correction_in_min)
	user1_value = "-"
user1_correction_hours = int(user1_correction_in_min/60)
user1_correction_mins = int(user1_correction_in_min%60)
if user1_value != "-":
	user1_value = "+"

user2_correction_in_min = (avg_tolerance_hours*60 + avg_tolerance_mins) - (user2_hours_in_min+mtime2)
if user2_correction_in_min < 0 :
	user2_correction_in_min = abs(user2_correction_in_min)
	user2_value = "-"
user2_correction_hours = int(user2_correction_in_min/60)
user2_correction_mins = int(user2_correction_in_min%60)
if user2_value != "-":
	user2_value = "+"

print("System time needs to be adjusted by " +sys_value +str(system_correction_hours)+ ":"+str(system_correction_mins))
print("User 1 time needs to be adjusted by " + user1_value +str(user1_correction_hours) + ":"+str(user1_correction_mins))
print("User 2 time needs to be adjusted by " + user2_value + str(user2_correction_hours) + ":"+str(user2_correction_mins))


 