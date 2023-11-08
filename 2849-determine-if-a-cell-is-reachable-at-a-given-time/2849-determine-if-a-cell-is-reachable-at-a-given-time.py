class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        
        if sx == fx and sy == fy and t == 1:
            return False

        farther = None
        x = abs(sx - fx)
        y = abs(sy - fy)
        if x > y:
            farther = x
        else: 
            farther = y

        if farther > t:
            return False
        else: 
            return True