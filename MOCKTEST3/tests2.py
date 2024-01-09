class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        self.value += 1

    def __str__(self):
        return f"Counter value: {self.value}"

# Creating an instance of Counter
counter = Counter(5)

# Incrementing the counter
counter.increment()

# Printing the counter, which will use the __str__ method
#counter_str = str(counter)  # using str() to explicitly call __str__



print(type(counter.__str__()))
