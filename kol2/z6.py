def print_msg(msg):
    # This is the outer enclosing function

    def printer():
        # This is the nested function
        print(msg)
    #return printer# zwrocenie obiektu funkcji ktory trzeba wywolac
    printer() # po prostu wywolanie funkcji

# We execute the function
# Output: Hello
x=print_msg("Hello") 

print("--------------------------")
def is_called():
    def is_returned():
        print("Hello")
    return is_returned # wywołanie

new = is_called() # wywoałanie funkcji czyli zwraca obiekt funkcji ktory tez trzeba wywolac
new()# wywołanie funkcji zwroconej z funkcji podstawowej