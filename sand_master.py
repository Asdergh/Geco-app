import pandas as pd
import numpy as np
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
        
        try:
            self.file_name = "GecoData.csv" # TODO: перейти на csv        
            self.GecoBase = pd.read_csv(self.file_name)
            self.GecoBase = self.GecoBase.iloc[:, [1, 2, 3, 4]]
            #pd.read_csv(self.file_name)
        except BaseException:
            self.file_name = "GecoData.csv"
            with open("GecoData.csv", "w") as file:
                pass
            self.GecoBase = pd.DataFrame({"Body_lenght": [], "Tail_lenght": [], "Weight": [], "Age_Label": []})
        self.figure = plt.figure()
        self.surface = self.figure.add_subplot()


    def load_data(self, *argv): 
        print(self.GecoBase)       
        self.GecoBase.loc[f"{argv[4]}"] = np.array([argv[0], argv[1], argv[2], argv[3]])
        print(self.GecoBase)
    
    def load_to_file(self, value):
        self.GecoBase.to_csv(self.file_name)



            
    def graphs(self, graph_type=True):
        
        self.weight = self.GecoBase.iloc[:, 2].to_numpy()
        self.labels = self.GecoBase.iloc[:, 3].to_numpy()
        print(self.weight, self.labels)
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
        self.flag = True
        self.orientation = "vertical"
        super(Geco_layout, self).__init__(**kwargs)
        self.geco_number = self.GecoBase.to_numpy().shape[0]
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

    # TODO: исправить! Использовать self.
    def add_data(self, value):

        self.load_data(int(self.body_lenght.text), int(self.tail_lenght.text), 
                    int(self.weight.text), int(self.age.text), self.geco_number)
        """except BaseException :
            self.load_data(body_lenght=int(self.body_lenght[-1]), tail_lenght=int(self.tail_lenght[-1]),
                                weight=int(self.weight[-1]), age_label=int(self.age_label[-1]), number=self.geco_number)"""
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

DB = pd.read_csv("GecoData.csv")
print(DB.iloc[:, [1, 2, 3, 4]])
