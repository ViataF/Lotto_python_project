# Viata Fredericks Class 1
import lotto_num
guess=0

# Class that contains the results for lotto. What user wins and how many guesses are right
class Results:
    def __init__(self, counter):
        self.counter = counter

# the counter will increase by 1 every time a user number and lotto number are the same
    def count(self):
        for number in lotto_num.users_numbers:
            if number in lotto_num.lotto_numbers:
                self.counter += 1
        return self.counter

# This is what is won if the user_number is equal to the lotto number
    def prize_won(self):
        if self.counter == 6:
            return 10000000
        elif self.counter == 5:
            return 8584
        elif self.counter == 4:
            return 2384
        elif self.counter == 3:
            return 100.50
        elif self.counter == 2:
            return 20
        else:
            return "0, try again next time"


