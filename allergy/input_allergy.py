def input_allergy():
    print("아래의 알러지 유발 성분 중 해당하는 것의 번호를 입력해주세요.")
    print('1: 난류 \n2: 우유 \n3: 메밀 \n4: 땅콩 \n5: 대두 \n6: 밀'
          '\n7: 고등어 \n8: 게 \n9: 새우 \n10: 돼지고기 \n11: 복숭아'
          '\n12: 토마토 \n13: 아황산 \n14: 호두 \n15: 닭고기 \n16: 쇠고기'
          '\n17: 오징어 \n18: 조개류')
    print('띄어쓰기로 구분해서 입력해주세요\n')
    user_allergy = input()

    user_allergy = user_allergy.split(' ')

    return user_allergy