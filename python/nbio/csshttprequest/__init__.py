__license__ = "Apache 2.0"
__copyright__ = "Copyright 2008 nb.io"
__author__ = "Randy Reddig - ydnar@nb.io"


import urllib


PREFIX = "about:"
LENGTH = 2000 - len(PREFIX) # Internet Explorer 2KB URI limit


def encode(string):
    quoted = urllib.quote(string)
    out = ""
    for i in range(0, len(quoted), LENGTH):
        out += "@import url(" + PREFIX + quoted[i:i+LENGTH] + ");\n"
    return out