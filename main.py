from enum import IntEnum

class ClassType(IntEnum):
        NoneType = 0,
        Knight = 1,
        Archer = 2,
        Mage = 3

def ChooseClass():
    print("직업을 선택하세요")
    print("[1] 기사")
    print("[2] 궁수")
    print("[3] 법사")

    user_input = str(input())
    choice = ClassType.NoneType
    
    if user_input == "1":
            choice = ClassType.Knight
    elif user_input == "2":
            choice = ClassType.Archer
    elif user_input == "3":
            choice = ClassType.Mage
    
    return choice

def main():
    
    while True:
        choice = ChooseClass()

        if choice != ClassType.NoneType:
            break
        
        

if __name__ == "__main__":
    main();