def is_called():
    def is_returned():
        print("Hello")
    return is_returned # wywołanie


new = is_called()

# Outputs "Hello"
new()