# Applicazione Chat con Redis

Questa è una semplice applicazione di chat scritta in Python che utilizza Redis come database. Permette agli utenti di inviare e visualizzare messaggi in una chat condivisa. L'applicazione fornisce opzioni per l'invio di messaggi, la visualizzazione dei messaggi più recenti e l'uscita dalla chat oltre a resettare il database di redis.

## Primi passi

1. Clona il repository:
   ```
   git clone https://github.com/LeonardoRocca-13/Consegne_Nosql.git
   ```

2. Installa la libreria Redis per Python:
   ```
   pip install redis
   ```

3. Esegui l'applicazione:
   ```
   python chat.py
   ```

## Utilizzo

1. Avvia l'applicazione eseguendo lo script `chat.py`.

2. Se sei un utente registrato, inserisci la tua email, il tuo nome utente e la tua password. Se sei un nuovo utente, inserisci questi dettagli per registrarti.

3. Dopo aver effettuato l'accesso o la registrazione, vedrai un menu con le seguenti opzioni:

- **1. Identifica l'utente**: Inserisci la tua email, il tuo nome utente e la tua password per identificarti.
- **2. Scrivi messaggio**: Inserisci i tuoi messaggi per inviarli alla chat room. Inserisci 'q' per smettere di inviare messaggi.
- **3. Leggi gli ultimi 10 messaggi**: Visualizza i 10 messaggi più recenti nella chat room.
- **4. Cancella utente**: Cancella il tuo account utente.
- **5. Cancella database**: Cancella il database Redis.
- **6. Esci**: Esci dall'applicazione di chat.

4. Seleziona un'opzione inserendo il numero corrispondente.

## Licenza

Questo progetto è concesso in licenza con la [Licenza MIT](LICENSE).

## Technologie Utilizzate

- [Redis](https://redis.io) - Un datastore open-source in-memory.
- [Python](https://www.python.org) - Il linguaggio di programmazione utilizzato per questa applicazione.

Sentiti libero di contribuire a questo progetto inviando segnalazioni di bug o richieste di nuove funzionalità.