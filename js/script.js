// automatically call backend on page load
const URI = "http://localhost:5000/"

function addElement(pName, price) {
  const newDiv = document.createElement("div");
  newDiv.className = "product"

  const img = document.createElement("img");
  img.src = "./images/logo_protod.png"

  const title = document.createElement("h3");
  const titleContent = document.createTextNode(pName);

  title.appendChild(titleContent);

  const parrafo = document.createElement("p");
  const parrafoContent = document.createTextNode("El producto tiene el precio de Q" + price);

  parrafo.appendChild(parrafoContent);

  newDiv.appendChild(img)
  newDiv.appendChild(title)
  newDiv.appendChild(parrafo);

  const currentDiv = document.getElementById("product-grid");
  currentDiv.appendChild(newDiv);
}

window.addEventListener("DOMContentLoaded", (event) => {
  get_request();
});


const get_request = async () => {
  const response = await fetch(URI + 'read?market=democracia', { method: "GET", mode: "cors", cache: "no-cache" });
  const jsonData = await response.json();

  console.log(jsonData);

  for (let i = 0; i < jobject.names().length(); i++) {
    Log.v(TAG, "key = " + jobject.names().getString(i) + " value = " + jobject.get(jobject.names().getString(i)));
  }
}


const userAction = async () => {
  const response = await fetch('http://example.com/movies.json', {
    method: 'POST',
    body: myBody, // string or object
    headers: {
      'Content-Type': 'application/json'
    }
  });
  const myJson = await response.json(); //extract JSON from the http response
  // do something with myJson
}
