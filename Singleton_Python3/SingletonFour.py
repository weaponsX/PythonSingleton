
# 使用元类 metaclass

"""
元类（metaclass）可以控制类的创建过程，它主要做三件事：

 **拦截类的创建
 **修改类的定义
 **返回修改后的类
"""

class SingletonFour(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingletonFour, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

#ptyhon 2
# class TestSingletonFour:
#     __metaclass__ = Singleton


#python3
class TestSingletonFour(metaclass=SingletonFour):
    pass


one = TestSingletonFour()
two = TestSingletonFour()
# 打印one和two的地址，是一样的
print(id(one), id(two))