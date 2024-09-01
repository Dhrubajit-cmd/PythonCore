# In this exercise we shall create Kaun Banega CrorePati Command.
# Question :
# Create a program capable of displaying questions to users like KBC.
# Use list data-type to store the quesitons and their correct answers.
# Display the final amount this player is taking home after playing the game.

# Let's start :
questions = ["1.Who was the Prime Minister of India from 2014-2019",
             "2. The International Literacy Day is observed on",
             "3.The language of Lakshadweep a Union Territory in India is",
             "4.Bahubali Festival is related to",
             "5.In which group of places the Kumbha Mela is held every twelve years"]
answers = ["Shri Narendra Damodardas Modi","September 8","Malayalam","Jainism","Prayagraj,Haridwar,Ujjain,Nasik"]
print("Welcome to KBC. \n")
for i in questions:
    # print(i)
    if i == questions[0]:
        print(questions[0])
        m = input("Enter your answer: \n")
        if (m == answers[0]):
            win1 = 5000
            print(f"Congratulations.You have won Rs.{win1}. \n")
            balance1 = win1
        else:
            balance1 = 0
            total = balance1
            print(f"You won a  total balance of Rs.{total}. \n")
            break
    elif i == questions[1]:
        print(questions[1])
        m = input("Enter your answer: \n")
        if (m == answers[1]):
            win2 = 10000
            print(f"Congratulations.You have won Rs.{win2}. \n")
            balance2 = win2
        else:
            balance2 = 0
            total = balance1 + balance2
            print(f"You won a  total balance of Rs.{total}. \n")
            break
    elif i == questions[2]:
        print(questions[2])
        m = input("Enter your answer: \n")
        if (m == answers[2]):
            win3 = 50000
            print(f"Congratulations.You have won Rs.{win3}. \n")
            balance3 = win3
        else:
            balance3 = 0
            total = balance1 + balance2 + balance3
            print(f"You won a  total balance of Rs.{total}. \n")
            break
    elif i == questions[3]:
        print(questions[3])
        m = input("Enter your answer: \n")
        if (m == answers[3]):
            win4 = 100000
            print(f"Congratulations.You have won Rs.{win4}. \n")
            balance4 = win4
        else:
            balance4 = 0
            total = balance1 + balance2 + balance3 + balance4
            print(f"You won a  total balance of Rs.{total}. \n")
            break
    elif i == questions[4]:
        print(questions[4])
        m = input("Enter your answer: \n")
        if (m == answers[4]):
            win5 = 10000000
            print(f"Congratulations.You have won Rs.{win5}. \n")
            balance5 = win5
            # print(f"Your current balance is Rs.{balance5}. \n")
            total = balance1 + balance2 + balance3 + balance4 + balance5
            print(f"You won a  total balance of Rs.{total}. \n")
        else:
            balance5 = 0
            total = balance1 + balance2 + balance3 + balance4 + balance5
            print(f"You won a  total balance of Rs.{total}. \n")
print("Thank you for playing KBC. \n")
