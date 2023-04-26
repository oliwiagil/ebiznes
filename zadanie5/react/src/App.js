import './App.css';
import { BrowserRouter, Link, Route } from 'react-router-dom';
import { Product } from './components/Product';

function App() {
  return (
    <div className="App">
        <BrowserRouter>
            <p>Witaj!</p>
            <p>produkt/cena/zapłać</p>
            <Product></Product>
        </BrowserRouter>
    </div>
  );
}

export default App;
