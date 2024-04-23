import argparse
from pathlib import Path
import os 
import subprocess
from typing import Sequence, Final, NamedTuple


class CLI():
    CMD_PATH: str = "path"
    CMD_OUTPUT: str= "output"
    CMD_BIBLIOGRAPHY : str = "bibliography"
    args : Sequence[str] | None
    path : Path | None
    bib : str | None
    tex : str | None
    cite : bool
    output : bool | None
    output : str | None
    template : str | None = "template.html"
    filter : str | None = "tex_md.lua"
    cite : bool = True

    def __init__(self):
        parser = argparse.ArgumentParser(description="MDBook Backend that converts Latext to html with pandoc")
        parser.add_argument(f"-{CLI.CMD_PATH[0]}", f"--{CLI.CMD_PATH}", help="Use a folder directory with all source files -- TODO add functionality to specify args")
        parser.add_argument(f"-{CLI.CMD_OUTPUT[0]}", f"--{CLI.CMD_OUTPUT}", help="Using a directory will auto name the output file dir_name/dir_name.md, if a file is used the output will be to that file")
        parser.add_argument(f"-{CLI.CMD_BIBLIOGRAPHY[0]}", f"--{CLI.CMD_BIBLIOGRAPHY}", action="store_true", help="adds a the --citeproc and bibliography args")
        self.args = parser.parse_args()
        if getattr(self.args, CLI.CMD_PATH):
            self.cmd_path()
        if getattr(self.args, CLI.CMD_OUTPUT):
            self.cmd_output()
        if getattr(self.args, CLI.CMD_BIBLIOGRAPHY):
            self.cmd_bibliography()
        else:
            self.cite = False
            parser.print_help()

    def run(self):
        command = ["pandoc"]
        if self.cite:
            command += [f"--bibliography={self.bib}", "--citeproc"]

        # input file
        command += [self.tex]

        # "-s" is "standalone", "--mathjax" enables the url import (can remove i think)
        # "-f" is input format
        # "-t" is output format
        command += ["-s", "--mathjax", "-f", "latex", "-t", "html"]
        # "-o" is output path
        command += ["-o", self.output]


        command += [f"--template={self.template}"]
        command += [f"--lua-filter={self.filter}"]
        print(command)
        subprocess.call(command)
        

    def cmd_bibliography(self):
        arg : str = getattr(self.args, CLI.CMD_BIBLIOGRAPHY)
        print(arg is True)
        if arg is True or False:
            self.bib = f"{self.path}.bib"
            return
        path = Path(arg)
        if not path:
            print("This is not a directory or file path, you should use a directory")
            raise SystemExit(1)
        if not path.is_dir():
            self.bib = path
        else:
           self.bib = path.joinpath(f"{path.name}.md")


    def cmd_path(self):
        arg : str = getattr(self.args, CLI.CMD_PATH)
        path : Path = Path(arg)
        if not path:
            print("The target directory does not exist")
            raise SystemExit(1)
        if not path.is_dir():
            print("This is not a directory, you should use a directory")
            raise SystemExit(1)
        name = path.name
        self.output = name
        print(path.name)
        p = path.joinpath(name)
        self.path = p
        self.tex = f"{p}.tex"


    def cmd_output(self):
        arg : str = getattr(self.args, CLI.CMD_OUTPUT)
        path = Path(arg)
        if not path:
            print("This is not a directory or file path, you should use a directory")
            raise SystemExit(1)
        if not path.is_dir():
            self.output = path
        else:
           self.output = path.joinpath(f"{path.name}.md")
    

if __name__ == '__main__':
    cli = CLI()
    cli.run()
    



