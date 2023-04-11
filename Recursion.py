#Arithmetic sequence(등차수열): 1, 3, 5, 7 ... 연속한 두 항의 공차가 일정한 수열
        
def seq(n):
    #경계조건(탈출)
    if n == 1: 
        return 1
    else:
        #재귀호출
        return seq(n-1) + 3 #공차3
         

print(seq(1)) #1 
print(seq(3)) #7 공차가 3일때, 3번째 값 1 4 7, #관계성립(작은 <-> 큰)


        
#Fibonacci number(피보나치수열): 어떤 수열의 앞의 두 항의 합과 같은 수열
def fib(n):
    #경계조건(탈출)
    if n == 1 or n == 2:
        return 1
    else:
        #재귀호출
        return fib(n-1) + fib(n-2)
    
print(fib(4)) #3 #관계성립(작은 <-> 큰), 1 1 2 3 5 ...
    

    
        