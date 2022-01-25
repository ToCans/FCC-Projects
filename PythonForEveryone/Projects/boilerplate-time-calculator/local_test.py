def add_time(start, duration, *weekday):

    # Create some sort of list for weekdays (have key and value)
    # Have a while loop for finding weekday
    # identify days based on first three letters

    

    # Counters
    hour_count = 0
    minute_count = 0
    days_later = 0

    # Inputs
    time_input = start.split(" ")
    start_morn_aft = time_input[1]


    # Weekday Calc
    # 0 = Mon, 1 = Tues, 2 = Wed, 3 = Thurs, 4 = Fri, 5 = Sat, 6 = Sun
    if weekday:
        weekday = weekday[0]
        weekday_let = weekday[0]
        if weekday[0] == "m" or weekday[0] == "M":
            #weekday = "Monday"
            weekday_count = 0
        elif weekday[0] == "t" or weekday[0] == "T":
            if weekday [1] == "u" or weekday[1] == "U":
                #weekday = "Tuesday"
                weekday_count = 1
            else:
                #weekday = "Thursday"
                weekday_count = 3
        elif weekday[0] == "s" or weekday[0] == "S":
            if weekday [1] == "a" or weekday[1] == "A":
                #weekday = "Saturday"
                weekday_count = 5
            else:
                #weekday = "Sunday"
                weekday_count = 6
        elif weekday[0] == "f" or weekday[0] == "F":
            #weekday = "Friday"
            weekday_count = 4
        else:
            #weekday = "Wednesday"
            weekday_count = 2


    # Splitting Inputs
    start_time = time_input[0].split(":")
    start_hour = int(start_time[0])
    start_min = int(start_time[1])

    # Adding duration
    dur_input = duration.split(":")
    dur_hour = int(dur_input[0])
    dur_min = int(dur_input[1])
    
    # 24 hr time for Calc
    if start_morn_aft == "PM":
        start_hour_add = start_hour + 12
    else:
        start_hour_add = start_hour

    # Adding Hours and Minutes Together
    new_time_hour = start_hour_add + dur_hour
    new_time_minute = start_min + dur_min

    # Accounting for Exceeding Values
    # Day Checkers
    while new_time_hour >= 23:
        new_time_hour -= 24
        days_later += 1

    if weekday:
        weekday_assign = days_later + weekday_count
        while (weekday_assign) > 6:
            weekday_assign -= 7
        if weekday_assign == 0:
            weekday_string = "Monday"
        elif weekday_assign == 1:
            weekday_string = "Tuesday"
        elif weekday_assign == 2:
            weekday_string = "Wednesday"
        elif weekday_assign == 3:
            weekday_string = "Thursday"
        elif weekday_assign == 4:
            weekday_string = "Friday"
        elif weekday_assign == 5:
            weekday_string = "Saturday"
        elif weekday_assign == 6:
            weekday_string = "Sunday"




    # Minute Checkers
    if new_time_minute > 59:
        new_time_hour += 1
        final_minute = new_time_minute - 60
    else:
        final_minute = new_time_minute
    
    # Hour Checkers
    if new_time_hour >= 12:
        final_mon_aft = "PM" 
    else:
        final_mon_aft = "AM"
       
    if new_time_hour > 12:
        final_hour = new_time_hour - 12
    else:
        final_hour = new_time_hour

    # String Alternatives
    # Minute String
    if final_hour == 0:
        final_hour = "12"
    else:
        final_hour = str(final_hour)

    if final_minute < 10:
        final_minute = "0"+str(final_minute)
    else:
        final_minute = str(final_minute)

    if days_later == 1:
        days_later_string = "(next day)"
        if weekday:
            new_time = new_time = final_hour+":"+final_minute+" "+final_mon_aft +", "+ weekday_string+" "+ days_later_string
        else:
            new_time = new_time = final_hour+":"+final_minute+" "+final_mon_aft+" "+ days_later_string
    elif days_later > 1:
        days_later_string =  "("+str(days_later)+" days later)"
        if weekday:
            new_time = new_time = final_hour+":"+final_minute+" "+final_mon_aft +", "+ weekday_string+" "+ days_later_string
        else:
            new_time = new_time = final_hour+":"+final_minute+" "+final_mon_aft+" "+ days_later_string
    else:
        if weekday:
            new_time = new_time = final_hour+":"+final_minute+" "+final_mon_aft+", "+ weekday_string
        else:
            new_time = new_time = final_hour+":"+final_minute+" "+final_mon_aft

    return new_time

print(add_time("8:16 PM", "466:02", "tuesday"))