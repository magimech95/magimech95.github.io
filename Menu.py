from functionality.ViewAndUpdateDetails import ViewAndUpdateDetails
from functionality.OpenFD import OpenFD
from functionality.TransferFunds import TransferFunds
from functionality.MakePayment import MakePayment
 
print("Welcome to Infy Bank!!")
print("**********************")
 
print("Choose an option from below:\n")
 
end=False
 
while(end==False):
    print("1. View and Update my details")
    print("2. Open a FD")
    print("3. Transfer Funds")
    print("4. Make a payment")
    print("5. View fund flow")
    print("6. Exit")
    option=input()
    if(option.isdigit() and (int(option)>=1 and int(option)<=6)):
        if(int(option)==1):
            print("View my details")
            ViewAndUpdateDetails()
 
        if(int(option)==2):
            print("Open FD")
            OpenFD()
 
        if(int(option)==3):
            print("Transfer Funds")
            TransferFunds()
           
        if(int(option)==4):
            print("Make a payment")
            MakePayment()
 
        if(int(option)==5):
            print("View fund flow")
           
        if(int(option)==6):
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option ( 1,2,3,4,5,6 )")
