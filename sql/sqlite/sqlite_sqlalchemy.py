from sqlalchemy import (
    create_engine, insert,
    MetaData, Table, Column, Integer, String, Boolean)


class BaseSqliteConnector:
    def __init__(self, db_path):
        self.engine = create_engine(db_path)
        self.conn = self.engine.connect()

        self.metadata = MetaData()
        self.establish_tables()

    def establish_tables(self):
        """
        Method to be overridden with the actual tables required.
        Below is just for demonstration
        """
        self.student = Table(
            Column('Id', Integer(),primary_key=True),
            Column('Name', String(255), nullable=False),
            Column('Major', String(255)),
            Column('Pass', Boolean(), default=True),
            name='student',
            metadata=self.metadata
        )
        
        self.metadata.create_all(self.engine)

    def execute_query(self, query, return_result = True, fetch = 'all', amount = 1):
        if return_result is False:
            # If no return is needed, simply execute and not return anything
            self.conn.execute(query)
            return
        
        # Otherwise execute the query and decide how data is to be returned.
        exe = self.conn.execute(query)
        if fetch == 'all':
            result = exe.fetchall()
        elif fetch == 'many':
            result = exe.fetchmany(amount)
        elif fetch == 'one':
            result = exe.fetchone()
        else:
            result = None
        return result
    
    def insert_data(self, table_name, values_list):
        """
        Insert data into a table.
        The table has to be established by the init method
        
        Name of table's variable as established in init method
        list of dictionaries, each dict key value is the column and value of that row
        """
        insert_query = insert(self._get_table_object(table_name))
        self.conn.execute(insert_query, values_list)
        

    def _get_table_object(self, table_name):
        table = getattr(self, table_name)
        if table is None:
            raise Exception('Table does not exist')
        return table

    def close_connection(self):
        self.conn.close()