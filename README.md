**Do arguments in Python get passed by reference or by value?**

* All parameters (arguments) in the Python language are passed by reference.
* It means if you change what a parameter refers to within a function, the change also reflects back in the calling function.

**Example**
```
student={'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
def test(student):
   new={'alok':30,'Nevadan':28}
   student.update(new)
   print("Inside the function",student)
   return
test(student)
print("outside the function:",student)
```

**Output**

```
Inside the function {'Archana': 28, 'krishna': 25, 'Ramesh': 32, 'vineeth': 25, 'alok': 30, 'Nevadan': 28}
outside the function: {'Archana': 28, 'krishna': 25, 'Ramesh': 32, 'vineeth': 25, 'alok': 30, 'Nevadan': 28}
```

**Properties of first class functions**

* A function is an instance of the Object type.
* You can store the function in a variable.
* You can pass the function as a parameter to another function.
* You can return the function from a function.
* You can store them in data structures such as hash tables, lists, …

**Map and Filter**

* Map takes all objects in a list and allows you to apply a function to it.
* Filter takes all objects in a list and runs that through a function to create a new list with all objects that return True in that function.
* In map: Function will be applied to all objects of iterable. 
* In filter: Function will be applied to only those objects of iterable who goes True on the condition specified in expression.

