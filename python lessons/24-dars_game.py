import random as r
def son_top(number=10):
    son1 = r.randint(1,number)
    print("1 dan 10 gacha son o'yladim. Topa olasizmi?: ")
    urunish_us = 0
    while True:
        user_number = int(input())
        urunish_us +=1
        if son1 == user_number:
            print(f"Topdingiz! {son1} sonini o'ylagan edim. {urunish_us} ta taxmin bilan topdingiz.")
            break
        elif son1 < user_number:
            print(f"Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
            continue
        else:
            print(f"Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
            continue
    return urunish_us


def son_top_pc(son=10):
    print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
    user = input("Son o'ylagan bolsangiz istalgan tugmani bosing.")
    urunish_pc = 0
    son = 10
    i = 1
    while True:
        son2 = r.randint(i,son)
        user_input = input(f"Siz {son2} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)?? ")
        urunish_pc +=1
        if user_input == 't':
            print(f"Soningizni {urunish_pc} ta taxmin bilan topdim!")
            break
        elif user_input == '-':
            son = son2 - 1
            continue
        else:
            i = son2 + 1
            continue
    return urunish_pc

while True:
    print("Son top o'yini!")
    man = son_top()
    print("\nKeling endi sizni novbatingiz!")
    pc = son_top_pc()
    if man == pc:
        print(f"\nSoningizni {pc} ta taxmin bilan topdim!"
              f"\nSiz {man} ta taxmin bilan topdingiz. Hisobimiz durrang")
    elif man < pc:
        print(f"\nSoningizni {pc} ta taxmin bilan topdim!"
              f"\nSiz {man} ta taxmin bilan topdingiz va yutdingiz")
    else:
        print(f"\nSoningizni {pc} ta taxmin bilan topdim!"
              f"\nSiz {man} ta taxmin bilan topdingiz va yutqazdingiz")
    user = input("\nYana o'ynaymizmi? Ha: (1), Yoq: (0) ")
    if user == "1":
        continue
    else:
        break    
