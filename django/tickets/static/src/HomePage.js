const today = new Date();
let year = today.getFullYear();
const datePicker = document.getElementById("datePicker");
const daysOfWeek = [
  "Воскресенье",
  "Понедельник",
  "Вторник",
  "Среда",
  "Четверг",
  "Пятница",
  "Субота",
];

function formatDate(year, month, date) {
  if (month < 10) {
    month = "0" + month;
  }
  if (month === "00") {
    month = "12";
  }
  if (date < 10) {
    date = "0" + date;
  }
  return [year, month, date];
}

function getNextSevenDays(date) {
  const nextSevenDays = [today];
  for (let i = 0; i < 6; i++) {
    const nextDay = new Date(date);
    nextDay.setDate(date.getDate() + i + 1);
    nextSevenDays.push(new Date(nextDay));
  }

  return nextSevenDays;
}

function setCards(date) {
  let step = 0;
  const nextSevenDays = getNextSevenDays(date);
  for (let i = 1; i <= 7; i++) {
    const day = nextSevenDays[i - 1];
    const date = day.getDate();
    const year = day.getFullYear();
    const dayWeek = day.getDay();
    const month = day.getMonth() + 1;
    const [fYear, fMonth, fDate] = formatDate(year, month, date);
    document.getElementById(`day-${i}-weekd`).innerText = daysOfWeek[dayWeek];
    document.getElementById(`day-${i}-date`).innerText = `${fDate}.${fMonth}`;
  }
}

function initializeDatePicker() {
  const year = today.getFullYear();
  const month = today.getMonth() + 1;
  const date = today.getDate();
  const [fYear, fMonth, fDate] = formatDate(year, month, date);
  const todayFormatted = fYear + "-" + fMonth + "-" + fDate;
  datePicker.value = todayFormatted;
  datePicker.min = todayFormatted;
  datePicker.addEventListener("input", () => {
    const value = `${datePicker.value.substring(8)}.${datePicker.value.substring(5, 7)}`
    const allCards = document.querySelectorAll('.card')
    allCards.forEach((card) => {
      if (card.children[1].innerText === value) {
        card.classList.add("card-selected")
        lastCardSelected = card
      } else {
        card.classList.remove("card-selected")
      }
    })
  })
}
initializeDatePicker();

let lastCardSelected = document.getElementById("card-1");

function handleCard(id) {
  const card = document.getElementById(id);
  card.addEventListener("click", (e) => {
    let dateClicked;
    if (e.target.id !== id) {
      dateClicked = e.target.parentNode.children[1].innerText;
    } else {
      dateClicked = e.target.children[1].innerText;
    }

    if (
      datePicker.value.substring(5, 7) === "12" &&
      dateClicked.substring(3, 5) === "01"
    ) {
      year += 1;
    }

    const clickedFormated = `${year}-${dateClicked.substring(
      3
    )}-${dateClicked.substring(0, 2)}`;
    lastCardSelected.classList.remove("card-selected");
    card.classList.add("card-selected");
    lastCardSelected = card;
    datePicker.value = clickedFormated;
  });
}

function initializeCards() {
  setCards(today);
  handleCard("card-1");
  handleCard("card-2");
  handleCard("card-3");
  handleCard("card-4");
  handleCard("card-5");
  handleCard("card-6");
  handleCard("card-7");
}
initializeCards();

function hideOverflowElements() {
  const elements = document.querySelectorAll(".card");
  if (document.documentElement.scrollWidth <= 500) {
    elements.forEach((e) => {
      e.style.display = "none";
    });
    return;
  }
  // Получаем контейнер и элементы
  const container = document.getElementById("search-sec-container");

  // Вычисляем ширину контейнера и ширину всех элементов
  const containerWidth = container.offsetWidth - 100;

  // Скрываем элементы, которые не помещаются в контейнер
  let elementsWidth = 0;
  for (let i = 0; i <= elements.length - 1; i++) {
    elements[i].style.display = "";
    elementsWidth += elements[i].offsetWidth;
    if (elementsWidth > containerWidth) {
      elements[i].style.display = "none";
    }
  }
}
hideOverflowElements();
window.addEventListener("resize", hideOverflowElements);
