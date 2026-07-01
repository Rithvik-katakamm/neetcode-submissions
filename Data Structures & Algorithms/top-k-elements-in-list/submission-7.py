class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # init
        hashy = {}
        # create a freq map 
        for num in nums: 
            hashy[num] = hashy.get(num, 0) + 1 
        # create a bucket sort list of len nums + 1
        freq_list = [[] for _ in range(len(nums) + 1)] 
        # fill up the buckets with numbers
        for number, count in hashy.items():
            freq_list[count].append(number)
        # walk the bucket list fom the back and return k numbers
        res= []
        for i in range(len(freq_list) - 1, 0, -1):
            for n in freq_list[i]:
                res.append(n)
                if len(res) == k:
                    return res
