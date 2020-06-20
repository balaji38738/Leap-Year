from header import Header

class CSVStates(Header):
    @staticmethod
    def get_headers():
        return ['SrNo', 'State Name', 'TIN', 'StateCode']