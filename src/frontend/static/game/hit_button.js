/* 
Add Suffix / Prefix
Add _event_target
Add _result_target
Add _api_target
*/
function onClickHit() {

}
document.addEventListener("DOMContentLoaded", () => {
    // Wähle das Div anhand seiner Klasse aus
    const triggerDiv = document.querySelector(".hit-button");

    const coinSpan = document.querySelector('.coin-ammount');
    const materialSpan = document.querySelector('.material-ammount')

    

    if (triggerDiv) {
        triggerDiv.addEventListener("click", async () => {
            try {
                // Anfrage an deine Flask-API (passe den Endpunkt an, z. B. '/api/daten')
                const not_needed_response = await fetch("/api/increase?data=[coin]");
                const response = await fetch("/api/get?data=[coin, material]");

                if (!response.ok) {
                    throw new Error(`HTTP-Fehler! Status: ${response.status}`);
                }
                const data = await response.json();
                coinSpan.innerText = `${data.coin}`;
                materialSpan.innerText = `${data.material}`;
                console.log(`📀${data.coin} 🧱${data.material}`)
            } catch (error) {
                console.error("Fehler beim Abrufen der Daten:", error);
                alert("Fehler beim Abrufen der Daten");
            }
        });
    }
});