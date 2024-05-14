class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_and_points = []
        
        for point in points:
            dist_and_points.append((pow(pow(point[0], 2) + pow(point[1], 2) ,0.5), point))
            
        dist_and_points.sort(key=lambda x:x[0])
        
        return [dist_and_points[_][1] for _ in range(k)]