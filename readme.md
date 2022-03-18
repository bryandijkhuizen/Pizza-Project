# Pizza Server
## Checklist

* TCP Server & Client X 
* UDP Server & Client X

* Singleton Pattern X
* Composite Pattern X
* Visitor Pattern

* Other Patterns
    * Factory Pattern

## How does this work?

# Database Connection
* Er wordt gebruik gemaakt van een Cloud Database (Supabase: postgresql)
* Binnen deze module wordt gebruik gemaakt van de Supabase API die SQL Injections vermijdt (https://github.com/supabase/supabase/discussions/1452)

# Hashing
* Er wordt gebruik gemaakt van de cryptography library
    * Eerst wordt er een secret key gegenereert, die wordt opgeslagen in een hash.key file
         Deze key wordt gebruikt om de hash te berekenen.
    * Eerst wordt er d.m.v. de Pickle library een dump gemaakt van de Order Array, om te kunnen encrypten.
    * Daarna wordt deze verstuurd en op de server weer ontsleuteld.
    * De pickle data wordt vervolgens weer ingeladen en omgezet to een Order Array.


