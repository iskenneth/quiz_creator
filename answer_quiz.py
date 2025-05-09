import random
import kivy.app import App
import kivy.uix.label import Label
import kivy.uix.button import Button

class Question:
    def __init__(self, text_question, choices, correct_answer):
        self.text_question = text_question
        self.choices = choices
        self.correct_answer = correct_answer
        
    def is_correct (self, answer):
        return self.correct_answer == answer
        
def load_question_from_file(filename):
    question = []
    with open('quiz_data.txt', 'r') as file:
        lines = file.readlines()
    for options in range (0, len(lines), 6):
        question_text = lines[options].strip().split(":")[1].strip()
        choice_a = lines[options + 1].strip().split(":")[1].strip()
        choice_b = lines[options + 2].strip().split(":")[1].strip()
        choice_c = lines[options + 3].strip().split(":")[1].strip()
        choice_d = lines[options + 4].strip().split(":")[1].strip()
        correct_answer = lines[options + 5].strip().split(":")[1].strip()
               
        choices =  {
            'a' : choice_a,
            'b' : choice_b,
            'c' : choice_c,
            'd' : choice_d
        }
        tanong = Question(question_text, choices, correct_answer)
        question.append(tanong)              
    random.shuffle(question)         
    return question
    
class QuizApp(App):
    def build(self):
        self.question_count = 0
        self.score = 0
        self.question = load_question_from_file('quiz_data.txt')
        
        self.layout = BoxLayout (orientation = 'vertical')
        self.question_label = Label( text = "These are the Questions")
        self.layout.add_widget(self.question_label)
        
        self.buttons_layout = GridLayout(column=1)
        self.add_widget(self.buttons_layout)
        
        self.button_next = Button(text="Proceed to next Question", on_press=self.proceed_to_next_question)
        self.add_widget(self.buttons_next)
        
    def project_question(self):
            tanong = self.questions[self.question_index]  
            self.question_label.text = tanong.text_question
            
            self.buttons_layout.clear_widgets()
            
            choice_list = list(tanong.choices.items())
            random.shuffle(choice_list)
            
            label_map = {}
            options = ['a', 'b', 'c', 'd']
            
            for letters, (original_label, choice_text) in enumerate(choice_list): 
            label_map[options [letters]] = original label
            option_button = Button(text=f"{options[letters]}. {choice_text}",on_press=lambda instances, label=options[letters]: self.check_answer(label))
            self.add_widget(option_button)
            
    def check_answer(self, selected_label):            
            
            
     