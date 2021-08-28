# khan-bot

Automatically completes multiple choice Khan Academy assignments by keeping a dictionary of answers to all the questions.

## Installation

### Linux

```
git clone https://github.com/coder-robot-king/khan-bot
pip3 install selenium
wget https://chromedriver.storage.googleapis.com/93.0.4577.15/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver_linux64 /usr/local/bin
```

### Windows



## Running

### First-time Setup

```
python3 khanbot.py --setup
```

When the browser pops up, login to Khan Academy and save your password.

### Completing Problem Sets


```
python3 khanbot.py https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-new/ab-1-3/e/one-sided-limits-from-graphs?modal=1
```

Replace the above URL with the full URL of the problem set you would like to complete.
