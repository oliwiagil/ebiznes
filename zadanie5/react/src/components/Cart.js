import React, {useContext} from "react";
import { Payment } from './Payment';
import {ShopContext} from "../contexts/context";


export const Cart = () => {
    const {cart, clearCart} = useContext(ShopContext);

    return (
        <div>
            <div className="cart">
                <ul>
                    {cart.map((product) => (<li>
                        {product.name} {product.price} &nbsp;
                    </li>))}
                    <Payment value={cart.length}></Payment>
                    <button onClick={() => clearCart()}>Usuń wszystko z koszyka</button>
                </ul>
            </div>
        </div>

    )
}
