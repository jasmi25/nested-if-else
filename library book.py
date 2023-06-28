#Your local library needs your help! Given the expected and actual return dates
#for a library book, create a program that calculates the fine (if any). The fee
#structure is as follows:
#1. If the book is returned on or before the expected return date, no fine will
#be charged (i.e.: fine = 0).
#2. If the book is returned after the expected return. but still within the same
#calendar month and year as the expected return date, fine = Rs.15 * number of
#days late.
#3. If the book is returned after the expected return month but still within the
#same calendar year as the expected return date, the fine = Rs.500 * number of
#days late.
#4. If the book is returned after the calendar year in which it was expected,
#there is a fixed fine of Rs.10,000.
e_rd=int(input("enter e_day: "))
e_rm=int(input("enter e_month: "))
e_ry=int(input("enter e_year: "))
rd=int(input("enter r_day: "))
rm=int(input("enter r_month: "))
ry=int(input("enter r_year: "))
if e_rm==rm and e_ry==ry:
    if rd<=e_rd:
        print("no charge")
    elif rd>e_rd:
        late_d=rd-e_rd
        fine=15*late_d
        print("late_d=",late_d)
        print("fine=",fine)
    else:
        print("nothing")
elif e_rm<rm and ry==e_ry:
    if rd>=e_rd or e_rd>rd:
            late_d=e_rd-rd
            late_m=(rm-e_rm)*30
            total_late=late_m-late_d
            fine=500*total_late
            print("late_m=",total_late)
            print("fine=",fine)
    else:
            print("no fine")
elif rm==e_rm and ry>e_ry:
    if rd==e_rd:
            fine=10000
            print("fixed fine is",fine)
else:
     print("no fixed fine")
    
