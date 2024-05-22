import spark
import numpy as np


def generate_random_df():
    """
    This might be useful for generating random datasets for testing
    """
    size = 300000
    names = [
        str(x)
        for x in np.random.choice(
            ["Alex", "James", "Michael", "Peter", "Harry", "Matt"], size=size
        )
    ]
    ids = [int(x) for x in np.random.randint(1, 10, size)]
    fruits = [
        str(x)
        for x in np.random.choice(
            ["Apple", "Grapes", "Orange", "Pear", "Kiwi", "Durian"], size=size
        )
    ]

    df = spark.createDataFrame(
        list(zip(names, ids, fruits)), ["person_name", "id_number", "fruit"]
    )

    df.show()


def add_row_hash():
    """
    Adding a hash of the row can be used for various purposes
    """
    from pyspark.sql.functions import sha2, concat_ws

    df = spark.createDataFrame(
        [(1, "2", 5, 1), (3, "4", 7, 8)], ("col1", "col2", "col3", "col4")
    )
    df.withColumn("row_sha2", sha2(concat_ws("||", *df.columns), 256)).show(
        truncate=False
    )
