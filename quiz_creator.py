#Ask the user to input the question and 4 choices for answer
question = input("Enter your question: ")
choice_a = input("Enter answer for choice a: ")
choice_b = input("Enter answer for choice b: ")
choice_c = input("Enter answer for choice c: ")
choice_d = input("Enter answer for choice d: ")
correct_answer = input("What is the letter of the correct answer?: ") #Ask the user to confirm the correct answer
#Save the question+correct asnwer to .txt file 
with open('quiz_data.txt' , 'a') as file:
    file.write(f" Question: {question} \n")
#Ask user if they want to input another question
#If yes loop the program, if no break