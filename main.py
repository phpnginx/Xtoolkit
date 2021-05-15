from class_kernel import *
from class_command_line import *
from class_style import *
''' def commandline():
    while True:
        try:
            print(Kernel.get_name() + "@" + Kernel.get_env() + "~# ", end='')
            command = input("")
            # Callback.command(command)
            if not command.isspace() and command != "":
                Parser.parse(command)
        except KeyboardInterrupt:
            print("\n\nExiting...")
            return "exit"
'''

if __name__ == '__main__':
    Style=Style()
    Kernel=XtoolkitKernel(Style)
    Parser=CommandParser(Style)
    commandline = CommandLine(Style,Kernel)
    commandline.cmdloop()

    print(Kernel.get_name())