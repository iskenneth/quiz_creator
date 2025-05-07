
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
    for options in range (0, len(lines), 6):
        question_text = lines[options].strip().split(":")[1].strip()
        choice_a = lines[option + 1].strip().split(":")[1].strip()
               choice_b = lines[option + 1].strip().split(":")[1].strip()
               choice_c = lines[option + 1].strip().split(":")[1].strip()
               choice_d = lines[option + 1].strip().split(":")[1].strip()
               correct_answer = lines[option + 5].strip().split(":")[1].strip()
               
               choices = [choice_a, choice_b, choice_c, choice_d]
               question = Question(question_text, choices, correct_answer)

               
        

        
