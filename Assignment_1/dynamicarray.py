            # que 1 : insert at dynamic array 

class dynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.size = 0
        self.resize_factor = resize_factor
    
    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bound")
        self.array.insert(index, element)
        self.size += 1


        #que 2 : - 

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bound")
        del self.array[index]
        self.size-=1




        #que3:- get the size of linkedlist 

    def get_size(self):
        return self.size
    
        #que 4 : - is empty 

    def is_empty(self):
        return self.size == 0
    

        #Que 4 : - rotate 

    def rotate(self, k):
        if self.size == 0 or k == 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]


            #Que 5 :- 

    def reverse(self):
        self.array.reverse()

            #Que 6:- append 

    def append(self, ele):
        self.array.append(ele)
        self.size += 1

            #que 7 :- prepend 
    
    def prepend(self, ele):
        self.array.insert(0, ele)
        self.size += 1
        

        #Que 8 :-  merge 

    def merge(self, other_array):
        self.array.extend(other_array.array)
        self.size += other_array.size


        #que 9 : _ 



        #que 10 :- fine middle 

    def find_middle(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]
    
            #que 11 :- index of specific value 


    def index_of(self, ele):
        for i in range(self.size):
            if self.array[i] == ele:
                return i
        return -1
    

            #Que 12 :-  resize 


    def resize(self, new_resize_factor):
        self.resize_factor = new_resize_factor




    
    


