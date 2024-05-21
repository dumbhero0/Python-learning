#WAP to demonstrate global variable
data=5
def globaldata():
    global data
    data=10
    print("data=",data)
globaldata()
print("value of data= ",data)    