class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next
        pos = 1

        first = -1
        last = -1
        minDistance = float('inf')
        maxDistance = -1

        while curr.next:
            next_node = curr.next

            # Check if current node is a critical point
            is_max = curr.val > prev.val and curr.val > next_node.val
            is_min = curr.val < prev.val and curr.val < next_node.val

            if is_max or is_min:
                if first == -1:
                    # First critical point
                    first = pos
                else:
                    # Distance from previous critical point
                    minDistance = min(minDistance, pos - last)

                    # Distance from first critical point
                    maxDistance = pos - first

                last = pos

            prev = curr
            curr = next_node
            pos += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [minDistance, maxDistance]