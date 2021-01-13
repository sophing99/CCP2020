def compare_allergy(user_info, food_allergy):
    allergy_info = {1: '난류', 2: '우유', 3: '메밀', 4: '땅콩', 5: '대두',
                    6: '밀', 7: '고등어', 8: '게', 9: '새우', 10: '돼지고기',
                    11: '복숭아', 12: '토마토', 13: '아황산', 14: '호두',
                    15: '닭고기', 16: '쇠고기', 17: '오징어', 18:'조개류'}

    user_allergy = []
    for i in range(len(user_info)):
        user_allergy.append(allergy_info[int(user_info[i])])

    match_allergy = []
    for i in range(len(user_allergy)):
        is_allergy = food_allergy[user_allergy[i]]
        if (is_allergy == 1):
            match_allergy.append(user_allergy[i])

    return match_allergy