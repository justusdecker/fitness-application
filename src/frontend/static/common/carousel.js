const cards = document.querySelectorAll('.quests');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

let currentIndex = 0;

function showCard(index) {
  // Entferne die 'active'-Klasse von allen Karten
  cards.forEach(card => card.classList.remove('active'));
  
  // Füge die 'active'-Klasse der neuen Karte hinzu
  cards[index].classList.add('active');
  console.log(index);
}

// Nächste Karte (mit Endlos-Loop)
nextBtn.addEventListener('click', () => {
  currentIndex++;
  if (currentIndex >= cards.length) {
    currentIndex = 0; // Springt zurück zum Anfang
  }
  showCard(currentIndex);
});

// Vorherige Karte (mit Endlos-Loop)
prevBtn.addEventListener('click', () => {
  currentIndex--;
  if (currentIndex < 0) {
    currentIndex = cards.length - 1; // Springt zum Ende
  }
  showCard(currentIndex);
});
cards[0].classList.add('active');