"""
Sets are mildly like lists and tuples, in that they hold a collection of values.
The main differences are that they hold a list of unordered and unique values.
Sets are also more optimised for membership operations and other things.

So they are commonly used for union, intersections, and differences
"""


def initialise_sets():
    data_scientist = {"Python", "R", "SQL", "Git", "Tableau", "SAS"}
    data_engineer = {"Python", "Scala", "Git", "SQL", "Hadoop"}

    # To create an empty set, set() must be used `{}` will always create an empty dictionary
    empty_set = set()

    return {"data_engineer": data_engineer, "data_scientist": data_scientist}


def membership_tests():
    data_engineer = initialise_sets()["data_engineer"]
    print("Python" in data_engineer)

    list_of_skills = {"Python", "Git"}
    print(list_of_skills.issubset(data_engineer))

    print(data_engineer.issuperset(list_of_skills))


def add_remove_items():
    data_scientist, data_engineer = initialise_sets()["data_scientist"], initialise_sets()["data_engineer"]
    data_engineer.add("Spark")
    print(data_engineer)

    data_engineer.remove("Hadoop")  # Raises KeyError if the item doesn't exist
    print(data_engineer)

    data_engineer.discard("Scala")  # Doesn't raise any errors if the item doesn't already exist

    tool = data_scientist.pop()  # Remove and return an arbitrary value
    print(tool)

    data_scientist.clear()  # Remove all values from the set

    additional_skills = {"Communication", "Cloud", "Python"}
    data_engineer.update(additional_skills)  # Add the items that don't already exist into the set


def set_operations():
    """
    These are some of the main things that makes sets more unique
    """
    data_scientist, data_engineer = initialise_sets()["data_scientist"], initialise_sets()["data_engineer"]
    all_skills = data_engineer.union(data_scientist)
    print(all_skills)

    all_skills_2 = data_engineer | data_scientist  # This notation works too
    print(all_skills_2)

    common_skills = data_engineer.intersection(data_scientist)
    print(common_skills)

    nothing_in_common = data_scientist.isdisjoint(data_engineer)
    print(nothing_in_common)  # Expecting False here as there are common skills

    different_skills = data_engineer.difference(data_scientist)  # returns the items in data_engineer, but not in other
    print(different_skills)

    all_different_skills = data_engineer.symmetric_difference(data_scientist)  # Returns left right difference
    # dataScientist ^ dataEngineer is the other notation as well
    print(all_different_skills)


def set_comprehension():
    result = {skill for skill in ['GIT', 'PYTHON', 'SQL'] if skill not in {'GIT', 'PYTHON', 'JAVA'}}
    print(result)


membership_tests()
