Counter 

data = "I love my country"
my_counter= 0
for x in (data):
    print(x)
    my_counter = my_counter+1
print(my_counter)

When we have 1 condition were (if & else are used in same place )

data = "india his history"
for x in (data):
    if x =="i":
        print(x,"success")
    else:
        print(x,"failure")

When We have 2 condition then we use elif statement
data ="india is history"
for x in (data):
      if x == "i":
           print(x,"success")
      elif x=="s":
           print(x,"success")
      else:
          print(x,"failure")


When we want to break Itreation

data = "india his history"
for x in (data):
    if x == "i" or i == "s":
        print(x,"success")
        break
    else:
        print(x,"failure")






























































