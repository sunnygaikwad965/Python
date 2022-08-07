 Arguments means it can take any no of arguments
 output will be inform of tuple 
        
def student_passed(*names):

    print(names)

##student_passed("dhoni")
student_passed("kholi","sachin")



Arguments means data with keys
output will be in form of dictonary

def students_passed(**names):

    print(names)

students_passed(name="dhoni")
students_passed(name="kholi",age=33)



In this below program Return is last excutable function
def student_mark(eng,maths,student_name):

    total = eng+maths
    return total

print(student_mark(40,50,"dhoni"))


def students_mark(eng,hindi,student_name):

        total= eng + hindi
        return total,student_name

output,output1 = student_mark(50+90,"dhoni")
print(output)
print(output1)



Scoping

var = 100
def fun():
    var = 10
    print(var)

print(var)
fun()
print(var)



var = 100
def fun():
    global var
    var = 10
    print(var)


print(var)
fun()
print(var)



Counter stops at 100th time

counter = 0
def fun():
    global counter
    print("hello", counter)
    counter = counter + 1
    if counter ==100:
     return
    fun()
fun()






































































