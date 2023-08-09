import random

from art import *
import gamedata

def account_display(account):
    name=account["name"]
    description=account["description"]
    country=account['country']
    return f"{name}, {description}, from {country}"
def check(guess,follower1,follower2):


    if guess==1 and follower1>follower2:

        print(f"You are right\n"
              f"{a1['name']} has {follower1} milloin followers\n"
              f"Where as {a2['name']} has {follower2} million\n")

        con= int(input("Do you want to continue?\n 1.Yes\n2.No\n"))
        if con==2:
            return False

        elif con==1:
            return True
    elif guess==2 and follower1<follower2:


        print(f"You are right\n"
              f"{a1['name']} has {follower1} million followers\n"
              f"Where as {a2['name']} has {follower2} million\n")

        con= int(input("Do you want to continue?\n 1.Yes\n2.No\n"))
        if con==2:
            return False
        elif con==1:
            return True
    elif guess==2 or guess==1 and follower1==follower2:

        print(f"Both {a1['name']} and {a2['name']} have equal followers ")

        con= int(input("Do you want to continue?\n 1.Yes\n2.No\n"))
        if con==2:
            return False

        elif con==1:
            return True
    else:

        print(f"Wrong {a1['name']} has {follower1} million followers\n"
              f"Where as {a2['name']} has {follower2} million followers\n")

        con= int(input("Do you want to continue?\n 1.Yes\n2.No\n"))
        if con==2:
            return False
        elif con==1:
            return True



tprint("Higher-Lower")
a1=random.choice(gamedata.data)
a2=random.choice(gamedata.data)
print(f"Compare1: {account_display(a1)}")
tprint("vs")
print(f"Compare2: {account_display(a2)}")
guess = int(input("Who has more followers 1 or 2: \n"))
follower1= a1["follower_count"]
follower2= a2["follower_count"]



d=check(guess,follower1,follower2)

while d is True:

    a1=a2
    a2=random.choice(gamedata.data)
    print(f"Compare1: {account_display(a1)}")
    tprint("vs")
    print(f"Compare2: {account_display(a2)}")
    guess = int(input("Who has more followers 1 or 2: \n"))
    follower1= a1["follower_count"]
    follower2= a2["follower_count"]
    d=check(guess,follower1,follower2)




















