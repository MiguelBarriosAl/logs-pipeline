import csv

chunk_size = 3  # In a production environment it can be set at a higher number
chunk_list = list()


def sink_file(path: str) -> list:
    """
    Reading of Csv files stored in chunks according to the variable "chunk size".
    :param path: Path to csv file
    :return: Separation of stored chunk data in a list
    """
    with open(path, "r") as file:
        reader_csv = csv.reader(file, delimiter=";")
        next(reader_csv)
        chunked_list = list(reader_csv)
        for i in range(0, len(chunked_list), chunk_size):
            chunk_list.append(chunked_list[i:i + chunk_size])
        return chunk_list
