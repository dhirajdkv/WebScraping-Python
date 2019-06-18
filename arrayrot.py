a1 = [1,2,3,4,5]
a2 = [4,5,1,2,3]
a = [str(i) for i in a1]
a = "".join(a)
b = [str(i) for i in a2]
b = "".join(b)
temp = ''
temp = a+a
if len(a1) != len(a2):
    print("No")
if(temp.count(b)>0):
    print("yeppp")
else:
    print("No")
    
