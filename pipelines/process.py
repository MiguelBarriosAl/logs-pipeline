from testers import test_out_of_order

TIME_UNIT = 60 * 60


class Process_Log:
    def __init__(self, chunk_list: list):
        self.chunks = chunk_list
        self.chunks_range = load_per_range(self.chunks)
        self.index_campaign = 4
        self.index_source = 3
        self.index_medium = 2
        self.chunk_list = []
        self.records = {}

    def _get_values(self, index):
        for chunk in self.chunks_range:
            timestamp = chunk[0][0]
            for c in chunk:
                self.chunk_list += [c[index]]
            self.max_value = max(set(self.chunk_list), key=self.chunk_list.count)
            self.chunk_list = []
            self.records[timestamp] = self.max_value
        return self.records

    def campaign(self):
        return self._get_values(self.index_campaign)

    def source(self):
        return self._get_values(self.index_source)

    def medium(self):
        return self._get_values(self.index_medium)


def load_per_range(lists_logs: list[list]) -> list[list]:
    """
    :param lists_logs: List of logs separated in chunks
    :return: Valid log list
    """
    log_per_hour = []
    all_logs = []
    pre_log = 0
    limit_range = int(lists_logs[0][0][0]) + TIME_UNIT
    for logs in lists_logs:
        for log in logs:
            init_time = int(log[0])
            check_order = test_out_of_order(init_time, pre_log)
            if init_time <= limit_range and check_order is True:
                # Log inside of range
                log_per_hour.append(log)
                pre_log = init_time
            elif init_time > limit_range and check_order is True:
                # Log out of range
                pre_log = init_time
                limit_range = limit_range + TIME_UNIT
                log_per_hour = [log]
                all_logs.append(log_per_hour)
            elif check_order is False:
                # Log ignored
                all_logs.append(log_per_hour)
                pass
    return all_logs
