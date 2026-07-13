# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 22:52:06 2026

@author: idris
"""


print("Class and Objects\n")
class dog:
    def __init__(self, name, color):
        self.name=name
        self.color=color
        
    def bark(self):
        print(f"{self.name} is barking and its color is {self.color}")
dog1=dog("buddy", "white")
dog1.bark()