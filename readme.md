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
    * Factory Pattern

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


