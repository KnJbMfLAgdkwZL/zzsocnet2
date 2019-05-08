class controller:
    def __init__(self):
        name = self.getName()
        print(f'Constructor {name}')

    def __del__(self):
        name = self.getName()
        print(f'Destructor {name}')

    def getName(self):
        return self.__class__.__name__

