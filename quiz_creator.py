from kivy.app import App
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
        super().__init__(orientation='vertical', **kwargs)  #arranging buttons vertically
     
        self.question_input = TextInput(hint_text="Enter your question", multiline=False)
        self.add_widget(self.question_input)
           
        self.choice_a_input = TextInput(hint_text="Enter answer for choice A", multiline=False)
        self.add_widget(self.choice_a_input)

        self.choice_b_input = TextInput(hint_text="Enter answer for choice B", multiline=False)
        self.add_widget(self.choice_b_input)

        self.choice_c_input = TextInput(hint_text="Enter answer for choice C", multiline=False)
        self.add_widget(self.choice_c_input)

        self.choice_d_input = TextInput(hint_text="Enter answer for choice D", multiline=False)
        self.add_widget(self.choice_d_input)
    
        self.answer_spinner = Spinner(
            text = "Select correct answer",
            values = ('a', 'b', 'c', 'd')
        )
        self.add_widget(self.answer_spinner)
        
        save_button = Button(text = "Save Question")
        save_button.bind(on_pres=self.save_question)
        self.add_widget(save_button)
        
        self.feedback = Label(text = "")
        self.add_widget(self.feedback)
        
    def save_question(self, instance):
        question = self.question_input.text
        choice_a = self.choice_a_input.text
        choice_b = self.choice_b_input.text
        choice_c = self.choice_c_input.text
        choice_d = self.choice_d_input.text
        correct_answer = self.correct_answer_spinner.text
        
        if correct_answer not in ('a', 'b', 'c', 'd'):
            self.feedback.text = "[ERROR 404!!] Select a valid correct answer."
            return
        
        convert_to_txt(question, choice_a, choice_b, choice_c, choice_d, correct_answer)
        self.feedback.text = "[SAVED] Question added successfully!"
        
        self.question_input.text = ""
        self.choice_a_input.text = ""
        self.choice_b_input.text = ""
        self.choice_c_input.text = ""
        self.choice_d_input.text = ""
        self.correct_answer_spinner.text = ""
        
class QuizApp(App):
    def build(self):
      return  QuizCreator()
      
if __name__ == "__main__":
    QuizApp().run()                            
        