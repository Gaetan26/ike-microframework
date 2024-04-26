

class State:
    def __init__(self, master:object, state_name:str, toogle_state_func:object, globals_:dict):
        self.master = master
        self.state_name = state_name
        self.toogle_state = toogle_state_func
        self.page_title = self.state_name.capitalize()
        self.globals = globals_