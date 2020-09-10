from decimal import *

data_list = list(map(Decimal, "2.54 2.36 2.636 2.9 9.25 6363".split()))
print(sum(data_list))
print("Sike, that's the wrong number!")
