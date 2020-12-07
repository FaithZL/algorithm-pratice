# -*- coding: utf-8 -*-

class Rect(object):
    def __init__(self, width, height, id):
        self.__x = -1
        self.__y = -1
        self.__width = width
        self.__id
        self.__height = height
        self.__transpose = False

    def set_id(self, val):
        self.__id = val

    def set_x(self, x):
        self.__x = y

    def set_y(self, y):
        self.__y = y

    @property
    def transpose(self):
        return self.__transpose

    def set_transpose(self, val):
        self.__transpose = val

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