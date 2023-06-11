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
    request();
});


const request = async() => {
    console.log("init");
    const response = await fetch(URI + 'read?market=democracia');
    const JSON = await response.json();
    console.log(JSON);
    console.log("end");
}   
