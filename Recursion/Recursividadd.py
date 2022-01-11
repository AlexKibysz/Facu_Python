# proceso de recursion
# producto(3,4)
# 1  3+producto(3,3)
#  2       3+producto(3,2)
#   3           3+producto(3,1)
#    4                 3+producto(3,0)  b=0 por lo tanto return 0

# proceso backtracking
# 4 b=0 entonces return 0 3+0 = 3
# 3 el resultado de 4 es 3 entonces 3+3 = 6
# 2 el resultado de 3 es 6 entonces 3+6 = 9
# 1 el resultado 2 es 9 por lo tanto 3+9 = 12
# entonces el producto(3,4) es = 12

def producto(a, b):
    if a == 0 or b == 0:
        return 0
    return a + producto(a, b - 1)


a = producto(6, 6)
print(a)


#RECURSION FIBONACCI
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterminos = 20


if nterminos <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterminos):
       print(recur_fibo(i))


#fibonacci(1) y fibonacci (2) == 1

                    #n-1   #n-2
#fibonacci(6) = fibonacci(5) + fibonacci(4)
#  fibonacci(5)                     + fibonacci(4)
# fibonacci(4) + fibonacci(3)          fibonacci(3) + fibonacci(2)
#fibonacci(3) + fibonacci(2)
