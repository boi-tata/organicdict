class OrganicDict(dict):
    """Based on `dict` type, has all attributes and methods of that, but
    implements some new features"""

    def __init__(self, seed={}):
        if not isinstance(seed, dict):
            from functools import reduce

            seed = reduce(self._merge, map(self._tuple_to_dict, seed))
        super().__init__(seed)


    def mutate(self, item):
        """
        item: `dict`, `sequence`
        
        Update a path or group of paths.
        If item is a `dict` instance, merge the calling object with item,
        comparing all keys in same depth.
        If item is a sequence, consider thats represent the path to be updated.
        In any case, conflicting keys will be updated, receiving item value, 
        and item keys missing on obejct will be created"""
        
        assert isinstance(item, (dict, tuple, list)), "item needs to be `dict`, `list` or `tuple` instance"
        if not isinstance(item, dict):
            item = self._tuple_to_dict(item)
        self._merge(self, item)


    def search(self, path):
        """Check for a path in object. If is a valid path, return the value.
        Otherwise, return `None`"""
        
        p = self
        for k in path:
            if k not in p: return None
            p = p[k]
        return p


    def defoliate(self):
        """Return a generator thats iterate over all values"""
        
        return self._get_leafs(self)


    @classmethod
    def _get_leafs(cls, d):
        for k in d:
            if isinstance(d[k], dict): yield from cls._get_leafs(d[k])
            else: yield d[k]


    @classmethod
    def _merge(cls, d1, d2):
        if not (isinstance(d1, dict) and isinstance(d2, dict)): return d2

        d1.update(
            dict(
                ((k, v) if k not in d1 else (k, cls._merge(d1[k], d2[k])) for k, v in d2.items())
            )
        )
        return d1

    
    @classmethod
    def _tuple_to_dict(cls, t):
        return t[0] if len(t) < 2 else {t[0]: cls._tuple_to_dict(t[1:])}