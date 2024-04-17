# Linked lists

A linked list has the attribute of not following an exact order, in other words, it doesn't necessarily have to store data one value "stacked" next to the other.

The way this list can acces or find the next value is through nodes, sets of a value and a reference to the next node.

Similar to some puzzle pieces, the bigger parto of the piece will store the value and the smaller part will be the link to the next piece.

![Puzzle pieces](2-puzzle_piece.jpeg)

As a whole, this type of data structue will have a head, body, and tail. The operations to add or remove a head and tail are very similar and the operations are as followed:


Linked list operations | What it does | Python code | Big O performance
-------- | -------- | -------- | --------
insert_head(value) | Adds a value before the head, as to become the new head | your_deque.appendleft(value) | O(1)
insert_tail(value) | Adds value after the tail, as to become the tail | your_deque.append(value) | O(1)
remove_head() | Removes first node | value = your_deque.popleft() | O(1)
remove_tail(index) | Removes last node | value = your_deque.pop() | O(1)


In python language an example would look like this:



[Welcome page](0-welcome.md)
