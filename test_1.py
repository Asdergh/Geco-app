import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json as js
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label



class Data_Analyse():

    def __init__(self) -> None:
        
        self.file_name = "GecoData.json"
        self.GecoBase = pd.DataFrame({"BodyLenght": [], "TailLenght" : [], "Weight": [], "AgeLabel": []})
        self.json_data = self.GecoBase.to_json()
        self.json_data = js.loads(self.json_data)
        self.figure = plt.figure()
        self.surface = self.figure.add_subplot()

        



    def load_data(self, body_lenght, tail_lenght, weight, age_label, number=0):
        
        self.GecoBase.loc[f"geco_number{number}"] = np.array([body_lenght, tail_lenght, weight, age_label])
        print(self.GecoBase)

    
    def load_to_file(self, value):
        
        try:
            with open(self.file_name, "r") as file:
                self.FileData = pd.read_json(file)
                #self.FileData = js.loads(self.FileData.to_json())
                self.json_data = self.GecoBase.to_numpy()
                general_data = np.vstack((self.json_data, self.FileData.to_numpy()))
                print(general_data)
                self.json_data = pd.DataFrame(general_data)
                self.json_data = self.json_data.to_json()
                self.json_data = js.loads(self.json_data)


            
            with open(self.file_name, "w") as file:
                js.dump(self.json_data, file)

        except BaseException:
            print("error")
            with open(self.file_name, "w") as file:
                print(self.GecoBase)
                self.json_data = self.GecoBase.to_json()
                self.json_data = js.loads(self.json_data)
                js.dump(self.json_data, file)
            

            
    def graphs(self, value, graph_type="plot"):
        
        try:
            self.weight = np.asarray(self.FileData.iloc[:, 2])
            self.labels = np.asarray(self.FileData.iloc[:, 3])

        except BaseException:
            self.weight = np.asarray(self.GecoBase.iloc[:, 2])
            self.labels = np.asarray(self.GecoBase.iloc[:, 3])

        self.colors = ["blue", "red", "green"]
        if graph_type == "plot":
            for (index, label) in enumerate(np.unique(self.labels)):
                self.surface.plot(range(0, len(self.weight[self.labels==label])), self.weight[self.labels==label],
                                    color=self.colors[index], alpha=0.3, label=f"возврастная категория номер: [{label}]")
        
        elif graph_type == "histo":
            for (index, label) in enumerate(np.unique(self.labels)):
                self.surface.hist(self.weight[self.labels==label], 20, color=self.colors[index], 
                                label=f"возврастная категория номер: [{label}]", alpha=0.3)
        
        plt.legend(loc="upper left")
        plt.show()



class Geco_layout(BoxLayout, Data_Analyse):
    def __init__(self, **kwargs):
        self.geco_number = 0
        self.orientation = "vertical"
        super(Geco_layout, self).__init__(**kwargs)
        self.add_widget(Label(text="geco body lenght"))
        self.body_lenght = TextInput()
        self.add_widget(self.body_lenght)
        self.add_widget(Label(text="geco tail lenght"))
        self.tail_lenght = TextInput()
        self.add_widget(self.tail_lenght)
        self.add_widget(Label(text="weight"))
        self.weight = TextInput()
        self.add_widget(self.weight)
        self.add_widget(Label(text="age"))
        self.age = TextInput()
        self.add_widget(self.age)
        self.add_widget(Label(text="number"))
        self.data_base_button = Button(text="add data in database!!!")
        self.graph_button = Button(text="get a graph!!!")
        self.file_button = Button(text="load all data to a file!!!")
        self.add_widget(self.data_base_button)
        self.add_widget(self.file_button)
        self.add_widget(self.graph_button)
        self.data_base_button.bind(on_press=self.add_data)
        self.file_button.bind(on_press=self.load_to_file)
        self.graph_button.bind(on_press=self.graphs)

        
        
    def add_data(self, value):
        if type(self.body_lenght) == list:
            self.load_data(body_lenght=int(self.body_lenght[-1]), tail_lenght=int(self.tail_lenght[-1]),
                                weight=int(self.weight[-1]), age_label=int(self.age_label[-1]), number=self.geco_number)
        else:       
            self.load_data(body_lenght=int(self.body_lenght.text), tail_lenght=int(self.tail_lenght.text), 
                        weight=int(self.weight.text), age_label=int(self.age.text), number=self.geco_number)
        print(type(self.body_lenght))
        self.geco_number += 1
    
class Geco_app(App):
     def build(self):
        return Geco_layout()
     
if __name__ == "__main__":
    Geco_app().run()
    


                

                   
              
         

         
          