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



