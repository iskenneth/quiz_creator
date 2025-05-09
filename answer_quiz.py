import random

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
               
               choices =  {
                   'a' = choices_a,
                   'b' = choices_b,
                   'c' = choices_c,
                   'd' = choices_d
               }
               tanong = Question(question_text, choices, correct_answer)
               question.append(tanong)              
    random.shuffle(question)         
    return question
    
    def take_quiz(question):
        score = 0
        
        for tanong in question:
            print("\n" + tanong.text)
            
            choice_list = list(tanong.choice.items())
            random.shuffle(choice_list)
            
            label_map = {}
            display_labels = ['a', 'b', 'c','d']
            
            for i, (original_label, choice_text) in enumerate(choice_list):
                label_map[display_labels [i]] = original_label
                print(f"{display_labels[i]}.) {choice_text}")
                
            user_input = input("What is your answer (a/b/c/d)").lower()           
            
            if user_input in label map:
                selected_label = label_map[user_input]
                if selected_label == question.correct_anwer:
                    print ("Your answer is correct!!")
                    score +=1
                else:
                    print(f"Wrong!!, correct answer is {question.correct_amswer')      
            else:
                print("Error!!")      
                      
print(f"\n Your final score is: {score}/{len(question)}")                  
                                            
                                            
                                           
                    
                    
    
    
    
 
    
                                  
     
               

               
        

        
