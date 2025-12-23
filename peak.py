def Input(Array,n):
     for i in range (0,n):
          ele=int(input("enter num of arrray"))
          Array.append(ele)

Array = []
n = int(input("Enter number of elements : "))
Input(Array, n)
 print(Array)