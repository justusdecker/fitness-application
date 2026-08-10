document.addEventListener("DOMContentLoaded", () => {
    // Wähle das Div anhand seiner Klasse aus
    const quests = document.querySelectorAll(".quest");

    const levelBadgeDiv = document.querySelector('.level-badge');
    const xpCurrentSpan = document.querySelector('.xp-current');
    const xpMaxSpan = document.querySelector('.xp-max');
    const xpBarDiv = document.querySelector('.xp-bar-fill');


    
    quests.forEach(quest, async () => {
        // get new xp value
        // get neww level value
        // overwrite xp value and xp meter
        // overwrite level value

        const not_needed_response = await fetch("/api/increase?data=[coin]");
        const response = await fetch("/api/get?data=[coin, material]");
        const data = await response.json();
        //TODO: Add a new Badge if not exist, else +1 the Badge
        
    });

});