#i=1
#summ = 0
#while i<=101:
#    if i%5 == 0:
#        summ +=i       
#    i=i+1
#print(summ)

#number = int(input('give me an integer'))
#i=1
#counter=1
#while(i<=number):
#    counter *= i
#    i +=1
#print(counter)

#i=1
#summ = 0
#while i<=1001:
#    summ =summ+i
#    i+=3
#print(summ)


#list = range(1,102)

#summ=0
#for i in list:
#    if i%2==0:
#        summ = summ+i
#print(summ)

#number = int(input('give me an integer'))
#list = range(1,number+1)
#summ=0
#for i in list:
#        summ = summ+i
#print(summ)


#number = int(input('give me an integer'))
#list = range(1,number+1)
#summ=0
#for i in list:
#        summ = summ+pow(i,2)
#print(summ)


#number = int(input('give me an integer'))
#list = range(0,number+1)
#for i in list:
#        print(pow(10,i))


#count = 20
#for x in range(0,10):
#    count = count - 1
#    if x == 2:
#        break
#print(count)

#k = 1
#while k<5:
#    if k % 7 == 0:
#        break
#    k = k + 2
#print(k)

#my_list = ["dog", 24, "cat", 12]
#count = 0
#for element in my_list:
#    if element == "cat":
#        continue
#    count = count + 1
#print(count)

#my_str = "university"
#count = 0
#for char in my_str:
#    if char == "i":
#        continue
#    else:
#        count = count + 1
#print(count)

#my_str = "university"
#count = 0
#for char in my_str:
#    count = count + 1
#    if char == "e":
#        break  
#print(count)

#my_list = [6, 5, 7, 2, 3, 5, 7, 8] 
#count = 0
#for number in my_list:
#    if number == 5 or number == 7:
#        continue
#    else:
#        count = count + number
#print(count)

#m = 0
#for x in range(1,4):
#    print('*********')
#    for y in range(1,3):   
#        m = m + 1
#        print(m)
#print('------------')
#print (m)

#m = 0
#for x in range (1,3):
#   for y in range (4,6):
#      m = m + x + y
#print (m)

#m = 03
#for x in range (1,3):
#   k = 0
#   for y in range (-2,0):
#      k = k + y
#      m = m + k
#print (m)

#m = 0
#for x in [3,5,3]:
#   for y in range (10,11):
#      m = m + x + y
#      print(m)
#      print('-------------')
#print (m)


#m = 0
#x = 1
#while x < 4:
#    y = 1
#    while y < 3:
#        m = m + x + y
#        y = y + 1
#    x = x + 1
#print(m)


#m = 0
#x = 1
#while x < 4:
#    y = 1
#    while y < 5:   
#        m = m + y
#        y = y + 1
#        if x + y == 5:
#            break
#    x = x + 1
#print (m)

#m = 0
#$x = 10
#hile x > 8:
#   for y in range(1,3):
#        m = m + 1
#    x = x - 1
#print(m)

#m = 1
#for x in [1,2,3]:
#    for y in [3,1,4]:
#        if x == y:
#            m = m * x 
#print (m)

#m = 1
#my_list_1 = [2 , 4, 1]
#for x in my_list_1:
#    for y in range(1,3):
#        if (x + y) % 3:
#            print(x,y)
#            m = m * x
#print (m)

m = 0
my_str_1 = "university"
my_str_2 = "mississipy"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 == char_2:
            m = m + 1
print(m)
