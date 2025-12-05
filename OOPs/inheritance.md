## Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

**Parent class** is the class being inherited from, also called base class.

**Child class** is the class that inherits from another class, also called derived class.

```
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()
```

## __init__() function in inheritance

- We want to add the `__init__()` function to the child class (instead of the pass keyword).
- When you add the `__init__()` function, the child class will no longer inherit the parent's `__init__()` function.
- To keep the inheritance of the parent's `__init__()` function, add a call to the parent's `__init__()` function:

```
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
```

## __super()__ function in inheritance

- Python also has a `super()` function that will make the child class inherit all the methods and properties from its parent.
- By using the `super()` function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

```
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
```