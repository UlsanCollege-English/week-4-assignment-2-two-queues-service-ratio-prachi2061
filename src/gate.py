from collections import deque

class Gate:
    def __init__(self):
        self._pattern = ["fastpass", "regular", "regular", "regular"]
        self._idx = 0
        self._fast = deque()
        self._reg = deque()

    def arrive(self, line, person_id):
        if line == "fastpass":
            self._fast.append(person_id)
        elif line == "regular":
            self._reg.append(person_id)
        else:
            raise ValueError("Unknown line type")

    def serve(self):
        if not self._fast and not self._reg:
            raise IndexError("Both lines are empty")

        while True:
            line_to_serve = self._pattern[self._idx]

            if line_to_serve == "fastpass" and self._fast:
                person = self._fast.popleft()
                self._idx = (self._idx + 1) % len(self._pattern)
                return person
            elif line_to_serve == "regular" and self._reg:
                person = self._reg.popleft()
                self._idx = (self._idx + 1) % len(self._pattern)
                return person
            else:
                self._idx = (self._idx + 1) % len(self._pattern)

    def peek_next_line(self):
        temp_idx = self._idx
        
        for _ in range(len(self._pattern)):
            line = self._pattern[temp_idx]
            if line == "fastpass" and self._fast:
                return "fastpass"
            if line == "regular" and self._reg:
                return "regular"
            temp_idx = (temp_idx + 1) % len(self._pattern)
        
        return None
