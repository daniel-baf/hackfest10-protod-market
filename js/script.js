// automatically call backend on page load
const URI = "http://localhost:5000/"

// request list from backend
async function get_product_list() {
    console.log("calling");
    const result = await request_data('democracia');
}

// HTTP requests
function request_data(market) {
    fetch(URI + "read?market=" + market)
        .then((response) => response.json())
        .then((json) => console.log(json));
}


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
    // var query = document.getElementById("product-grid");
    // console.log(query);
    // 
    // addElement("Frijoles", "50"); 
    get_product_list();
});

