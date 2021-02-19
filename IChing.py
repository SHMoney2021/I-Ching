# -*- coding: utf-8 -*-
"""
 I-CHING package
 by  https://github.com/SHMoney2021

 周易蓍草占卜过程：
    大衍之数五十，其用四十有九。分而为二以象两，挂一以象三，揲之以四以象四时，归奇于扐以象闰；\
    五岁再闰，故再扐而后挂。天数五，地数五。五位相得而各有合。天数二十有五，地数三十，凡天地之数五十有五。\
    此所以成变化而行鬼神也。乾之策二百一十有六，坤之策百四十有四，凡三百有六十，当期之日。\
    二篇之策，万有一千五百二十，当万物之数也。是故四营而成《易》，十有八变而成卦，八卦而小成。\
    引而伸之，触类而长之，天下之能事毕矣。显道神德行，是故可与酬酢，可与祐神矣。\
    子曰：“知变化之道者，其知神之所为乎？”
 解析：
    三变得一爻，十八变得一卦，为本卦，本卦老阳老阴爻变得到变卦，本卦+变卦即为占卜结果
    得到一爻的过程：(50 - 1) - [5, 9] - [4, 8] - [4, 8] = [24, 28, 32, 36]
 本代码占卜流程示例(泰 之 颐)：
    1. 按初爻到上爻顺序算得本卦 [7, 9, 9, 8, 8, 6]，从而变卦为 [7, 6, 6, 8, 8, 9]
    2. 本卦变换为字符串'111000'，外卦'000'为地， 内卦'111'为天，查表'111000'得到本卦卦名 '泰'
    3. 变卦变换为字符串'100001'，外卦'001'为山， 内卦'100'为雷，查表'100001'得到变卦卦名 '颐'
    4. 因此占卜结果为：泰 之 颐
    5. 根据变爻选择判词(7种情况之一)
 todo list:
    1. 添加卦爻辞
    2. 根据本卦变卦选择占卜结果判词
    3. 图形化占卜过程（动态图像显示蓍草占卜全过程）
    4. 优化数据结构
    5. 添加通过网络展示功能
"""
import time
from collections import Counter
from random import randint
import numpy as np
from turtle import *

# IChing类 - 封装占卜操作
class IChing():
    # 算得本卦及变卦
    # 结果：['011011', '111001']
    @staticmethod
    def get_guas() -> list:
        # 按初爻到上爻顺序算得本卦
        gua = [IChing._get_yao() for x in range(6)]
        gua_b = ''.join([str(x % 2) for x in gua])
        # 按初爻到上爻顺序算得变卦
        BIAN69 = {6: 9, 9: 6, 7: 7, 8: 8}
        gua2 = [BIAN69[x] for x in gua]
        gua_c = ''.join([str(x % 2) for x in gua2])
        return [gua_b, gua_c]

    # 查询卦名
    # 结果：'巽'
    @staticmethod
    def get_gua_name(gua) -> str:
        return IChingData.gua_name(gua)

    # 查询卦象
    # 结果：'风风'
    @staticmethod
    def get_gua_xiang(gua) -> str:
        return IChingData.gua_xiang(gua)

    # 根据本卦及变卦得到占卜结果
    # 结果采用朱熹总结的七种情况返回卦辞或爻辞
    @staticmethod
    def get_results(gua_b, gua_c) -> list:
        # 本卦
        result_guas = IChing.get_gua_name(gua_b)
        # 变卦
        if gua_b != gua_c:
            result_guas += ' 之 ' + IChing.get_gua_name(gua_c)
        # 判辞
        result_text = ''
        return [result_guas, result_text]

    # 算得一变
    # 结果：1st[5, 9] 2nd[4, 8] 3rd[4, 8]
    @staticmethod
    def _get_bian(shicao_nums) -> int:
        # 限定在中间值[-10, 10]之间模拟实际占卜过程，实际中随意两分不会差异太大
        # tian_num = randint(shicao_nums // 2 - 10, shicao_nums // 2 + 10)
        tian_num = randint(1, shicao_nums - 2)
        di_num = shicao_nums - tian_num
        di_num -= 1
        tian_num = tian_num % 4
        if tian_num == 0:
            tian_num = 4
        di_num = di_num % 4
        if di_num == 0:
            di_num = 4
        return tian_num + di_num + 1

    # 算得一爻
    # 结果: [6, 7, 8, 9]
    @staticmethod
    def _get_yao() -> int:
        shicao_nums = 50
        shicao_nums -= 1
        # 三变得一爻
        bian1st = IChing._get_bian(shicao_nums)
        assert bian1st in [5, 9]
        shicao_nums -= bian1st
        bian2nd = IChing._get_bian(shicao_nums)
        assert bian2nd in [4, 8]
        shicao_nums -= bian2nd
        bian3rd = IChing._get_bian(shicao_nums)
        assert bian3rd in [4, 8]
        shicao_nums -= bian3rd
        assert shicao_nums in [24, 28, 32, 36]
        return shicao_nums // 4

    # 卦辞
    @staticmethod
    def _get_gua_ci(gua) -> str:
        return IChingData.gua_ci(gua)

    # 爻辞
    @staticmethod
    def _get_gua_yaoci(gua, yao) -> str:
        return IChingData.gua_yaoci(gua, yao)


