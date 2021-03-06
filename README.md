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

**Reduce**

* `reduce()` works differently than `map()` and `filter()`. 
* It does not return a new list based on the function and iterable we've passed. 
* Instead, it returns a single value.

```
We start with a list [2, 4, 7, 3] and pass the add(x, y) function to reduce() alongside this list, without an initial value

reduce() calls add(2, 4), and add() returns 6

reduce() calls add(6, 7) (result of the previous call to add() and the next element in the list as parameters), and add() returns 13

reduce() calls add(13, 3), and add() returns 16
```

* In Python 3 `reduce()` isn't a built-in function anymore, and it can be found in the functools module.

**Iterables and iterators**

* Iterable is an object, which one can iterate over. 
* It generates an Iterator when passed to iter() method.
* Iterator is an object, which is used to iterate over an iterable object using __next__() method.
* Iterators have __next__() method, which returns the next item of the object.
* Every iterator is also an iterable, but not every iterable is an iterator.
* A list is iterable but a list is not an iterator.
* An iterator can be created from an iterable by using the function iter(). 
* To make this possible, the class of an object needs either a method __iter__, which returns an iterator






