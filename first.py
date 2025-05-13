"""
n=input("enter the number")
if int(n)%2 == 0:
    print("even")
else:
    print("odd") 
    """
    
'''
n = int(input("enter a number:"))
m= int(input("enter the range:"))
for i in range(1,m+1):
    print(f"{n}X{i} = {n*i}")
    '''
'''
h = int(input("enter a number"))
i=1
while i<=h:
    i+=1
    print(i)
    '''

'''
h = int(input("Enter a number: "))
i = 1
while i <= h:
    print(i)  
    i += 1  
'''
'''
def square(i):
    print(i**i)
    
square(4)
'''
'''list/array
fruits=['apple', 'banana', 'cherry', 'orange', 'grapes']
print(len(fruits))
for fruit in fruits:
    print(fruit)
    '''
'''
y=(1,2,3)
a,b,c=y
print(a,b,c)
    '''
'''
nums={1,2,2,3,4,5}
num={6}
print(nums)
print(3 in nums)
print(nums.union(num))
   ''' 
   
laptop = {
    "brand":"lenovo",
    "model":"l13",
    "price":250
}
    
print(laptop["brand"])
laptop["price"]=250
laptop["origin"]="china"
for key , value in laptop.items():
    print(key,":",value)
    
    