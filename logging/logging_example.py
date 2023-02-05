import logging


def main():
    logging.basicConfig(level=logging.WARNING)
    # The line above determines what level of logging to display
    # This will only show WARNING and above (ERROR, and CRITICAL)

    # These are the basic levels of logging that are out of the box
    # More can be custom defined
    logging.debug("debug message")
    logging.info("info message")
    logging.warning("warning message")
    logging.error("error message")
    logging.critical("critical message")


def more_complex_example():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


def logging_to_file():
    """
    Just specifying this will mean that it won't push to console anymore
    """
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="basic.log"
    )


def logging_to_external_service():
    from logging.handlers import SysLogHandler
    # There are many log handlers that can send logs to different places
    # Custom log handlers can also be defined
    
    # There are a whole range of different hosts
    HOST = 'logs.papertrailapp.com'  # Dummy host
    PORT = 37554

    # The basic logger will no longer be applicable here.
    logger = logging.getLogger("example_logs")
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(HOST, PORT))
    logger.addHandler(handler)
    # Not restricted to one handler as well
    # Can add as many as you want.

    # Be extra careful what is being logged when sending to external destinations.
    # Logs can contain sensitive data.
    # Or DON'T log sensitve data all together.
    # Never assume log files are secure