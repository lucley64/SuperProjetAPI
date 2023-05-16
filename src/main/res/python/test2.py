def produit(a, b):
    res = 0
    if (a % 2 == 0):
        def somme(a, b):
            return a+b
        while a > 0:
            a -= 1
            res = somme(res, b)
        return res
    else :
        return 0

print(produit(4, 4))