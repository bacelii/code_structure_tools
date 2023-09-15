"""
When overloading the __getattr__ method this could cause infinite recursion when used with copy, deepcopy

Why? Because when deepcopy starts making a new
object it doesn't at first run through the init
-> so if your __getattr__ function relies on 
any attributes set in the init, will try to access them, and then end up calling the __getattr__ function again and cause infinite 
recursion

Solution:

def __getattr__(self,name):
    if name[:2] == "__":
        raise AttributeError(name)
"""