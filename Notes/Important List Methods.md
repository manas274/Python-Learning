1. **append()**
Adds one item at the end of the list
'''python
>>> my_list = [1,2,3]
>>> my_list.append(4)
Output : [1,2,3,4]

2. insert()
Inserts an item at the specified index
>>> my_list = [1,2,3]
>>> my_list.insert(1, 99)
Output: [1,99,2,3,4]

3. pop()
Removes and returns the item at the last
>>> my_list = [1,2,3]
>>> my_list.pop()
Output : [1,2]

4. sort()
Sorts the list in ascending order
>>> my_list = [3,1,2]
>>> my_list.sort()
Output : [1,2,3]

5. count()
Returns the number of occurrences of an item
>>> my_list = [1,2,2,2,3]
>>> my_list.count(2)
Output : 3

6. extend()
Adds multiple items from an iterable to the end
>>> my_list = [1,2,3]
>>> my_list.extend([4,5,6])
Output : [1,2,3,4,5,6]

7. remove()
Removes the first occurrence of the value
>>> my_list = [1,2,3,2]
>>> my_list.remove(2)
Output : [1,3,2]

8. clear ()
Removes all the items in list
>>> my_list = [1,2,3]
>>> my_list.remove()
Output : []

9. reverse()
Reverses the list in place
>>> my_list = [1,2,3]
>>> my_list.reverse()
Output : [3,2,1]

10. index()
Returns the index of the first occurrence of an item
>>> my_list = [1,2,3]
>>> my_list.index(3)
Output : 2

11. copy()
Creates a shallow copy of the list
>>> my_list = [1,2,3]
>>> my_list_new = my_list.copy()
>>> print(my_list_new)
Output : [1,2,3]

<!-- Changes in original list wont affect copy -->