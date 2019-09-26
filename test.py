class CustomClass:
    abc = 3

    def add_instance_method(self, a, b):
        return a + b

    @classmethod
    def add_class_method(cls, a, b):
        return a + b

    @staticmethod
    def add_static_method(a, b):
        return a + b


print(CustomClass.add_instance_method(None, 3, 5))

# 첫번째 인자가 클래스지만 생략하고 접근 해야한다
print(CustomClass.add_class_method(3, 5))

print(CustomClass.add_static_method(3, 5))

# classmethod도 staticmethod도 객체에서 접근이 가능하다

a = CustomClass()

print(a.add_class_method(5, 5))
print(a.add_static_method(5, 5))


print(a.add_static_method(3,4))
