class Template :
    def __init__ (self,givenType) :
        self.__templateType__  = givenType
    
class PrettyType(type) :
    def __new__(cls,name,bases,dct) :
        print(cls,name,bases,dct)
        newInstance = super().__new__(cls,name,bases,dct)
        return newInstance

    def __repr__ (self) :
        return f"{self.__name__}"

class Array(Template,metaclass=PrettyType) :
    def __init__ (self,givenType) :
        super().__init__(givenType)

a = Array(int)
print(type(a))
