#python code goes here
#python version :3 
import pickle
omkar = {"name":"omkar","age":21}
dhiraj = {"name":"dhiraj","age":20}
db={}
db["omkar"]=omkar
db["dhiraj"]=dhiraj
db_path = open("myPickle","ab")
pickle.dump(db,db_path)
db_path.close()

db_file = open("myPickle","rb")
myData = pickle.load(db_file)
for data in myData:
    print(data+":"+str(myData[data]))
    
