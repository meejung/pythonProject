print("===============welcome to super simple hamburger store!!====================")


print("""

=====================

1.평범한 메뉴 확인
2.평범한 메뉴 추가
3.평범한 메뉴 삭제
4.평범하게 구걸하기
5.평범하게 가게 폭파시키기
=====================
""")

menu = ['평범한버거','완전 평범한 버거','심각하게 평범한 버거','더블 평범한 버거']

while True:
    number = int(input("원하는 번호를 입력하세요."))
    if number == 1:
        print('=======menu=======')
        for  i in menu:
            print(i)
        print('==================')
    elif number == 2:
        add_menu = input("추가할 메뉴 이름을 입력하시오")
        menu.append(add_menu)
    elif number == 3:
        remove_menu = input("삭제할 메뉴의 이름을 입력하세요")
        menu.remove(remove_menu)
    elif number == 4:
        print("You: 제발 돈 좀 줘요")
        print("손님: 와우 구걸도 진짜 평범하네 불쌍하니까 돈 줘야지")
        print("100원 추가되었습니다")
    elif number == 5:
        print("""
        ▇▇▇▇▇▇▇▇        ▇▇▇▇▇▇▇ ▇  
           ▇    ▇               ▇   ▇     ▇   
           ▇    ▇               ▇   ▇     ▇▇    
        ▇▇▇▇▇▇▇▇        ▇▇▇▇▇▇▇ ▇
              ▇                             
        ▇▇▇▇▇▇▇▇            ▇▇▇▇▇▇▇
                                              ▇
        ▇▇▇▇▇▇▇▇            ▇▇▇▇▇▇▇ 
                     ▇            ▇           
                     ▇            ▇▇▇▇▇▇▇
        """)
        print("the end")
        break
    else:
        print("번호를 다시 입력하세요")

