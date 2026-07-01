class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # understand
        # input: target -> int, position -> list, speed -> list
        # where target is the destination of each car (literal number)
        # position[i] is where the cars start relative to the 'start'
        # speed[i] is the speed of the car at ith position 
        # distance = speed x time 
        # when any 2 cars meet before the target they become a 'fleet', esaentially meaning they are counted as 1 at the finish line or target
        # return the number of car fleets that reach the target 

        # approuch 
        # zip the position and the speend, sort
        # go through the list in xrevese order since we are asking the question 
        # what depends on what? (stack)
        # then calculate distance remaining, time 
        # push a slower time into the stack always 
        # return the ler of stack 

        # code 
        # init stack 
        stack = []
        # sort the list
        physics = sorted(zip(position, speed))
        # loop through sorted list in reverse order
        for pos,spd in reversed(physics): 
            # calculate distance remaining and time
            dist = target - pos; time = dist/spd 
            # if the stack is empty then push time in there
            if not stack:
                stack.append(time)
            # if time is greater than the top stack, push
            elif time > stack[-1]:
                stack.append(time) 
        # return len of stack 
        return len(stack)