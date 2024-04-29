import psycopg2
import logging
from config.config import Config


class PostgreSQL:
    def __init__(self):
        self.connection = psycopg2.connect(
            host=Config.POSTGRES_HOST,
            port=Config.POSTGRES_PORT,
            database=Config.POSTGRES_DB,
            user=Config.POSTGRES_USER,
            password=Config.POSTGRES_PASSWORD,
        )
        self.cursor = self.connection.cursor()
        self.logger = logging.getLogger(__name__)

    def fetch_table_queries(self):
        try:
            self.cursor.execute("SELECT table_name, query FROM table_conf;")
            self.logger.info("fetched data from configurations table")
            return self.cursor.fetchall()
        except Exception as e:
            self.logger.error(f"Error fetching table queries from PostgreSQL: {str(e)}")
            return []

    def create_table(self, table_name):
        try:
            self.cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    sf_id VARCHAR(100)
                )
            """
            )
            self.connection.commit()
            self.logger.info(f"created {table_name} in postgres")
        except Exception as e:
            self.logger.error(
                f"Error creating table {table_name} in PostgreSQL: {str(e)}"
            )

    def insert_data(self, table_name, records):
        try:
            for record in records:
                sf_id = record["Id"]
                self.cursor.execute(
                    f"INSERT INTO {table_name} (sf_id) VALUES (%s);", (sf_id,)
                )
            self.connection.commit()
            self.logger.info(f"inserted data in {table_name}")
        except Exception as e:
            self.logger.error(
                f"Error saving records to PostgreSQL table {table_name}: {str(e)}"
            )

    def get_ids_from_db(self, table_name):
        try:
            self.cursor.execute(f"SELECT sf_id FROM {table_name};")
            return [row[0] for row in self.cursor.fetchall()]
        except Exception as e:
            self.logger.error(
                f"Error fetching IDs from table {table_name} in PostgreSQL: {str(e)}"
            )
            return []

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
