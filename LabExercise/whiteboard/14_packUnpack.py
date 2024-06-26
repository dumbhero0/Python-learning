#given [10,20,5] unpack it into three variables and display cube.(use exponential operator for cube)
#packing variables
def packUnpack(*data):
    a,b,c = data
    print(a**3,b**3,c**3)
    
value=[10,20,5]
packUnpack(*value)

    