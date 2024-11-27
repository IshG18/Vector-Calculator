class Vector:
   
    def __init__(self, array) -> int | float:
        self.nums = array
        self.len = len(array)
    
#Adding and Subtracting with itself and numbers
    def __add__(self, var):
        output = []
        if isinstance(var, Vector):
            output = []
            length = self.len if self.len >= var.len else var.len
            for i in range(length):
                value1 = self.nums[i] if i < self.len else 0
                value2 = var.nums[i] if i < var.len else 0
                output.append(value1+value2)
            return Vector(output)
        
        elif type(var) == float or int:
            for i in self.nums:
                output.append(i+var)
            return Vector(output)

    def __sub__(self, var):
        output = []
        if isinstance(var, Vector):
            output = []
            length = self.len if self.len >= var.len else var.len
            for i in range(length):
                value1 = self.nums[i] if i < self.len else 0
                value2 = var.nums[i] if i < var.len else 0
                output.append(value1-value2)
            return Vector(output)
        
        elif type(var) == float or int:
            for i in self.nums:
                output.append(i-var)
            return Vector(output)

#Scaling and Division with itself and numbers
    def __mul__(self, var):
        output = []
        if isinstance(var, Vector):
            length = self.len if self.len >= var.len else var.len
            for i in range(length):
                value1 = self.nums[i] if i < self.len else 1
                value2 = var.nums[i] if i < var.len else 1
                output.append(value1*value2)
            return Vector(output)
        
        elif type(var) == float or int:
            for i in self.nums:
                output.append(i*var)
            return Vector(output)
        
    def __truediv__(self, var):
        output = []
        if isinstance(var, Vector):
            output = []
            length = self.len if self.len >= var.len else var.len
            for i in range(length):
                value1 = self.nums[i] if i < self.len else 1
                value2 = var.nums[i] if i < var.len else 1
                output.append(value1/value2)
            return Vector(output)

        elif type(var) == float or int:
            for i in self.nums:
                output.append(i/var)
            return Vector(output)
            
    def __neg__(self):
        output = []
        for i in self.nums:
            output.append(i*-1)
        return Vector(output)
    
    def __rmul__(self, var):
        return self.__mul__(var)
    
    def __rtruediv__(self, var):
        return self.__truediv__(var)
    
    def __radd__(self, var):
        return self.__add__(var)
    
    def __rsub__(self, var):
        return self.__sub__(var)
    
#Shows as list
    def __repr__(self):
        return f"{self.nums}"
