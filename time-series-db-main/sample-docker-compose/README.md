# Sample docker compose

* Δημιουργία δύο containers (mqtt & mysql) και ενός δικτύου (`peopleflows_network`).
    ```
    docker-compose -f docker-compose.core.yml up
    ```

* Δημιουργία ενός ακόμη container (κενό ubuntu- `peopleflows_ext`) που μπορεί να συνδέεται στο ίδιο δίκτυο (`peopleflows_network`).
    ```
    docker-compose -f docker-compose.ext.yml up
    ```

    Με χρήση του νέου container `peopleflows_ext` μπορούμε να προσπελάσουμε τον `peopleflows_mqtt`:
    ```
    $ docker exec -ti peopleflows_ext bash

    root@838de541adaa:/# apt update
    root@838de541adaa:/# apt install mosquitto-clients
    root@838de541adaa:/# mosquitto_pub -h peopleflows_mqtt -t test -m hello

    ```
