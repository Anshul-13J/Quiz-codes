/*Find the minimum absolute difference of indexes between 'x' and 'o' in a string consisting only of 'x','.','o'
If no such pair is found return -1.

Example:
input='x....x.o..x..'
output= 2

input='....xxxx...x'
output= -1
*/

def find_ind(string , var):     
    '''
    To return list of all the indexes of var in string.
    
    '''
    x=[]
    for i in range(len(string)):
        if A[i]== var:
            x.append(i)
    return x
    

def search(A):
    
    
    x = find_ind(A,'x') 
    o = find_ind(A,'o') 
    diff = []
    for i in x:
        for j in o:
            diff.append(abs(i-j))
            
    if len(diff)==0:
        return -1
    
    diff.sort()
    return diff[0]
    
    
    

A= input()
print(search(A))
        
        
    
