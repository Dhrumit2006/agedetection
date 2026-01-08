year1=int(input("Enter Your Birth Year:"))
month1=int(input("Enter Your Birth Month:"))
date1=int(input("Enter Your Birth Date:"))

import calendar

days_in_month=calendar.monthrange(year1,month1)[1]


from datetime import datetime
day=datetime.now().day
month=datetime.now().month

year=datetime.now().year

a=year-year1
b=month-month1
c=day-date1

if month1 > 12 or date1 > 31:
    print("Invalid Input.")
else:
    print("")


if (year1%400==0):
    if(month1==2 and date1>29):
        print("Invalid Date.")
    else:
        print("")
else:
    if(month1==2 and date1>28):
        print("Invalid Date")
    else:
        print("")


if b==0 and c<30 and c!=0:
    po=abs(c)

    print(f"{po} days left to your {a} birthday")

elif b==0 and c==0:
    print("Yayyyy !!")
    print("Today is your birthday")
    print(f"Chapter {a} unfolded...!!")
else:
    po2=abs(b)
    print(f"Your Birthday is approximately {po2}  months away")


if c<0:
    b-=1
    previous_month=month-1 or 12
    c+=days_in_month

   
if b<0:
    a-=1
    b+=12

print("Your Exact age is ")
print(a,"years")

if b==0 and c==0:
    print("")
else:
    print(b,"months")
    print(c,"days")





