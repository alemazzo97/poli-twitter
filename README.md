# poli-twitter

Repo per il progetto di Cognitive Behavioral and Social Data (2019/2020)

## Requisiti

- [Python 3](https://www.python.org/downloads/)
- [Cartella Drive](https://drive.google.com/drive/u/0/folders/1Pn-C3gxSJV-5_WAxw-2DoAP5Fm8Ayya3) con i tweets

> In fase di installazione fare attenzione python sia stato aggiunto alla PATH

Per verificare la corretta installazione, aprire un terminale e digitare `python -V`. Se vedete la versione installata, tutto apposto.

## Installare le dipendenze

Terminale aperto dentro la `root` del progetto. Eseguire i comandi:

- `pip install numpy`
- `pip install pandas`
- `pip install csv`
- `pip install googletrans`
- `pip install textblob`

## Eseguire

Terminale aperto dentro la cartella `src`. Eseguire il comando:

```bash
python <nome-file>.py
```

---

### Attenzione

> La cartella con i `Tweets` deve essere posizionata in un percorso specifico e poi indicato nel file `filter.py`

> Prima di eseguire il file `sentiment.py` dovete prima eseguire `filter.py` per ottenere dei tweet puliti sui cui fare sentiment analysis.
