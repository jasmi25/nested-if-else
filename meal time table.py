#Take two user inputs one as day and one as meal time. Show the following
#table using nested if statements :
#1. Day = Monday
#Breakfast = Poori Sabzi
#Lunch = Sambhar Rice
#Dinner = Chicken Rice
#2. Day = Tuesday
#◦ Breakfast = Poha
#◦ Lunch = Rajma Rice
#dinner=roti sabji
day=input("enter day")
time=input("enter time")
if day=="monday":
    if time=="morning breakfast":
        print("poori sabji")
    elif time=="afternoon lunch":
        print("sambher")
    elif time=="evening dinner":
        print("Chicken Rice")
    else:
        print("none")
elif day=="tuesday":
    if time=="morning breakfast":
        print("poha")
    elif time=="afternoon lunch":
        print("rajma rice")
    elif time=="evening dinner":
        print("roti sabji")
    else:
        print("nothing")
        
