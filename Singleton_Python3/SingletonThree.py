# 使用装饰器

"""
我们知道，装饰器（decorator）可以动态地修改一个类或函数的功能。
这里，我们也可以使用装饰器来装饰某个类，使其只能生成一个实例
"""

from functools import wraps

def singleton(cls):
    instance = {}
    @wraps(cls)
    def getInstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return getInstance

@singleton
class SingletonThree:
    a = 1

one = SingletonThree()
two = SingletonThree()
# 打印one和two的地址，是一样的
print(id(one), id(two))






