# tmplot.py

Plotter for when you just want to draw a little diagram.

1. [Install tmplot.py](#anchor1)
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

### dependencies
- python3 (>=3.9.12 tested)
    - matplotlib
    - seaborn
    - numpy
    - argsparse
    - sys


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

|                                                  | Support / Unsupport   | Usage example                                      |
| ------------------------------------------------ | --------------------- | -------------------------------------------------- |
| FILE input                                       | O                     | tmplot.py -x test1.txt -y test2.txt                |
| PIPE input                                       | O                     | cat test.txt &#124; tmplot.py plot -x - -y -       |
| PNG output                                       | O                     | default output                                     |
| JPG output                                       | O                     | cat test.txt &#124; tmplot.py plot -x - -y - --jpg |
| delimiter characters in PIPE input               | O                     | -s / --split  "\t"                                 |
| Specify input data type in xdata                 | X(O in the future)    |                                                    |
| Specify input data type in ydata                 | X(O in the future)    |                                                    |
| set picture title                                | O                     | --title title                                      |
| set picture xlabel                               | O                     | --xlabel xlabel                                    |
| set picture ylabel                               | O                     | --ylabel ylabel                                    |
| set output picture prefix                        | O                     | --prefix prefix                                    |
| Plot with connecting the dots                    | O                     | cat test.txt &#124; tmplot.py plot -x - -y -       |
| Plot without connecting the dots                 | O                     | cat test.txt &#124; tmplot.py scatter -x - -y -    |
| Draw a histogram                                 | O                     | cat test.txt &#124; tmplot.py hist -x - -y -       |
| Draw a barplot                                   | X( O in the feature ) |                                                    |
| sort input data                                  | X                     | use: sort command                                  |
| normalize input data                             | O                     | --xnorm, --ynorm                                   |
| standardize input data                           | O                     | --xstand, --ystand                                 |
| Drawing range on x-axis                          | O                     | --xlim [1:10]                                      |
| Drawing range on y-axis                          | O                     | --ylim [1:10]                                      |
| Cut off input data at maximum and minimum values | X                     | use: --xlim or --ylim                              |
| Perform the same process on all input data.      | X                     | use: awk '{print $1 * 2, $2 + 10}'                 |
|                                                  |                       |                                                    |


<a id="anchor6"></a>
## Other tmplot
tmplot (all written in Rust) https://github.com/th2ch-g/tmplot


