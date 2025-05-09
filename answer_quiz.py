import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

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
        self.questions = load_question_from_file('quiz_data.txt')
        
        self.layout = BoxLayout (orientation = 'vertical')
        self.question_label = Label( text = "These are the Questions")
        self.layout.add_widget(self.question_label)
        
        self.buttons_layout = GridLayout(cols=1)
        self.layout.add_widget(self.buttons_layout)
        
        self.button_next = Button(text="Proceed_to_next_Question", on_press=self.next_question)
        self.layout.add_widget(self.button_next)
       
        self.project_question()
        return self.layout
        
    def project_question(self):
            tanong = self.questions[self.question_count]  
            self.question_label.text = tanong.text_question
            
            self.buttons_layout.clear_widgets()
            
            choice_list = list(tanong.choices.items())
            random.shuffle(choice_list)
            
            label_map = {}
            options = ['a', 'b', 'c', 'd']
            
            for letters, (original_label, choice_text) in enumerate(choice_list): 
                label_map[options [letters]] = original_label
                option_button = Button(text=f"{options[letters]}. {choice_text}", on_press=lambda instance, label=options[letters]: self.check_answer(label))

                self.buttons_layout.add_widget(option_button)
            
    def check_answer(self, selected_label):
         tanong = self.questions[self.question_count]
         if selected_label == tanong.correct_answer:
                self.score +=1
                self.show_popup("Correct!!", "on to the next one")
         else:
                self.show_popup("Wrong!!",  f"correct answer is {tanong.correct_answer}")  
                
    def next_question(self, instance):
        self.question_count += 1
        if self.question_count < len(self.questions):
            self.project_question()
        else:
            self.show_score()            
   
    def show_score(self):
         score_message = f"Your final score is: {self.score}/{len(self.questions)}"    
         self.show_popup("Done....", score_message)
         
    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 400)) 
        popup.open()        
         
if __name__ == '__main__':
    QuizApp().run()
       