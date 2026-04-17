def apply_discount(price, discount_pct):
    return price * (1 - discount_pct / 100)

def apply_tax(price, tax_pct):
    return price * (1 + tax_pct / 100)


def final_price(price, quantity, discount_pct, tax_pct):
    subtotal=(price*quantity)
    descuento=(apply_discount(subtotal, discount_pct))
    preciofinal=(apply_tax(descuento, tax_pct))
    return round(preciofinal,2)

def best_deal(price_a, qty_a, disc_a, price_b, qty_b, disc_b, tax_pct):
    preciofin_A=apply_tax(apply_discount(price_a*qty_a, disc_a), tax_pct)
    preciofin_B=apply_tax(apply_discount(price_b*qty_b, disc_b), tax_pct)
    if preciofin_A>preciofin_B:
        return "B"
    elif preciofin_A<preciofin_B:
        return "A"
    else:return "A"