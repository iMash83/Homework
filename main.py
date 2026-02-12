age = int(input("Enter your age: >>>"))
citizenship = input("Where are you from?")  
if age >= 18 and citizenship == "UA":
    print("Here is your beer")
elif age >=21 and citizenship == "US":
    print("Here is your beer")
else:
    print("Sorry, you can't have beer")