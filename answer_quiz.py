#Create a new question 
class Question:
    def __init__(self, text_question, choices, correct_answer):
        self.text_question = text_question
        self.choices = choices
        self.correct_answer = correct_answer
        
    def is_correct (self, answer):
        return self.correct_answer == answer
        
#When creating: a. Ask for the question text  b. Ask for 4 choices (A, B, C, D) c. Ask which letter is the correct answer
# Store the question text, choices, and correct answer
#Show the question and choices to the user
#Ask the user to enter their answer
#Compare the user's answer to the correct answer
# If the answer is correct, say "Correct!" Else, say "Wrong"  