const cards = document.querySelectorAll('.quests');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

let currentIndex = 0; 

/** 
 * * Entfernt die 'active'-Klasse von allen Karten
 * * Füge die 'active'-Klasse der neuen Karte hinzu
 * * Gibt den Index in einer DebugMsg aus
 * @param {string} index
 * @return {void} none
 * */  
function showCard(index) {
  cards.forEach(card => card.classList.remove('active'));
  cards[index].classList.add('active');
  console.log(`carousel:active -> ${index}`);
}

// Nächste Karte (mit Endlos-Loop)
nextBtn.addEventListener('click', () => {
  currentIndex++;
  if (currentIndex >= cards.length) { currentIndex = 0; }
  showCard(currentIndex);
});

// Vorherige Karte (mit Endlos-Loop)
prevBtn.addEventListener('click', () => {
  currentIndex--;
  if (currentIndex < 0) { currentIndex = cards.length - 1; }
  showCard(currentIndex);
});
cards[0].classList.add('active');