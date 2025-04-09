from kivy.app import app
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button 
from kivy.uix.spinner import Spinner

    #Save the question+correct asnwer to .txt file 
def convert_to_txt (question, choice_a, choice_b,choice_c, choice_d, correct_answer): 
    with open('quiz_data.txt' , 'a') as file:
        file.write(f" Question: {question} \n")
        file.write(f" a.): {choice_a} \n")
        file.write(f" b.): {choice_b} \n")
        file.write(f" c.): {choice_c} \n")
        file.write(f" d.): {choice_d} \n")
        file.write(f" Correct Answer: {correct_answer} \n")

class QuizCreator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)  #arranging buttongs vertically
        self.question_input = TextInput(hint_text="Enter your question", multiline=False)
