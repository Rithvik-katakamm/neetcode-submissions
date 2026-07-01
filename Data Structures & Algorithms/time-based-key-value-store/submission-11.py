class TimeMap:

    def __init__(self):
        self.hashy = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # set the key and value pairs. 
        if key in self.hashy:
            self.hashy[key].append((value, timestamp))
        else:
            self.hashy[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # retrive the nums that are being asked for 
        
        # check if the key has no values
        if key not in self.hashy:
            return ""  
        # init the left qnd the right pointe 
        left = 0 
        right = len(self.hashy[key]) - 1 
        # while left is less or equal to right 
        while left <= right:
            # calc mid 
            mid = (left + right) // 2
            # check if mid is target 
            if self.hashy[key][mid][1] == timestamp:
                return self.hashy[key][mid][0]
            # check if mid is less than timestamp
            elif self.hashy[key][mid][1] < timestamp:
                left = mid + 1 
            # if not mid is greater than timestamp 
            else:
                right = mid - 1 
        # check if right is -1 (multiple values clause)
        if right == -1:
            # return empty
            return "" 
        # else 
        else:
            # return right
            return self.hashy[key][right][0]


        
