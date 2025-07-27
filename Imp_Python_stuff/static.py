class MyClass:
    @staticmethod
    def greet():
        return "Hello"

    @classmethod
    def who_am_i(cls):
        return cls.__name__

print(MyClass.greet())      # Output: Hello
print(MyClass.who_am_i())   # Output: MyClass
