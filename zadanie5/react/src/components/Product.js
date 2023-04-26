import {useContext, useEffect, useState} from "react";
import {ShopContext} from "../contexts/context";

async function getProducts() {
    return await fetch(`http://localhost:9000/products`)
        .then(response => response.json())
}

export const Product = () => {
    const {cart, addCart} = useContext(ShopContext);
    const [products, setProducts] = useState([]);

    useEffect
    ( () => {
        const productsServer = getProducts()
        productsServer.then((product)=>{setProducts(product)}
        )
    },[])

    return (
        <div>
            <div className="products">
                <p>Dostępne produkty (w nawiasie podana jest cena):</p>
                <ul>
                    {products.map((product) => (<li>
                        {product.name} ({product.price})&nbsp;
                        <button onClick={() => addCart(product)}>Dodaj do koszyka</button>
                    </li>))}
                </ul>
                <p>Produkty w koszyku {cart.length}</p>
            </div>
        </div>

    )
}


