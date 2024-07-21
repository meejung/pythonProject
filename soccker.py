print("안녕하세요, 구단주님. 팀 선수를 영입하고 판매하세요.====================================================================================================================================")
print("""
======================
1. 선수 확인
2. 선수 영입
3. 선수 판매
4. 종료하기
5. 구단 없애기
======================L
""")
players = ['Son Heung Min','Lionel Messi','Kylian Mbappé','Jordi Alba','Zinedine Zidane','Dani Carvajal','Virgil van Dijk','Kim Min Jae']

while True:
    number = int(input("원하는 번호를 입력하세요."))
    if number == 1:
        print("======players======")
        for i in players:
            print(i)
        print("================")
    elif number == 2:
        add_player = input("영입할 선수의 이름을 입력 하세요.")
        players.append(add_player)
    elif number == 3:
        remove_player = input("판매할 선수의 이름을 입력 하세요.")
        players.remove(remove_player)
    elif number == 4:
        print("종료합니다.")
        break
    elif number == 5:
        players = []
        print("구단이 없어졌습니다.")
    else:
        print("번호를 다시 입력하세요.")
