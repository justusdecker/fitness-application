
document.addEventListener("DOMContentLoaded", () => {
    // Wähle das Div anhand seiner Klasse aus
    const quests = document.querySelectorAll(".quests");

    const levelBadgeDiv = document.querySelector('.level-badge');
    const xpCurrentMaxSpan = document.querySelector('.xp-current-max');
    const xpBarDiv = document.querySelector('.xp-bar-fill');

    const coinSpan = document.querySelector('.coin-ammount');
    const materialSpan = document.querySelector('.material-ammount');

    console.log(quests.length)
    
    quests.forEach(quest => {
        console.log("Gefundene Quest-ID:", quest.id);
        quest.addEventListener("click", async () => {
            
            const not_needed_response = await fetch(`/api/quest_solve/${quest.id}`);
            const response = await fetch("/api/get");
            const data = await response.json();

            const level = data.level;
            const xp = data.fxp;
            const xpMax = data.xp_max;
            const xpBarPercentage = data.xp_percentage;

            console.log();
            levelBadgeDiv.innerText = `Lv. ${level}`;
            xpCurrentMaxSpan.innerText = `${xp} / ${xpMax} XP`;
            xpBarDiv.width = xpBarPercentage; //! Maybe this is wrong
            coinSpan.innerText = `${data.coin}`;
            materialSpan.innerText = `${data.material}`;
        });
        

        //TODO: Add a new Badge if not exist, else +1 the Badge
        
    });

});