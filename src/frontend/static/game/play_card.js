const playing_cards = document.querySelectorAll('.play-card');

function getPlayCardDialog(data) {
    return `
<dialog  id="card-dialog-${data.id}">
    
    <div class="card extended object-popup">
        <div class="nav-btn close">X</div>
        <div class="nav-btn extended">Arbeit</div>
        <div class="nav-btn extended">Inventar</div>
        <div class="nav-btn extended">Upgrade</div>
        <div class="nav-btn extended">Verkaufen</div>
        <div class="nav-btn extended">Kaufen</div>
        ${showPlayCard(data, true)}
        <!--
        Show Card
        If Card is not from the User <- do not show options! <- only buy
        redirect after btn press
        -->
    </div>
</dialog>

    `

}



function showPlayCard(data, rec = false) {
    
    return `
    <div class="all-play-cards" id=${data.id}>
            
        <div class="play-card-container" onClick="openCardDialog('card-dialog-${data.id}')">
            <div class="play-card ${data.rarity}">
                <div class="play-card-header">
                    <h2 class="play-card-title ${data.rarity}">${data.title}</h2>
                    <span class="play-card-cost">${data.cost}📀</span>
                </div>
                    
                <div class="play-card-image-container">
                    <img src=${data.img} alt=${data.img} class="play-card-image"/>
                </div>
                    
                <div class="play-card-body">
                    <p class="play-card-description">
                        ${data.description}
                    </p>
                </div>
                    
                <div class="play-card-footer">
                    <div class="stat atk">
                        <span class="stat-label">ATK</span>
                        <span class="stat-value">WBR</span>
                    </div>
                    <div class="stat def">
                        <span class="stat-label">DEF</span>
                        <span class="stat-value">WBR</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
    `

}



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