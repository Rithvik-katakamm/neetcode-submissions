class TimeMap:
    """ This class will define the blue print for a time based key-value data structure
    it will be able to store multiple values and time stamps (they must be a pair) per key and the class should also 
    return the corresponding value when user passes in the time stamp"""

    def __init__(self):
        self.hashy = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashy:
            self.hashy[key].append((value, timestamp))
        else:
            self.hashy[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # aeema like the time is auto sorted 
        # we could cache the key;s list to make our lives easier but why waste the space
        # init the pointers
        left = 0 
        if key not in self.hashy:
            return ""
        right = len(self.hashy[key]) - 1
        # while the left poitner is less than right poiter
        while left <= right:
            # cal mid
            mid =  (left + right) // 2 
            # if mid is target
            if self.hashy[key][mid][1] == timestamp: 
                # return the value associated with the timestamp
                return self.hashy[key][mid][0]
            # if mid < target
            if self.hashy[key][mid][1] < timestamp:
                # move left pointer
                left = mid + 1 
            # if mid > target
            else:
                # move right pointer
                right = mid - 1 
        # return the lowest value ;eft of the target. 
        if right < 0:
            return ''
        else:
            return self.hashy[key][right][0]
        
