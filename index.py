import covid_19_project.mysql_connector as mc
import covid_19_project.user_reg as u_reg
import covid_19_project.user_auth as u_auth
import covid_19_project.smtp as smtp
import random
print("*"*20)
print("ENTER 1 IF YOU ARE AN EXISTING USER")
print("ENTER 2 IF YOU ARE A NEW USER")
selection = int(input())
def login():
    print("Enter Your Email to login:")
    email = input()
    authentication = u_auth.user_auth(email, count=0)
    if authentication == 1:
        otp = int(random.randint(100000, 999999))
        smtp.otp_sender(email, otp)
        print("ENTER OTP SEND TO YOUR REGISTERED MAIL ID")
        input_otp = int(input())
        if input_otp == otp:
            print("LOGIN SUCCESSFULL")
            import covid_19_project.covid_data_analysis as cda
        else:
            print("INVALID OTP")
            login()
    else:
        print("INVALID EMAIL !")
        login()

def reg():
    print("Enter Your Name:")
    name = input()
    print("Enter Your Email")
    email = input()
    u_reg.user_reg(name, email)
    login()
if selection==1:
    login()
elif selection==2:
    reg()