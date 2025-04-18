import pytest
from src.main import LogBook
from src.main import log_call

def test_add_and_get_logs():
    """ tests adding and retrieving logs from LogBook """
    #create a class instance
    logs = LogBook()
    #test add log
    logs.add_log("foo")
    logs.add_log("")
    #test get log
    assert logs.get_logs() == ["foo",""]

def test_clear_logs():
    """ tests that logs are cleared correctly """
    logs = LogBook()
    logs.add_log("bar")
    logs.clear()
    assert logs.get_logs() == []

#test decorated functions correctly log their name
def test_name_logging():
    """ tests if decorated functions correctly log their name """
    logs = LogBook()
    
    @log_call(logs)
    def greet(name: str) -> str:
        """ this function greets the user"""
        return f"Hello, {name}"
    
    result = greet("Jill")
    assert result == "Hello, Jill"
    assert logs.get_logs() == ["Called function: greet"]