# LinkedIn-AutoConnect
Automatically send connection requests to people in a given LinkedIn search query. This means that you can target any search query you like. Personally, I used it to connect to colleagues that I was 2nd connections with. 

###System Requirements:
* 🤟 (tested on Windows and Mac)
* 🐍 download Python 3 - I recommend the Anaconda distribution but you don't need it for this 
    * [Anaconda for Mac](https://repo.anaconda.com/archive/Anaconda3-2019.10-MacOSX-x86_64.pkg)
    * [Anaconda for Windows](https://repo.anaconda.com/archive/Anaconda3-2019.10-Windows-x86_64.exe)
    * [Anaconda for Linux](https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh)
* 📡 download ChromeDriver and drop it into your Python bin directory or another directory that Python can find
    * [ChromeDriver binary](https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/)
    * my Python bin directory: ```Users/rfrigo/anaconda3/bin```

```Auth.py``` will handle login to LinkedIn. Alternatively, you can just run ```AutoConnect.py``` if you're already logged in. Just paste in your search query. ;)
The main reason they're separate is because if your login is flagged as suspicious, LinkedIn will send you a code to verify by email, so that way you can run ```Auth.py```, input the code, and then run ```AutoConnect.py```. ```Auth.py``` is pretty pointless if you don't hardcode your email and password or use command line args, shown below.

```python Auth.py --noprompt mylinkedinemail@domain.com mylinkedinpassword123```

```python AutoConnect.py --noprompt linked.com/yoursearchquery```

**(linux/unix only):**
if you want Auth and AutoConnect to run together, just paste both lines in a .sh file and run from the command line: ```sh file.sh```

##Possible Future Additions
(feel free to make a pull/push request)

* timing for every hour, when LinkedIn says you're making too many connections, so you don't have to rerun it
* saving current link when it finishes running so it can leave off where it started instead of having to go through hella pages of connections you already sent
