import sys
from distutils.core import setup, Extension

pre = "py%i%i//" % sys.version_info[:2]
if sys.version_info[:2] == (2,5) and '64 bit' in sys.version:
    bufferoverflowU = ['bufferoverflowU']
else:
    bufferoverflowU = []

setup(
    name = "_curses",
    version  = "2.2",
    ext_modules = [
        Extension ('_curses',
            sources = [pre + '_cursesmodule.c'],
            define_macros = [("WINDOW_HAS_FLAGS", None)],
            libraries = ['pdcurses', 'user32', 'advapi32'] + bufferoverflowU
            ),
        Extension ('_curses_panel',
            sources = [pre + '_curses_panel.c'],
            define_macros = [("WINDOW_HAS_FLAGS", None)],
            libraries = ['pdcurses', 'user32', 'advapi32'] + bufferoverflowU
            )
        ],
    )
