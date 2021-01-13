"""
1.인식한 글자가 판단 기준인 알레르기 대상 식품에 해당하는 품목을 정확히 포함하고 있을 때 일치하는 것으로 간주한다.-->우유,메밀,땅콩,대두,밀,게,새우,호두

2.맨앞 2글자가 기준과 일치하는 경우에는 정확히 일치하는 것으로 간주한다.-->고등어, 돼지고기, 복숭아, 토마토, 닭고기, 쇠고기, 아황산, 오징어

3. 인식된 글자가 메추리알, 거위알, 오리알인 경우에는 난류로 취급한다.

**포함 여부 기준

- 인식된 글자의 맨앞이나 맨뒤가 '우우'일 경우에는 우유와 일치
- 팡콩, 당콩, 명콩-->땅콩과 일치, 말,멀-->밀과 일치, 짓,젓-->잣과 일치, 머밀,머말,메멀-->메밀과 일치, 흐두,호도,호드-->호두와 일치
"""

import pandas as pd
import openpyxl
from allergy.allergy_method import *

def allergy_check(text):
    allergy = pd.read_excel('C:/Users/dainyoo/Desktop/korea/CCP/allergy.xlsx')
    allergy['허용 기준 method'] = [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1]

    method1_list = pd.read_excel('C:/Users/dainyoo/Desktop/korea/CCP/method1.xlsx', index_col=0)

    text = text.split(" ")
    script = pd.Series(text)
    word_amount = len(script)

    contain_allergy = {'난류':0, '우유':0, '메밀':0, '땅콩':0, '대두':0, '밀':0, '고등어':0, '게':0,
                       '새우':0, '돼지고기':0, '복숭아':0, '토마토':0, '아황산':0, '호두':0, '닭고기':0,
                       '쇠고기':0, '오징어':0, '조개류':0}

    allergy_num = len(allergy)

    for i in range(allergy_num):
        method = allergy.iloc[i][1]

        if (method==1):
            for j in range (word_amount):
                if (method1(allergy.iloc[i][0], script[j], method1_list)):
                    allergy_exist = allergy.iloc[i][0]
                    contain_allergy[allergy_exist] = 1

        if (method==2):
            for j in range (word_amount):
                if (method2(allergy.iloc[i][0], script[j])):
                    allergy_exist = allergy.iloc[i][0]
                    contain_allergy[allergy_exist] = 1

    return contain_allergy