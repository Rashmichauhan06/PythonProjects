from datetime import date
present= date.today()
print("Present date is ", present)

while(True):
    year= int(input("Enter the birth year: \n"))
    month= int(input("Enter the birth month: \n"))
    day=int(input("Enter the birth day: \n"))
    birth= date(year,month,day)

    if year> present.year:
        print("Enter valid year")
        break

    age= present.year - birth.year - ((present.month,present.day) < (birth.month,birth.day))
    print("The age is ", age)
    quit= input("Type q to quit: ").lower()
    if quit == 'q':
        break

