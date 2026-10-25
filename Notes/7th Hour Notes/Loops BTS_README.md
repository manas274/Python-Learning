>>> Main 3 things:
# Iteration tool
# Iterable object
# __next__

>>>iteration tool
>>>(for, comprehension)

>>> iteration tools only work on iterable objects 
>>> iterable objects (lists,file etc)

>>> "__next__" this is response, most important

>>> Step 01:
>>> iter tool query iterable object to put loop on it, iter tool sends a method "iter()"
>>> iter object responds with  "__next__" 
>>> iterable object always points on the starting location of the memory
>>> when "__next__" comes in response again it means there are more values



# Open iteration.py in integrated terminal


>>>ls
>>>python
>>> f = open('iteration.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'print("anas is here") \n'
>>> f.readline()
'username = "ahmed"\n'
>>> f.readline()
'print(username)'
>>> f.readline()
''   
>>> f.readline()
''
#readline() returns an empty string ('') when the end of the file is reached.

>>> f = open('iteration.py')
>>> f.__next__()
'import time\n'

<!-- __next__() returns the next item from an iterator. When no items remain, it raises StopIteration. -->
<!-- same response but this RAW method, readline method uses this internally  -->

>>> f.__next__()
'print("anas is here") \n'
>>> f.__next__()
'username = "ahmed"\n'
>>> f.__next__()
'print(username) '
>>> f.__next__()
Traceback (most recent call last):
File "<python-input-33>", line 1, in <module>
StopIteration     -> exception raised

#readline method handles this expression well and returns an empty string

# Loops
>>> for line in open('iteration.py'):  

<!-- for line in open('iteration.py').readlines was also used in this loop but it gets heavy on the memory so now people dont use it -->
...     print(line)
...     
import time

print("anas is here")

username = "ahmed"

print(username)

>> for line in open('iteration.py'):
...     print(line, end=' ')
...     
import time
print("anas is here")
username = "ahmed"
print(username) >>> 

f = open('chai.py')
while True:
line = f.readline()
if not line: break
print(line, end='')


Lists or Array:

>>>myList = [1, 2,3, 4]
>>>I = iter(myList)
>>>I
<list_iterator object at 0x102f4fa30>

<!-- 0x102f4fa30 is iterator object memory address, it will not change because __next__() advances the position of the existing iterator instead of creating a new iterator object. -->

>>> I.__next__ ()
 1
>>> I
<list_iterator object at 0x102f4fa30>
>>> I.__next__ ()
2
>>> I.__next__()
3
>>> I.__next__ ()
4
>>> I.__next__ ()
Traceback (most recent call last) :
File "<stdin>", line 1, in <module>
StopIteration

# File
>>> f = open('iteration.py')
>>> iter(f) is f
True
>>> iter(f) is f.__ iter __ ()
True
<!-- True only for file. -->

>>> f = open('iteration.py')
>>> next(f)
'import time\n'


# List
>>> myNewList = [1, 2,3]
>>> iter(myNewList) is myNewList
False
>>> x = iter(myList)
>>> next(x)
1
>>> next(x)
2
>>> next(x)
3

<!-- iter(f) is f → True: A file object is already an iterator, so iter(f) returns the same object.

iter(myNewList) is myNewList → False: A list is iterable but not an iterator, so iter(myNewList) returns a separate iterator object. -->

<!-- List and file both are iterable but file is iterator aswell so we dont have to define x = iter() for file, but we have to define it for list 

A file object is already an iterator, so we can call next(f) directly. A list is iterable but not an iterator, so we use iter(myList) to obtain an iterator. -->

<!-- 
List → Iterable, not iterator
Tuple → Iterable, not iterator
Dictionary → Iterable, not iterator
String → Iterable, not iterator
File object → Iterable and iterator -->

# Dictionary
>>> D = {'a': 1, 'b':2}
>>> for key in D.keys():  
<!-- to print keys(a,b) and for values(1,2) we will use D.values -->
... print (key)
...
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at @x102f81990>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
StopIteration

# Range
>>> range(5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> r = iter(R)
>>> next(r)
0
>>> next(r)
1
>>> next(r)
2
>>> next(r)
3
>>> next(r)
4
>>> next(r)
Traceback (most recent call last):
  File "<python-input-99>", line 1, in <module>
    next(r)
    ~~~~^^^
StopIteration

<!-- range is not inclusive so last number will not be printed -->