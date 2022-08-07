print("hello")
print("welcome to my programming")

Function Without Arguement:

def My_fun():

    print("hello")
    print("welcome to programming")

My_fun()

Function With Arguement:
        
def My_Fun(name):

    print("hello",name)
    print("welcome to my programming")

My_Fun("dhoni")
My_Fun("kholi")

Function With Keyword Arguement:

def My_Fun(name,country):

        if isinstance(name,str):          
            if isinstance(country,str):
                print("hello",name,"from",country)
                print("welcome to my programming")

My_Fun("dhoni","india")
My_Fun("Kholi","Bangalore")
My_Fun("ashwin",4)


Function Defination With Default arguement 

def My_Fun(name,country="india"):

        print("hello",name,"from",country)
        print("welcome to my programming")

My_Fun("kholi")
My_Fun("Dhoni","australia")



def My_Fun(name,country=None):

        print("hello",name,"from",country)
        print("welcome to my programming")

My_Fun("kholi")
My_Fun("ricky","australia")






























