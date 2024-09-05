class SingletonBase:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonBase, cls).__new__(cls)
            cls._instances[cls]._initialize(*args, **kwargs)
        return cls._instances[cls]

    def _initialize(self, *args, **kwargs):
        pass  # To be overridden by subclasses