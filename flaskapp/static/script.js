// créer script.js et l'inclure dans cette page : OK
// on déclare une variable form, et on dit qu'elle fait partie de notre html on souhaite récupérer
// avec document.querySelector("#nom_de_class_ou_id")

let form = document.querySelector("#user-text-form");

// NEW FUNCTION : CREATE ELEMENT AND APPENDCHILD
function createDiv(text, parent, id){

    let div = document.createElement('div');
    div.id = id;
    div.textContent = text;
    parent.appendChild(div);
    return div
}

    // On crée une fonction qui agira selon la méthode qu'on définit 
    // dans notr cas, nous souhaitons récupérer ce que  l'user à mi
async function postFormData (url, data, headers) {
    try {
        const response = await fetch(url, {
            method: "POST",
            body: data,
            headers: headers,
        });
        return await response.json();
    }
    catch (error) {
        return console.log(error);
    }
    }

form.addEventListener("submit", function (event) {
    event.preventDefault();

    // Envoyer le contenu du formulaire au serveur
    postFormData("/ajax", document.querySelector('#userText').value, {
        "Content-Type": "plain/text"
        })
        .then(response => {
            createDiv(response.article, chatbox, "chatbox")
            createDiv(response.url, chatbox, "chatbox")
            createDiv(response.location, gmap, "gmap")})
        })

                // .then(response => {console.log(response)}


        
// Voir le résultat dans la console avec les outils de navigateur
// on veut créer des nouveaux éléments dans le DOM

    // let chatbox = document.querySelector("#chatbox")
    // createDiv(response, chatbox);
    // })

    // on créer une div qui permet de chatbox lors du SUBMIT



