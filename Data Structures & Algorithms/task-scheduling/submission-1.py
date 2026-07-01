class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            # Understand: 
            # input = tasks -> list[char], n -> int
            # so each 'cycle' can complete one task in any order 
            # if the task is the same it cannot occur until n cycles have passed 
            # output - min number of cycles to complete tasks -> int 

            # Approuch:
            # lets use a hash map to get the freq count per letter
            # lets push these counts into the heap 
            # lets them pop the top element of the heap if its there 
            # lets add it to a quene along with when it can come back after n steps 
            # lets always check the queue to see if anything can come back to the heap 
            # lets do this until both are empty 
            # return how many steps this took 

            # Code:
            # init our states
            hashy = {}
            time = 0 
            cooldown = deque()
            # makea hash map with a freq count
            for char in tasks: 
                if char in hashy:
                    hashy[char] += 1
                else:
                    hashy[char] = 1 
            # max heap that thing (extract freq only)
            heap = [-i for i in hashy.values()]
            heapq.heapify(heap) 
            # loop through heap while heap and queue are not empty
            while heap or cooldown:
                # increament time 
                time += 1 
                # if the heap is not empty 
                if heap:
                    # pop off the top element into a variable and reduce the count by 1
                    number = heapq.heappop(heap) + 1
                    # if the popped number is not 0
                    if number != 0:
                        # push it into the queue with the time it can return
                        cooldown.append((number, time + n)) 

                # if the queue is not empty and the time in the first tuple is the current time
                if cooldown and cooldown[0][1] == time:
                        # return it to the heap 
                        heapq.heappush(heap, cooldown[0][0])
                        # remove it from the queue
                        cooldown.popleft()

            # return the step count 
            return time 


        # Complexity: 