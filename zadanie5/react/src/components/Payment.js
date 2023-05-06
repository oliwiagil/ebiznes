import {useContext} from "react";
import {ShopContext} from "../contexts/context";
import axios from "axios";


export function Payment(props) {
    const {clearCart} = useContext(ShopContext);

    return (
        <button onClick={() => {pay(props.value); clearCart();}}>Zapłać za {props.value}</button>
    );
}

function pay(value){
    axios.post('http://localhost:9000/addpayment', { value: value })
}

