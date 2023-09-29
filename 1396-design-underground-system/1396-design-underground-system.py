class UndergroundSystem:

    def __init__(self):
        """
        you will be given checkin time for a person to a station
        you will also be given checkout time for that person where they left
        
        you will use this to calculate the average time to reach from the start to the end.
        
        when asked you will return
        
        you will have a dictionary for the travel times which will store time travel and number of travels
        
        
        you will also have a check in dict and when checkout is called: remove from the dict
        
        and use that to calculate the time from one station to the other.
        """
        self.checkin = defaultdict(tuple)
        self.travel = defaultdict(lambda: defaultdict(int))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.checkin.pop(id)
        self.travel[(checkin_station, stationName)]["total_time"] += t - checkin_time
        self.travel[(checkin_station, stationName)]["frequency"] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travel[(startStation, endStation)]["total_time"] / self.travel[(startStation, endStation)]["frequency"]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)