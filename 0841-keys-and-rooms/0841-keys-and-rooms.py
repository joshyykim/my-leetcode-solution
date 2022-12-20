class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        d = {}
        for i,li in enumerate(rooms):
            d[i] = li
        s = set(rooms[0])
        res = set(rooms[0])
        itr = 0
        for room in rooms:
            itr += len(room)
        for i in range(itr):
            if len(s) < 1:
                return False
            key = s.pop()
            s.update(d[key])
            res.update(d[key])
        return [i for i in range(len(rooms))] == list(res) or [i for i in range(1, len(rooms))] == list(res) 