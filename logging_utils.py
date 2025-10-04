from datetime import datetime
from string import Formatter
from os import listdir, mkdir, remove
from os.path import abspath, exists, join

# PRESETS
LOG_PATH = "./logs/"
PRESET_LOGGING = "{time} - {level} - {content}"
PRESET_LOG4J2 = "[{time}] [{thread}/{level}] {content}"
PRESET_LEVEL_EMPHASIZED = "{level} - {time} >>> {content}"


def get_current_datetime():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


class SafeFormatter(Formatter):
    def get_value(self, key, args, kwargs):
        try:
            return super().get_value(key, args, kwargs)
        except (KeyError, IndexError):
            return ""


class Logging(object):
    CURRENT_TIME = datetime.now()

    def __init__(self, expiration: int = 30, pattern: str = None, use_thread: bool = False):
        """
        Initialization.

        :param expiration: After how long the longs are expired. The unit is day.
        :param pattern: Message format, including time, thread, level and content.
        """
        self.expiration = expiration
        self.pattern = pattern
        self.use_thread = use_thread
        if self.pattern is None:
            self.pattern = PRESET_LOG4J2
            self.use_thread = True

        if not exists(LOG_PATH):
            mkdir(LOG_PATH)

        self.remove_expired_logs()
        self.file_path = f"{abspath(join(LOG_PATH, get_current_datetime()))}.txt"

        # initialize safe formatter
        fmt = SafeFormatter()

    def remove_expired_logs(self):
        """
        Remove expired logs, which has existed for a time period longer than expiration.
        """
        logs = listdir(abspath(LOG_PATH))
        logs = map(lambda x: x.replace(".txt", ""), filter(lambda x: ".txt" in x, logs))
        for log in logs:
            created_time = datetime.strptime(log, "%Y%m%d_%H%M%S")
            time_delta = Logging.CURRENT_TIME - created_time
            if time_delta.days >= self.expiration:
                remove(abspath(join(LOG_PATH, log) + '.txt'))

    def generate_log(self, log_pattern: str, level: str, content: str, thread: str) -> str:
        """
        Generate log messages.

        :param log_pattern: Format of log messages.
        :param thread: Running thread.
        :param level: Log level.
        :param content: Log messages.

        :return: Params to fill into f-strings.
        """
        if self.use_thread:
            return log_pattern.format(time=get_current_time(), thread=thread, level=level, content=content+"\n")
        else:
            return log_pattern.format(time=get_current_time(), level=level, content=content + "\n")

    def info(self, thread: str = "main", content: str = "The program service is running normally..."):
        """
        Log info-level messages.
        """
        with open(self.file_path, encoding="utf-8", mode="a") as log_object:
            log_object.write(self.generate_log(self.pattern, "INFO", content, thread))

    def warning(self, thread: str = "main",
                content: str = "The program is facing tiny problems, but don't be worried."):
        """
        Log warn-level messages.
        """
        with open(self.file_path, encoding="utf-8", mode="a") as log_object:
            log_object.write(self.generate_log(self.pattern, "WARN", content, thread))

    def error(self, thread: str = "main", content: str = "The program is facing challenges."):
        """
        Log error-level messages.
        """
        with open(self.file_path, encoding="utf-8", mode="a") as log_object:
            log_object.write(self.generate_log(self.pattern, "ERROR", content, thread))

    def critical(self, thread: str = "main", content: str = "The program has met severe threats, so it's quitting."):
        """
        Log critical-level messages.
        """
        with open(self.file_path, encoding="utf-8", mode="a") as log_object:
            log_object.write(self.generate_log(self.pattern, "CRITICAL", content, thread))

    def close(self):
        """
        Log an ending message.
        """
        self.info(content="Shutting down...")
