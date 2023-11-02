def check_password_strength(password):
    length=len(password)
    l=1
    u=0
    lo=0
    s=0
    n=0
    if length<8:
        print("yes")
        l=0

    for i in range(0,length,1):
        ch=password[i]
        if ch.isupper():
            u=1
            
        if ch.islower():
            lo=1

        if ch=='!' or ch=='@' or ch=='#' or ch=='$' or ch=='%':
            s=1
        
        if ch.isnumeric():
            n=1

    if l==1 and u==1 and lo==1 and s==1:
        return True
    else:
        return False

password=input("Enter password : ")
if check_password_strength(password)==True:
    print("Password is Strong")
else:
    print("Weak Password. Please use strong password")