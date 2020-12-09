# -*- coding: utf-8 -*-

from rect import Rect

# lowest-level left align best fit 
# https://wenku.baidu.com/view/6c5ad9f24693daef5ef73df4.html
# https://www.cnblogs.com/slysky/p/3949027.html
# (1)面积较大的矩形装入后产生的空洞较大,面积较小的矩形装入后产生的空洞较小;
# (2)面积较大的矩形装入后产生的空洞常常可以装入面积较小的矩形;
# (3)装入过程中产生的轮廓线越规整,即组成轮廓线的水平线数量越少，就越有利于后期矩形的装入.

# horizontal line
class HL(object):
    def __init__(self, x, width, height):
        self.x = x
        self.width = width
        self.height = height

class Box(object):

    def __init__(self, rect_list, width=2048, height=2048):
        
        self.__rect_list = rect_list

        self.__filled_rect_list = []

        self.__width = width

        self.__hl_list = []

        self.__height = height

        self.initial()

    def initial(self):
        self.__hl_list.append(HL(0, self.__width, 0))

    def run(self):
        self.initial()
        idx = 0
        while (not self.complete()):
            lhl_idx = self.lowest_horizontal_line()
            rect_idx = self.full_fit_first(lhl_idx)
            if rect_idx is None:
                rect_idx = self.width_fit_first(lhl_idx)
            if rect_idx is None:
                rect_idx = self.height_fit_first(lhl_idx)
            if rect_idx is None:
                rect_idx = self.joint_width_fit_first(lhl_idx)
            if rect_idx is None:
                rect_idx = self.placeable_first(lhl_idx)
            if rect_idx is None:
                break
            self.filling(rect_idx)

        return self.__rect_list

    def complete(self):
        return not (self.__rect_list)


    # 完全匹配优先，在可装入轮廓线中选择最低水平线(lowest horizontal line)e_k，如果有多个线段，优先选取最左边的
    # 从待装箱矩形中装入顺序依次与e_k进行比较，如果存在宽度或高度与e_kw相等并且刚好能左填平或右填平，则优先装入
    # 完全匹配能够减少装入后的轮廓线数量
    def full_fit_first(self, lhl_idx):
        lh = self.left_height(lhl_idx)
        rh = self.right_height(lhl_idx)
        width = self.__hl_list[lhl_idx].width
        satisfy_idx_list = []
        for i, rect in enumerate(self.__rect_list):
            if rect.width == width and rect.height in [lh, rh]:
                satisfy_idx_list.append(i)
            elif rect.width in [lh, rh] and rect.height == width:
                satisfy_idx_list.append(i)
        

    # 宽度优先匹配，在装入过程中优先装入宽度或高度与最低水平线相等的矩形，如果存在多个矩形，则装入面积最大的
    # WFF策略装入矩形之后，不会增加轮廓线的数量，该策略的好处是延迟较小矩形被装入的趋势
    def width_fit_first(self, lhl_idx):
        for i, rect in enumerate(self.__rect_list):
            pass

    # 高度优先匹配，在装入过程中优先装入，按序列顺序查询高度或宽度不大于最低水平线e_k，并且可以左填平的矩形
    # 与与FFF，WFF不同的是，HFF可能会产生产生更小的可装填区域，但可以提升轮廓线e_k-1的宽度
    def height_fit_first(self, lhl_idx):
        for i, rect in enumerate(self.__rect_list):
            pass

    # 组合宽度匹配优先，按照序列顺序查找两个矩形的组合，使组合之后的宽度等于最低水平线的长度，如果存在多种组合，则使用
    # 面积比较大的单个矩形填入
    # JWFF,WFF,FFF都避免在最低水平线上产生新的更小的可装填区域，从而减少了装箱过程中产生空洞的可能性
    def joint_width_fit_first(self, lhl_idx):
        for i, rect in enumerate(self.__rect_list):
            pass

    # 在一定范围内，查找宽度或高度不大于最低水平线的矩形，若其存在，直接装填，如果存在多个，则装填最大的面积最大的矩形
    # PF可能在最低水平线上产生新的更小的可装填区域
    def placeable_first(self, lhl_idx):
        for i, rect in enumerate(self.__rect_list):
            pass

    def lowest_horizontal_line(self):
        height = self.__height
        ret = -1
        for i, hl in enumerate(self.__hl_list):
            if hl.height < height:
                height = hl.height
                ret = i
        return ret

    def lowest_horizontal_line_height(self, lhl_idx):
        lh = self.left_height(lhl_idx)
        rh = self.right_height(lhl_idx)
        return rh if rh < lh else lh
        
    def left_height(self, lhl_idx):
        if lhl_idx == 0:
            return self.__height - self.__hl_list[lhl_idx].height
        return self.__hl_list[lhl_idx - 1].height - self.__hl_list[lhl_idx].height

    def right_height(self, lhl_idx):
        if lhl_idx == len(self.__hl_list) - 1:
            return self.__height - self.__hl_list[lhl_idx].height
        return self.__hl_list[lhl_idx + 1].height - self.__hl_list[lhl_idx].height

    def usage(self):
        valid_area = 0
        for rect in self.__filled_rect_list:
            valid_area += rect.area()
        return valid_area / (self.__height * self.__width)

    # 装填，更新矩形数据，更新水平线数据
    def filling(self, rect_idx, lhl_idx):
        pass




