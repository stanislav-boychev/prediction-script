"""doc
Module defining class for access prediction api endpoints
"""
import urllib
import urllib.request
import json

class PredictionRequest(object):
    """doc
    Class for requesting predictions for given list of teams pairs
    """
    def __init__(self, scheme, host, port, path):
        self.scheme = scheme
        self.host = host
        self.port = port
        self.path = path

    def execute(self, teams):
        """doc
        The method accepts list of team pairs. For each pair a request is made
        to prediction api endpoint.
        Args:
            teams: List of team pairs. Example: [['Team1', 'Team2'], ['TeamA', 'TeamB']]
        Returns:
            List of probabilities(percentage points). The list may contain None
            if a probability can't be calculated. Example ['24%', '10%', None]
        """
        url = f"{self.scheme}://{self.host}:{self.port}/{self.path}"
        try:
            probabilities = [self.__get_probability(url, pair) for pair in teams]
            return [True, probabilities]
        except urllib.error.URLError:
            return [False, f'Connection refused: {url}']

    @classmethod
    def __get_probability(cls, url, teams):
        params = urllib.parse.urlencode(list(zip(('team1', 'team2'), teams)))
        try:
            response = urllib.request.urlopen(f'{url}?{params}').read()
            return json.loads(response)['probability']
        except urllib.error.HTTPError:
            return None
