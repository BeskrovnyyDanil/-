import math
def triangl_1(kat1, kat2):
    kvgip = kat1 ** 2 + kat2 ** 2
    gip = math.sqrt(kvgip)
    return gip
def triangl_2(kat1, kat2):
    kvgip = kat1 ** 2 + kat2 ** 2
    gip = math.sqrt(kvgip)
    return gip
if triangl_1(3, 4) > triangl_2(5, 8):
    print("Первая больше")
else:
    print("Первая меньше")
