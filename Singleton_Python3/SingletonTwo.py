
# 使用__new__
# 为了使类只能出现一个实例，我们可以使用 __new__ 来控制实例的创建过程

"""
在下面的代码中，我们将类的实例和一个类变量 _instance 关联起来，
如果 cls._instance 为 None 则创建实例，否则直接返回 cls._instance。
"""
class SingletonTwo:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonTwo, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class TestClss(SingletonTwo):
    a = 1


one = TestClss()
two = TestClss()
# 打印one和two的地址，是一样的
print(id(one), id(two))

