def n_elem_ciag(n, a1=1, q=2):
    return a1 * q**(n-1)

print("Podaj n, a1 oraz q aby obliczyc nty wyraz ciagu geometrycznego: ")
n = int(input("Podaj n: "))
a1 = float(input("Podaj a1: "))
q = float(input("Podaj q: "))

print(n, "wyraz ciagu geometrycznego wynosi: ", n_elem_ciag(n,a1,q))
