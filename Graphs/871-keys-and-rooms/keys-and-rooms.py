class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()                 # Remember rooms already entered
        def dfs(room):
            visited.add(room)           # Enter this room
            for key in rooms[room]:     # Look at keys inside this room
                if key not in visited:  # Do not revisit a room
                    dfs(key)            # Use the key to explore that room
        dfs(0)                          # Start with room 0
        return len(visited) == len(rooms) # Were all rooms visited?