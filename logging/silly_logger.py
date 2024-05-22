from datetime import datetime


class SillyLog:
    """
    Just a silly thing to imitate a proper logger for now
    """

    @staticmethod
    def _get_time():
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    def info(self, message):
        print(f"{self._get_time()} (INFO) {message}")

    def debug(self, message):
        print(f"{self._get_time()} (DEBUG)    {message}")

    def error(self, message):
        print(f"{self._get_time()} (ERROR) {message}")


def get_logger(log_name):
    """
    Initialise a logger

    This obviously is not a proper logger.
    This is a placeholder so that the calls to a logger will be in place in the code
    """
    # Sample code from other notebook
    # logging_settings = LoggingSettings(
    #     logger_name=log_name,
    #     keyvault_scope=KVScope,
    #     log_db_server_name=f'{sqlServrName}.database.windows.net',
    #     log_db_database_name=sqlDbName,
    #     log_db_username_secret='fooo',
    #     log_db_password_secret='foooo',
    #     log_db_destination_table_name='blah',
    #     log_level=logging.DEBUG
    # )
    # return get_logger_factory(logging_settings).get_logger_for_name(logger_name, logging.DEBUG)

    return SillyLog()
