import ctypes

class NumberArray:
    
    def __init__(self,size=10):
        if size>0:
            self._size=size
        else:
            raise ValueError
        self._n=0 
        self._A = self._make_array(self._size) 
    
    def _make_array(self, c):
        return (c * ctypes.py_object)( ) 
    
    def __len__(self):
        return self._n
      
    def __getitem__(self, k):
        #Checks if k is a valid index and if it is, it will return the kth item from the array.
        if k >= self._n and k <(-(self._n)):
            raise IndexError ('Invalid Index')
        if k<0:
            key+=self._n
        return self._A[k]
    
    def __setitem__(self, k, item):
        #Checks if k is valid index or not. Overwrites the kth element by item.
        if k>=self._n and k<(-(self._n)):
            raise IndexError ('Invalid Index')
        if k<0:
            key+=self._n
        self._A[k]= item
    
    def append(self, item):
        #Appends item to the array
        if self._n == self._size:
            self._resize(2*self._size)
        self._A[self._n] = item
        self._n += 1
            
    def insert(self,index,value):
        if index > self._n or index < 0:
            raise IndexError ('Invalid Index')
        self.append(value)
        for i in range(self._n,index,-1):
            self._A[i]=self_A[i-1]
        self._A[index]=value
        self._n += 1    
            
    def resize(self, c):
        B=self._make_array(c)
        for k in range(self,c):
            B[k] = self._A[k]
        self._A = B
        self._size = c
    
    def remove(self, k):
        if k >= self._n and k <(-(self._n)):
            raise IndexError ('Invalid Index')
        for i in range(k,self._n-1):
            self._A[i]=self._A[i+1]
        self._n -= 1
