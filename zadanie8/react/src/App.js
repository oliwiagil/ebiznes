import './App.css';
import {BrowserRouter, Link, Route} from "react-router-dom";
import {Login} from "./components/Login";
import {Loggedin} from "./components/Loggedin";
import {Register} from "./components/Register";
import {Registered} from "./components/Registered";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                Witaj!
                <ul>
                    <li><Link to="/">Strona główna</Link></li>
                    <li><Link to="/login">Log in</Link></li>
                    <li><Link to="/register">Register</Link></li>
                </ul>
                <Route path="/login" component={Login}/>
                <Route path="/loggedin" component={Loggedin}/>
                <Route path="/register" component={Register}/>
                <Route path="/registered" component={Registered}/>
            </BrowserRouter>
        </div>
    );
}

export default App;

