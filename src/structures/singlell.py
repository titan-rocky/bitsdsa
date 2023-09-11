class Node :
    def __init__ (self,value) :
        self.val = value
        self.next = None


class linkedList :
    '''
    Creates a linked list of type "valType"
    '''
    def __init__(self,valType=int) :
        self.valType = valType
        self.__length = 0
        self.head = None

    def isEmpty(self) :
        return self.__length==0

    def insert(self,val,index=-1) :
        '''
            This method inserts an element at the mentioned index
            Defaults to -1 (last index)
        '''

        new = Node(val)

        if not(isinstance(val,self.valType)) :
            raise ValueError(f"expected {self.valType}, got {type(val)}")

        if (index>=self.__length or index < (-self.__length) ) :
            raise IndexError("Linked List Index out of range")
            
        if self.isEmpty() :
            self.head = new
            return
        
        if (index==-1) :
            self.append(val)
            return

        if (index<0) :
            index = (self.__length)+index

        if (index==0) :
            new.next = self.head
            self.head = new
            self.__length+=1
            return
        
            
        j = self.head
            
        for i in range(index) :
            j = j.next
            
        k = j.next
        new.next = k
        j.next = new
        
        self.__length+=1


    def getLength(self) :
        return self.__length

    def append(self,val) :
        '''
            This method adds an element at the end of the list
        '''

        new = Node(val)
        
        if self.isEmpty() :
            self.head = new
        
        else :
            j = self.head
        
            while (j.next!=None) :
                j = j.next
            
            j.next = new
        
        self.__length+=1


    def delete(self,node,index=-1) :
        if (index>=self.__length or index < (-self.__length) ) :
            raise IndexError("Linked List index out of range")
        if (index==0) :
            if (self.isEmpty()) : raise LLError
            d = self.head
            self.head = self.head.next
            del d


    def __repr__(self) :
        s = f"length : {self.__length}\n"
        j = self.head
        while (j!=None) :
            s = s + str(j.val) + "->"
            j = j.next
        s += "Null"
        return s
        
    def __del__(self) :
        pass

a = linkedList(str)
a.append('a')
a.append('b')
a.insert(2,-2)
print(a)
help(a)
