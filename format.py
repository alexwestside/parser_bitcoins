from decimal import *

context = Context(prec=5, rounding=ROUND_HALF_UP)
setcontext(context)


n = Decimal(1.99999997)
# print('{:.5f}'.format(n))
# print('%.8f' % (n))
# print(Decimal(n).quantize(Decimal('.01')))

# print('{0:.6f}'.format(n))
# print(round(n))
# print(Decimal(n))
print(Decimal(n).quantize(rounding=None, context=6))