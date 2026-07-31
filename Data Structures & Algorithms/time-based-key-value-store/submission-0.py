class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return "" 
        values = self.storage[key] 
        left, right = 0, len(values) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                result = values[mid][0] 
                left = mid + 1
            else:
                right = mid - 1
        return result         
