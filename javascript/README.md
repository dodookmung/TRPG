# JavaScript

npm 외부 모듈 없이 Vanilla JavaScript로 TRPG를 구현</br>
TRPG 특성상 콘솔에서 입력을 받기 때문에 node.js로 구현함</br>


</br></br>
```javascript
function Fight(player, monster) {
    while (true) {
        // 플레이어가 몬스터 공격
        monster.hp -= player.attack;
        if (monster.hp <= 0) {
            console.log("승리했습니다!");
            console.log(`남은 체력 : ${player.hp}`);
            break;
        }
    }
}
```

`Fight()` 함수에서 먼저 `monster.hp` 와 `player.attack`를 대조하기 때문에</br>
체력이 0이나 -1 음수까지 가더라도, `player.attack`가 높다면</br>
"승리하였습니다" 출력하는 버그가 있음.