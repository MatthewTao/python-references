import csv


def read_csv(path, headers=None):
    with open(path, mode='r') as file:
        csv_file = csv.reader(file)

        rows = 0
        results = []
        keys = []
        for lines in csv_file:
            if rows > 0:
                results.append(
                    dict(
                        zip(keys,lines)
                    )
                )
            elif rows == 0 and headers is not None:
                keys = headers
            elif rows == 0 and headers is None:
                keys = lines
            rows += 1
    return results


if __name__ == '__main__':
    print('read csv with no headers provided',
        read_csv(
            path='testing-csv.csv',
            headers=None
        )
    )

    print('read csv with headers provided',
        read_csv(
            path='testing-csv.csv',
            headers=['col1', 'col2', 'col3']
        )
    )
