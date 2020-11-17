// sleeping in milliseconds
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
// writes a string to an element
async function writeToId(str, id) {
    dom_elem = document.getElementById(id);
    for (let i = 0; i < str.length ; i++) {
        await sleep(10);
        dom_elem.innerHTML += str[i];
    }
}

// redirects to note showing page
async function openNote() { 
    if ($("#idInput").val().length != 10) {  
        $('#invalidAlert').show();
        await sleep(5000);
        $('#invalidAlert').hide();
    }
    else {
        $('#invalidAlert').hide();
        window.location.assign("/shared/" + document.getElementById("idInput").value); 
    }
}