// const cards = document.querySelectorAll('.play-card');
/**
 * 
 * @param {string} id
 * @return {null} 
 */
function closeCardDialog(id) {
    const dialog = document.getElementById(id);
    console.log(dialog, id)
    dialog.close();
    dialog.style.display = 'none';
}

function openCardDialog(id) {
    const dialog = document.getElementById(id);

    if (!dialog.open) {
        dialog.style.display = 'flex';
        dialog.showModal();
    }
    
}


async function onCardClick(id) {
    const card = document.getElementById(id);
    
    const response = await fetch(`/api/card/get/${id}`);
    if (!response.ok) {
        throw new Error(`HTTP-Fehler! Status: ${response.status}`);
    }
    const data = await response.json();

    const title = data.title;
    const description = data.description;
    const cost = data.costForRarityLevel;
    const rarity = data.rarityAsStr;
    const img = data.img;


}