const display = document.getElementById("display");
const previous = document.getElementById("previous");
const keys = document.querySelector(".keys");

let currentInput = "0";
let firstOperand = null;
let operator = null;
let waitingForSecondOperand = false;

function updateDisplay() {
  display.textContent = currentInput;
}

function enterNumber(number) {
  if (waitingForSecondOperand) {
    currentInput = number;
    waitingForSecondOperand = false;
  } else {
    currentInput = currentInput === "0" ? number : currentInput + number;
  }
  updateDisplay();
}

function enterDecimal() {
  if (waitingForSecondOperand) {
    currentInput = "0.";
    waitingForSecondOperand = false;
  } else if (!currentInput.includes(".")) {
    currentInput += ".";
  }
  updateDisplay();
}

function calculate(a, b, op) {
  switch (op) {
    case "+": return a + b;
    case "−": return a - b;
    case "×": return a * b;
    case "÷": return b === 0 ? null : a / b;
    default: return b;
  }
}

function chooseOperator(nextOperator) {
  const inputValue = Number(currentInput);

  if (operator && !waitingForSecondOperand) {
    const result = calculate(firstOperand, inputValue, operator);
    if (result === null) {
      showError();
      return;
    }
    currentInput = String(Number(result.toPrecision(12)));
    updateDisplay();
    firstOperand = result;
  } else {
    firstOperand = inputValue;
  }

  operator = nextOperator;
  waitingForSecondOperand = true;
  previous.textContent = `${firstOperand} ${operator}`;
}

function showError() {
  currentInput = "خطا";
  firstOperand = null;
  operator = null;
  waitingForSecondOperand = true;
  previous.textContent = "تقسیم بر صفر امکان‌پذیر نیست";
  updateDisplay();
}

function performCalculation() {
  if (operator === null || waitingForSecondOperand) return;

  const secondOperand = Number(currentInput);
  const result = calculate(firstOperand, secondOperand, operator);

  if (result === null) {
    showError();
    return;
  }

  previous.textContent = `${firstOperand} ${operator} ${secondOperand} =`;
  currentInput = String(Number(result.toPrecision(12)));
  firstOperand = null;
  operator = null;
  waitingForSecondOperand = true;
  updateDisplay();
}

function clearCalculator() {
  currentInput = "0";
  firstOperand = null;
  operator = null;
  waitingForSecondOperand = false;
  previous.textContent = "";
  updateDisplay();
}

function deleteLast() {
  if (waitingForSecondOperand || currentInput === "خطا") return;
  currentInput = currentInput.length > 1 ? currentInput.slice(0, -1) : "0";
  if (currentInput === "-") currentInput = "0";
  updateDisplay();
}

function applyPercent() {
  if (currentInput === "خطا") return;
  currentInput = String(Number(currentInput) / 100);
  updateDisplay();
}

keys.addEventListener("click", (event) => {
  const button = event.target.closest("button");
  if (!button) return;

  if (button.dataset.number !== undefined) {
    enterNumber(button.dataset.number);
  } else if (button.dataset.operator) {
    chooseOperator(button.dataset.operator);
  } else {
    switch (button.dataset.action) {
      case "decimal": enterDecimal(); break;
      case "clear": clearCalculator(); break;
      case "delete": deleteLast(); break;
      case "percent": applyPercent(); break;
      case "equals": performCalculation(); break;
    }
  }
});

document.addEventListener("keydown", (event) => {
  if (/^[0-9]$/.test(event.key)) enterNumber(event.key);
  else if (event.key === ".") enterDecimal();
  else if (event.key === "+") chooseOperator("+");
  else if (event.key === "-") chooseOperator("−");
  else if (event.key === "*") chooseOperator("×");
  else if (event.key === "/") {
    event.preventDefault();
    chooseOperator("÷");
  } else if (event.key === "Enter" || event.key === "=") performCalculation();
  else if (event.key === "Backspace") deleteLast();
  else if (event.key === "Escape") clearCalculator();
});
