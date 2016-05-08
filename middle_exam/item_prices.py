def sum(l):
    l_length = len(l)
    sum_amount = 0
    for x in range(0,l_length):
        sum_amount+= l[x]

    return sum_amount

def items_price(a, b):
    a_length = len(a)
    b_length = len(b)
    price_per_quantity = []
    if(a_length != b_length):
        print('Sorry! The items in the two list must be the same.')
    else:
        for x in range(0,a_length):
            price_per_quantity.append(a[x]*b[x])

    return sum(price_per_quantity)

a = [2, 3, 5, 7, 9]
b = [5, 8, 4, 1, 11]

print(items_price(a,b))
