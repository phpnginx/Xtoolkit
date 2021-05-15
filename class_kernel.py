class XtoolkitKernel:
    def __init__(self, class_style):
        self.__name = "main"
        self.__env = "main"
        self.__version = "0.2"
        print(class_style.green("[OK] ") + class_style.cyan("Kernel Started"))

    def get_name(self):
        return self.__name

    def get_env(self):
        return self.__env

    def set_name(self, arg):
        self.__name = arg

    def set_env(self, arg):
        self.__env = arg

    def get_version(self):
        return self.__version
