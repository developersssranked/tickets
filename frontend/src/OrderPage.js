const freePlaces = parseInt(document.getElementById("freePlaces").innerText.match(/\d/gm))
const input = document.getElementById("seatsInput") 
input.max = freePlaces


input.addEventListener('input', () => {
    const value = parseFloat(input.value);
    if (isNaN(value)) {
      input.setCustomValidity('Пожалуйста, введите число');
    } else if (value < input.min) {
      input.setCustomValidity(`Количество свободных мест не может быть меньше ${input.min}`);
    } else if (value > input.max) {
      input.setCustomValidity(`Введённое значение превышает количество свободных мест`);
    } else {
      input.setCustomValidity('');
    }
    input.reportValidity();
  });