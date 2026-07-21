let products = [];
let panier = [];


// Charger les produits
fetch("products.json")
    .then(response => response.json())
    .then(data => {

        products = data;

        afficherProduits(products);

    })
    .catch(error => {

        console.error(
            "Erreur chargement produits :",
            error
        );

    });



// Afficher les produits
function afficherProduits(liste) {

    const container = document.getElementById("products");

    container.innerHTML = "";


    liste.forEach(product => {


        const card = document.createElement("div");

        card.className = "product";


        card.innerHTML = `

            <img src="${product.image}" 
            alt="${product.nom}">


            <div class="product-info">

                <h3>${product.nom}</h3>

                <p>${product.description}</p>

                <div class="price">
                    ${product.prix.toFixed(2)} €
                </div>


                <button 
                class="add-btn"
                onclick="ajouterPanier(${product.id})">

                    Ajouter au panier

                </button>

            </div>

        `;


        container.appendChild(card);


    });

}



// Filtrer par catégorie
function filtrerCategorie(categorie){


    if(categorie === "Tous"){

        afficherProduits(products);

        return;

    }


    const resultat = products.filter(product =>

        product.categorie === categorie

    );


    afficherProduits(resultat);


}



// Recherche produit
function rechercherProduit(){


    const recherche = document
        .getElementById("search")
        .value
        .toLowerCase();



    const resultat = products.filter(product =>

        product.nom
        .toLowerCase()
        .includes(recherche)

    );


    afficherProduits(resultat);


}




// Ajouter au panier
function ajouterPanier(id){


    const produit = products.find(p => p.id === id);


    panier.push(produit);


    mettreAJourPanier();


}



// Ouvrir panier
function ouvrirPanier(){

    document
    .getElementById("cart")
    .classList
    .add("active");

}



// Fermer panier
function fermerPanier(){

    document
    .getElementById("cart")
    .classList
    .remove("active");

}



// Mise à jour panier
function mettreAJourPanier(){


    const items =
    document.getElementById("cartItems");


    const total =
    document.getElementById("total");


    const count =
    document.getElementById("count");



    items.innerHTML="";


    let somme = 0;



    panier.forEach((item,index)=>{


        somme += item.prix;


        const div =
        document.createElement("div");


        div.className="cart-item";


        div.innerHTML=`

            <span>
                ${item.nom}
            </span>


            <span>
                ${item.prix.toFixed(2)} €
            </span>

        `;


        items.appendChild(div);


    });



    total.innerText =
    somme.toFixed(2);



    count.innerText =
    panier.length;


}