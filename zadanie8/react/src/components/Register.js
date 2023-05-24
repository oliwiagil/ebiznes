import {useState} from "react";
import {Redirect} from "react-router-dom";


export const Register = () => {
    const [correct, setCorrect] = useState('');
    const [wrong, setWrong] = useState('');

    const checkLogin = async(e) => {
        e.preventDefault();

        const formData = new FormData(e.target);
        const requestOptions = {
            method: 'POST',
            body: JSON.stringify({ username: formData.get("username"), password: formData.get("password")})
        };
        fetch('http://localhost:8080/register', requestOptions)
            .then(function(response){
                if(response.status===200) {setCorrect(true)}
                else{setWrong(true)}
            });
    }

    return (
        <div>
            {correct && <p><Redirect push to="/registered"/></p>}
            {wrong && <p>Konto o podnej nazwie już istnieje!</p>}
            <form method="post" onSubmit={checkLogin}>
                <p>Zarejestruj się:</p>
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
                <button type="submit">Stwórz konto</button>
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

