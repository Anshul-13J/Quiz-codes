'''
For a number, let us say 'A', find two numbers 'x' & 'y' such that product of x & y is strictly greater than A and sum of x & y is minimum, then print x+y.

For example:

input=10 output=7

input=5 output=5
'''

def find(A):
    
    for i in range(1,1000000):
        for j in range(1,i+1):
            if i*j> A:
                return i+j
            
A= int(input())
print(find(A))
