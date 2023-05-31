import {useState} from "react";

export const Chat = () => {
    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');

    const submitMessage = async(e) => {
        // Prevent the browser from reloading the page
        e.preventDefault();

        const formData = new FormData(e.target);
        let message = formData.get("message")
        const requestOptions = {
            method: 'POST',
            body: JSON.stringify({ message: message})
        };

        setQuestion(message)
        setAnswer("")

        fetch('http://localhost:8080/', requestOptions)
            .then(response => {
                  if(response.status===200) {
                      return(response.json())
                  }
            })
            .then(data => {
                let tmpAnswer=data.content
                if (tmpAnswer.startsWith('"') && tmpAnswer.endsWith('"')) {
                    setAnswer(tmpAnswer.slice(1, -1))
                }
                else{ setAnswer(tmpAnswer) }
            });
    }


    return (
        <div>
            <div>
                <h1>Witaj w sklepie!</h1>
                <h2>Zadaj poniżej pytanie.</h2>
                {question && <p> <span style={{ color: "green" }}>Twoje pytanie:</span> {question}</p>}
                {answer && <p><span style={{ color: "lightcoral" }}>Odpowiedź:</span> {answer}</p>}
                <form method="post" onSubmit={submitMessage}>
                    <input type={"text"} name={"message"} style={{ width: '400px' }}/>
                    <button type="submit" style={{ verticalAlign: 'top' }}>Wyślij zapytanie</button>
                </form>
                <br />
                <p>Możesz zapytać o dostępne kategorie oraz produkty wpisując odpowiednio "kategorie" lub "produkty".</p>
                <p>Możesz też otrzymać listę produktów należących do danej kategorii.</p>
                <p>W tym celu wpisz nazwę interesującej Cię kategorii.</p>
                <p>Dostępne kategorie możesz sprawdzić wpisując "kategorie".</p>
                <br />
                <p>Możesz też zadać dowolne pytanie na które odpowie sztuczna inteligencja.</p>
                <p>Uwaga: Otrzymanie odpowiedzi na dowolne pytanie może trochę potrwać.</p>
            </div>
        </div>

    )
}


