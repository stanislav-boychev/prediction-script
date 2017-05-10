"""doc
Module defines configuration reader for prediction script
"""
import yaml

class ConfigurationReader(object):
    """doc
    Class for reading script config
    """

    @classmethod
    def read(cls, filename):
        """doc
        The method accepts filename string. Returns dictionary
        Args:
            filename: Example: config.yml
        Returns:
            Dictionary: {'host': 'localhost', ...}
        """
        with open(filename, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)
                return {}
