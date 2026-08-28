class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        current = 0  # start from time 0
        farthest = 0
        count = 0
        i = 0
        while current < time:
            while i < len(clips) and clips[i][0] <= current:
                # clips[i][0] <= current => Look at all clips that can start before or at current
                # Among them, choose the clip that reaches the farthest
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest == current:
                return -1
            # Move current to farthest and count one clip
            count += 1
            current = farthest
        return count

