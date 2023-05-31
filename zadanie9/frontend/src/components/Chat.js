import {useEffect, useState} from "react";

export const Chat = () => {
    const openingText = ["Dzień dobry, jeśli chcesz poznać dostępne kategorie wpisz poniżej \"kategorie\".",
        "Dzień dobry, jeśli chcesz poznać dostępne kategorie wpisz poniżej \"produkty\".",
        "Dzień dobry, jeśli wpiszesz interesującą Cię kategorię to otrzymasz listę produktów z tej kategorii (pamiętaj aby najpierw sprawdzić dostępne kategorie poprzez wpisanie \"kategorie\").",
        "Dzień dobry, możesz zadać mi dowolne pytanie, a ja postaram się na nie odpowiedzieć.",
        "Dzień dobry, nasz sklep oferuje szeroką gamę produktów. Aby się o tym przekonać wpisz \"produkty\"."
    ]

    const closingText = ["Życzymy miłego dnia.",
        "Dziękujemy za zainteresowanie naszym sklepem.",
        "W razie dalszych pytań chętnie służymy pomocą.",
        "Do zobaczenia następnym razem!",
        "Mamy nadzieję, że nasza pomoc była przydatna."
    ]

    const [question, setQuestion] = useState('');
    const [answer, setAnswer] = useState('');
    const [opening, setOpening] = useState(openingText[Math.floor(Math.random()*openingText.length)]);
    const [closing, setClosing] = useState('');
    const [count, setCount] = useState(0);

    useEffect(() => {
        if (count === 3) {
            setClosing(closingText[Math.floor(Math.random()*closingText.length)])
        }else if(count>=4){
            setCount(0)
            setClosing('')
        }
    }, [count]);

    const incrementCount = () => {
        setCount(count + 1);
    };

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
        setOpening("")

        incrementCount()

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
                {opening && <p>{opening}</p>}
                {question && <p> <span style={{ color: "green" }}>Twoje pytanie:</span> {question}</p>}
                {answer && <p><span style={{ color: "lightcoral" }}>Odpowiedź:</span> {answer}</p>}
                {closing && <p>{closing}</p>}
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


