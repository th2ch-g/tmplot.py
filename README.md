# tmplot.py
![last-commit](https://img.shields.io/github/last-commit/th2ch-g/tmplot.py)
![license](https://img.shields.io/github/license/th2ch-g/tmplot.py)
![language](https://img.shields.io/github/languages/top/th2ch-g/tmplot.py)
![repo-size](https://img.shields.io/github/repo-size/th2ch-g/tmplot.py)
![stars](https://img.shields.io/github/stars/th2ch-g/tmplot.py)

One liner Plotter for when you just want to draw a little diagram.


## Install
~~~shell
conda create -n plot "python>=3.7" -y
pip install "git+https://github.com/th2ch-g/tmplot.py.git"
tmplot --version
~~~

## Update
~~~shell
pip install "git+https://github.com/th2ch-g/tmplot.py.git" -U
~~~

## Quick start
### plot mode
~~~shell
$ head -n 5 sample.txt
1 24
2 26
3 29
4 31
5 32
$ cat sample.txt | tmplot plot -f -
~~~

### scatter mode
- Same as plot mode


### hist mode
~~~shell

$ head -n 5 sample.txt | awk '{print $2}'
24
26
29
31
32
$ cat sample.txt | awk '{print $2}' | tmplot hist -f -
~~~

