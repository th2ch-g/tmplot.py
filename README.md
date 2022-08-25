# tmplot.py

Plotter for when you just want to draw a little diagram.

1. [Install tmplo.py](#anchor1)
1. [Gallery](#anchor2)
1. [Quick start](#anchor3)
1. [Mode & Options](#anchor4)
1. [Support function & Usage](#anchor5)
1. [Other tmplot](#anchor6)


<a id="anchor1"></a>
## Install tmplot.py
~~~
git clone https://github.com/th2ch-g/tmplot.py.git && \
cd tmplot.py && \
sed -e "1i#\!$(which python3)" -i tmplot.py
~~~


<a id="anchor2"></a>
# Gallery



<a id="anchor3"></a>
# Quick start



<a id="anchor4"></a>
## Mode & Options
~~~
~~~


<a id="anchor5"></a>
## Support function & Usage
|                                  | Supports / Unsupports  | Usage example                                      |
| -------------------------------- | ---------------------- | -------------------------------------------------- |
| FILE input                       | O                      | tmplot.py -x test1.txt -y test2.txt                |
| PIPE input                       | O                      | cat test.txt &#124; tmplot.py plot -x - -y -       |
| PNG output                       | O                      | default output                                     |
| JPG output                       | O                      | cat test.txt &#124; tmplot.py plot -x - -y - --jpg |
| set picture title                | O                      | --title <TITLE>                                    |
| set picture xlabel               | O                      | --xlabel <XLABEL>                                  |
| set picture ylabel               | O                      | --ylabel <YLABEL>                                  |
| set output picture prefix        | O                      | --prefix <PREFIX>                                  |
| Plot with connecting the dots    | O                      | cat test.txt &#124; tmplot.py plot -x - -y -       |
| Plot without connecting the dots | O                      | cat test.txt &#124; tmplot.py scatter -x - -y -    |
| Draw a histogram                 | O                      | cat test.txt &#124; tmplot.py hist -x - -y -       |
| Draw a barplot                   | X( O int the feature ) |                                                    |
| sort inputed data                | X                      | use: sort command                                  |
| normalize inputed data           | O                      | --xnorm, --ynorm                                   |
| standardize inputed data         | O                      | --xstand, --ystand                                 |



<a id="anchor6"></a>
## Other tmplot
tmplot (all written in Rust) https://github.com/th2ch-g/tmplot


