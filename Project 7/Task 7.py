#math.random call krva kr 1-100 ki value call krvani h aur value ke basis check kro >18 to eligible using decorators.

import random

def check_age(func):


    def wrapper():
        age = random.randint(10, 20)
        print(f"Generated Age: {age}")
        if age > 18:
            func(age)
        else:
            print("Not Eligible")

    return wrapper

@check_age
def eligibility(age):
    print("✅ Eligible for Job")
eligibility()