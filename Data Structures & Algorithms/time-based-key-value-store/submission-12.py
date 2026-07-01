class TimeMap:

    def __init__(self):
        self.hashy = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hashy:
            self.hashy[key].append((value, timestamp))
        else:
            self.hashy[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        # if hashy empty
        if key not in self.hashy:
            return ''
        # cache the key value asked 
        val = self.hashy[key] # list
        # init the 2 pointers 
        left = 0 
        right = len(val) - 1 

        # while left is less than or equal to right
        while left <= right: 
            # calc mid
            mid = (left + right) // 2 
            # check if mid is timestamo
            if val[mid][1] == timestamp:
                return val[mid][0]   
            # if mid < timestamp
            elif val[mid][1] < timestamp:
                # move left right of mid 
                left = mid + 1 
            # or 
            else:
                #move the right left of mid
                right = mid - 1
        # if right is -1 
        if right == -1:
            # return nan
            return ""
        # else: 
        else:
            # return right pointer number as it would have crosed over to point at the largest timestamp_prev
            return val[right][0]

