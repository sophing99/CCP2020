import pandas as pd

def method1(name, text, method1_list):
    check_list = method1_list.loc[name]
    check_len = check_list.count()

    for k in range (check_len):
        if (text == check_list[k]):
            return True
    return False

def method2(name, text):
    check_name = name[0:2]
    result = text.find(check_name)

    if (result==0):
        return True
    else:
        return False