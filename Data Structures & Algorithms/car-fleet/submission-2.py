class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        
        for pos, spd in zip(position, speed):
            time = (target - pos) / spd
            cars.append((pos, spd, time))

        cars.sort(key = lambda car: car[0], reverse=True)

        for p,s,t in cars:
            if stack and t <= stack[-1]:
                pass
            else:
                stack.append(t)
            
        return len(stack)


         
