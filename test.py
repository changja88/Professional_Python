a = 'i am eun chang am hyun'
b = 'am'
print(
    a.find(b)
)
print(
    a.rfind(b)
)

str1 = "this is really a string example....wow!!!"
str2 = "is"

print(
    str1.find(str2)
)
print(
    str1.rfind(str2)
)


# print str1.rfind(str2)
# print str1.rfind(str2, 0, 10)
# print str1.rfind(str2, 10, 0)
#
# print str1.find(str2)
# print str1.find(str2, 0, 10)
# print str1.find(str2, 10, 0)
def a(a, *, b):
    return a + b


from inspect import signature
sig = signature(a)
print(a)
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
