'''
def convert(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c
print(convert(78))
'''
f = float(input("Enter fahrenheight; "))
c = (f - 32) * 5/9
print(c)