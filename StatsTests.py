from ConfigReader import ConfigReader as cr

class ChiSquareTest:
    def __init__(self, data_path : str):
        self.data : dict = cr.read(data_path)
    def execute(self) -> dict:
        result = {}
        return result

