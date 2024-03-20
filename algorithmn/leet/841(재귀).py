class Solution(object):
    visited =[]
    rooms=[[]]
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited=[False]*len(rooms)
        self.rooms = rooms
        
        self.dfs(0)
        
        if False in visited:
            return False
        return True
    
    def dfs(self,current):
        if self.visited[current]:
            return
        self.visited[current] =True
        for room in self.rooms[current]:
            if self.visited[room]:
                continue
            
            self.dfs(room)
    
    
    
s=Solution()
s.canVisitAllRooms([[1],[2],[3],[]])