'''
Big O 
- describe the efficiency of algorithm
tightest bound of the runtime

also space complexity 

in recursive calls, stack space counts

ArrayList / dynamically resizing array allows us to have benefits of array
while flexible size
 - runtime of insertion - how do we describe?

 logN time - if number of elemens gets halved each time, it will likely be 
O log N runtime

Recursive call - O (branches ^ depth)

Tips for coding interview - start with brute force, then deal with
edge cases and a more optimal algorithm 

Make runtime vs space tradeoff - this is so important
ex) dynamic program - save the values that came out so we're sacrificing space
but we dont have to compute the values that came out before

USE HASH TABLES

ch 1. Array and Strings

they are interchangeable in a way that string might be easier if u make it array
and vice versa

Hashtable - maps keys to values for highly efficient lookup

when collision happens, resolve in 2 ways - Linear probing / chaining

L.P - search for an open slot
Chaining - theres going to be a list, for C we can use linked list I guess

2. Linked List 

commonly use a "runner" technique

3. Stacks and Queues

Stack is LIFO - pop, push, peek, isEmpty
Queue is FIFO - add, remove, peek, is empty

4. Trees and Graphs

Binary tree vs Binary search - binary tree inequality is true only for 
its child. Binary search, it goes down to all descendents

Two types of balanced tree - red-black trees and AVL trees
redblack - Every node is either red or black

Binary - full - 0 or 2 nodes / complete left oriented

Min heap - least element at the top and we insert from the bottom

graphs - represent by adjacency list & adjacency Matrices

2 most common way to search a graph is DPS and BFS
DPS - start at a designated node and explore that individual depth completely,
before moving onto the next node. Preferred if we want to visit every node
in graph. 

the search function will look like
if root == null return;
visit (root);
root.visited = true;
for each Node n in root.adjacent {
    if root.visited == false {
        search(n)
    }
}

Basically this will search a then its first neighbor which will be b,
and before it visits a's other neighbor, it will visit b's first neighbor


BFS - explore neigbor before moving onto its children. Best if we want to 
find the shortest path. BFS is actually not recursive, it uses a queue
Need to look up a little more

Bidirectional search - runs two simultaneous breadth-first searches. 

Need to do more study on BFS and shortest path problem

























