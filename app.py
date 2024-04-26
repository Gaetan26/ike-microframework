from customtkinter import CTk, CTkFrame


class App(CTk):

    def __init__(self, title="New App", width=350, height=350, width_resizable=False, height_resizable=False):
        super().__init__()
        self.title(title)
        self.geometry(f"{width}x{height}")
        self.resizable(width=width_resizable, height=height_resizable)
        self.states = dict()
        self.globals = dict()

        self.MainFrame = CTkFrame(self, corner_radius=0)
        self.MainFrame.grid(column=0, row=0, sticky='nwes')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
    
    
    def add_state(self, state:object):
        self.states[state.state_name] = state


    def toggle_state(self, target_state_name):
        state = self.states.get(target_state_name)
        if state is not None:
            if state.page_title is not None:
                self.title(state.page_title)
            self.clean_screen()
            state.render()
    

    def clean_screen(self):
        for children in self.MainFrame.winfo_children():
            children.grid_forget()
            children.destroy()