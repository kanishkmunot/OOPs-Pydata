# First Code - Getting Started

class Employee:
   pass #(If we don't to write anything)


person1 = Employee()
person2 = Employee()

person1.fname = "james"
person1.lname = "arthur"
person1.salary = 1200000

person2.fname = "andrew"
person2.lname = "moore"
person2.salary = 870000

print("Salary of Andrew Moore is", person2.salary)



# Second Code

class Employee:
   def __init__(self,fname,lname,salary):
     self.fname = fname #self.fname is the variable of the class, fname is the argument of the function
     self.lname = lname
     self.salary = salary
  


Walter = Employee("Walter","Lewin",4040000)
xyz = Employee("xyz","surname",2067000)

print(Walter.salary, xyz.salary)



# Third Code


class Employee:
   increment = 2.7
   def __init__(self,fname,lname,salary):
     self.fname = fname #self.fname is the variable of the class, fname is the argument of the function
     self.lname = lname
     self.salary = salary
     # self.increment = 1.4
     
   def increase (self):
      self.salary = int(self.salary * Employee.increment)
# if i wrote self.increment then it will first it check if theere's a increment variable in the instance and then of class


Walter = Employee("Walter","Lewin",4040000)
xyz = Employee("xyz","surname",2067000)

print("Salary of Walter before increment",Walter.salary)

Walter.increase()

print("Salary of Walter after increment",Walter.salary)

print(Walter.__dict__) # To check the list of all the variables of an instance

Walter.increment = 3.3

print(Walter.__dict__)
print(Employee.__dict__)




# Fourth Code

class Employee:
   increment = 2.7
   def __init__(self,fname,lname,salary):
     self.fname = fname #self.fname is the variable of the class, fname is the argument of the function
     self.lname = lname
     self.salary = salary
     # self.increment = 1.4

   def increase (self):
      self.salary = int(self.salary * Employee.increment)
# if i wrote self.increment then it will first it check if theere's a increment variable in the instance and then of class

   @classmethod
   def change_increment(myclass,amount): #takes the whole class as an argument
     myclass.increment = amount
   

Walter = Employee("Walter","Lewin",4040000)
print(Walter.salary)
Employee.change_increment(5.9)
Walter.increase()
print(Walter.salary)




# Fifth Code


class Employee:
   increment = 2.7
   def __init__(self,fname,lname,salary):
     self.fname = fname #self.fname is the variable of the class, fname is the argument of the function
     self.lname = lname
     self.salary = salary
     # self.increment = 1.4

   def increase (self):
      self.salary = int(self.salary * Employee.increment)
# if i wrote self.increment then it will first it check if theere's a increment variable in the instance and then of class

   @classmethod
   def change_increment(myclass,amount): #takes the whole class as an argument
     myclass.increment = amount

  ## If we don't want class or instance variable, we just want a simple function like we usually make in python

   @staticmethod
   def isopen(day):
     if day=="sunday":
       return False
     else:
       return True


Walter = Employee("Walter","Lewin",4040000)
print(Walter.salary)
Employee.change_increment(5.9)
Walter.increase()
print(Walter.salary)

print(Walter.isopen('sunday'))
# OR
print(Employee.isopen('sunday'))



# Sixth Code


class Employee:
   increment = 2.7
   def __init__(self,fname,lname,salary):
     self.fname = fname #self.fname is the variable of the class, fname is the argument of the function
     self.lname = lname
     self.salary = salary
     # self.increment = 1.4

   def increase (self):
      self.salary = int(self.salary * Employee.increment)
# if i wrote self.increment then it will first it check if theere's a increment variable in the instance and then of class

   @classmethod
   def change_increment(myclass,amount): #takes the whole class as an argument
     myclass.increment = amount

  ## If we don't want class or instance variable, we just want a simple function like we usually make in python

   @staticmethod
   def isopen(day):
     if day=="sunday":
       return False
     else:
       return True


Walter = Employee("Walter","Lewin",4040000)
print(Walter.salary)
Employee.change_increment(5.9)
Walter.increase()
print(Walter.salary)

print(Walter.isopen('sunday'))
# OR
print(Employee.isopen('sunday'))

class encode(Employee):
  def __init__(self,fname,lname,salary,interest,laptop):
    super().__init__(fname,lname,salary)
    self.interest = interest
    self.laptop = laptop

programmer = encode("Walter","Lewin",4040000,"cricket",)


# Seventh Code:



class Employee:
   increment = 2.7
   def __init__(self,fname,lname,salary):
     self.fname = fname #self.fname is the variable of the class, fname is the argument of the function
     self.lname = lname
     self.salary = salary
     # self.increment = 1.4

   def increase (self):
      self.salary = int(self.salary * Employee.increment)
# if i wrote self.increment then it will first it check if theere's a increment variable in the instance and then of class

   @classmethod
   def change_increment(myclass,amount): #takes the whole class as an argument
     myclass.increment = amount

  ## If we don't want class or instance variable, we just want a simple function like we usually make in python

   @staticmethod
   def isopen(day):
     if day=="sunday":
       return False
     else:
       return True

   def __add__(self,other):
    return self.salary + other.salary


Walter = Employee("Walter","Lewin",4040000)
xyz = Employee("xyz","surname",2067000)
print(Walter.salary)
Employee.change_increment(5.9)
Walter.increase()
print(Walter.salary)

print(Walter.isopen('sunday'))
# OR
print(Employee.isopen('sunday'))
print(Walter + xyz)

a = 5
print(a.__add__(7))
print(a.__mul__(7))

# Explore __repr__ , __str__
