# Stacks

A way to picture this kind of data structure with an everyday example is imagining
a pile of 20+ books on different topics and trying to get one but not quite remembering
where it is. The safest way to get to the right one is by grabbing the one on top, putting it aside, and going down
the pile doing the same thing until you find the one you want.

*add image*

The most common stack operations in Python are the following, along with an explanation and their corresponding performance in Big O notation:

Stack operation | What it does | Python code | Big O performance
-------- | -------- | -------- | --------
push(value) | Adds a value to the stack | your_stack.push(value) | O(1) Adding the value at the end of the stack with no need to iterate over other values
pop() | Deletes and stores the last pushed value of the stack | your_stack.pop() | O(1) No need to iterate over other values
size() | Calculates the size of the stack | your_stack.size() | O(1)

One great advantage of using this data structure is that you can store and later use the values and also keeping a "log" of what has been happening in the code.

This is an example of a problem that uses a stack data structure:

### Follow the pattern of the following values and add the following value to continue with the pattern, print the resulting list of values, then, delete the last value added and print it.

```python
my_stack = (2,4,6)

my_stack.push(8)

print(my_stack) #(2,4,6,8)

pop_it = my_stack.pop()

print(pop_it) #(8)
```



[Welcome page](0-welcome.md)

