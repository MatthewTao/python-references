import spark
import numpy as np

size = 300000
names = [str(x) for x in np.random.choice(["Alex", "James", "Michael", "Peter", "Harry", "Matt"], size=size)]
ids = [int(x) for x in np.random.randint(1, 10, size)]
fruits = [str(x) for x in np.random.choice(["Apple", "Grapes", "Orange", "Pear", "Kiwi", "Durian"], size=size)]

df = spark.createDataFrame(list(zip(names, ids, fruits)), ["person_name", "id_number", "fruit"])

df.show()
