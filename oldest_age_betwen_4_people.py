print("Enter the age four people:")
person=int(input(""))
person1=int(input(""))
person2=int(input(""))
person3=int(input(""))
if(person>person1 and person>person2 and person>person3):
    print("The oldest person is",person)
elif(person1>person and person1>person2 and person1>person3):
    print("The oldest person is",person1)
elif(person2>person1 and person2>person and person2>person3):
    print("The oldest person is",person2)
else:
      print("The oldest person is",person3)
  
