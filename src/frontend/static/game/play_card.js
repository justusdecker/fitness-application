
function setCardToWork(id) {
    window.location.href = `/api/update/cardtowork/${id}`
}

function getPlayCardDialog(data) {
    
    const buySellText = data.owned ? '<div class="nav-btn extended">Verkaufen</div>' : '<div class="nav-btn extended">Kaufen</div>';
    const workInventorUpgradeText = data.owned ? `<div class="nav-btn extended" onClick="setCardToWork(${data.id})">Arbeit</div><div class="nav-btn extended">Inventar</div><div class="nav-btn extended">Upgrade</div>` : '';

    return `
<dialog  id="card-dialog-${data.id}">
    
    <div class="card extended object-popup">
        <div class="besides spaced">
            <h1 style="color:var(--rarity-mythic-normal);">Kartenverwaltung</h1>
            <div class="nav-btn close" onClick="closeCardDialog('card-dialog-${data.id}')">X</div>
        </div>
        <div class="besides">
            ${showPlayCard(data, true)}
            <div>
                ${workInventorUpgradeText}
                ${buySellText}
            </div>
        </div>
    
       
        
        
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
                    <span class="play-card-cost" id="${data.rarity}">${data.cost}📀</span>
                    
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
                    <div class="stat">
                        <span class="stat-label">probably remove this</span>
                        <span class="stat-value">...</span>
                    
                    </div>
                </div>
            </div>
        </div>
    </div>
    `

}

function costRarityShowSwitcher() {
    const objects = document.querySelectorAll('.play-card-cost');
    
    objects.forEach(object => {
        // Ursprünglichen Inhalt (z.B. Kosten) speichern
        const originalContent = object.innerHTML;
        
        // Alternativen Inhalt festlegen (z.B. die ID oder ein Dataset-Attribut)
        const hoverContent = object.id; 

        object.addEventListener('mouseover', () => {
            object.innerHTML = hoverContent;
        });

        object.addEventListener('mouseleave', () => {
            object.innerHTML = originalContent;
        });
    });
}

function playingCardsForeacher() {
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
}
