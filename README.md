# I-Ching
I-CHING package(Python周易占卜)

 I-CHING package

 by  https://github.com/SHMoney2021


 周易蓍草占卜过程：

    大衍之数五十，其用四十有九。分而为二以象两，挂一以象三，揲之以四以象四时，归奇于扐以象闰；
    五岁再闰，故再扐而后挂。天数五，地数五。五位相得而各有合。天数二十有五，地数三十，凡天地之数五十有五。
    此所以成变化而行鬼神也。乾之策二百一十有六，坤之策百四十有四，凡三百有六十，当期之日。
    二篇之策，万有一千五百二十，当万物之数也。是故四营而成《易》，十有八变而成卦，八卦而小成。
    引而伸之，触类而长之，天下之能事毕矣。显道神德行，是故可与酬酢，可与祐神矣。
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

    1. 图形化占卜过程（动态图像显示蓍草占卜全过程）
    2. 优化数据结构
    3. 添加通过网络展示功能


 Turtle图形显示：

![image](https://pic2.zhimg.com/80/v2-2ab66b3815bec7574eb344ced0739271_1440w.jpg)


 shell output:

    D:\python\python.exe D:/IChing.py
    ['011010', '水风', '井']
    ['001000', '地山', '谦']
    ['井 之 谦', '九五：井冽，寒泉食。']
    -------TEST-------
    After 10000 times & 0.25823440 seconds, the result is:
    Counter({'解': 198, '姤': 191, '大过': 184, '谦': 178, '随': 171, '困': 171, '萃': 171, '升': 168, '夬': 168, '贲': 168, '同人': 168, '剥': 168, '大有': 167, '履': 167, '益': 166, '坎': 166, '师': 165, '涣': 164, '既济': 164, '小过': 162, '渐': 162, '讼': 161, '坤': 159, '未济': 159, '咸': 158, '大壮': 158, '小畜': 157, '旅': 157, '蹇': 156, '艮': 156, '蛊': 155, '鼎': 155, '离': 155, '遯': 155, '节': 155, '无妄': 153, '家人': 153, '井': 153, '兑': 151, '巽': 151, '乾': 151, '大畜': 150, '复': 149, '比': 149, '蒙': 148, '噬嗑': 148, '否': 147, '恒': 147, '损': 147, '震': 146, '观': 145, '泰': 145, '需': 144, '豫': 144, '明夷': 144, '屯': 143, '丰': 143, '颐': 143, '中孚': 142, '归妹': 139, '睽': 139, '革': 136, '临': 134, '晋': 133})
    From the result, mean=156.25, std=12.91, std/mean=0.08
    -----TEST END-----






