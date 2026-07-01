class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Understand:
        # input, tasks -> list[n], n -> int
        # 1 cycle = 1 completed task
        # same lettered tasks must occur after after n steps
        # output: min number of cycles to get through the list

        # Approuch: 
        # lets first count the freq of each letter in the list 
        # then lets take the highest freq letter and run it first 
        # we'll then track when it can come back to the schedular to get compleeted 
        # we'll keep doing this until we dont have any tasks left to process

        # Code:
        # init a hashmap for freq and a time variable for tracking cycle count also a queue why not
        hashy = {}
        time = 0 
        cooldown = deque()
        # build the freq map 
        for i in tasks:
            if i in hashy:
                hashy[i] += 1 
            else:
                hashy[i] = 1
        # extract the values and push them into a max heap
        heap = [-number for number in hashy.values()]
        heapq.heapify(heap) 
        # loop through the heap
        while heap or cooldown:
            time += 1  
            # does the heap have any numbers in it?
            if heap: 
                # pop off the top, decrement by 1
                number = heapq.heappop(heap) + 1
                # check if the number is 0 or not
                if number != 0: 
                    # push into queue with time + n
                    cooldown.append((number, time + n))
            # does the queue have any numbers in it that match the current time stamp?
            if cooldown and cooldown[0][1] == time:
                # push the freq back into the heap
                heapq.heappush(heap, cooldown[0][0])
                # pop it off the queue 
                cooldown.popleft()

        # return time 
        return time 

        # Complexity: 
