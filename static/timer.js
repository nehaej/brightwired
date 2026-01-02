//pomodoro timer 
const start = document.getElementById("start1");
const stopit = document.getElementById("stop1");
const reset = document.getElementById("reset1");
const timer = document.getElementById("pomo");

let timeLeft = 1500;
let interval;

const updateTimer = () => {
  const minutes = Math.floor(timeLeft / 60);
  const seconds = timeLeft % 60;

  timer.innerHTML = `${minutes.toString().padStart(2,'0')}
  :
  ${seconds.toString().padStart(2,'0')}`;
};

const startTimer = () => {
  clearInterval(interval);
  
  interval = setInterval(() => {
    timeLeft--;
    updateTimer();

    if (timeLeft === 0) {
      clearInterval(interval);
      alert("Time's up");
      timeLeft = 1500;
      updateTimer();
    }
  }, 1000);
};

const stopTimer = () => {clearInterval(interval);};

const resetTimer = () => {
  clearInterval(interval);
  timeLeft = 1500;
  updateTimer();
}

start.addEventListener("click",startTimer)
stopit.addEventListener("click",stopTimer)
reset.addEventListener("click",resetTimer)
