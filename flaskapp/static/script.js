// créer script.js et l'inclure dans cette page : OK
// on déclare une variable form, et on dit qu'elle fait partie de notre html on souhaite récupérer
// avec document.querySelector("#nom_de_class_ou_id")

let form = document.querySelector("#user-text-form");

// NEW FUNCTION : CREATE ELEMENT AND APPENDCHILD
function createDiv(text,parent){

    let div = document.createElement('div');
    div.id = 'chatbox';
    div.textContent = text;
    parent.appendChild(div);
}


    // On crée une fonction qui agira selon la méthode qu'on définit 
    // dans notr cas, nous souhaitons récupérer ce que  l'user à mi
function postFormData (url, data, headers) {
    return fetch(url, {
                method:"POST",
                body: data,
                headers : headers,
                })

        .then(response => response.json()) //fonction anonyme de ES6
        .catch(error => console.log(error));
    }

    form.addEventListener("submit", function (event) {
        event.preventDefault();

    // Envoyer le contenu du formulaire au serveur
    postFormData("/ajax", document.querySelector('#userText').value, {
        "Content-Type": "plain/text"
    })

    // Voir le résultat dans la console avec les outils de navigateur
    // on veut créer des nouveaux éléments dans le DOM
    .then(response => {console.log(response); 
    })

    let chatbox = document.querySelector("#chatbox")
    createDiv("On se calme", chatbox);
    })

    // on créer une div qui permet de chatbox lors du SUBMIT



