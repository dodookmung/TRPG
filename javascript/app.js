const readline = require('readline');

function ask(question) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    return new Promise(resolve => {
        rl.question(question, (answer) => {
            rl.close();
            resolve(answer);
        });
    });
}



const ClassType = {
    NONE: 0,
    KNIGHT: 1,
    ARCHER: 2,
    MAGE: 3
};

const MonsterType = {
    NONE: 0,
    SLIME: 1,
    ORC: 2,
    SKELETON: 3
}

async function chooseClass() {
    console.log("직업을 선택하세요!");
    console.log("[1] 기사");
    console.log("[2] 궁수");
    console.log("[3] 법사");

    let choice = ClassType.NONE;
    const input = await ask(">");

    switch (input.trim()) {
        case "1":
            choice = ClassType.KNIGHT
            break;
        case "2":
            choice = ClassType.ARCHER
            break;
        case "3":
            choice = ClassType.MAGE
            break;
    }

    return choice
}

function Player() {
    return {
        hp: 0,
        attack: 0,
        classType: ClassType.NONE
    };
}

function Monster() {
    return {
        hp: 0,
        attack: 0
    };
}

function createPlayer(choice, player) {
    // 기사(100/10) 궁수(75/12) 법사(50/15)
    switch (choice) {
        case ClassType.KNIGHT:
            player.hp = 100;
            player.attack = 10;
            break;
        case ClassType.ARCHER:
            player.hp = 75;
            player.attack = 12;
            break;
        case ClassType.MAGE:
            player.hp = 50;
            player.attack = 15;
            break;
        default:
            player.hp = 0;
            player.attack = 0;
            break;
    }
}

function createRandomMonster(monster) {
    randMonster = Math.floor(Math.random() * 4);
    switch (randMonster) {
        case parseInt(MonsterType.SLIME):
            console.log("슬라입이 스폰되었습니다!");
            monster.hp = 20;
            monster.attack = 2;
            break;
        case parseInt(MonsterType.ORC):
            console.log("오크가 스폰되었습니다!");
            monster.hp = 40;
            monster.attack = 4;
            break;
        case parseInt(MonsterType.SKELETON):
            console.log("스켈레톤이 스폰되었습니다!");
            monster.hp = 30;
            monster.attack = 3;
            break;
        default:
            monster.hp = 0;
            monster.attack = 0;
            break;
    }
}

function Fight(player, monster) {
    while (true) {
        // 플레이어가 몬스터 공격
        monster.hp -= player.attack;
        if (monster.hp <= 0) {
            console.log("승리했습니다!");
            console.log(`남은 체력 : ${player.hp}`);
            break;
        }

        // 몬스터 반격
        player.hp -= monster.attack;
        if (player.hp <= 0) {
            console.log("패배 했습니다!");
            console.log(`남은 체력 : ${player.hp}`);
            break;
        }
    }
}
 
async function enterField(player) {
    while (true) {
        console.log("필드에 접속했습니다!");

        // 랜덤으로 1~3 몬스터 중 하나를 리스폰
        let monster = Monster();
        createRandomMonster(monster);

        console.log("[1] 전투 모드로 돌입");
        console.log("[2] 일정 확률로 마을로 도망");

        const input = await ask(">");
        if (input == "1") {
            Fight(player, monster);
        }
        else if (input == "2") {
            // 도망 확률 33%
            randValue = Math.floor(Math.random() * 101);
            if (randValue <= 33) {
                console.log("도망치는데 성공했습니다!");
                break;
            }
            else {
                Fight(player, monster);
            }
        }
    }
}

async function enterGame(player) {
    while (true) {
        console.log("마을에 접속했습니다!");
        console.log("[1] 필드로 간다");
        console.log("[2] 로비로 돌아가기");

        const input = await ask(">");
        if (input == "1") {
            await enterField(player);
        }
        else if (input == "2") {
            break;
        }
    }
}

async function main() {
    let choice = ClassType.NONE;
    
    while (true) {
        choice = await chooseClass();
        
        if (choice !== ClassType.NONE) {
            // 캐릭터 생성
            let player = Player();
            createPlayer(choice, player);
            console.log(`HP ${player.hp} Attack ${player.attack}`);
            
            await enterGame(player);
        }
    }
}

main();