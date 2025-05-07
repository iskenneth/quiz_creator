#Create a new question 
class Question:
    def __init__(self, text_question, choices, correct_answer):
        self.text_question = text_question
        self.choices = choices
        self.correct_answer = correct_answer
        
    def is_correct (self, answer):
        return self.correct_answer == answer
        
    def load_question_from_file(quiz_data.txt):
        question = []
    with open(quiz_data.txt, 'r') as file:
        lines = file.readlines()
        
