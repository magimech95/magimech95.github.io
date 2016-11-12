from database import Func
from functionality.OpenFD import OpenFD
 
class ViewAndUpdateDetails():
    def __init__(self):
        self.__cid=None
        self.__cust_details=None
        self.login()
        self.display_details()
        self.update_details()
 
    def login(self):
        while self.__cid is None:
            cid = input("Enter customer Id: ")
            pwd = input("Enter password: ")
            self.__cid=Func.login(cid, pwd)
   
    def display_details(self):
        print("The details are :")
        print("-----------------")
        self.__cust_details=Func.get_customer_details(self.__cid)
        print("Name : "+ self.__cust_details[0])
        print("Gender : "+ self.__cust_details[1])
        print("Age : "+ str(self.__cust_details[2]))
        print("Phone : "+ str(self.__cust_details[3]))
 
    def update_details(self):
        choice = input("Do you want to update your age, PAN or phone? Press 'Y' or 'N': ")
        if choice.upper()=="Y":
            while True:
                age = input("Enter new age. Press Enter to skip ")
                if Func.update_customer_age(self.__cid, age):
                    break
            while True:
                phone = input("Enter new phone. Press Enter to skip ")
                if Func.update_customer_phone(self.__cid, phone):
                    break
            while True and self.__cust_details[4] is None:
                pan = input("Enter new PAN. Press Enter to skip ")
                if Func.update_customer_pan(self.__cid, pan, self.__cust_details[0]):
                    break
            cust_details=Func.get_customer_details(self.__cid)
            print("Updated age: "+str(cust_details[2]))
            print("Updated phone: "+str(cust_details[3]))
            print("Successfully updated")
        choice = input("Do you want to open a FD? Press 'Y' or 'N': ")
        if choice.upper()=='Y':
            OpenFD(self.__cid)
 
