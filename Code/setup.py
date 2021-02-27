"""
    Name:       TikTok Search Engine
    Author:     Guilherme Anacleto Ferreira
    Email:      guilhermeanacleto@hotmail.com
    Modified:   2021-02-23
    A file created to turn tiktok program in executable file.
"""

import sys
from cx_Freeze import setup, Executable
import TikTokApi
import playwright
import pandas

#This variable can remove or input console,
#but when console is off the program has a bug to execute,
#i didn't discovered why, so.. Im accepting suggestions.
base = None

#Here we have some configurations about the executable file
executables = [Executable(
    #archive main.py.
    script='main.py',
    #Variable base.
    base=base,
    #Icon archive.
    icon='iconeico.ico'
)
]

#Here we have some options of how executable will work.
buildOptions = dict(
    #Packages you want include.
    packages=[],
    #The librarys that you want include too.
    includes=["TikTokApi","playwright","pandas"],
    #Any folder necessary to program works well.
    include_files=["iconeico.ico"],
    #Here you can remove any file of the executable
    excludes=[]
)

#Finally some info tips, all information here will apperar 
#in propertys of the archive
setup(
    #Name of the program
    name="TikTok Scrapper",
    #Program Version
    version="1.0",
    #Program description
    description="A program that can scrapp tiktok information.",
    #Here we can specify the options that we create before.
    options=dict(build_exe=buildOptions),
    executables=executables)

#To create an executable with thios archiuve you have to run "python setup.py build"
