console.log("imrunning")
function showPlayCard(data) {
    
    return `
    <div class="all-play-cards" id=${data.id}>
            
        <div class="play-card-container">
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