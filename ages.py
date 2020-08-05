# Viata Fredericks Class1
from tkinter import *

# Raises an exception error and exit if the age anything other than in integer
try:
    age = int(input("Please enter your age:\n"))
except ValueError:
    print("Value error occurred. Please enter an integer next time!")
    exit()
except EOFError:
    print("EOFError occurred. Please enter an integer next time!")
    exit()
except TypeError:
    print("Type error occurred. Please enter an integer next time!")
    exit()


# This function is to verify the age of the contestant
def verify_age(user_age):
    # doctest used to test if it works
    """
    >>> verify_age(34)
    Get ready to play!
    """
# If the users age is less than 18, it will stop running
    if user_age < 18:
        print("You are underage, please come back when you are 18 or above.\n")
        exit()

    # A message will pop up if the user is older than 18
    else:
        print("Get ready to play!")
        popup = Tk()
        popup.title("Lottery Number Challenge")
        label = Label(popup, text='Welcome to the Ithuba National Lottery of South Africa!', width=50, height=10)
        label.pack()
        button = Button(popup, text="Okay", command=popup.destroy, )
        button.pack(side="top", pady=10)
        popup.mainloop()

