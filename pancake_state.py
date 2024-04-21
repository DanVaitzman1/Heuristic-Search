class pancake_state:

    def __init__(self, state_str):
        self.state_str = state_str
        self.stateList = list(map(int, state_str.split(',')))

    def get_neighbors(self):
        neighborsList = []
        for i in range(2, len(self.stateList) + 1):
            flipped_part = self.stateList[-i:][::-1]
            result = self.stateList[:-i] + flipped_part
            s = pancake_state(','.join(map(str, result)))
            neighborsList.append((s, sum(self.stateList[-i:])))
        return neighborsList

    def __hash__(self):
        return hash((self.state_str,))

    def __eq__(self, other):
        return self.state_str == other.state_str

    def __str__(self):
        return f"{self.stateList}"

    def __repr__(self):
        return f"{self.stateList}"

    def get_state_str(self):
        return self.state_str

    def get_state_list(self):
        return self.stateList






