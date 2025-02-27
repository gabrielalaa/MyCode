class Patient:
    # CONSTRUCTOR:
    def __init__(self, name):
        self.ID = None
        self.Name = name
        self.dob = None


class Hospital:
    def __init__(self, name):
        self.ID = None
        self.name = name
        self.patients = []
        self.staff = []

    # METHODS
    def occupancy(self):
        pass

    def admission(self):
        pass

    def serialize(self):
        pass


class HealthMinistry:
    def __init__(self):
        self.hospitals = []

    def getHospitals(self,):
        return self.hospitals

    def addHospital(self, hospital):
        self.hospitals.append(hospital)

    def getHospitalByID(self, hospital):
        if hospital in self.hospitals:
            return hospital.ID

    def deleteHospital(self, hospital):
        if hospital in self.hospitals:
            self.hospitals.remove(hospital)
