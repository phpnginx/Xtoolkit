from cmd import Cmd
import os
import sys
from class_kernel import *

class CommandParser:
    def __init__(self, class_style):
        print(class_style.green("[OK] ") + class_style.yellow("Command Parser Loaded"))

    def parse(self, command):
        return command


class CommandLine(Cmd):
    def __init__(self,class_style,kernel):
        Cmd.__init__(self)
        self.doc_header = "Documented commands (type help <topic>):"
        self.misc_header = "Miscellaneous help topics:"
        self.undoc_header = "Undocumented commands:"
        self.__Style=class_style
        self.__Kernel=kernel
        self.prompt = self.__Kernel.get_name() + "@" + self.__Kernel.get_env() + "~# "
        self.__Kernel.set_name("HELLO")

    def do_change(self, line):
        print("HE")
    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'
        if arg:
            # XXX check arg syntax
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc=getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n"%str(doc))
                        return
                except AttributeError:
                    pass
                self.stdout.write("%s\n"%str(self.nohelp % (arg,)))
                return
            func()
        else:
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == 'help_':
                    help[name[5:]]=1
            names.sort()
            # There can be duplicates if routines overridden
            prevname = ''
            for name in names:
                if name[:3] == 'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd=name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)
            self.stdout.write("%s\n"%str(self.doc_leader))
            self.print_topics(self.__Style.red(self.doc_header),   cmds_doc,   15,80)
            self.print_topics(self.misc_header,  help.keys(),15,80)
            self.print_topics(self.undoc_header, cmds_undoc, 15,80)