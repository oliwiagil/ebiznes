import './App.css';
import {BrowserRouter, Link, Route} from "react-router-dom";
import {Login} from "./components/Login";
import {Loggedin} from "./components/Loggedin";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                Witaj!
                <ul>
                    <li><Link to="/">Strona główna</Link></li>
                    <li><Link to="/login">Log in</Link></li>
                </ul>
                <Route path="/login" component={Login}/>
                <Route path="/loggedin" component={Loggedin}/>
            </BrowserRouter>
        </div>
    );
}

export default App;

