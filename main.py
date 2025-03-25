import os
from scripts.features import ClassType


def ClearScreen():
      # Windows
      os.system('cls')
      # Linux or Mac OS
      #os.system('clear')






def ChooseClass():
    print('직업을 선택하세요.')
    print('[1] 기사')
    print('[2] 궁수')
    print('[3] 법사')
    print()

    user_input = str(input('> '))
    choice = ClassType.NoneType
    
    if user_input == '1':
        choice = ClassType.Knight
    elif user_input == '2':
        choice = ClassType.Archer
    elif user_input == '3':
        choice = ClassType.Mage
    
    return choice


class Player:
    def __init__(self):
        self.hp = 0
        self.attack = 0


def CreatePlayer(choice:ClassType, player:Player):
    hp = 0
    attack = 0
    # 기사(100/10) 궁수(75/12) 법사(50/15)
    if choice == ClassType.Knight:
        player.hp=100
        player.attack=10
    elif choice == ClassType.Archer:
        player.hp=75
        player.attack=12
    elif choice == ClassType.Mage:
        player.hp=50
        player.attack=15
    else:
        player.hp=0
        player.attack=0
          

def main():
    
    while True:
        # 캐릭터 선택
        choice = ChooseClass()

        if choice == ClassType.NoneType:
            ClearScreen()
            print('[ 잘못된 입력입니다. 다시 선택해주세요.]')
        elif choice != ClassType.NoneType:
            # 캐릭터 생성
            player = Player()
            CreatePlayer(choice, player)
            
            print(f'HP:{player.hp}, Attack:{player.attack}')

            # 필드로 가서 몬스터랑 싸운다
        
        

if __name__ == '__main__':
    main()