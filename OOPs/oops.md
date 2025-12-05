## What's OOP ?

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

- provides clear strucutre to programs.
- keep it DRY(Don't repeat yourself).
- Allows you to build reusable applications with less code.

## Classess and objects
Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects.

```
class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
```

```
del p1
```

##  __init__() method
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
     
    p1 = Person("Surya",90)
    print(p1.name)
    print(p1.age)
```

## self parameter

The self parameter is a reference to the current instance of the class. It is used to access properties and methods that belong to the class.

```
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()
```

It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class.

## class Properties Vs Object Properties

Properties defined inside the `__init__() ` menthod are object propreties. Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:

```
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)
```