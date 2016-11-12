from database import Func
import random
from validations import validatations
from exceptions import CustomExceptions
 
class MakePayment():
    def __init__(self, cid=None):
        self.__cid=cid
        self.login()
        self.make_payment()
 
    def login(self):
        while self.__cid is None:
            cid = input("Enter customer Id: ")
            pwd = input("Enter password: ")
            self.__cid=Func.login(cid, pwd)
 
    def generate_captcha(self):
        c=list(str(random.randrange(1000,9999)))
        c.insert(1, random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        return "".join(c)
 
    def make_payment(self):
        while True:
            try:
                while True:
                    try:
                        acc_no=input("Enter account number: ").upper()
                        acc_details=Func.get_saving_details(acc_no)
                        if acc_details is not None and acc_details[1]!=self.__cid:
                            raise CustomExceptions.InvalidPaymentAccount()
                        if acc_details:
                            break
                    except CustomExceptions.InvalidPaymentAccount as e:
                        print(e)
                amount=input("Enter amount: ")
                validatations.validatePaymentAmount(amount)
                validatations.validateMinimumBal(acc_details[2], amount)
                break
            except CustomExceptions.InvalidPaymentAmountException as e:
                print(e)
            except CustomExceptions.MinimumBalanceException as e:
                print(e)
                print("You can withdraw upto "+str(acc_details[2]-1000)+" only")
                print("Please select another account")
 
        while True:
            try:
                captcha=self.generate_captcha()
                entered_captcha=input("Enter the Captcha as shown {} : ".format(captcha))
                if(entered_captcha==captcha):
                    descr=input("Enter Description: ")
                    pid=Func.make_payment(acc_no, int(amount), descr, acc_details)
                    if pid:
                        print("Your payment was successful with payment ID "+str(pid));
                        print("Balance left in your Account is Rs. "+str(acc_details[2]-int(amount)));
                    break
                else:
                    raise CustomExceptions.InvalidCaptchaException()
            except CustomExceptions.InvalidCaptchaException as e:
                print(e)
 
 
