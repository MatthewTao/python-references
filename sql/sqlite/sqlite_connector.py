import sqlite3


class SqliteConnector:
    def __init__(self, path):
        """
        Connect to the database in the init method and stop there
        """
        self.connection = sqlite3.connect(path)
        self.cursor = None

    def execute_query(self, query):
        """
        Executes any query and returns the results
        
        Ideally the query would be something like below, using paramatrised queries.
        cursor.execute("INSERT INTO staff (person_id, lastname) VALUES (?, ?)", (51, "Mc'Donald")) 
        """
        self._get_cursor()
        response = None
        try:
            response = self.cursor.execute(query)
        except Exception as e:
            print(f'Execution failed: {e}')
            self._rollback()
        else:
            self._commit()
        
        return response

    def _get_cursor(self):
        self.cursor = self.connection.cursor()

    def _close_cursor(self):
        if self.cursor is None:
            pass
        else:
            self.cursor.close()

    def close_connection(self):
        self.connection.close()

    def _commit(self):
        if self.connection is None:
            print('No cursor to commit')
        else:
            self.connection.commit()

    def _rollback(self):
        if self.connection is None:
            print('No cursor to rollback')
        else:
            self.connection.rollback()
