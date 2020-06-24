class USCensusDAO:
    def __init__(self):
        self.state_id = "State Id"
        self.state = "State"
        self.population = "Population"
        self.housing_units = "Housing Units"
        self.total_area = "Total Area"
        self.water_area = "Water Area"
        self.land_area = "Land Area"
        self.population_density = "Population Density"
        self.housing_density = "Housing Density"

    def __repr__(self):
        attributes = [self.state_id, self.state, self.population,
            self.housing_units, self.total_area, self.water_area,
            self.land_area, self.population_density, self.housing_density
        ]
        return ",".join(attributes)