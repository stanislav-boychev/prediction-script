"""doc
Module defines the main prediction script
"""
from prediction_request import PredictionRequest
from configuration_reader import ConfigurationReader
from teams_reader import TeamsReader
from prediction_presenter import PredictionPresenter

class PredictionScript(object):
    """doc
    The PredictionScript can be configured using config.yml. The team pairs are stored
    in file input.txt. Each team pair is on separate line and each team is separated
    by '&'
    """

    @classmethod
    def execute(cls):
        """doc
        Executes the script
        """
        config = ConfigurationReader().read('config.yml')
        try:
            scheme = config['scheme']
            host = config['host']
            port = config['port']
            path = config['path']
        except KeyError as exc:
            print(f'Missing key from from the confing file: {exc}')
            return
        request = PredictionRequest(scheme, host, port, path)
        teams = TeamsReader().read('input.txt')
        success, result = request.execute(teams)
        if success:
            formatted = PredictionPresenter().present(result)
            print(formatted)
        else:
            print(result)

PredictionScript().execute()
