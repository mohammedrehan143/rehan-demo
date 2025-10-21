# mini projrct class student withe fathers name and mothers name and 
# section and year
class studs:
    def __init__(self,name,fname,mname,sec,year):
        self.name = name
        self.fname = fname
        self.mname = mname
        self.sec = sec
        self.year = year
        
    def info(self):
        print("student name =",self.name)
        print("fathers name =",self.fname)
        print("mothers name =",self.mname)
        print("section =",self.sec)
        print("year =",self.year)
        
a=input("student name")
b=input("fathers  name")
c=input("mothers  name")
d=input("section of the student")
e = input("year of graduating")
bur = studs(a,b,c,d,e)   #object decleration 
bur.info() #function calling 
# here we didnt use the print function so we wont get none in the answer  
        