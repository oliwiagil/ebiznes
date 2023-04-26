import {useEffect, useState} from "react";
import { Payment } from './Payment';

async function getProducts() {
    return await fetch(`http://localhost:9000/products`)
        .then(response => response.json())
}

export const Product = () => {
    const [products, setProducts] = useState([]);

    useEffect( () => {
        const productsServer = getProducts()
        productsServer.then((product)=>{setProducts(product)}
        )
    },[])

    return (
        <div>
            <div className="products">
                <ul>
                    {products.map((product) => (<li>
                        {product.name} {product.price}&nbsp;
                        <Payment value={product.price}></Payment>
                    </li>))}
                </ul>
            </div>
        </div>

    )
}


