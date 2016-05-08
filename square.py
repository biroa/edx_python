# Type your code here
num = int(input('give me a number:'))
def square(n):
    i=1    
    while(i<=n):
        echo = ''
        for j in range(0,n):
            echo=echo+'*'
        print(echo)
        i+=1

square(num)
