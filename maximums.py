def max_of_two(x, y):
    max=x
    if y>=x :
        return y
    else :
        return x

def max_of_three(x, y, z):
    if y>=x and y>z:
        return y
    elif x>=y and x>z:
        return x
    else:
        return z
