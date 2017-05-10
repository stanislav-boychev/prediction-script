"""doc
Module defines class for reading teams from file
"""

class TeamsReader(object):
    """doc
    Class for reading list of teams from file. The team pairs are stored
    in file specified by filename. Each team pair is on separate line and each
    team is separated by '&'
    """

    @classmethod
    def read(cls, filename):
        """doc
        The method accepts filename string. Returns list of team pairs
        Args:
            filename: Example: input.txt
        Returns:
            list of team pairs: [['Team1', 'Team2'], ['TeamA', 'TeamB']]
        """
        with open(filename, 'r') as stream:
            teams = stream.read().splitlines()
            return [string.split(' & ') for string in teams]
