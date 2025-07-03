// 게임 상태 변수
let answer = [];
let attempts = 9;

// DOM 참조
const input1 = document.getElementById('number1');
const input2 = document.getElementById('number2');
const input3 = document.getElementById('number3');
const resultsDiv = document.getElementById('results');
const attemptsSpan = document.getElementById('attempts');
const submitButton = document.querySelector('.submit-button');
const resultImg = document.getElementById('game-result-img');

// 초기화
initGame();

function initGame() {
    // 0~9 중복 없는 세 자리 숫자 생성
    const nums = [];
    while (nums.length < 3) {
        const n = Math.floor(Math.random() * 10);
        if (!nums.includes(n)) {
            nums.push(n);
        }
    }
    answer = nums;
    console.log('정답:', answer);

    // 시도 횟수 리셋
    attempts = 9;
    attemptsSpan.textContent = attempts;

    // 결과창 및 인풋 비움
    resultsDiv.innerHTML = '';
    input1.value = '';
    input2.value = '';
    input3.value = '';
    resultImg.src = '';

    // 버튼 활성화
    submitButton.disabled = false;
}

function check_numbers() {
    if (attempts <= 0) return;

    const n1 = input1.value.trim();
    const n2 = input2.value.trim();
    const n3 = input3.value.trim();

    // 유효성 검사
    if (n1 === '' || n2 === '' || n3 === '') {
        input1.value = '';
        input2.value = '';
        input3.value = '';
        return;
    }

    // 숫자 배열로 변환
    const guess = [parseInt(n1), parseInt(n2), parseInt(n3)];

    // 스트라이크,볼 계산
    let strikes = 0;
    let balls = 0;

    for (let i = 0; i < 3; i++) {
        if (guess[i] === answer[i]) {
            strikes++;
        } else if (answer.includes(guess[i])) {
            balls++;
        }
    }

    // 출력할 div 생성
    const resultLine = document.createElement('div');
    resultLine.classList.add('check-result');

    const leftDiv = document.createElement('div');
    leftDiv.classList.add('left');
    leftDiv.textContent = `${n1} ${n2} ${n3}`;

    const rightDiv = document.createElement('div');
    rightDiv.classList.add('right');

    if (strikes === 0 && balls === 0) {
        // 아웃
        const outSpan = document.createElement('span');
        outSpan.classList.add('num-result', 'out');
        outSpan.textContent = 'O';
        rightDiv.appendChild(outSpan);
    } else {
        for (let i = 0; i < strikes; i++) {
            const sSpan = document.createElement('span');
            sSpan.classList.add('num-result', 'strike');
            sSpan.textContent = 'S';
            rightDiv.appendChild(sSpan);
        }
        for (let i = 0; i < balls; i++) {
            const bSpan = document.createElement('span');
            bSpan.classList.add('num-result', 'ball');
            bSpan.textContent = 'B';
            rightDiv.appendChild(bSpan);
        }
    }

    resultLine.appendChild(leftDiv);
    resultLine.appendChild(rightDiv);
    resultsDiv.appendChild(resultLine);

    // 시도 횟수 감소
    attempts--;
    attemptsSpan.textContent = attempts;

    // 게임 종료 조건
    if (strikes === 3) {
        resultImg.src = 'success.png';
        submitButton.disabled = true;
    } else if (attempts === 0) {
        resultImg.src = 'fail.png';
        submitButton.disabled = true;
    }

    // 입력창 비움 + 포커스
    input1.value = '';
    input2.value = '';
    input3.value = '';
    input1.focus();
}