# IChingData类 - 封装卦爻数据
class IChingData():
    DICT_GUA2NAME = {'111111': '乾', '000000': '坤', '100010': '屯', '010001': '蒙', '111010': '需', '010111': '讼',
                     '010000': '师', '000010': '比', '111011': '小畜', '110111': '履', '111000': '泰', '000111': '否',
                     '101111': '同人', '111101': '大有', '001000': '谦', '000100': '豫', '100110': '随', '011001': '蛊',
                     '110000': '临', '000011': '观', '100101': '噬磕', '101001': '贲', '000001': '剥', '100000': '复',
                     '100111': '无妄', '111001': '大畜', '100001': '颐', '011110': '大过', '010010': '坎', '101101': '离',
                     '001110': '咸', '011100': '恒', '001111': '遯', '111100': '大壮', '000101': '晋', '101000': '明夷',
                     '101011': '家人', '110101': '睽', '001010': '蹇', '010100': '解', '110001': '损', '100011': '益',
                     '111110': '夬', '011111': '姤', '000110': '萃', '011000': '升', '010110': '困', '011010': '井',
                     '101110': '革', '011101': '鼎', '100100': '震', '001001': '艮', '001011': '渐', '110100': '归妹',
                     '101100': '丰', '001101': '旅', '011011': '巽', '110110': '兑', '010011': '涣', '110010': '节',
                     '110011': '中孚', '001100': '小过', '101010': '既济', '010101': '未济'}

    DICT_GUA2XIANG = {'111111': '天天', '000000': '地地', '100010': '水雷', '010001': '山水', '111010': '水天', '010111': '天水',
                      '010000': '地水', '000010': '水地', '111011': '风天', '110111': '天泽', '111000': '地天', '000111': '天地',
                      '101111': '天火', '111101': '火天', '001000': '地山', '000100': '雷地', '100110': '泽雷', '011001': '山风',
                      '110000': '地泽', '000011': '风地', '100101': '火雷', '101001': '山火', '000001': '山地', '100000': '地雷',
                      '100111': '天雷', '111001': '山天', '100001': '山雷', '011110': '泽风', '010010': '水水', '101101': '火火',
                      '001110': '泽山', '011100': '雷风', '001111': '天山', '111100': '雷天', '000101': '火地', '101000': '地火',
                      '101011': '风火', '110101': '火泽', '001010': '水山', '010100': '雷水', '110001': '山泽', '100011': '风雷',
                      '111110': '泽天', '011111': '天风', '000110': '泽地', '011000': '地风', '010110': '泽水', '011010': '水风',
                      '101110': '泽火', '011101': '火风', '100100': '雷雷', '001001': '山山', '001011': '风山', '110100': '雷泽',
                      '101100': '雷火', '001101': '火山', '011011': '风风', '110110': '泽泽', '010011': '风水', '110010': '水泽',
                      '110011': '风泽', '001100': '雷山', '101010': '水火', '010101': '火水'}

    # todo 添加卦辞、爻辞查询
    DICT_GUA2CI = {}
    DICT_GUA2YAOCI = {}

    @staticmethod
    def gua_name(gua) -> str:
        return IChingData.DICT_GUA2NAME.get(gua)

    @staticmethod
    def gua_xiang(gua) -> str:
        return IChingData.DICT_GUA2XIANG.get(gua)

    @staticmethod
    def gua_ci(gua) -> str:
        return IChingData.DICT_GUA2CI.get(gua)

    @staticmethod
    def gua_yaoci(gua, yao) -> str:
        return IChingData.DICT_GUA2YAOCI.get(gua)


