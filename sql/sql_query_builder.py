"""
This is a simple silly query builder for python.
Most other query builders don't seem to be maintained anymore.
Perhaps they are all 'finished', or more likely that most have moved to ORMs

In any case, this can be useful for quick and simple uses.
"""
import functools


class Query:
    keywords = [
        "SELECT",
        "FROM",
        "WHERE",
        "ORDER BY",
        "LIMIT",
    ]
    DEFAULT_SEPERATOR = ","
    INDENT = "    "
    SEPERATOR = {
        "WHERE": " AND",
    }

    def __init__(self):
        self.data = {k: [] for k in self.keywords}

    def __str__(self):
        return "".join(self._lines())

    def __getattr__(self, name):
        return functools.partial(self.add, name.replace("_", " "))

    def add(self, keyword, *args):
        target = self.data[keyword]

        for arg in args:
            target.append(self._cleanup(arg))

        return self

    def _lines(self):
        for keyword, things in self.data.items():
            if not things:
                continue

            yield f"{keyword}\n"
            yield from self._lines_keyword(keyword, things)

    def _lines_keyword(self, keyword, things):
        for i, thing in enumerate(things, 1):
            last = i == len(things)
            yield self.INDENT + thing

            if not last:
                yield self.SEPERATOR.get(keyword, self.DEFAULT_SEPERATOR)
            yield "\n"

    @staticmethod
    def _cleanup(thing):
        return thing.strip()


if __name__ == "__main__":
    query = Query()
    print(str(query.SELECT("*").FROM("dummy.table")))

    print(
        str(
            Query()
            .SELECT("col1", "col2", "col3")
            .FROM("dummy.table")
            .WHERE("col1 > 2", "col3 = 'haha'")
        )
    )
