"""doc
Module defines presenter class for formatting list of probabilities
"""

class PredictionPresenter(object):
    """doc
    Presenter class for formatting the output
    """
    def present(self, probabilities):
        """doc
        The method formats a list of probabilities.
        Args:
            probabilities: List of probabilities(percentage points).
            Example: ['24%', '10%', None]
        Returns:
            String of 'T' of 'F'. 'T' if >50%, otherwise 'F'
        """
        converted = [self.__convert(p) for p in probabilities]
        return ''.join(converted)

    @classmethod
    def __convert(cls, probability):
        if probability is None:
            return 'F'
        if int(probability.strip('%')) > 50:
            return 'T'
        return 'F'
