from sqlite_connector import SqliteConnector


if __name__ == '__main__':
    connector = SqliteConnector('test_db.db')
    connector.execute_query('CREATE TABLE IF NOT EXISTS test_table (col1, col2, col3)')

    foo = input('Check the db file exists and has the table.\nEnter to continue')

    connector.execute_query('DROP TABLE IF EXISTS test_table')

    foo = input('Check that table no longer exists\nEnter to finish off')
