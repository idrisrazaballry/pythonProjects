# -*- coding: utf-8 -*-
"""
Created on Wed Sep 10 07:28:33 2025

@author: idris
"""

contacts={}

def show_menu():
    print("---Contact Book----\n")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Contact")
    
def add_contact():
    name=input("Enter the contact name:\n")
    phone=input("Enter the conatct number:\n")
    email=input("ENter the contact email:\n")
    contacts[name]={"phone":phone, "email":email}
    print(f"conatct {name} has been added to your connatct book successfully!")
    
def view_contacts():
    if contacts:
        print("----Contact List----\n")
        for name,details in contacts.items():
            print(f"Name :{name}")
            print(f"Phone:{details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("Your conntact book is empty")
        
def search_contact():
    name=input("Enter the name of the contact you want to search:\n")
    if name in contacts:
        print("----Contact Details for {name}----")
        print(f"Name :{name}")
        print(f"Phone:{contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"Conatct {name} not found in your contact book")
def edit_contact():
    name=input("Enter the nameof the conatct you want to edit:\n")
    if name in contacts:
        print(f"----Editing the contact: {name}----\n")
        print("1. Edit Phone")
        print("2. Edit Email")
        print("3. ")