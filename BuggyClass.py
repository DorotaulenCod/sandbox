class BuggyClass:
    def do_something(self):
        result = 1 / 0  # to jest buggy, bo dzieli przez zero
        print(result)