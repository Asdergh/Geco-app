import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import json as js

class Data_An():
    def __init__(self, file_name) -> None:

        self.figure = plt.figure()
        self.axis_3d = self.figure.add_subplot(projection="3d")
        self.data = pd.DataFrame({"Param_one": [], "Param_two": [], "Param_three": [], "Class_label": []})
        self.file_name = file_name
    
    def add_element(self, param_1=None, param_2=None, 
                    param_3=None, cls=None, number=None):
        flag = False
        try:
            with open(self.file_name, "r") as file:
                self.File_Data = pd.read_json(file)
                self.File_Array = self.File_Data.iloc[:, [0, 1, 2, 3]].to_numpy()

            with open(self.file_name, "w") as file:
                    self.data.loc[f"obj{number}"] = [param_1, param_2, param_3, cls]
                    self.json_data = self.data.to_json()
                    self.array_data = self.data.iloc[:, [0, 1, 2]].to_numpy()
                    self.json_data = js.loads(self.json_data)
                    self.json_data.update(self.File_Data)
                    js.dump(self.json_data, file)

        except BaseException:
            with open(self.file_name, "w") as file:
                self.data.loc[f"obj{number}"] = [param_1, param_2, param_3, cls]
                self.json_data = self.data.to_json()
                self.json_data = js.loads(self.json_data)
                flag == True
                js.dump(self.json_data, file)

    def visualise_data(self):
        self.markers = ["v", "2", "^", "o", "v"]
        self.colors = ["gray", "red", "green", "blue", "y"]
        label = self.File_Array[:, 3]
        for (index, cls) in enumerate(np.unique(label)):
            self.axis_3d.scatter(self.File_Array[label==cls, 0], self.File_Array[label==cls, 1], self.File_Array[label==cls, 2],
                    color=self.colors[index], marker=self.markers[index], alpha=0.3, label=f"label: {index}")
        plt.legend(loc="upper left")
        plt.show()

obj = Data_An(file_name="enother_data.json")

param_one_distrib = np.random.normal(12, 0.23, size=400)
param_two_distrib = np.random.normal(10, 3.5, size=400)
param_thre_distrib = np.random.normal(13, 4.5, size=400)
data = np.array([param_one_distrib, param_two_distrib, param_thre_distrib]).T
i = 0
print(data)
for (index, elem) in enumerate(data):
    obj.add_element(param_1=float(elem[0]), param_2=float(elem[1]), param_3=float(elem[2]), cls=rd.randint(0, 3), number=index)
obj.visualise_data()



#obj.preper_Data()
#obj.network_fit()

            



            



