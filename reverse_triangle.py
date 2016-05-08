# Type your code here
num = int(input('give me a number:'))
def reversetriangle(n):
    for i in range(n,0,-1):
        echo=''
        for j in range(0,i):
            echo+=echo+'*'
        print(echo)
reversetriangle(num)
