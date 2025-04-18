from functools import wraps

class LogBook:
    """ This class manages log books """
    def __init__(self):
        self.logs = [] #give me a place to accumulate messages as they come in

    def add_log(self, message: str) -> None:
        """Adds a message to the logs."""
        #what built in list method lets you track a new message unil the end?
        # must accept any string, even ""
        self.logs.append(message)

    def get_logs(self) -> list[str]:
        """Returns a copy of the current logs."""
        return self.logs.copy()

    def clear(self) -> None:
        """Clears the log history."""
        self.logs.clear()
        #after calling clear, calling get_logs should give me an empty list again

def log_call(my_logbook: LogBook) -> callable:
    """ logs the name of the function whenever it's called """
    #create inner decorator function
    def decorator(func: callable) -> callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            #log the call
            my_logbook.add_log(f"Called function: {func.__name__}")
            #forward to the real function
            return func(*args, **kwargs)
        #return the wrapped function    
        return wrapper
    return decorator
    
if __name__=="__main__":
    logs = LogBook()
    
    @log_call(logs)
    def greet(name: str) -> str:
        """ this function greets the user"""
        return f"Hello, {name}"
    
    print(greet("Jill"))
    logs.add_log("foo")
    print(logs.get_logs())
    logs.clear()
    print(logs.get_logs())