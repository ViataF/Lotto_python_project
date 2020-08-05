# Viata Fredericks class 1
import ages
import lotto_num
import counting
import datetime

# Inputs of all modules
counter = 0
current_date = datetime.date.today()


# Calling functions from p3 and p1
ages.verify_age(ages.age)
# creating an object in order to print results of class Results
objPrize = counting.Results(counter)

# open text file mini_projects
file = open("Mini_project.txt", "a+")

# writes in this results in the file
file.write("\ncurrent date:"+str(current_date)+"\n")
file.write(input("Please enter your name:\n"))
file.write("\nThe numbers you have chose:" + str(lotto_num.user_pick()) + "\n")
file.write("Lottery numbers are:" + str(lotto_num.lottery_numbers()) + "\n")
file.write("\nNumber of guesses correct:"+str(objPrize.count()) + "\n")
file.write("You won: R" + str(objPrize.prize_won() + "\n"))
# close the file!!
file.close()

# Opens file and reads it
file = open("Mini_project.txt", "r")
print(file.read())
file.close()

print("\nThank you for playing with Ithuba National Lottery of South Africa! \n Hope to see you soon!")
