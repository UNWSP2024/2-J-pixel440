
def average_age():
    age_1 = int(input("Enter the age of friend 1: "))
    age_2 = int(input("Enter the age of friend 2: "))
    age_3 = int(input("Enter the age of friend 3: "))
    age_4 = int(input("Enter the age of friend 4: "))
    age_5 = int(input("Enter the age friend 5: "))


total_of_ages = (age_1 + age_2 + age_3 + age_4 + age_5)

average=total_of_ages/5.0

print("Average age is:",average)

# Line which calls the above function.
average_age()
