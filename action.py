# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\wzb\Desktop\file\文件打开.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *




def openfile(self):
    openfile_name = QFileDialog.getOpenFileName(None,'选择文件','','CSV files(*.csv)')
    self.lineEdit.setText(openfile_name[0])
    self.path = openfile_name[0]
    if len(self.path) > 0:
        self.showdata()
    
def showdata(self):
    if len(self.path) > 0:
        data = pd.read_csv(self.path)
        row = data.shape[0]
        col = data.shape[1]
        headers = data.columns.values.tolist()
        print(row,col,headers)
    self.csvModel = QStandardItemModel(row,col)
    self.csvModel.setHorizontalHeaderLabels(headers)
    self.tableView.setModel(self.csvModel)

    
    for i in range(row):
        for j in range(col):
            item = QStandardItem(str(data.iloc[i,j]))
            #print(item)
            self.csvModel.setItem(i,j,item)

            



