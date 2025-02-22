# 08. On Time for the Exam 75/100

exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_total_minutes = exam_hours * 60 + exam_minutes
arrival_total_minutes = arrival_hours * 60 + arrival_minutes
difference = exam_total_minutes - arrival_total_minutes

if 0 <= difference <= 30: #on time case
    print("On Time")
    if 0 < difference <= 30 :
        print(f"{difference} minutes before the start")
elif 30 < difference : #early case
    print("Early")
    if 30 < difference < 60 :
        print(f"{difference} minutes before the start")
    else :
        remaining_hours = int((exam_total_minutes - arrival_total_minutes) / 60)
        remaining_minutes = (exam_total_minutes - arrival_total_minutes) % 60
        print(f"{remaining_hours}:{remaining_minutes:02d} hours before the start")
else : #late case
    print("Late")
    if difference < -60 :
        remaining_hours = int((arrival_total_minutes - exam_total_minutes) / 60)
        remaining_minutes = (exam_total_minutes - arrival_total_minutes) % 60
        print(f"{remaining_hours}:{remaining_minutes:02d} hours after the start")
    else :
        print(f"{arrival_total_minutes - exam_total_minutes:02d} minutes after the start")
