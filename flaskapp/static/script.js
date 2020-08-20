// créer script.js et l'inclure dans cette page : OK
// on déclare une variable form, et on dit qu'elle fait partie de notre html on souhaite récupérer
// avec document.querySelector("#nom_de_class_ou_id")

let form = document.querySelector("#user-text-form");
let chatbox = document.querySelector("#chatbox");


// NEW FUNCTION : CREATE ELEMENT AND APPENDCHILD INTO THE DOM
function createDiv(text, parent, type) {
    let div = document.createElement(type);
    div.textContent = text;
    parent.appendChild(div);
    return div
}

function createDivForLink(text, parent, id, type) {
  let div = document.createElement(type);
  div.id  = id;
  div.textContent = text;
  parent.appendChild(div);
  return div
}


// NEW FONCTION : CREATE A LINK INTO AND APPENDCHILD INTO THE DOM
function createLink(parent, id, type, url, text) {
    let linky = document.createElement(type);
    linky.id = id;
    linky.href = url;
    linky.textContent = text; 
    linky.target = "_blank"
    parent.appendChild(linky)
    return linky
}

// Initialize and add the map
function initMap(location, latitude, longitude, maps) {
    // The location of REIMS

    var position = {lat: latitude, lng: longitude};
    
    var location = {
      lat: latitude,
      lng: longitude    
    };

    // The map, centered at REIMS
    var map = new google.maps.Map(
      document.getElementById(maps), {
        zoom: 15,
        center: location
      });
    // The marker, positioned at REIMS
    var marker = new google.maps.Marker({
      position: position,
      map : map
    });
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
          createDiv(response.question, chatbox, "p") //reprend la question
          createDiv(response.answer, chatbox, "p") // réponse automatique
          createDiv(response.article + response.url, chatbox, "p") //résumé wiki
          initMap(response.location, response.latitude, response.longitude, "map")
          })
      })



