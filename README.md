# Kafka Multi-Producer & Consumer Project 1.0

### Overview

This project demonstrates a **multi-producer, single-consumer** architecture using **Apache Kafka**. Three different producers send messages to separate Kafka topics, and a single consumer listens to all topics, processing messages and logging errors into a **PostgreSQL** database.

### Technologies Used

- **Apache Kafka** (message broker)
- **Python** (for producers & consumer)
- **PostgreSQL** (database for error logging)
- **Docker** (for Kafka & PostgreSQL setup)

### Project Structure

```
kafka_project/
├── docker-compose.yml  # Kafka & PostgreSQL setup
├── producer_1.py        # Temperature sensor producer
├── producer_2.py        # User activity producer
├── producer_3.py        # Error log producer
├── consumer.py          # Kafka consumer processing messages
├── README.md            # Project documentation
```

### How It Works

1. **Producer 1** sends temperature sensor data to `sensor-data` topic.
2. **Producer 2** sends user activity logs to `user-logs` topic.
3. **Producer 3** sends system errors to `error-logs` topic.
4. **Consumer** listens to all three topics and logs any errors into the `error_messages` table in PostgreSQL.

### Running the Project

1. Start Kafka and PostgreSQL:
   ```sh
   docker compose up -d
   ```
2. Start the consumer:
   ```sh
   python consumer.py
   ```
3. Start the producers (in separate terminals):
   ```sh
   python producer_1.py
   python producer_2.py
   python producer_3.py
   ```
4. Verify error logging in PostgreSQL:
   ```sql
   SELECT * FROM error_messages;
   ```

---

### Επισκόπηση

Αυτό το project δείχνει μια **αρχιτεκτονική πολλαπλών producers και ενός consumer** χρησιμοποιώντας **Apache Kafka**. Τρεις διαφορετικοί producers στέλνουν μηνύματα σε ξεχωριστά Kafka topics, και ένας consumer τα επεξεργάζεται, καταγράφοντας τυχόν σφάλματα στη **βάση PostgreSQL**.

### Τεχνολογίες που Χρησιμοποιούνται

- **Apache Kafka** (μηχανισμός ανταλλαγής μηνυμάτων)
- **Python** (για τους producers & consumer)
- **PostgreSQL** (για αποθήκευση errors)
- **Docker** (για Kafka & PostgreSQL setup)

### Δομή του Project

```
kafka_project/
├── docker-compose.yml  # Ρύθμιση Kafka & PostgreSQL
├── producer_1.py        # Producer αισθητήρα θερμοκρασίας
├── producer_2.py        # Producer καταγραφής δραστηριότητας χρήστη
├── producer_3.py        # Producer καταγραφής errors
├── consumer.py          # Consumer που διαχειρίζεται τα μηνύματα
├── README.md            # Τεκμηρίωση έργου
```

### Πώς Λειτουργεί

1. **Ο Producer 1** στέλνει δεδομένα αισθητήρων θερμοκρασίας στο topic `sensor-data`.
2. **Ο Producer 2** στέλνει δραστηριότητες χρηστών στο topic `user-logs`.
3. **Ο Producer 3** στέλνει errors στο topic `error-logs`.
4. **Ο Consumer** ακούει και τα τρία topics και καταγράφει τα errors στον πίνακα `error_messages` της PostgreSQL.

### Εκτέλεση του Project

1. Ξεκινήστε το Kafka και τη βάση PostgreSQL:
   ```sh
   docker compose up -d
   ```
2. Εκκινήστε τον consumer:
   ```sh
   python consumer.py
   ```
3. Εκκινήστε τους producers (σε ξεχωριστά terminals):
   ```sh
   python producer_1.py
   python producer_2.py
   python producer_3.py
   ```
4. Επαληθεύστε τα errors στη βάση PostgreSQL:
   ```sql
   SELECT * FROM error_messages;
   ```

