
class Storage:
    def __init__(self,path:str):
        self.path = path
        self.file = None
    def open(self):
        if self.file is not None:
            raise RuntimeError("Storage is already open")
        self.file = open(self.path,"a+b")
    def is_open(self)->bool:
        return self.file is not None
    

    