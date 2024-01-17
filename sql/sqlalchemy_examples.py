"""
This code uses a sample data base that can be found here
https://www.kaggle.com/datasets/groleo/european-football-database?resource=download
"""
from sqlalchemy import (
    create_engine,
    insert,
    select,
    and_,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
)
import pandas as pd

"""
For Unix
# sqlite://<nohostname>/<path>
# where <path> is relative:
engine = create_engine('sqlite:///foo.db')

# or absolute, starting with a slash:
engine = create_engine('sqlite:////absolute/path/to/foo.db')

For Windows
relative path
engine = create_engine('sqlite:///foo.db')

absolute path
engine = create_engine(r'sqlite:///C:\path\to\foo.db')
"""
SAMPLE_TABLE_PATH = r"sqlite:///D:\data_and_stuff\european_database.sqlite"


def simple_select_example():
    engine = create_engine(SAMPLE_TABLE_PATH)
    conn = engine.connect()

    metadata = MetaData()  # extracting the metadata
    division = Table("divisions", metadata, autoload_with=engine)
    print(repr(metadata.tables["divisions"]))
    print(division.columns.keys())

    query = select(division)
    print(f"Query generated {query}")

    exe = conn.execute(query)  # executing the query
    result = exe.fetchmany(5)  # extracting top 5 results
    print(result)

    # Manual close here. Consider using `with` block
    conn.close()


def select_example():
    engine = create_engine(SAMPLE_TABLE_PATH)
    conn = engine.connect()
    metadata = MetaData()
    division = Table("divisions", metadata, autoload_with=engine)
    match = Table("matchs", metadata, autoload_with=engine)

    query = (
        select(division, match)
        .select_from(
            division.join(match, division.columns.division == match.columns.Div)
        )
        .where(and_(division.columns.division == "E1", match.columns.season == 2009))
        .order_by(match.columns.HomeTeam)
    )
    output = conn.execute(query)
    results = output.fetchall()

    data = pd.DataFrame(results)
    print(data.head())


def quick_end_to_end_example():
    """
    A small demonstration of the four CRUD methods

    The statement generation would work with or without a valid connection
    """
    engine = create_engine("sqlite:///quick_example.sqlite")
    conn = engine.connect()
    metadata = MetaData()

    Student = Table(
        "Student",
        metadata,
        Column("Id", Integer(), primary_key=True),
        Column("Name", String(255), nullable=False),
        Column("Major", String(255)),
        Column("Pass", Boolean(), default=True),
    )

    metadata.create_all(engine)

    query = insert(Student).values(Id=1, Name="Matthew", Major="English", Pass=True)
    print(f"\n\n{query}")
    conn.execute(query)

    query = select(Student)
    output = conn.execute(query).fetchall()
    print(f"\n\n{query}")
    print(output)

    # Insert many rows
    many_in_query = insert(Student)
    values_list = [
        {"Id": "2", "Name": "Nisha", "Major": "Science", "Pass": False},
        {"Id": "3", "Name": "Natasha", "Major": "Math", "Pass": True},
        {"Id": "4", "Name": "Ben", "Major": "English", "Pass": False},
    ]
    conn.execute(many_in_query, values_list)
    output = conn.execute(Student.select()).fetchall()
    print(f"\n\n{many_in_query}")
    print(output)

    # SELECT with WHERE
    query = select(Student).where(Student.columns.Major == "English")
    output = conn.execute(query)
    print(f"\n\n{query}")
    print(output.fetchall())

    # SELECT with WHERE AND
    query = Student.select().where(
        and_(Student.columns.Major == "English", Student.columns.Pass != True)
    )
    output = conn.execute(query)
    print(f"\n\n{query}")
    print(output.fetchall())

    """
in
Student.select().where(Student.columns.Major.in_(['English','Math']))

and, or, not
Student.select().where(or_(Student.columns.Major == 'English', Student.columns.Pass = True))

order by
Student.select().order_by(desc(Student.columns.Name))

limit
Student.select().limit(3)

sum, avg, count, min, max
select([func.sum(Student.columns.Id)])

group by
select([func.sum(Student.columns.Id),Student.columns.Major]).group_by(Student.columns.Pass)

distinct
select([Student.columns.Major.distinct()])
"""
    # Full list of expressions here https://docs.sqlalchemy.org/en/14/core/expression_api.html

    # Putting that data into Pandas DataFrame
    """
    data = pd.DataFrame(results)
    data.columns = results[0].keys()
    data.show()
    """

    # UPDATE
    query = Student.update().values(Pass=True).where(Student.columns.Name == "Nisha")
    conn.execute(query)

    query = select(Student).where(Student.columns.Name == "Nisha")
    output = conn.execute(query)
    print(f"\n\n{query}")
    print(output.fetchall())

    query = Student.update().values(Pass=False).where(Student.columns.Name == "Nisha")
    conn.execute(query)

    query = select(Student).where(Student.columns.Name == "Nisha")
    output = conn.execute(query)
    print(f"\n\n{query}")
    print(output.fetchall())

    # DELETE
    query = Student.delete().where(Student.columns.Name == "Ben")
    conn.execute(query)

    query = select(Student)
    output = conn.execute(query)
    print(f"\n\n{query}")
    print(output.fetchall())

    query = insert(Student).values(Id=4, Name="Ben", Major="English", Pass=False)
    conn.execute(query)

    query = select(Student)
    output = conn.execute(query)
    print(f"\n\n{query}")
    print(output.fetchall())

    conn.close()


quick_end_to_end_example()
