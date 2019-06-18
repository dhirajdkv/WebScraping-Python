#python code goes here
#python version :3 
class Myprime:
    def __init__(self,last):
        self.last = last
    def prime(self):
        for i in range(2,self.last+1):
            for j in range(2,self.last+1):
                if i!=j:
                    if i%j==0:
                    	flag=1
                    	print(str(i)+"is not a prime number")
                    	break
                    else:
                    	flag=2
                elif i==j:
                    continue
            if flag==2:
                print(str(i)+"is a prime number")
            
p1 = Myprime(20)
print(p1.prime())
