# Pizza Server

# Design

* UML diagram\
![alt text](https://github.com/bryandijkhuizen/Pizza-Project/blob/master/docs/img/default_uml.svg)

* Activity diagram\
![alt text](https://github.com/bryandijkhuizen/Pizza-Project/blob/master/docs/img/activity_diagram.svg)

* Network diagram\
![alt text](https://github.com/bryandijkhuizen/Pizza-Project/blob/master/docs/img/default_network.svg)




# Dependencies and Setup

* Dependencies
    * Pickle [`pip install pickle`](https://pypi.python.org/pypi/pickle)
    * Flask [`pip install flask`](https://pypi.python.org/pypi/Flask)
    * Supabase [`pip install supabase`](https://pypi.python.org/pypi/supabase)
    * Dotenv [`pip install dotenv`](https://pypi.python.org/pypi/Dotenv)
    * Cryptography [`pip install cryptography`](https://pypi.python.org/pypi/cryptography)
## Checklist

* TCP Server & Client X 
* UDP Server & Client X

* Singleton Pattern X
* Composite Pattern X
* Visitor Pattern

* Other Patterns
    * Factory Pattern X

## Design Patterns Used
### Singleton
* Singleton Pattern wordt in de Socket Classes (TCPSocketClient, TCPSocketServer, UDPSocketClient, UDPSocketServer) gebruikt om ervoor te zorgen dat er maar 1 socket object wordt aangemaakt.

### Composite
* In de CommunicationManager wordt een Composite structuur gebruikt om een lijst met alle soorten protocollen te maken en zo kan er een worden geslecteerd zonder dat in elke klasse een een aanpassing moet worden gemaakt.

* Er is een if statement in the pizza_client en pizza_server classes die checkt welke protocol er gebruikt moet worden. (TCP of UDP)

### Factory 
* Het Factory Pattern wordt gebruikt in order_serializer.py om de juiste order serializer te kiezen.

* Zo kan een order makkelijk worden omgezet naar een Pickle object of een order object.

# How does this work?

### Database Connection
* Er wordt gebruik gemaakt van een Cloud Database (Supabase: postgresql)
* Binnen deze module wordt gebruik gemaakt van de Supabase API die SQL Injections vermijdt (https://github.com/supabase/supabase/discussions/1452)

### Client Website Frontend
* Er wordt gebruik gemaakt van Flask (https://pypi.python.org/pypi/Flask)
* De layout is ontworpen met Tailwind CSS (https://tailwindcss.com/)
* De input op de HTML pagina wordt d.m.v. een POST request verstuurd naar de client server


### Hashing & Encryption
* Er wordt gebruik gemaakt van de cryptography library
    * Eerst wordt er een secret key gegenereert, die wordt opgeslagen in een hash.key file
         * Deze key wordt gebruikt om de hash te berekenen.
    * Eerst wordt er d.m.v. de Pickle library een dump gemaakt van de Order Array, om te kunnen encrypten.
    * Daarna wordt deze verstuurd en op de server weer ontsleuteld.
    * De pickle data wordt vervolgens weer ingeladen en omgezet to een Order Array.


### TCP Server
* In de TCPSocketServer class wordt een socket uit de socket library gebruikt om een TCP server te maken
    * Eerst wordt d.m.v. het singleton pattern gecontroleerd of er al een server object bestaat.
    * Als er nog geen server object bestaat wordt er een nieuw server object aangemaakt.
    * In de constructor wordt het IP en de poort gekozen en initialiseer je de serializer

* In de listen_for_orders() methode wordt in de while loop gewacht op een connectie.
* Als er een connectie is wordt er een datastroom aangemaakt geopend om de data te ontvangen.
* De ontvangen data wordt vervolgens ontsleuteld en als er een Order Array is wordt deze vervolgens omgezet naar een Order object.
* De order wordt vervolgens in een database opgeslagen en de order wordt op de server afgedrukt.

### UDP Server
* In de UDPSocketServer class wordt een socket uit de socket library gebruikt om een UDP server te maken
    * Eerst wordt d.m.v. het singleton pattern gecontroleerd of er al een server object bestaat.
    * Als er nog geen server object bestaat wordt er een nieuw server object aangemaakt.
    * In de constructor wordt het IP en de poort gekozen en initialiseer je de serializer, ook wordt de buffer grootte ingesteld.
* Vervolgens wordt het socket object aangemaakt met de gegevens van de UDP server.

* In de listen_for_orders() methode wordt in de while loop gewacht op data (in tegenstelling tot bij TCP waar een connectie nodig is).

* De ontvangen data wordt vervolgens ontsleuteld en als er een Order Array is wordt deze vervolgens omgezet naar een Order object.
* De order wordt vervolgens in een database opgeslagen en de order wordt op de server afgedrukt.

### TCP Client

* In de TCPSocketClient class wordt een socket uit de socket library gebruikt om een TCP client te maken
    * Eerst wordt d.m.v. het singleton pattern gecontroleerd of er al een client object bestaat.
    * Als er nog geen client object bestaat wordt er een nieuw client object aangemaakt.
    * In de constructor wordt het IP en de poort gekozen en de order wordt ook ontvangen

* Er wordt een datastroom aangemaakt om de data te versturen.
* Er moet een verbinding worden gemaakt met de server.
* Voordat de data versleuteld kan worden moet er een sleutel worden gegenereerd.
* Dan wordt de order omgezet naar een Pickle object, deze wordt versleuteld en vervolgens verstuurd.
* Als alles is verstuurd moet er een bericht worden ontvangen van de server.

### UDP Client

* In de UDPSocketClient class wordt een socket uit de socket library gebruikt om een UDP client te maken
    * Eerst wordt d.m.v. het singleton pattern gecontroleerd of er al een client object bestaat.
    * Als er nog geen client object bestaat wordt er een nieuw client object aangemaakt.
    * In de constructor wordt het IP, de poort, de buffer grootte geinitialiseerd en ook wordt er een socket object aangemaakt.

* In de send_order() methode:
    * Voordat de data versleuteld kan worden moet er een sleutel worden gegenereerd.
    * Dan wordt de order omgezet naar een Pickle object, deze wordt versleuteld en vervolgens verstuurd.