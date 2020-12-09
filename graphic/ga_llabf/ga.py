# -*- coding: utf-8 -*-

import llabf
import rect

# 1.个体染色体编码
# 2.k=0,随机产生m个个体初始化为群体pop(k)
# 3.对单个个执行对应算法，计算时个体适应度
# 4.判断是否满足停止条件，满足则输出最佳结果，否则，继续
# 5.利用排序选择操作选择m个个体形成新的群体selpop(k+1)
# 6.根据交叉概率Pc进行交叉操作，产生群体crosspop(k+1)
# 7.根据编译概率Pm进行编译操作，产生群体mutpop(k+1)
# 8.pop(k+1)=mutpop(k+1); k++ 转3，循环

class Zooid(object):
    def __init__(self, rect_list, max_width=2048, max_height=2048):
        self.__rect_list = rect_list

        self.__max_width = max_width

        self.__max_height = max_height

        self.__box_list = []
        
    def llabf(self):
        pass
        
    def fitness(self):
        pass
    
    def cross(self):
        pass
    
    def mutate(self):
        pass
    
    def encoding(self):
        pass


class GA(object):
    def __init__(self):
        self.__zooid_list = []
    
    def init_population(self, rect_list, size=100):
        pass
    
    def run(self):
        pass
        
    