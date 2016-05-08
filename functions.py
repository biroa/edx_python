#def calculate (k):
#    result = int(k)+5
#    return result
#
#n = input('give a number: ')
#result = calculate(n)
#print(result)


#def multiply(i,j):
    #return i*j


#def area_and_perimeter(height,width):
    #area = height*width
    #perimeter = (2*height)+(2*width)

    #return [area,perimeter]

#def circle_area(r):
    #pi=3.14
    #area = pow(r,2)*pi
    #return area

#def sum_list(list):
#    i=0
#    val = 0
#    while i<len(list):
#        val = val + list[i]
#        i +=1
#    return val/len(list)

#print(sum_list([1,2,3,4]))

#def maximum(list):
#    max = list[0]
#    i=0
#    while i<len(list):
#        if(max<list[i]):
#            max = list[i]
#        i=i+1
#    return max

#print(maximum([1,2,3,4]))

#def expr_evaluation(x):
#    y=pow(x,4)-12*pow(x,3)+13*pow(x,2)+11
#    return y

#print(expr_evaluation(3))

def magnitude_of_a_vector(list):
    magnitude = sqrt(pow(x,list[0])+pow(y,list[1])+pow(y,list[2]))
    return magnitude
