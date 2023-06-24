import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json as js
from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


plt.style.use("seaborn")
class Data_Analyse():

    def __init__(self) -> None:
        
        self.file_name = "GecoData.text"
        self.GecoBase = pd.DataFrame({"BodyLenght": [], "TailLenght" : [], "Weight": [], "AgeLabel": []})
        self.json_data = self.GecoBase.to_json()
        self.json_data = js.loads(self.json_data)
        self.figure = plt.figure()
        self.surface = self.figure.add_subplot()

        self.data = []
        with open(self.file_name, "r") as file:
            for string in file.readlines():
                tmp_array = string.split("\t")
                self.data.append([int(tmp_array[0]), int(tmp_array[1]), int(tmp_array[2]), int(tmp_array[3])])
        self.data = np.asarray(self.data)

        



    def load_data(self, body_lenght, tail_lenght, weight, age_label, number=0):
        
        self.GecoBase.loc[f"geco_number{number}"] = np.array([body_lenght, tail_lenght, weight, age_label])
        print(self.GecoBase)

    
    def load_to_file(self, value):
        
        with open(self.file_name, "a") as file:
            self.data = self.GecoBase.to_numpy()
            for item in self.data:
                file.write(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\n")


            
    def graphs(self, graph_type=True):
        
        self.weight = self.data[:, 2]
        self.labels = self.data[:, 3]
        print(self.labels)
        self.colors = ["blue", "red", "green"]
        if graph_type:
            for (index, label) in enumerate(np.unique(self.labels)):
                plt.plot(range(0, len(self.weight[self.labels==label])), self.weight[self.labels==label],
                                    color=self.colors[index], alpha=0.3, label=f"возврастная категория номер: [{label}]")
        
        else:
            for (index, label) in enumerate(np.unique(self.labels)):
                plt.hist(self.weight[self.labels==label], 20, color=self.colors[index], 
                                label=f"возврастная категория номер: [{label}]", alpha=0.3)
        
        plt.legend(loc="upper left")
        plt.show()



class Geco_layout(BoxLayout, Data_Analyse):
    def __init__(self, **kwargs):
        self.geco_number = 0
        self.flag = True
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
        self.turn_button = Button(text="turn graph type [histo/curve]")
        self.add_widget(self.data_base_button)
        self.add_widget(self.file_button)
        self.add_widget(self.graph_button)
        self.add_widget(self.turn_button)
        self.data_base_button.bind(on_press=self.add_data)
        self.file_button.bind(on_press=self.load_to_file)
        self.graph_button.bind(on_press=self.graph)
        self.turn_button.bind(on_press=self.turn_graph_type)
        self.Geco_data = MDDataTable(
            column_data=[("Body_lenght", dp(30)), ("Tail_lenght", dp(30)), ("Weight", dp(30)), ("Age Label", dp(30))],
            row_data = [(f"{item[0]}", f"{item[1]}", f"{item[2]}", f"{item[3]}") for (index, item) in enumerate(self.data)]
        )
        self.add_widget(self.Geco_data)        
        
    def add_data(self, value):
        if type(self.body_lenght) == list:
            self.load_data(body_lenght=int(self.body_lenght.text), tail_lenght=int(self.tail_lenght[-1]),
                                weight=int(self.weight[-1]), age_label=int(self.age_label[-1]), number=self.geco_number)
        else:       
            self.load_data(body_lenght=int(self.body_lenght.text), tail_lenght=int(self.tail_lenght.text), 
                        weight=int(self.weight.text), age_label=int(self.age.text), number=self.geco_number)
        print(type(self.body_lenght))
        self.geco_number += 1
    
    def turn_graph_type(self, value):
        if self.flag == True:
            self.flag = False
        else:
            self.flag = True
    
    def graph(self, value):
        self.graphs(graph_type=self.flag)

    
class Geco_app(MDApp):
     
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Geco_layout()
     
if __name__ == "__main__":
    Geco_app().run()
    


                

                   
              
         

         
          