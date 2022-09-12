class A(int):
    pass
def t()->list[int]:
    pass
print(t.__annotations__.get('return',''))
a=issubclass(t.__annotations__.get('return',''),int)
print(a)