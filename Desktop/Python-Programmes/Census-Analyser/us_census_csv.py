from header import Header

class USCensusCSV(Header):
    @staticmethod
    def get_headers():
        return ["State Id", "State", "Population",
            "Housing units", "Total area", "Water area",
            "Land area", "Population Density", "Housing Density"
        ]