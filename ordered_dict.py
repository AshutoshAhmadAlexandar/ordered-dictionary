class OrderedDict(object):
    def __init__(self):
        self._keys = []
        self._values = []

    def keys(self):
        return self._keys

    def values(self):
        return self._values

    def items(self):
        results = []
        for key, value in zip(self._keys, self._values):
            results.append((key, value))
        return results
        
    def __setitem__(self, key, value):
        #self._keys.append(key)
        #self._values.append(value)
        '''
        if key in self._keys:
            pos = self._keys.index(key)
            self._values.pop(pos-1)
            self._values.insert(pos-1, value)
            return None
        self._keys.append(key)
        self._values.append(value)
        '''
        index = 0
        for a_key, a_value in zip(self._keys, self._values):
            if a_key == key:
                self._values[index] = value
                return None
            index += 1
        self._keys.append(key)
        self._values.append(value)
        
    def __getitem__(self, a_key):
        for key, value in zip(self._keys, self._values):
            if a_key == key:
                return value
        raise KeyError("No value for key {}".format(repr(a_key)))
        
    def __contains__(self, item):
        for key in self._keys:
            if key == item:
                return True
        return False
        
    def __len__(self):
        return len(self._keys)
        
    
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        
        for key, value in zip(self._keys, self._values):
            if key not in other or other[key] != value:
                return False
        return True
        '''
        #other_key = []
        #other_values = []
        #for k, v in other.items():
        #    other_key.append(k)
        #    other_values.append(v)
        for key, value in zip(self._keys, self._values):
            self_pos = self._keys.index(key)
            #other_pos = other_key.index(key)
            if key not in other or other[key] != value:
                return False
            if key in other:
                other_pos = other._keys.index(key)
                if self_pos != other_pos or self._values[self_pos] != other._values[self_pos]:
                    return False
        return True
        '''
        
    def __ne__(self, other):
        return not self == other
        
    def __str__(self):
        result = '{'
        for key, value in zip(self._keys, self._values):
            result += '{}: {}, '.format(repr(key), repr(value))
        result = result.rstrip(', ')
        result += '}'
        return result
        
    __repr__ = __str__
    
    
    def __add__(self, other):
        new = OrderedDict()
        '''
        for key, value in zip(self._keys, self._values):
            new[key] = value
            
        for key, value in zip(other._keys, other._values):
            new[key] = value
            
    
        for key, value in zip(other._keys, other._values):
            if key in new:
                new.__delitem__(key)
                new[key] = value
            else:
                new[key] = value
      '''
        for key, value in zip(other._keys, other._values):
           new[key] = value
        for key, value in zip(self._keys, self._values):
           if key in new:
               continue
           else:
               new[key] = value
        return new
        
    
    #def __delitem__(self, key):
    #    del self[key]
    
    @classmethod
    def from_keys(cls, sequence):
        new = OrderedDict()
        for item in sequence:
            new[item] = None
        return new