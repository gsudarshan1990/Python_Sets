class Flight:
    """This class is used for the description about the features of the flight"""
    def __init__(self, number, origin, destination, num_passengers, total_weight, pilot, crew):
        """
        This is used for the initializing the instance variables
        :param number: Provides the flight number
        :param origin: Provides the origin of the flight
        :param destination: Provides the destination of the flight
        :param num_passengers: Provides the total number of passengers needs to be carried
        :param total_weight: provides the total_weight to be carried
        :param pilot: provides the name of the pilot
        :param crew: provides the crew of the pilot
        """
        self.number = number
        self.origin = origin
        self.destination = destination
        self.num_passengers = num_passengers
        self._total_weight = total_weight
        self._pilot = pilot
        self._crew = crew

    @property
    def total_weight(self):
        """This is the property for the weight"""
        return self._total_weight

    @total_weight.setter
    def total_weight(self, weight):
        if weight > 0 and isinstance(weight, float):
            self._total_weight = weight

    @property
    def pilot(self):
        """This is the property for the pilot"""
        return self._pilot

    @pilot.setter
    def pilot(self, new_pilot):
        self._pilot = new_pilot

    @property
    def crew(self):
        """This is the property for the crew"""
        return self._crew

    @crew.setter
    def crew(self, new_crew):
        self._crew = new_crew

    def display_flight_data(self):
        """
        This is used for returning the details related to the flight
        :return: Nothing
        """
        print("== Flight ==")
        print("Number:", self.number)
        print("Number of Passengers:", self.num_passengers)
        print("Weight:", self.weight)
        print("Pilot:", self._pilot)
        print("Crew:", self._crew)