#!/bin/env python
import numpy as np
import matplotlib.pyplot as plt


def multipoint(f,x0,h,flag='f'):
    """TODO: Docstring for multipoint.

    :f: 函数
    :x0: 数或者数组
    :h: 步长
    :flag: 'f'-前差,'b'-后差,'c'-中心差,'3f'-3点前差,'3b'-3点后差
    :returns: x0的一阶导数。

    """
    y0  = f(x0)
    y1  = f(x0+h)
    y2  = f(x0+2*h)
    y_1 = f(x0-h)
    y_2 = f(x0-2*h)

    if 'f' in flag:
        df = (y1-y0)/h
    if 'b' in flag:
        df = (y0-y_1)/h
    if 'c' in flag:
        df = (y1-y_1)/(2*h)
    if '3f' in flag:
        df = (-3*y0+4*y1-y2)/(2*h)
    if '3b' in flag:
        df = (3*y0+4*y_1-y_2)/(2*h)

    return df


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    print("==========例题4.1.2==========")

    x  = np.linspace(0,np.pi,16)
    y  = np.sin(x)
    yp = np.cos(x)
    df1 = multipoint(np.sin,x,np.pi/64,'f')
    df3 = multipoint(np.sin,x,np.pi/64,'c')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,df1,'r-',x,df3,'k.-',x,y,'b--',x,yp,'o')
    plt.grid()
    plt.legend(("front difference","center differenc","sin(x)","cos(x)"))
    # plt.legend("1","2","原函数","导数函数")
    plt.show()

if __name__ == "__main__":
    main()


