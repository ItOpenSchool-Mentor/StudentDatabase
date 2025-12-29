
a = 3.1
b = 4.1
res = a + b

print(res)

# using round
print(round(res, 1))

# using decimal Module
from decimal import Decimal
print(Decimal('3.1') + Decimal('4.1'))

print(Decimal(str(3.1)) + Decimal(str(4.1)))


