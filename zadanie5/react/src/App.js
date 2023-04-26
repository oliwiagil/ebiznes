import './App.css';
import {BrowserRouter, Link, Route} from "react-router-dom";
import {Product} from "./components/Product";
import {Cart} from "./components/Cart";
import {ShopContextProvider} from "./contexts/context";

function App() {
    return (
        <div className="App">
            <ShopContextProvider>
                <BrowserRouter>
                    Witaj!
                    <ul>
                        <li><Link to="/">Sklep</Link></li>
                        <li><Link to="/products">Produkty</Link></li>
                        <li><Link to="/cart">Koszyk</Link></li>
                    </ul>
                    <Route path="/products" component={Product}/>
                    <Route path="/cart" component={Cart}/>
                </BrowserRouter>
            </ShopContextProvider>
        </div>
    );
}

export default App;

