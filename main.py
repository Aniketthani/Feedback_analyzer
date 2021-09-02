from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.toast import toast
from predict import make_prediction
import re

KV = '''
MDBoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: "Feedback Analyzer"
        
        
        elevation: 10
        
        Image:
            source:'images/logo.png'
            size_hint_x:0.1
            pos_hint:{'x':1}
            
            

    MDFloatLayout:

        MDTextFieldRound:
            id:feedback
            icon_left: 'email'
            normal_color: app.theme_cls.accent_color
            pos_hint:{'center_x':0.5,'center_y':0.8}
            size_hint:0.7,0.05
            hint_text: 'Enter Feedback To Classify'

        MDRaisedButton:
            text: "Submit"
            font_size: "18sp"
            pos_hint:{'center_x':0.5,'center_y':0.7}
            on_press:app.run_model()

        MDChip:
            id:prediction
            text:"Prediction : None"
            pos_hint:{'center_x':0.3,'center_y':0.5}
            font_size: "38sp"
            icon:''
            text_color:1,1,1,1
            color:0,0,1,1
            


        

        MDRaisedButton:
            text:'Clear All'
            font_size:'18sp'
            pos_hint:{'center_x':0.5,'center_y':0.2}
            on_press:app.clear_all()
            

'''


class Example(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        

    

    def build(self):
        self.theme_cls.primary_palette="DeepPurple"
        return Builder.load_string(KV)



    def run_model(self,*args):
        if self.root.ids.feedback.text:
            data={
                'data': [[self.root.ids.feedback.text]],
            }
            inferrence=make_prediction(data).split(":")[1].split("]")[0][2]
            
            result="None"
            if inferrence=="0":
                result="Negative Feedback"
                self.root.ids.prediction.color=(1,0,0,1)
                self.root.ids.prediction.text_color=(0,0,0,1)
            elif inferrence=="1":
                result="Positive Feedback"
                self.root.ids.prediction.color=(0,1,0,1)
                self.root.ids.prediction.text_color=(0,0,0,1)
            print(inferrence)
            self.root.ids.prediction.text=f"Prediction : {result}"
        else:
            toast("Please enter a feedback")


    
    def clear_all(self,*args):
        self.root.ids.prediction.text="Prediction : None"
        self.root.ids.feedback.text=""
        self.root.ids.prediction.text_color=(1,1,1,1)
        self.root.ids.prediction.color=(0,0,1,1)


Example().run()
