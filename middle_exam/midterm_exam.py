########### Midterm Exam Question 1

#x = ["dog", 2, "cat", 34, 5.8]
#m = 0
#for i in range(len(x)):
#    print(i)
#    m = m + i
#print(m)

########### Midterm Exam Question 2

#def my_fun(x,y):
#    m = x ** y  
#y = my_fun(2, 3)    
#print(y)

########### Midterm Exam Question 3

#i = 1
#while False:
#    if i % 5 == 0:
#        break
#    i = i + 2
#print(i)

########### Midterm Exam Question 4

#count = 0
#list_1 = []
#for i in range(1,4):
#    list_1.append(i**2)
#for x in list_1:
#    print(x)
#    count = count + x
#print(count)

########### Midterm Exam Question 5

#def my_fun(a):
#    a[0] = 'new value:'     
#    a[1] = a[1] + 1      #
#
#x = ['old value:', 99]
#my_fun(x)
#print (x[0], x[1])

########### Midterm Exam Question 6

#x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
#count = 0
#for item in x:
#    m = 0
#    if item == "pet" or item == 3:
#        m = x.index(item)
#        count = count + m
#print(count)

########### Midterm Exam Question 7

#count = 0
#my_list = [2, 4, 1, 5, 7, 3, 9, 4]
#new_list = my_list[1:7:2]
#for item in new_list:
#    count = count + 1
#print(count)

########### Midterm Exam Question 8

#x = 0
#my_list = []
#while x < 10:
#    if x % 2 == 0:
#        my_list.append("dog")
#    elif x % 3 == 0:
#        my_list.remove("dog")
#    x = x + 1
#print(my_list.count("dog"))

########### Midterm Exam Question 9

#list_1 = ["dog", 3, "cat" , 25, 2.4]
#list_2 = ["car", 25, "dog" , 43]
#count = 0
#for item in list_1:
#    if item in list_2:
#        count = count + 1
#print (count)

########### Midterm Exam Question 10

#def my_fun(x):
#    z = 0
#    for item in x:
#        m = x.count(item)
#        if m > z:
#            z = m
#    return z
#
#y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
#print (my_fun(y))

########### Midterm Exam Question 11
#[1, 41, 81]

#my_list = []
#for k in range(1,101,20):
#    my_list.append(k)
#    print(k)
#print (my_list[: :2] ) => [1, 41, 81]

########### Midterm Exam Question 12 ???
#[1, 5, 3, 1, 1, 5]

#def my_fun(x):
#    for k in range (len(x)):
#        x.extend(x[:k])
#m = [1,5,3]
#my_fun(m)
#print(m) => [1, 5, 3, 1, 1, 5]

########### Midterm Exam Question 13
#[1, 5, 3, [], [1], [1, 5]]

#def my_fun(x):
#    for k in range (len(x)):
#        print(k)
#        print(x[:k])
#        x.append(x[:k])
#m = [1,5,3]
#my_fun(m)
#print(m) => [1, 5, 3, [], [1], [1, 5]]

########### Midterm Exam Question 14
# We stick to the index that means we push
# Elements upward in the list
#[1, 9, 8, 3, 2, 7]

#my_list = [9, 8, 7]
#for k in range (3):
#    print(k)
#    my_list.insert(-k, k+1)
#print(my_list) => [1, 9, 8, 3, 2, 7]

########### Midterm Exam Question 15
# ['cat', 62]

#my_list = [12, "cat", 3.4, "dog", 62]
#new_list = []
#for k in range(5):
#    if k % 2:
#        m = my_list.pop(k)
#        print(m)
#        new_list.append(m)
#print(new_list)=> ['cat', 62]

########### Midterm Exam Question 16
# [2, 3, 15]

#def my_fun(my_list,s,e):
#    del (my_list[s:e])
# 
#values = [2, 9, 16, 3, 24, 13, 15]
#my_fun(values,-6,-4)
#my_fun(values,2,4)
#print(values) => [2, 3, 15]

########### Midterm Exam Question 17
# [3]

#def my_fun(i):
#    values = []
#    values.append(i)
#    return values
#my_fun(5)
#print(my_fun(3)) => [3]

########### Midterm Exam Question 18
# [9, 3, 15]

#def my_fun(m):
#    x = []
#    for k in range(len(m)):
#        if m[k] % 3 == 0 and m[k] % 2:
#            x.insert(k, m[k])
#    return x
# 
#values = [2, 9, 16, 3, 24, 13, 15]
#print(my_fun(values)) => [9, 3, 15]

########### Midterm Exam Question 19
# [6,5,9]

#def my_fun(m, increment):
#    x = 0
#    while x < len(m):
#        m[x] = m[x] + increment
#        x = x + 1
#    return m 
#
#values = [4, 3, 7]
#print(my_fun(values, 2))  => [6,5,9]

########### Midterm Exam Question 20
# [[3,4], 2.9,'dog']

#def my_fun(m):
#    x = m[:]
#    for k in x:
#        if type(k) == int:
#            m.remove(k)
#
#values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
#my_fun(values)
#print(values) => [[3,4], 2.9,'dog']
