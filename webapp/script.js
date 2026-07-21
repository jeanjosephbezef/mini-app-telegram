let tousLesProduits = [];
let panier = [];


async function chargerProduits(){

    const reponse = await fetch("products.json");

    tousLesProduits = await reponse.json();

    afficherProduits(tousLesProduits);

}

function afficherProduits(produits){

    const zone = document.getElementById("products");

    zone.innerHTML = "";


    produits.forEach(produit => {


        zone.innerHTML += `

        <div class="card">

            <img src="images/${produit.image}">

            <div class="infos">

                <h3>${produit.nom}</h3>

                <p>${produit.description}</p>

                <strong>
                ${produit.prix.toFixed(2)} €
                </strong>

                <button onclick='ajouter(${JSON.stringify(produit)})'>
                Ajouter 🛒
                </button>

            </div>

        </div>

        `;

    });

}



function ajouter(produit){

    panier.push(produit);

    afficherCompteur();

}



function afficherCompteur(){

    document.getElementById("count").innerHTML = panier.length;

}



function ouvrirPanier(){

    document.getElementById("cart").style.display="block";

    afficherPanier();

}



function fermerPanier(){

    document.getElementById("cart").style.display="none";

}



function afficherPanier(){

    let zone=document.getElementById("cartItems");

    zone.innerHTML="";


    let total=0;


    panier.forEach((p,index)=>{


        total += p.prix;


        zone.innerHTML += `

        <div class="cartLine">

        ${p.nom}

        ${p.prix} €

        <button onclick="supprimer(${index})">
        ❌
        </button>

        </div>

        `;


    });


    document.getElementById("total").innerHTML =
    total.toFixed(2);

}



function supprimer(index){

    panier.splice(index,1);

    afficherCompteur();

    afficherPanier();

}



chargerProduits(); 

function filtrerCategorie(categorie){

    let produitsFiltres = tousLesProduits.filter(
        produit => produit.categorie === categorie
    );


    afficherProduits(produitsFiltres);

}