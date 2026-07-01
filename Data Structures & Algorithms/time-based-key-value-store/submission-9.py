class TimeMap:
    """ This class will define the blue print for a time based key-value data structure
    it will be able to store multiple values and time stamps (they must be a pair) per key and the class should also 
    return the corresponding value when user passes in the time stamp"""

    def __init__(self):
        self.hashy = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # populate the hashmap
        if key in self.hashy:
            self.hashy[key].append((value, timestamp)) 
        else:
            self.hashy[key] = [(value, timestamp)]
        
    def get(self, key: str, timestamp: int) -> str:
        # aeema like the time is auto sorted 

        # check if key is not in hashy return ""
        if key not in self.hashy:
            return ""
        # init the pointer
        left = 0 
        right = len(self.hashy[key]) - 1 
        # while left < right
        while left <= right:
            # calc mid
            mid = (left + right) // 2
            # example: hashy = {'rithvik': [(happy, 2), (sad, 4)]}
            # if mid is target 
            if self.hashy[key][mid][1] == timestamp:
                # return values
                return self.hashy[key][mid][0]
            # if mid is less than timestamp
            if self.hashy[key][mid][1] < timestamp: 
                # move left pointer
                left = mid + 1 
            # else if mid is greater than timestamp
            else:
                # move right pointer
                right = mid - 1
        # return right index
        if right == -1:
            return ""
        else:
            return self.hashy[key][right][0]
 