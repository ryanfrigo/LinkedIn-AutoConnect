# LinkedIn-AutoConnect
Automatically send connection requests to people in a given LinkedIn search query. This means that you can target any search query you like. Personally, I used it to connect to colleagues that I was 2nd connections with. 

### System Requirements:
* 🤟 (tested on Windows and Mac)
* 🐍 download Python 3 - I recommend the Anaconda distribution but you don't need it for this 
    * [Anaconda for Mac](https://repo.anaconda.com/archive/Anaconda3-2019.10-MacOSX-x86_64.pkg)
    * [Anaconda for Windows](https://repo.anaconda.com/archive/Anaconda3-2019.10-Windows-x86_64.exe)
    * [Anaconda for Linux](https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh)
* 📡 download ChromeDriver and drop it into your Python bin directory or another directory that Python can find
    * [ChromeDriver binary](https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/)
    * my Python bin directory: ```Users/rfrigo/anaconda3/bin```

First time you run it, your login may be flagged as suspicious, LinkedIn will send you a code to verify by email, next time it should work fine.

For running it without prompts:
```python AutoConnect.py --noprompt mylinkedinemail@domain.com mylinkedinpassword123 linked.com/yoursearchquery```

I recommend running the Jupyter Notebook file (.ipynb) becuase you'll be able to authenticate separately and just keep running the AutoConnect part. You can just hardcode in your username, password and search query link.

Also, it should crash when LinkedIn blocks you from making connections (temporarily). This goes away in 5-10 minutes, and is why I recommend running in a Jupyter Notebook so you don't have to open a new ChromeDriver and re-auth.

### Possible Future Additions
(feel free to make a pull/merge request)

* timing for every hour, when LinkedIn says you're making too many connections, so you don't have to rerun it
* saving current link when it finishes running so it can leave off where it started instead of having to go through hella pages of connections you already sent
