import configparser
import threading
from os import path


class Singleton:
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "_instance"):
            return cls._instance
        with cls._lock:
            if hasattr(cls, "_instance"):
                return cls._instance
            cls._instance = object.__new__(cls)
        return cls._instance


class ConfigReader(Singleton):
    _config_file_path = path.dirname(path.dirname(__file__)) + "/config/config.conf"

    _parser = configparser.ConfigParser()

    _lock = threading.Lock()

    _init_flag = False

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        self._parser.read(self._config_file_path)

    def _write(self):
        self._parser.write(open(self._config_file_path, "w"))
        self._init_flag = False
