inp = (int)(input("Enter the decimal number: "))
emp = []
while(inp>1):
    inpbin = inp % 2
    inp = inp / 2
    emp.append(inpbin)
emp.append(inp)
emp = emp[::-1]
for item in emp:
    print(int(item),end="")
            
