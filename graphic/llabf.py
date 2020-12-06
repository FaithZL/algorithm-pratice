#!/usr/bin/python
# -*- coding: utf-8 -*-

class Rect(object):
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.update(x, y, width, height)

    def update(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def set_x(self, x):
        self.__x = y

    def set_y(self, y):
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

# lowest-level left align best fit 
# https://wenku.baidu.com/view/6c5ad9f24693daef5ef73df4.html
# (1)面积较大的矩形装入后产生的空洞较大,面积较小的矩形装入后产生的空洞较小;
# (2)面积较大的矩形装入后产生的空洞常常可以装入面积较小的矩形;
# (3)装入过程中产生的轮廓线越规整,即组成轮廓线的水平线数量越少，就越有利于后期矩形的装入.
class LLABF(object):
    def __init__(self, box_list, maxSize=2048):
        
        self.__box_list = box_list

        self.__maxSize = maxSize

    # 完全匹配优先，在可装入轮廓线中选择最低水平线(lowest horizontal line)e_k，如果有多个线段，优先选取最左边的
    # 从待装箱矩形中装入顺序依次与e_k进行比较，如果存在宽度或高度与e_kw相等并且刚好能左填平或右填平，则优先装入
    # 完全匹配能够减少装入后的轮廓线数量
    def full_fit_first(self):
        pass

    # 宽度优先匹配，在装入过程中优先装入宽度或高度与最低水平线相等的矩形，如果存在多个矩形，则装入面积最大的
    # WFF策略装入矩形之后，不会增加轮廓线的数量，该策略的好处是延迟较小矩形被装入的趋势
    def width_fit_first(self):
        pass

    # 高度优先匹配，在装入过程中优先装入，按序列顺序查询高度或宽度不大于最低水平线e_k，并且可以左填平的矩形
    # 与与FFF，WFF不同的是，HFF可能会产生产生更小的可装填区域，但可以提升轮廓线e_k-1的宽度
    def height_fit_first(self):
        pass

    # 组合宽度匹配优先，按照序列顺序查找两个矩形的组合，使组合之后的宽度等于最低水平线的长度，如果存在多种组合，则使用
    # 面积比较大的单个矩形填入
    # JWFF,WFF,FFF都避免在最低水平线上产生新的更小的可装填区域，从而减少了装箱过程中产生空洞的可能性
    def joint_width_fit_first(self):
        pass

    # 在一定范围内，查找宽度或高度不大于最低水平线的矩形，若其存在，直接装填，如果存在多个，则装填最大的面积最大的矩形
    # PF可能在最低水平线上产生新的更小的可装填区域
    def placeable_first(self):
        pass