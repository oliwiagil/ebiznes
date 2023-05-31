import './App.css';
import {BrowserRouter} from "react-router-dom";
import { Chat } from './components/Chat';

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Chat></Chat>
            </BrowserRouter>
        </div>
    );
}

export default App;

