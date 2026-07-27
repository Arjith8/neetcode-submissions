class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        track_s1, track_s2 = {}, {}
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            track_s1[s1[i]] = track_s1.get(s1[i], 0) + 1
        
        complete = len(track_s1)
        for i in range(len(s1)):
            if s2[i] in track_s1:
                track_s1[s2[i]] -= 1
                if track_s1[s2[i]] == 0:
                    complete -= 1
                    if complete == 0:
                        return True
        left = 0
        for i in range(len(s1), len(s2)):
            if s2[left] in track_s1:
                if track_s1[s2[left]] == 0:
                    complete += 1
                track_s1[s2[left]] += 1

            if s2[i] in track_s1:
                track_s1[s2[i]] -= 1
                if track_s1[s2[i]] == 0:
                    complete -= 1
                if complete == 0:
                    print(s2[i])
                    return True
            

            left += 1
        
        return False



            

        