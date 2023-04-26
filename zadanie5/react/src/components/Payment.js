export function Payment(props) {
    return (
        <button onClick={() => pay(props.value)}>Zapłać {props.value}</button>
    );
}

function pay(value){
    console.log(value)

    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ value: value })
    };
    fetch('http://localhost:9000/addpayment', requestOptions)
}

