employee=[]
chatlist=[]

def addemployee():
    name=input("enter employee name ")
    employee.append(name)

def chat(username):
    if(username in employee):
        message=input("enter message")
        chatlist.append(message)
        print("message send succesfully")
    else:
        print("this user is not exisit")
def stopappp():
        print("Application say bye bye")

def showchat():
    i=1
    for x in message:
        print(i," ",x)
        i=i+1
def showemp():
    for x in employee:
        print(x)
v=True

while(v):

    step=input("Enter a for addemployee\nEnter c for chat\nEnter sh for show chat\nEnter st for stop application\nEnter se for show employee\n")
    if (step=="a"):
        addemployee()
    elif(step=="c"):
        name=input("enter name for chat")
        chat(name)
    elif(step=="sh"):
        showchat()
    elif(step=="st"):
        stopapp()
    elif(step=="se"):
        showemp()
        v=False
    else:


        print("Try again")




