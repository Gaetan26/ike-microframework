

class Model:
    
    def __init__(self, widget:object, attrs:dict, confs={}):
        self.widget = widget
        self.attrs = attrs
        self.confs = confs
        self.new_widget = None


    def __call__(self, master, attrs=None, confs=None, command=None):
        return self.new(master, attrs, confs, command)


    def new(self, master, attrs=None, confs=None, command=None) -> object:
        if attrs is not None:
            keys = list(attrs.keys())
            for key in keys:
                self.attrs[key] = attrs[key]

        if confs is not None:
            keys = list(confs.keys())
            for key in keys:
                self.confs[key] = confs[key]

        keys = list(self.attrs.keys())
        attrs_string = str()
        for key_index in range(0, len(keys)):
            key = keys[key_index]
            value = self.attrs.get(key)
            if type(value) == str:
                value = f'"{value}"'
            if key_index != (len(keys) - 1):
                attrs_string += f"{key}={value}, "
            else:
                attrs_string += f"{key}={value}"
            
        keys = list(self.confs.keys())
        confs_string = str()
        for key_index in range(0, len(keys)):
            key = keys[key_index]
            value = self.confs.get(key)
            if type(value) == str:
                value = f'"{value}"'
            if key_index != (len(keys) - 1):
                confs_string += f"{key}={value}, "
            else:
                confs_string += f"{key}={value}"

        if command is not None:
            code = f"self.new_widget = self.widget(master=_master, {attrs_string}, command=_command)"
            exec(code,{"_master":master, "self":self, "_command":command})
        else:
            code = f"self.new_widget = self.widget(master=_master, {attrs_string})"
            exec(code,{"_master":master, "self":self})

        code_ = f"self.new_widget.grid({confs_string})"
        exec(code_,{"self":self})
        
        return self.new_widget