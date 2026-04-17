# ---- Funciones provistas (NO modificar) ----

def is_even(n):
    if n % 2==0 and n!=0:
        return True
    else:
        return False

def is_positive(n):
    if  n >0:
        return True
    elif n<0:
        return False
    else:
        return "Zero"

# ---- Función a implementar ----

def classify_number(n):
    if is_even(n)==True and  is_positive(n)==True:
        return "positive even"
    elif is_even(n)==False and  is_positive(n)==True:
        return "positive odd"
    elif  is_even(n)==True and  is_positive(n)==False:
        return "negative even"
    elif is_even(n)==False and is_positive(n)==False:
        return "negative odd"
    else:return "zero"