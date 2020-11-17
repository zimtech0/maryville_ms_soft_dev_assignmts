What is the difference between a list and a dictionary?



A list is an ordered sequence of objects, whereas dictionaries are unordered sets. However, the main difference is that items in dictionaries are accessed by keys and not by their position.

More theoretically, we can say that dictionaries are the Python implementation of an associative array(an abstract data type). Associative arrays consist - like dictionaries of (key, value) pairs, such that each possible key appears at most once in the collection. Any key of the dictionary is associated (or mapped) to a value. The values of a dictionary can be any type of Python data. So, dictionaries are unordered key-value-pairs. Dictionaries are implemented as hash tables.

Dictionaries don't support the sequence operation of the sequence data types like strings, tuples and lists. Dictionaries belong to the built-in mapping type, but so far, they are the sole representative of this kind.

How are they coded differently and what different implementations they have?

In Python, a list is created by placing all the items (elements) inside square brackets [] , separated by commas. It can have any number of items and they may be of different types (integer, float, string etc.). A list can also have another list as an item which is called a nested list. The implementation uses a contiguous array of references to other objects, and keeps a pointer to this array and the array’s length in a list head structure.

This makes indexing a list (L[i]) an operation whose cost is independent of the size of the list or the value of the index.

To create a Python dictionary, a sequence of items need to be passed inside curly braces {} , and separated by using a comma (,). Each item has a key and a value expressed as a "key:value" pair. The values can belong to any data type and they can repeat, but the keys must remain unique. Python dictionaries are like hash tables in regards to implementation. 