import os
from enum import IntEnum
import random
# from scripts.features import ClassType


def ClearScreen():
    # Windows
    # os.system('cls')
    # Linux or Mac OS
    os.system('clear')




class ClassType(IntEnum):
    NoneType = 0
    Knight = 1
    Archer = 2
    Mage = 3


class Player:
    def __init__(self):
        self.hp = 0
        self.attack = 0


class MonsterType(IntEnum):
    NoneType = 0
    Slime = 1
    Orc = 2
    Skeleton = 3


class Monster:
    def __init__(self):
        self.hp = 0
        self.attack = 0


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


def CreatePlayer(choice:ClassType, player:Player):
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


def CreateRandomMonster(monster:Monster):
    randMonster = random.randrange(1,4)
    if randMonster == MonsterType.Slime.value:
        print("슬라임이 스폰되었습니다!")
        monster.hp = 20
        monster.attack = 2
    elif randMonster == MonsterType.Orc.value:
        print("오크가 스폰되었습니다!")
        monster.hp = 40
        monster.attack = 4
    elif randMonster == MonsterType.Skeleton.value:
        print("스켈레톤이 스폰되었습니다!")
        monster.hp = 30
        monster.attack = 3
    else:
        monster.hp = 0
        monster.attack = 0
    # 랜덤으로 1~3 몬스터 중 하나 리스폰


def Fighit(player:Player, monster:Monster):
    while True:
        monster.hp -= player.attack
        if monster.hp <= 0:
            print('승리했습니다!\n')
            print(f'남은 체력: {player.hp}')
            break

        # 몬스터 반격
        player.hp -= monster.attack
        if player.hp <= 0:
            print('패배했습니다!\n')
            break


def EnterField(player:Player):
    while True:
        print('필드에 접속했습니다!')

        # 랜덤으로 1~3 몬스터 중 하나 리스폰
        monster = Monster()
        CreateRandomMonster(monster)

        print('[1] 전투 모드로 돌입')
        print('[2] 일정 확률로 마을로 도망')

        user_input = str(input('> '))
        if user_input == '1':
            ClearScreen()
            Fighit(player, monster)
        elif user_input == '2':
            # 33% 확률로 도망
            randValue = random.randrange(0, 101)
            if randValue <= 33:
                print('도망치는데 성공했습니다!')
                break
            else:
                print('도망치는데 실패했습니다!')
                Fighit(player, monster)


def EnterGame(player:Player):
    while True:
        print('마을에 접속했습니다!')
        print('[1] 필드로 간다')
        print('[2] 로비로 돌아가기')

        user_input = str(input('> '))
        if user_input == '1':
            ClearScreen()
            EnterField(player)
            break
        elif user_input == '2':
            ClearScreen()
            break



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
            # print(f'HP:{player.hp}, Attack:{player.attack}')

            ClearScreen()
            EnterGame(player)
        
        

if __name__ == '__main__':
    main()