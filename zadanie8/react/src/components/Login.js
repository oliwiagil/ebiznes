import {useState} from "react";
import {Redirect} from "react-router-dom";


export const Login = () => {
    const [correct, setCorrect] = useState('');
    const [wrong, setWrong] = useState('');

    const checkLogin = async(e) => {
        // Prevent the browser from reloading the page
        e.preventDefault();

        const formData = new FormData(e.target);
        const requestOptions = {
            method: 'POST',
            body: JSON.stringify({ username: formData.get("username"), password: formData.get("password")})
        };
        fetch('http://localhost:8080/login', requestOptions)
            .then(function(response){
                if(response.status===200) {setCorrect(true)}
                else{setWrong(true)}
            });
    }

    return (
        <div>
            {correct && <p><Redirect push to="/loggedin"/></p>}
            {wrong && <p>Błędne dane logowania!</p>}
            <form method="post" onSubmit={checkLogin}>
            <p>Zaloguj się:</p>
                <label>
                    Wpisz login:
                    <input type={"text"} placeholder={"login"} name={"username"}/>
                </label>
                <br />
                <label>
                    Wpisz hasło:
                    <input type={"password"} placeholder={"hasło"} name={"password"}/>
                </label>
                <br />
                <button type="submit">Zaloguj</button>
            </form>
        </div>
    )
}
























/*
function checkLogin(e){
    // Prevent the browser from reloading the page
    e.preventDefault();

    const formData = new FormData(e.target);

    const requestOptions = {
        method: 'POST',
       // headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' }
        body: JSON.stringify({ username: formData.get("username"), password: formData.get("password")})
    };
    fetch('http://localhost:8080/login', requestOptions)
}
 */

