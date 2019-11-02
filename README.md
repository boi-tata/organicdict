# OrganicDict
OrganicDict is a Python object that's implements dict built-in type, adding some useful features.

## Origin

Its has projected initially as a function, to be used in some specific situations where is usefull convert a sequence of sequences, like SQL queries results, in `dict` objects, for better organization and easier access to data.
But is commom a situation where the result `dict` has 4 or more levels of depth and a not so consistent hierarchy, thats not so easy to deal with. Here is when the idea of transform this function to a object appeared.

## How to use

- Instanciation

````py
>>> obj = OrganicDict() # empty instance
>>> d = {'a': 1, 'b': 2}
>>> obj = OrganicDict(d) # Transform a dict in a OrganicDict
>>> l = [('a', 1), ('b', 2)]
>>> obj = OrganicDict(l) # Same as OrganicDict(dict(l))
>>> t = [
...    ('a', 'b', 'c'),
...    ('d', 'e', 'f')
... ]
>>> obj = OrganicDict(t) # Same as apply obj.mutate() method for each element of t in a empty instance
````

- Behavior

Is useful thinks a OrganicDict as a tree structure. So, its composed by some nodes and leafs. A path is a sequence of one or more nodes, followed by a leaf. Our tree is a composition of dicts, so any node needs to be a valid dict key (hashable object). The leafs could be from any type.

- obj.search(iterable)

Receives a iterable object (list, tuple, etc) thats represents a path to be verified. If existent, returns the leaf of path, otherwise None.
The search dont need to correspond to a leaf. In this case, the whole node is returned.

- obj.defoliate()

Return a generator thats iterate over all leafs on instance.

- obj.mutate(iterable)
- obj.mutate(dict)

If received a iterable, consider thats represents a path, with last value as a leaf, and updates this path to match with a search using the same iterable (returning the leaf), creating nodes on instance as needed.
If received a dict, considers thats represents a tree, and updates the instance to match any valid search in this tree, returning the same values.
In both cases, when have a conflict while mutating (a path correspond to a existent path or part of it), the newest value is preserved.