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

