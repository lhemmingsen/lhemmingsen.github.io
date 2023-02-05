quiz = "Welcome to my quiz. "
print(quiz)

startquiz = input("Would you like to begin? ").upper()
if  startquiz != "YES":
    quit() 

print(startquiz)
score = 0

question = input("What year is it currently? ")
if question == "2023":
    print("Correct. ")
    score += 1
else:
    print("Incorrect. The correct answer is 2023. ")

question = input("What is the current month? ")
if question.upper() == "FEBRUARY":
    print("Correct. ")
    score += 1
else:
    print("Incorrect. The correct answer is FEBRUARY. ")

question = input("Last question. Is this a quiz made using Python? ")
if question.upper() == "YES":
    print("Correct. ")
    score += 1
else:
    print("Incorrect. This quiz IS made using Python code. ")

print("You have finished the quiz. Here is your score: ")
print(score)
