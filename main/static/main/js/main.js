// redirections
function redirect(id) {
    document.getElementById(id).click();
}

// copied functionality of sleeping in milliseconds
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
