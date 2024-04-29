# Salesforce Postgres Synchronization

This Python script facilitates synchronization between Salesforce and PostgreSQL databases. It fetches data from Salesforce, saves it into PostgreSQL, and provides functionality to delete records from Salesforce.

## Features

- Fetch data from Salesforce based on specified queries.
- Save fetched data to PostgreSQL tables.
- Delete records from Salesforce based on record IDs.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your system (version 3.9 or higher).
- Required Python packages installed (see `requirements.txt`).
- Access to both Salesforce and PostgreSQL databases.
- Proper configuration set up for Salesforce and PostgreSQL connections.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/vishalpatidar99/salesforce-postgres-sync.git
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Install Redis for queue the jobs**
    - **Windows**: 
      - Download Redis from the [official website](https://redis.io/download).
      - Extract the downloaded file and navigate to the extracted directory.
      - Run the `redis-server.exe` to start the Redis server.

    - **MacOS**:
      - You can install Redis via Homebrew using the following command:
        ```bash
        brew install redis
        ```
      - Start the Redis server using the following command:
        ```bash
        redis-server
        ```
    - **Linux**:
      - Redis is available in most Linux distribution repositories. You can install it using the package manager specific to your distribution. For example, on Debian/Ubuntu, you can use:
        ```bash
        sudo apt-get update
        sudo apt-get install redis-server
        ```
      - Start the Redis server using the following command:
        ```bash
        sudo service redis-server start
        ```

3. **Set up configuration files for Salesforce (`config.py`) and PostgreSQL (`config.py`) connections.**

## Configurations Table Setup
To synchronize data between Salesforce and PostgreSQL, you need to define table configurations in the `table_conf` table in your PostgreSQL database. Follow these steps to set up the table 
1. **Create table_conf Table: If not already created, create a table named table_conf in your PostgreSQL database. You can use the following SQL command to create the table:**
     ```bash
     CREATE TABLE IF NOT EXISTS table_conf (
        id SERIAL PRIMARY KEY,
        table_name VARCHAR(255) NOT NULL,
        query TEXT NOT NULL
    );
     ```
2. **Insert Table Configurations: Insert entries into the table_conf table for each table you want to synchronize between Salesforce and PostgreSQL. Each entry should specify the Salesforce object's table name and a SOQL query to fetch data from Salesforce. For example:**
    ```bash
    INSERT INTO table_conf (table_name, query) VALUES ('Account', 'SELECT Id, Name FROM Account');
    ```

## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **The script will automatically fetch data from Salesforce, save it to PostgreSQL, and perform any specified operations.**

3. **Optionally, you can set up cron jobs to run the script at regular intervals for automatic synchronization.**

## Configuration

Ensure that you configure the following settings in the `config.py` file:

```python
# Salesforce credentials
SALESFORCE_USERNAME = 'your_salesforce_username'
SALESFORCE_PASSWORD = 'your_salesforce_password'
SALESFORCE_SECURITY_TOKEN = 'your_salesforce_security_token'

# PostgreSQL connection details
POSTGRES_HOST = 'your_postgres_host'
POSTGRES_PORT = 'your_postgres_port'
POSTGRES_DB = 'your_postgres_database'
POSTGRES_USER = 'your_postgres_username'
POSTGRES_PASSWORD = 'your_postgres_password'

# Redis connection details
REDIS_HOST = 'your_redis_host'
REDIS_PORT = 'your_redis_port'
REDIS_PASSWORD = 'your_redis_password'

# set log info
LOG_FILE = 'salesforce_postgres_sync.log'
LOG_LEVEL = logging.INFO