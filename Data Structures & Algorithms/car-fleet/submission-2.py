class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed_sorted = []
        for i in range(len(position)):
            pos_speed_sorted.append((position[i], speed[i]))
        
        pos_speed_sorted.sort(key=lambda x: x[0], reverse = True)
        num_pools = 0
        most_recent_pool_reach_time = 0
        for i in pos_speed_sorted:
            expected_time_of_arrival = (target-i[0])/i[1]
            print(expected_time_of_arrival)
            if most_recent_pool_reach_time >= expected_time_of_arrival:
                continue
            num_pools += 1
            most_recent_pool_reach_time = expected_time_of_arrival
        return num_pools
        