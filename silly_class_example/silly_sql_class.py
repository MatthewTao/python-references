class AbstractQuery:
    RAW_QUERY = """
SELECT * FROM dummy.table
    """
    def __init__(self, params: dict):
        self.params = self._validate_params(params)
        self._get_query()
        
    def _get_query(self):
        self.query = self.RAW_QUERY.format(**self.params)

    def _validate_params(self, params):
        validated = {}
        for key, value in params.items():
            try:
                assert isinstance(value, str)
            except:
                pass
            else:
                validated.update({key: value})
        return validated


class NewQuery(AbstractQuery):
    RAW_QUERY = """
SELECT * FROM {test_schema}.{test_table}
WHERE {where_clause}
    """


if __name__ == '__main__':
    params = {
        'test_schema': 'testingschema123',
        'test_table': 'testingtable',
        'where_clause': "1 = 1",
        'not_needed_field': 23
    }
    
    print(NewQuery(params).query)
