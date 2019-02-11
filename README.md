# fuzzer-lts2429


For this DVWA fuzzer to work, make sure you have a 64-bit version of Python 3+ and have installed pip and pip's virtual environment. Using pip, install *Requests*, MechanicalSoup, and Scrapy (If using a Windows machine, manually download Twisted [here: https://www.lfd.uci.edu/~gohlke/pythonlibs/#Twisted], install Twisted with pip, and then install Scrapy with pip).

After installing those Python packages, make sure that you can access pip's virtual environment while accessing the directory you'll use to store your code and enter this virtual environment.

Next, run the apache_start.bat and mysql_start.bat files from the xampp-portable folder, and do not close out of these processes until finished navigating the DVWA site.

Finally, to use this fuzzer, run this line in the command prompt, after ensuring that you are in your correct directory:

>python fuzz.py --custom-auth=dvwa

