function getHistory() {
  return document.getElementById("history-value").innerText;
}

function printHistory(num) {
  document.getElementById("history-value").innerText = num;
}

function getOutput() {
  return document.getElementById("output-value").innerText;
}

function printOutput(num) {
  if (num === "" || num === undefined) {
    document.getElementById("output-value").innerText = "";
  } else {
    document.getElementById("output-value").innerText = getFormattedNumber(num);
  }
}

function getFormattedNumber(num) {
  if (num === "-") {
    return "";
  }
  return Number(num).toLocaleString("en");
}

function reverseNumberFormat(num) {
  return Number(String(num).replace(/,/g, ""));
}

var operatorButtons = document.getElementsByClassName("operator");

for (var i = 0; i < operatorButtons.length; i++) {
  operatorButtons[i].addEventListener("click", function () {

    if (this.id === "clear") {
      printHistory("");
      printOutput("");

    } else if (this.id === "backspace") {
      var current = reverseNumberFormat(getOutput()).toString();
      current = current.slice(0, -1);
      printOutput(current);

    } else {
      var output = getOutput();
      var history = getHistory();

      if (output === "" && /[+\-*/%]$/.test(history.trim())) {
        history = history.trim().slice(0, -1);
      }

      if (output !== "" || history !== "") {
        if (output !== "") {
          var outputNum = reverseNumberFormat(output);
          history = history + " " + outputNum;
        }
      }

      if (this.id === "=") {
        var result = eval(history);
        printOutput(result);
        printHistory("");
      } else {
        history = history + " " + this.id;
        printHistory(history);
        printOutput("");
      }
    }
  });
}

var numberButtons = document.getElementsByClassName("number");

for (var j = 0; j < numberButtons.length; j++) {
  numberButtons[j].addEventListener("click", function () {
    var current = reverseNumberFormat(getOutput() || "0").toString();

    if (current === "0") {
      current = this.id;
    } else {
      current = current + this.id;
    }

    printOutput(current);
  });
}