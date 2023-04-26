import {useContext} from "react";
import {ShopContext} from "../contexts/context";

export function Payment(props) {
    const {clearCart} = useContext(ShopContext);

    return (
        <button onClick={() => {pay(props.value); clearCart();}}>Zapłać za {props.value}</button>
    );
}

function pay(value){
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ value: value })
    };
    fetch('http://localhost:9000/addpayment', requestOptions)
}

