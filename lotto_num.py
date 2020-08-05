# Viata Fredericks Class 1
import random
import array as arr

# Lotto_numbers is a list and user_numbers is an array
lotto_numbers = []
users_numbers = arr.array('i', [])


# Function for random lottery_numbers picked, which only picks 6 numbers between 1 and 49
def lottery_numbers():
    for i in range(0, 6):
        lotto_num = random.randint(1, 50)
        while lotto_num in lotto_numbers:
            lotto_num = random.randint(1, 50)
        lotto_numbers.append(lotto_num)
        lotto_numbers.sort()
    return lotto_numbers


# Function that takes user input to guess lotto numbers and sorts the list of numbers in ascending order.
def user_pick():
    for number in range(0, 6):
        try:
            number = int(input("Please enter a number between 1 and 49: "))
        except ValueError:
            print("Value error occurred. Please enter an integer next time!")
            exit()
        except EOFError:
            print("EOFError occurred. Please enter an integer next time!")
            exit()
        except TypeError:
            print("Type error occurred. Please enter an integer next time!")
            exit()
        while number in users_numbers:
            try:
                number = int(input("Please enter a number between 1 and 49: "))
            except ValueError:
                print("Value error occurred. Please enter an integer next time!")
                exit()
            except EOFError:
                print("EOFError occurred. Please enter an integer next time!")
                exit()
            except TypeError:
                print("Type error occurred. Please enter an integer next time!")
                exit()
        users_numbers.append(number)
        users_numbers_sorted = sorted(users_numbers)
    return users_numbers_sorted
