import csv


def read_csv(path, headers=None):
    """
    Function to write a CSV from a list of dictionaries.
    
    If the headers are not provided, it will assume the headers from the first row.
    """
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


def write_dict_to_csv(csv_path, data_dict, keys=None):
    """
    Function to write a csv from a list of dictionaries.

    If keys is not provided, it will assume the headers from the first row.
    """
    if keys is None:
        keys = data_dict[0].keys()

    with open(csv_path, 'w', encoding='utf-8', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data_dict)


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
