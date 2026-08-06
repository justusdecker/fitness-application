// Alle Karten auf einmal auswählen
const playing_cards = document.querySelectorAll('.play-card');

playing_cards.forEach(card => {
  // Mausbewegung für jede einzelne Karte
  card.addEventListener('mousemove', (e) => {
    const rect = card.getBoundingClientRect();
    
    // Mausposition relativ zur Kartenmitte
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    
    // Drehwinkel berechnen (max. 15 Grad Neigung)
    const rotateX = -((y - centerY) / centerY) * 15;
    const rotateY = ((x - centerX) / centerX) * 15;
    
    // Transformation anwenden
    card.style.transform = `rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.05)`;
  });

  // Karte zurücksetzen, wenn die Maus sie verlässt
  card.addEventListener('mouseleave', () => {
    card.style.transform = 'rotateX(0deg) rotateY(0deg) scale(1)';
    card.style.transition = 'transform 0.5s ease'; // Sanftes Zurückgleiten
  });

  // Transition während der Bewegung entfernen
  card.addEventListener('mouseenter', () => {
    card.style.transition = 'none';
  });
});