# coding: utf-8
import os
import sys
import platform
TOOL_NAME = "AmineMode"


class Variables:
    @property
    def BASHRIC_FILE_PATH(self) -> str:
        if self.PLATFORME == "termux":
            return os.environ.get("PREFIX") + "/etc/zshrc"
        elif self.PLATFORME == "ish shell":
            return os.environ.get("HOME") + "/.zshrc"
        else:
            shell = os.environ.get('SHELL')
            if shell.endswith("bash"):
                path = "/etc/bash.bashrc"
            elif shell.endswith("zsh"):
                path = "/etc/zsh/zshrc"
                if not os.path.exists(path):
                    path = "/etc/zshrc"
            return path

    @property
    def TOOL_SHORTCUT(self) -> str:
        """AmineMode shortcut"""
        with open(os.path.join(self.REAL_TOOL_PATH, "AmineMode.shortcut"), "r") as file:
            data = file.read()
        return data

    @property
    def ACTIVATE_FILE_PATH(self) -> str:
        """To get AmineMode activate file"""
        return os.path.join(self.TOOL_INSTALL_PATH, "AmineMode/bin/activate")

    @property
    def REAL_TOOL_PATH(self) -> str:
        """To get real AmineMode path"""
        return '/'.join(os.path.abspath(__file__).split('/')[:-2])

    @property
    def TOOLS_PATH(self) -> str:
        """To get the AmineMode [AmineMode/tools/] path"""
        return os.path.join(self.REAL_TOOL_PATH, "tools")

    @property
    def TOOL_INSTALL_PATH(self) -> str:
        """To get the installation path [~/.AmineMode/]"""
        tool_path = os.path.join(os.environ['HOME'], '.AmineMode')
        if not os.path.isdir(tool_path):
            os.mkdir(tool_path)
        return tool_path

    @property
    def CONFIG_PATH(self) -> str:
        """To get the config path [~/.config/]"""
        path = os.path.join(os.environ['HOME'], '.config')
        if not os.path.isdir(path):
            os.mkdir(path)
        return path

    @property
    def PLATFORME(self) -> str:
        """To get the platform name"""
        if sys.platform in ('win32', 'cygwin'):
            return 'win'

        elif sys.platform == 'darwin':
            return 'macosx'

        elif os.environ.get('PREFIX') is not None:
            return 'termux'

        elif platform.release().endswith("ish"):
            return "ish shell"

        elif sys.platform.startswith('linux') or sys.platform.startswith('freebsd'):
            return 'linux'
        return 'unknown'

    @property
    def SHELL_COMMAND(self):
        return os.environ["SHELL"]


Variables = Variables()

if __name__ == "__main__":
    print(eval(f"Variables.{sys.argv[1]}"))