# turtle图形显示占卜结果
def show_results(gua_b, gua_c):
    global g1, g2
    g1 = GUA(-100)
    g2 = GUA(100)

    ht(); penup(); goto(0, 200)
    write("周易占卜", align="center", font=("隶书", 60, ("bold")))

    penup(); goto(0, 200)
    for ch in gua_b:
        g1.push(YAO(ch))
    if gua_b != gua_c:
        for ch in gua_c:
            g2.push(YAO(ch))

    result_guas, result_text = IChing.get_results(gua_b, gua_c)

    penup(); goto(0, -100)
    write(result_guas, align="center", font=("隶书", 40, ("bold")))

    penup(); goto(0, -150)
    yin(50, "black", "white")
    yin(50, "white", "black")
    return

# 阳爻阴爻图形
class YAO(Turtle):
    def __init__(self, ch):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, 6 * 1.5, 2)
        if ch == '1':
            # 阳爻白色
            self.fillcolor(1, 1, 1)
        else:
            # 阴爻黑色
            self.fillcolor(0, 0, 0)
        self.st()


# 卦图形，每卦包含六爻
class GUA(list):
    def __init__(self, x):
        self.x = x

    def push(self, yao):
        yao.setx(self.x)
        yao.sety(-20 + 34 * len(self))
        self.append(yao)


def play():
    onkey(None, "space")
    clearscreen()
    main()


# 阴阳鱼小图
def yin(radius, color1, color2):
    speed('fastest')
    down()
    color("black", color1)
    begin_fill()
    circle(radius / 2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius / 2., 180)
    end_fill()
    left(90)
    up()
    forward(radius * 0.35)
    right(90)
    down()
    color(color1, color2)
    begin_fill()
    circle(radius * 0.15)
    end_fill()
    left(90)
    up()
    backward(radius * 0.35)
    down()
    left(90)


# 测试算得各卦的概率
def test(n):
    # 算n次频率统计
    R = []
    t = time.perf_counter()
    for _ in range(n):
        gua_b, gua_c = IChing.get_guas()
        R.append(IChing.get_gua_name(gua_b))
    print('-------TEST-------')
    print('After %d times & %.8f seconds, the result is:' % (n, time.perf_counter() - t))
    C = Counter(R)
    print(C)
    L = list(C.values())
    print('From the result, mean=%.2f, std=%.2f, std/mean=%.2f' % (
    np.mean(L), np.std(L, ddof=1), np.std(L, ddof=1) / np.mean(L)))
    print('-----TEST END-----')


# main() - 占卜并图形化显示
def main():
    # 占得本卦，变卦
    gua_b, gua_c = IChing.get_guas()
    print([gua_b, IChing.get_gua_xiang(gua_b), IChing.get_gua_name(gua_b)])
    print([gua_c, IChing.get_gua_xiang(gua_c), IChing.get_gua_name(gua_c)])
    print(IChing.get_results(gua_b, gua_c))
    # 可视化占卜结果
    show_results(gua_b, gua_c)

    onkey(play, "space")
    listen()
    return "EVENTLOOP"


if __name__ == "__main__":
    msg = main()
    # 测试10000次，看各卦概率是否平均
    test(10000)
    mainloop()
