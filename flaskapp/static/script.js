// créer script.js et l'inclure dans cette page : OK
// on déclare une variable form, et on dit qu'elle fait partie de notre html on souhaite récupérer
// avec document.querySelector("#nom_de_class_ou_id")

let form = document.querySelector("#user-text-form");
let chatbox = document.querySelector("#chatbox");
let buble = document.querySelector("#buble1");


// NEW FUNCTION : CREATE ELEMENT AND APPENDCHILD INTO THE DOM
function createDiv(text, parent, type) {
  let div = document.createElement(type);
  div.textContent = text;
  parent.appendChild(div);
  return div
} 

function createResponseWithLink(url, response, id, innertext){
  let newLink = document.createElement("a");
  newLink.href = url;
  newLink.target = "_blank";
  newLink.innerHTML = innertext;
  
  let par  = document.createElement("p");
  par.innerHTML = response;
  par.appendChild(newLink);

  document.getElementById(id).appendChild(par);
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
    }}


function processEverything(response){
  if (response.status === true) {
    createDiv(response.question, buble, "p");
    createDiv(response.answer, buble, "p");
    createResponseWithLink(response.url, response.article, "buble1",  " Pour plus d'informations...");
    initMap(response.location, response.latitude, response.longitude, "map");
  } else {
    createDiv(response.question, buble, "p");
    createDiv(response.answer, buble, "p");
    createResponseWithLink(response.url, response.article, "buble1", " ou relancer une recherche, cliquez-ici.");
  }
}

form.addEventListener("submit", function (event) {
  event.preventDefault();

  // Envoyer le contenu du formulaire au serveur
  postFormData("/ajax", document.querySelector('#userText').value, {
      "Content-Type": "plain/text"
      })
      .then(response => {processEverything(response)
    })
  })



  // // Envoyer le contenu du formulaire au serveur
  // postFormData("/ajax", document.querySelector('#userText').value, {
  //   "Content-Type": "plain/text"
  //   })
  //   .then(response => {
  //       createDiv(response.question, buble, "p") //reprend la question
  //       createDiv(response.answer, buble, "p") // réponse automatique
  //       createResponseWithLink(response.url, response.article, "buble1")
  //       initMap(response.location, response.latitude, response.longitude, "map")
  //       })
  //   })



// function sendError(){
//   let error_message = document.createElement("h1");
//   error_message.textContent = "DEBUG : JE NE TROUVE PAS TON LIEU, DIS MOI A NOUVEAU";
//   buble.appendChild(error_message);
//   return error_message
// }
