from src.postgres import PostgreSQL

POSTGRES = None

def setup_postgres():
    global POSTGRES

    if POSTGRES is None:
        POSTGRES = PostgreSQL()
    
    return POSTGRES
    

def close_postgres():
    if POSTGRES is not None:
        POSTGRES.close_connection()


def fetch_tables_wrapper():
    return setup_postgres().fetch_table_queries()


def create_table_wrapper(table_name):
    return setup_postgres().create_table(table_name)


def insert_data_wrapper(table_name, records):
    return setup_postgres().insert_data(table_name, records)


def ids_wrapper(table_name):
    return setup_postgres().get_ids_from_db(table_name)