class MetaCounter(type):
    count = 0

    def __new__(mcs, name, bases, namespace):
        mcs.count += 1
        namespace['count'] = mcs.count
        return super().__new__(mcs, name, bases, namespace)

class A(metaclass=MetaCounter):
    pass

class B(metaclass=MetaCounter):
    pass

class C(B):
    pass

print(A.count, B.count, C.count)