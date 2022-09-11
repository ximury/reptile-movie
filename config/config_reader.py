from config.config_init import ConfigReader


class NetConfig(ConfigReader):
    url: str = str()
    section = "net"

    def __init__(self):
        if self._init_flag:
            return
        super().__init__()
        self.url = self._parser.get(section=self.section, option="url")
        self._init_flag = True

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


class MovieConfig(ConfigReader):
    subject: str = str()
    section = "movie"

    def __init__(self):
        if self._init_flag:
            return
        super().__init__()
        self.subject = self._parser.get(section=self.section, option="subject")
        self._init_flag = True

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


class CloudConfig(ConfigReader):
    subject: str = str()
    icon_name: str = str()
    section = "cloud"

    def __init__(self):
        if self._init_flag:
            return
        super().__init__()
        self.subject = self._parser.get(section=self.section, option="subject")
        self.icon_name = self._parser.get(section=self.section, option="icon_name")
        self._init_flag = True

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


netConfig = NetConfig()
movieConfig = MovieConfig()
cloudConfig = CloudConfig()
