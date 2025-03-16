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

def main():
    
    while True:
        # 캐릭터 선택
        choice = ChooseClass()

        if choice == ClassType.NoneType:
            ClearScreen()
            print('[ 잘못된 입력입니다. 다시 선택해주세요.]')
        elif choice != ClassType.NoneType:
              break
        
        

if __name__ == '__main__':
    main()