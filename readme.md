# Read Python3 Source File With Correct Encoding

according to <https://www.python.org/dev/peps/pep-0263/>,
python3 source file encoding are default to be `utf-8`.

But `open()`'s encoding will be `gbk` on windows,
So don't use `open` without encoding to read a python3 source file. 
