import sqlite3
from sqlite_connector import SqliteConnector


def example_pandas_to_sqlite():
    import pandas as pd
    import sqlite3

    weather = pd.read_csv(
        "https://github.com/alanjones2/dataviz/raw/master/londonweather.csv"
    )
    conn = sqlite3.connect("weather.db")
    weather.to_sql(
        "weather", conn
    )  # 'weather' is the table name. It will be created if it doesn't exist
    # By defaul to_sql will try to create the table and will raise an error if the table already exists
    # Set `if_exists=append` or `if_exists=replace` depending on what is needed

    # likewise can also read from sqlite too in a similar fashion
    conn = sqlite3.connect("weather.db")
    weather = pd.read_sql("SELECT * FROM weather", conn)


def context_manager_example():
    con = sqlite3.connect(":memory:")
    con.execute(
        "create table person (id integer primary key, firstname varchar unique)"
    )

    # Successful, con.commit() is called automatically afterwards
    with con:
        con.execute("insert into person(firstname) values (?)", ("Joe",))

    # con.rollback() is called after the with block finishes with an exception, the
    # exception is still raised and must be caught
    try:
        with con:
            con.execute("insert into person(firstname) values (?)", ("Joe",))
    except sqlite3.IntegrityError:
        print("couldn't add Joe twice")

    # Connection object used as context manager only commits or rollbacks transactions,
    # so the connection object should be closed manually
    con.close()


if __name__ == "__main__":
    connector = SqliteConnector("test_db.db")
    connector.execute_query("CREATE TABLE IF NOT EXISTS test_table (col1, col2, col3)")

    input("Check the db file exists and has the table.\nEnter to continue")

    connector.execute_query("DROP TABLE IF EXISTS test_table")

    input("Check that table no longer exists\nEnter to finish off")
