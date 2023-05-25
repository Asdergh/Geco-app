import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import sys

sys.setrecursionlimit(1500)



import json as js

class Data_An():
    def __init__(self) -> None:
        
        self.file_name = "enother_data.json"
        self.figure = plt.figure()
        self.axis_3d = self.figure.add_subplot(projection="3d")
        self.axis_2d = self.figure.add_subplot()
        self.data = pd.DataFrame({"Body_lenght": [], "Tail_lenght": [], "Weight": [], "Class_age": []})
    
    def add_element(self, body_lenght=None, tail_lenght=None, 
                    weight=None, cls_age=None, number=None):
        flag = False
        try:
            with open(self.file_name, "r") as file:
                self.File_Data = pd.read_json(file)
                self.File_Array = self.File_Data.iloc[:, [0, 1, 2, 3]].to_numpy()

            with open(self.file_name, "w") as file:
                    self.data.loc[f"obj{number}"] = [body_lenght, tail_lenght, weight, cls_age]
                    self.json_data = self.data.to_json()
                    self.array_data = self.data.iloc[:, [0, 1, 2]].to_numpy()
                    self.json_data = js.loads(self.json_data)
                    self.json_data.update(self.File_Data)
                    js.dump(self.json_data, file)

        except BaseException:
            with open(self.file_name, "w") as file:
                self.data.loc[f"obj{number}"] = [body_lenght, tail_lenght, weight, cls_age]
                self.json_data = self.data.to_json()
                self.json_data = js.loads(self.json_data)
                flag == True
                js.dump(self.json_data, file)

    #show the data that we workiing with
    def visualise_data(self, graph_type=None):
        self.label = self.File_Array[:, 3]
        self.markers = ["v", "2", "^", "o", "v"]
        self.colors = ["gray", "red", "green", "blue", "y"]

        if graph_type == None:
            for (index, cls) in enumerate(np.unique(self.label)):
                self.axis_3d.scatter(self.File_Array[self.label==cls, 0], self.File_Array[self.label==cls, 1], self.File_Array[self.label==cls, 2],
                        color=self.colors[index], marker=self.markers[index], alpha=0.3, label=f"label: {index}")
        elif graph_type == "plot":
            self.weight = self.File_Array[:, 3]
            for (index, cls_age) in enumerate(np.unique(self.label)):
                self.axis_2d.plot(range(len(self.File_Array[self.label==cls_age, 3])), self.File_Array[self.label==cls_age, 3],
                                   color=self.colors[index], marker=self.markers[index], label=f"age group: {cls_age}")
        
        plt.legend(loc="upper left")
        plt.show()
            

class Geco_layout(BoxLayout, Data_An):
    def __init__(self, **kwargs):
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
        self.geco_number = TextInput()
        self.add_widget(self.geco_number)
        self.button_1 = Button(text="add data in database!!!")
        self.button_2 = Button(text="get a graph")
        self.add_widget(self.button_1)
        self.button_1.bind(on_press=self.add_data)
    def add_data(self, value):
        self.add_element(body_lenght=self.body_lenght, tail_lenght=self.tail_lenght, 
                         weight=self.weight, number=self.geco_number, cls_age=self.age)
class Geco_app(App):
     def build(self):
        return Geco_layout()
     
if __name__ == "__main__":
    Geco_app().run()

"""param_one_distrib = np.random.normal(12, 0.23, size=400)
param_two_distrib = np.random.normal(10, 3.5, size=400)
param_thre_distrib = np.random.normal(13, 4.5, size=400)
data = np.array([param_one_distrib, param_two_distrib, param_thre_distrib]).T
i = 0
print(data)
for (index, elem) in enumerate(data):
    obj.add_element(body_lenght=float(elem[0]), tail_lenght=float(elem[1]), weight=float(elem[2]), cls_age=rd.randint(0, 3), number=index)
obj.visualise_data(graph_type="plot")"""



#obj.preper_Data()
#obj.network_fit()

            



            



