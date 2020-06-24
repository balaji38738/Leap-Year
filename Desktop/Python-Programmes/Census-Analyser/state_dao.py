class StateDAO:
    def __init__(self, headers):
        if "SrNo" in headers:
            self.sr_no = "Sr.No"
        if set(headers).intersection({"State Name", "State"}):
            self.state_name = "State"
        if "TIN" in headers:
            self.TIN = "TIN"
        if "StateCode" in headers:
            self.state_code = "State Code"
        if "Population" in headers:
            self.population = "Population"
        if "AreaInSqKm" in headers:
            self.area_in_sq_km = "Area in Sq.Km"
        if "DensityPerSqKm" in headers:
            self.density_per_sq_km = "Density in Sq.Km"
        
    def __repr__(self):
        possible_attributes = ["sr_no", "state_name",
            "TIN", "state_code", "population",
            "area_in_sq_km", "density_per_sq_km"
        ]
        attributes = []
        for attr in possible_attributes:
            if attr in dir(self):
                attributes.append(getattr(self, attr))
        return ",".join(attributes)

x = StateDAO(['SrNo', 'State Name', 'TIN', 'StateCode'])
print(x)
