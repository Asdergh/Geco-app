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

        self.ppn = Perceptron(max_iter=40, eta0=0.01, random_state=0)
        self.svc_linear = SVC(C=0.01, gamma=0.2, random_state=0, kernel="linear")
        self.svc_rbf = SVC(C=0.01, gamma=0.2, kernel="rbf", random_state=0)
        self.snn = StandardScaler()

        self.x1 = self.data.iloc[:, [0, 1, 2]].to_numpy()
        self.y = self.data.iloc[:, [3]].to_numpy()

        self.file_name = file_name
    
    def add_element(self, param_1=None, param_2=None, 
                    param_3=None, cls=None, number=None):
        flag = False
        try:
            with open(self.file_name, "r") as file:
                self.File_Data = pd.read_json(file)
                self.File_Data = self.File_Data.to_json()
                print(self.File_Data)

            with open(self.file_name, "w") as file:
                    self.data.loc[f"obj{number}"] = [param_1, param_2, param_3, cls]
                    self.json_data = self.data.to_json()
                    self.json_data = js.loads(self.json_data)
                    self.json_data = self.json_data.update(self.File_Data)
                    js.dump(self.json_data, file)

        except BaseException:
            with open(self.file_name, "w") as file:
                self.data.loc[f"obj{number}"] = [param_1, param_2, param_3, cls]
                self.json_data = self.data.to_json()
                self.json_data = js.loads(self.json_data)
                print(self.json_data)
                flag == True
                js.dump(self.json_data, file)

    def preper_Data(self, preprocessing_func_type=None):
        if preprocessing_func_type == None:
            self.y = np.unique(self.y)
            print(self.x1, self.y)

            self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x1, self.y, test_size=0.3, random_state=0)
            self.snn.fit(self.x1)
            self.x_train_std = self.snn.fit(self.x_train)
            self.x_test_std = self.snn.fit(self.x_test)
    
    def network_fit(self):

        self.ppn.fit(self.x_train_std, self.y_train, random_state=0)
        self.svc_linear.fit(self.x_trian_std, self.y_train, random_state=0)
        self.svc_rbf.fit(self.x_train_std, self.y_train, random_state=0)
        
    def visualise_data(self):
        self.markers = ["x", "2", "s", "o", "v"]
        self.colors = ["gray", "red", "green", "blue", "y"]
        for (index, cls) in np.unique(self.y):
            self.axis_3d.scatter(self.x1[self.y==cls, 0], self.x1[self.y==cls, 1], self.x1[self.y==cls, 2], 
                                 color=self.colors[index], marker=self.markers[index], alpha=0.3, label=f"label: {cls}")
        
        plt.show()

obj = Data_An(file_name="enother_data.json")

param_one_distrib = np.random.normal(12, 0.23, size=1000)
param_two_distrib = np.random.normal(10, 3.5, size=1000)
param_thre_distrib = np.random.normal(13, 4.5, size=1000)
data = np.array([param_one_distrib, param_two_distrib, param_thre_distrib])

while True:
    param_from_keybord = input("enter the params [param1, parma2, param3, cls, number] throu the space: ").split()
    if param_from_keybord == "stop":
        print("end!!!")
        break
    params = [int(x) for x in param_from_keybord]
    obj.add_element(param_1=params[0], param_2=params[1], param_3=params[2], cls=params[3], number=params[4])



#obj.preper_Data()
#obj.network_fit()

            



            



