# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 07:11:45 2025

@author: idris
"""

shopping_list=[]
def show_menu():
    print("---Shopping list menu---\n")
    print("1.View Shopping List")
    print("2. Add items in shopping list")
    print("3. Remove an item")
    print("4.Clear List")
    print("5. Exist")
while True:
    show_menu()
    choice=input("Enter your choice (1-5)\n")
    if choice== "1":
        print("----Shopping List---")
        if not shopping_list:
            print("Your list is empty")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index+1}. {item}")
    elif choice=="2":
        item=input("Enter the item to add\n")
        shopping_list.append(item)
        print(f"{item} hass been added to shopping list")
        
    elif choice=="3":
        item=input("Enter the item to remove\n")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list")
        else:
            print(f"{item} doesn't exit in list")
    elif choice=="4":
        shopping_list.clear()
        print("The shopping list has been cleared")
        
    elif choice=="5":
        print("Bye!, haapy shopping")
        break
    else:
        print("Invalid choice, please try again")