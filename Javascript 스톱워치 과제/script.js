let startBtn = document.getElementById('start');
let stopBtn = document.getElementById('stop');
let resetBtn = document.getElementById('reset');
let timeDisplay = document.getElementById('time');
let recordList = document.getElementById('record-list');
let deleteBtn = document.getElementById('delete-selected');
let selectAllCircle = document.querySelector('.select-all .circle');

let timer = null;
let elapsedMs = 0;
let allSelected = false;

function formatTime(ms) {
  let sec = Math.floor(ms / 1000);
  let centi = Math.floor((ms % 1000) / 10);
  return `${sec.toString().padStart(2, '0')}:${centi.toString().padStart(2, '0')}`;
}

function updateDisplay() {
  timeDisplay.textContent = formatTime(elapsedMs);
}

startBtn.addEventListener('click', () => {
  if (timer) return;
  timer = setInterval(() => {
    elapsedMs += 10;
    updateDisplay();
  }, 10);
});

stopBtn.addEventListener('click', () => {
  if (timer) {
    clearInterval(timer);
    timer = null;
    addRecord(formatTime(elapsedMs));
  }
});

resetBtn.addEventListener('click', () => {
  elapsedMs = 0;
  updateDisplay();
});

function addRecord(time) {
  let li = document.createElement('li');
  li.className = 'record-item';

  let left = document.createElement('div');
  left.className = 'record-left';

  let circle = document.createElement('span');
  circle.className = 'circle';
  circle.addEventListener('click', () => {
    circle.classList.toggle('checked');
    updateSelectAllState();
  });

  let timeSpan = document.createElement('span');
  timeSpan.className = 'record-time';
  timeSpan.textContent = time;

  left.appendChild(circle);
  left.appendChild(timeSpan);

  li.appendChild(left);
  recordList.appendChild(li);
}

deleteBtn.addEventListener('click', () => {
  let items = document.querySelectorAll('.record-item');
  items.forEach(item => {
    let circle = item.querySelector('.circle');
    if (circle.classList.contains('checked')) {
      item.remove();
    }
  });
  updateSelectAllState();
});

selectAllCircle.addEventListener('click', () => {

  allSelected = !allSelected;

  let circles = document.querySelectorAll('#record-list .circle');
  circles.forEach(circle => {
    if (allSelected) {
      circle.classList.add('checked');
    } else {
      circle.classList.remove('checked');
    }
  });

  if (allSelected) {
    selectAllCircle.classList.add('checked');
  } else {
    selectAllCircle.classList.remove('checked');
  }
});

function updateSelectAllState() {
  let circles = document.querySelectorAll('#record-list .circle');
  if (circles.length === 0) {
    selectAllCircle.classList.remove('checked');
    allSelected = false;
    return;
  }

  let checkedCount = 0;
  circles.forEach(circle => {
    if (circle.classList.contains('checked')) checkedCount++;
  });

  if (checkedCount === circles.length) {
    selectAllCircle.classList.add('checked');
    allSelected = true;
  } else {
    selectAllCircle.classList.remove('checked');
    allSelected = false;
  }
}