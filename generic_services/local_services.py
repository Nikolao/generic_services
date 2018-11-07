#
import os
import configparser


class ConfigurationService:
    """A mapping object representing configuration with sections and keys."""
    def __init__(self, file_name):
        self.config = configparser.ConfigParser()
        self.config.read(file_name)

    def get(self, section, key, default=None):
        if section in self.config:
            if key in self.config[section]:
                return self.config[section][key]
            else:
                return default
        else:
            return default


class StorageService:
    """An object representing the filesystem."""
    def __init__(self, directory, logger):
        self.directory = directory
        self.logger = logger

    def writeDocument(self, bucket, name, data, options={}):
        """options['mode'] = 'b'"""
        full_name = os.path.join(self.directory, bucket, name)
        mode = 'w' + options.get('mode', '')
        with open(full_name, mode) as f:
            f.write(data)

    def hasDocument(self, bucket, name):
        full_name = os.path.join(self.directory, bucket, name)
        return os.path.exists(full_name)

    def readDocument(self, bucket, name, options={}):
        """options['mode'] = 'b'"""
        full_name = os.path.join(self.directory, bucket, name)
        mode = 'r' + options.get('mode', '')
        with open(full_name, mode) as f:
            ret = f.read()
        return ret

    def removeDocument(self, bucket, name):
        full_name = os.path.join(self.directory, bucket, name)
        os.remove(full_name)


class DataService:
    def post(kind, data, options):
        pass

    def put(kind, id, version, data, options):
        pass

    def patch(kind, id, version, data, options):
        pass

    def delete(kind, id, options):
        pass

    def get(kind, id, options):
        pass

    def search(kind, query, options):
        pass


class HookService:
    def __init__(self):
        self._actions = {}

    def do_action(self, name, data, options):
        if name not in self._actions:
            return
        for call in self._actions[name]:
            function = call[0]
            argv = call[1]
            function(*argv)

    def add_action(self, name, function, argv=[], options={}):
        if name not in self._actions:
            self._actions[name] = []
        tmp = self._actions[name]
        tmp.append((function, argv))


class MessageService:
    def publish(queue, data, options):
        pass

    def subscribe(queue, function, options):
        pass


class QueueService:
    def push(event, data, options):
        pass

    def pull(event, options):
        pass

    def subscribe(event, function, options):
        pass


class CacheService:
    def write(key, data, options):
        pass

    def read(key, options):
        pass

    def remove(key, options):
        pass

#
