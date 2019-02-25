# fuzzer-lts2429


<<<<<<< HEAD
For this DVWA fuzzer to work, make sure you have a 64-bit version of Python 3+, have installed pip, and created a virtual environment with pip. Using pip, install MechanicalSoup. If you don't already have it, download the xampp-portable folder that's available through Apache's website.

After ensuring that these items are downloaded, make sure that you can access pip's virtual environment while accessing the directory you'll use to store your code and enter this virtual environment--aka, make sure you're in the correct directory in your system.

Next, run the apache_start.bat and mysql_start.bat files from the xampp-portable files, and do not close out of these processes until finished navigating the DVWA site.

Finally, to use this fuzzer, run one of these lines of commands in the command prompt, depending on the task you wih the fuzzer to accomplish, after ensuring that you are in your correct directory:

--Discover Options
>fuzz.py discover [url] --common-words=common_words.txt
>fuzz.py discover [url] --custom-auth=dvwa --common-words=common_words.txt


# fuzz.py
The "main()" file so to speak, it breaks down the commands given in the command prompt, and contains the authenticate() method that directs and formats the fuzzer's actions and outputs to the console for readability.

#discover.py
Contains 5 methods: link_discovery(), page_guessing(), parse_urls(), form_parameters(), and cookies(). Each method corresponds to the requirements of the DVWA's fuzzer.

#common-words.txt
Contains a list of words (separated by newlines) that could possibly be used in a url, hidden from the initial webpage. Used in the process of guessing such hidden pages.
=======
For this DVWA fuzzer to work, make sure you have a 64-bit version of Python 3+ and have installed pip and pip's virtual environment. Using pip, install *Requests*, MechanicalSoup, and Scrapy (If using a Windows machine, manually download Twisted [here: https://www.lfd.uci.edu/~gohlke/pythonlibs/#Twisted], install Twisted with pip, and then install Scrapy with pip).

After installing those Python packages, make sure that you can access pip's virtual environment while accessing the directory you'll use to store your code and enter this virtual environment.

Next, run the apache_start.bat and mysql_start.bat files from the xampp-portable folder, and do not close out of these processes until finished navigating the DVWA site.

Finally, to use this fuzzer, run this line in the command prompt, after ensuring that you are in your correct directory:

>python fuzz.py --custom-auth=dvwa
>>>>>>> 4a1bc31eedd6e8febe5adf198fe0dd4cdea2969b

