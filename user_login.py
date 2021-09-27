Sys_User_Name = "EthanWayne"
Sys_Password =  "123456"

User_Name = input("Please enter your name: ")
User_Password = input("Please enter your password: ")

if User_Name != Sys_User_Name and User_Password == Sys_Password:
    print("Wrong user name...")

elif User_Name == Sys_User_Name and User_Password != Sys_Password:
    print("Wrong password...")

elif User_Name != Sys_User_Name and User_Password != Sys_Password:
    print("Wrong user name and password!")

else:
    print("Login successfulS")