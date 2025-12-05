## Encapsulation

Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.
This prevents accidental changes to your data and hides the internal details of how your class works.

- In Python, you can make properties private by using a double underscore __ prefix:

```
class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age) # This will cause an error
```

- To access a private property, you can create a getter method:

- To modify a private property, you can create a setter method.

- The setter method can also validate the value before setting it:

