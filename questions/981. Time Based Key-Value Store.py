class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        l, r = 0, len(self.map[key]) - 1

        res, values = "", self.map[key]

        while l <= r:

            m = (l + r)//2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1


            else:
                r = m - 1


        return res




        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
