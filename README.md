# tmplot.py

One liner Plotter for when you just want to draw a little diagram.

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

[CAUTION] Please write shebang in a text editor etc, as using sed on MacOS may cause errors.

### dependencies
- python3 (>=3.9.12 tested)
    - matplotlib
    - seaborn
    - numpy
    - argparse
    - sys


<a id="anchor2"></a>
# Gallery
<a href=#plot1>
    <img src="img/plot1.png" class="galleryItem" width=200px></img>
</a>

<a href=#scatter1>
    <img src="img/scatter1.png" class="galleryItem" width=200px></img>
</a>

<a href=#hist1>
    <img src="img/hist1.png" class="galleryItem" width=200px></img>
</a>

<a href=#hist2>
    <img src="img/hist2.png" class="galleryItem" width=200px></img>
</a>

<a href=#bar1>
    <img src="img/bar1.png" class="galleryItem" width=200px></img>
</a>

<a href=#pie1>
    <img src="img/pie1.png" class="galleryItem" width=200px></img>
</a>


<a id="anchor3"></a>
# Quick start
<a id="plot1"></a>
Ex. plot1
~~~
for i in {0..100}; do echo ""; done | awk '{print rand(), rand()}' | tmplot.py plot -x - -y - --prefix plot1 --title plot1 --xlabel rand1 --ylabel rand2
~~~

<a id="scatter1"></a>
Ex.2 scatter1
~~~
for i in {0..100}; do echo ""; done | awk '{print rand(), rand()}' | tmplot.py scatter -x - -y - --prefix scatter1 --title scatter1 --xlabel rand1 --ylabel rand2 --xline "[0.2,0.6]" --yline "[0.2,0.8]"
~~~

<a id="hist1"></a>
Ex. hist1
~~~
cat data/grauss.0.1.10k.txt | tmplot.py hist -x - -y - -p hist1 -t t=p --label gauss.0.1.10k --hist-peak-highlight
~~~

<a id="hist2"></a>
Ex. hist2
~~~
for i in {0..100}; do echo ""; done | awk '{print rand()}' | tmplot.py hist -x - -y - --hist-cumulative -p hist2 -t t=p --seaborn-off --label rand --hist-bins 15
~~~

<a id="bar1"></a>
Ex. bar1
~~~
cat data/tag1.txt | tmplot.py bar -x - -y - --xlabel datas -p bar1 -t bar1 --ylabel percent --yline "[0.5]" --yline-color purple --xtype str --color green
~~~

<a id="pie1"></a>
Ex. pie1
~~~
cat data/tag1.txt | python3 tmplot.py pie -x - -y - -xt str --prefix pie1 -t t=p
~~~


<a id="anchor4"></a>
## Mode & Options
~~~
usage: tmplot.py [-h] -x XDATA -y YDATA [-s SPLIT] [-xt {float,int,str}] [-yt {float,int,str}] [-c COLOR] [-l LABEL] [--xlim XLIM] [--ylim YLIM] [--xlog] [--ylog] [--xline XLINE] [--yline YLINE]
                 [--xline-color XLINE_COLOR] [--yline-color YLINE_COLOR] [--xnorm] [--ynorm] [--xstand] [--ystand] [-p PREFIX] [-xl XLABEL] [-yl YLABEL] [-t TITLE] [-j] [--transparent] [--seaborn-off]
                 [--grid-off] [--hist-bins-width HIST_BINS_WIDTH] [--hist-bins HIST_BINS] [--hist-cumulative] [--hist-cumulative-color HIST_CUMULATIVE_COLOR] [--hist-peak-highlight]
                 [--hist-peak-highlight-color HIST_PEAK_HIGHLIGHT_COLOR] [--bar-width BAR_WIDTH]
                 {plot,scatter,hist,bar,violin,box,pie,empty}

Plotter that supports file and pipe input for quick description

positional arguments:
  {plot,scatter,hist,bar,violin,box,pie,empty}
                        choose plot mode
                        plot    : connect the dots and draw them.
                        scatter : NOT connect the dots and draw them.
                        hist    : draw histogram
                        bar     : draw bar graph
                        violin  : draw violin plot
                        box     : draw a box-and-whisker diagram
                        pie     : draw pie charti
                        empty   : draw NOTHING

optional arguments:
  -h, --help            show this help message and exit
  -x XDATA, --xdata XDATA
                        x_data of 2D-plot.
                        Supports FILE name or PIPE input. For pipe input, use "-x - "
  -y YDATA, --ydata YDATA
                        y_data of 2D-plot.
                        Supports FILE name or PIPE input. For pipe input, use "-y - "
  -s SPLIT, --split SPLIT
                        Target character for delimiter [default: <SPACE>]
  -xt {float,int,str}, --xtype {float,int,str}
                        Input x data type specification [default: float]
  -yt {float,int,str}, --ytype {float,int,str}
                        Input y data type specification [default: float]
  -c COLOR, --color COLOR
                        Main plotting color [default: cornflowerblue]
                        (See the official matplotlib site for color choices. https://matplotlib.org/stable/gallery/color/named_colors.html)
  -l LABEL, --label LABEL
                        Main plotting label [default: <None>]
  --xlim XLIM           plotting range. input data type must be int or float (Ex. --xlim "[10:100]") [default: not set]
  --ylim YLIM           plotting range. input data type must be int or float (Ex. --ylim "[10:100]") [default: not set]
  --xlog                Flag whether the x-axis should be log scaled
  --ylog                Flag whether the y-axis should be log scaled
  --xline XLINE         Draw an additional perpendicular lines to the x-axis (Ex. --xline 10) [default: not set]
  --yline YLINE         Draw an Additional perpendicular lines to the y-axis (Ex. --yline 10) [default: not set]
  --xline-color XLINE_COLOR
                        Color of additional perpendicular lines to the x-axis [default: orange]
                        (See the official matplotlib site for color choices. https://matplotlib.org/stable/gallery/color/named_colors.html)
  --yline-color YLINE_COLOR
                        Color of additional perpendicular lines to the y-axis [default: tomato]
                        (See the official matplotlib site for color choices. https://matplotlib.org/stable/gallery/color/named_colors.html)
  --xnorm               Flag whether inputed x data normalizationIf the data type is str, an error will occur
  --ynorm               Flag whether inputed y data normalizationIf the data type is str, an error will occur
  --xstand              Flag whether inputed x data standardizationIf the data type is str, an error will occur
  --ystand              Flag whether inputed y data standardizationIf the data type is str, an error will occur
  -p PREFIX, --prefix PREFIX
                        output picture file prefix. [default: out]
  -xl XLABEL, --xlabel XLABEL
                        output picture xlabel. [default: x] [default(pie): " "]
  -yl YLABEL, --ylabel YLABEL
                        output picture ylabel. [default: y] [default(hist): Frequency] [default(pie): " "]
  -t TITLE, --title TITLE
                        output picture title. [default: <NONE>] If you use "--title t=p", title will be the same as prefix
  -j, --jpg             Flag whether JPG output is performed. [default: <PREFIX>.png]
  --transparent         Flag whether make the background of the output image transparent
  --seaborn-off         Flag whether seaborn theme off
  --grid-off            Flag whether turn off grid
  --hist-bins-width HIST_BINS_WIDTH
                        value of histogram bin width. (Ex. --hist-bins-width 0.7) [default: auto]
                        [CAUTION] If combined with --hist-bins, --hist-bins takes precedence.
  --hist-bins HIST_BINS
                        number of bins in hist mode. (Ex. --hist-bins 60) [default: auto]
                        [CAUTION] If combined with --hist-bins-width, --hist-bins takes precedence.
  --hist-cumulative     Flag whether plot cumulative ratio with histogram
  --hist-cumulative-color HIST_CUMULATIVE_COLOR
                        Color of hitogram cumulative plot [default: green]
                        (See the official matplotlib site for color choices. https://matplotlib.org/stable/gallery/color/named_colors.html)
  --hist-peak-highlight
                        Flag whether the major peaks of the histogram are drawn as vertical lines
  --hist-peak-highlight-color HIST_PEAK_HIGHLIGHT_COLOR
                        Color of histogram highlight bar [default: red]
                        (See the official matplotlib site for color choices. https://matplotlib.org/stable/gallery/color/named_colors.html)
  --bar-width BAR_WIDTH
                        Value of bar width [default: 0.8]
~~~


<a id="anchor5"></a>
## Support function & Usage

|                                                   | Support / Unsupport | Usage example                                                                     |
| ------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------- |
| FILE input                                        | O                   | tmplot.py -x test1.txt -y test2.txt                                               |
| PIPE input                                        | O                   | cat test.txt &#124; tmplot.py plot -x - -y -                                      |
| PNG output                                        | O                   | default output                                                                    |
| JPG output                                        | O                   | cat test.txt &#124; tmplot.py plot -x - -y - --jpg                                |
| delimiter characters in PIPE input                | O                   | -s / --split  "\t"                                                                |
| Specify input data type in xdata, ydata           | O                   | --xtype int, --xtype float, --xtype str, (ydata is the same way)                  |
| set picture title                                 | O                   | --title title                                                                     |
| set picture xlabel, ylabel                        | O                   | --xlabel xlabel, (ylabel is the same way)                                         |
| set output picture prefix                         | O                   | --prefix prefix                                                                   |
| Plot with connecting the dots                     | O                   | cat test.txt &#124; tmplot.py plot -x - -y -                                      |
| Plot without connecting the dots                  | O                   | cat test.txt &#124; tmplot.py scatter -x - -y -                                   |
| Draw a histogram                                  | O                   | cat test.txt &#124; tmplot.py hist -x - -y -                                      |
| Draw a barplot                                    | O                   | cat test.txt &#124; tmplot.py bar -x - -y -                                       |
| Draw a pie chart                                  | O                   | cat test.txt &#124; tmplot.py pie -x - -y -                                       |
| Draw a bar chart                                  | O                   | cat test.txt &#124; tmplot.py bar -x - -y -                                       |
| Draw a violin plot                                | X(O in the future)  |                                                                                   |
| Draw a box plot                                   | X(O in the future)  |                                                                                   |
| Draw NOTHING                                      | O                   | cat test.txt &#124; tmploy.py empy -x - -y -                                      |
| Draw additional perpendicular line to the axis    | O                   | --xline "[0.3,-0.1,0.5]" (yline is the same way)                                  |
| Change additional perpenddicular line to the axis | O                   | --xline-color black                                                               |
| Log scale on axis                                 | O                   | --xlog or --ylog                                                                  |
| Set grid on / off                                 | O                   | default / --grid-off                                                              |
| Set seaborn theme on / off                        | O                   | default / --seaborn-off                                                           |
| Make the background transparent                   | O                   | --transparent                                                                     |
| Label main mode drawings                          | O                   | -l / --label foo                                                                  |
| Change color of main mode drawings                | O                   | -c / --color green                                                                |
| sort input data                                   | X                   | use: sort command                                                                 |
| normalize input data                              | O                   | --xnorm, --ynorm                                                                  |
| standardize input data                            | O                   | --xstand, --ystand                                                                |
| Drawing range on x-axis, y-axis                   | O                   | --xlim "[1:10]" (ylim is the same way)                                            |
| Cut off input data at maximum and minimum values  | X                   | use: --xlim or --ylim or awk                                                      |
| Perform the same process on all input data.       | X                   | use: awk '{print $1 * 2, $2 + 10}'                                                |
| Specify the number of bins in the histogram       | O                   | --hist-bins 33                                                                    |
| Specify the width of bins in the histogram        | O                   | --hist-bins-width 0.7 (If you use with --hist-bins, --hist-bins takes precedence) |
| Draw a line through the histogram primary peak    | O                   | --hist-peak-highlight                                                             |
| Change a line through the histogram primary peak  | O                   | --hist-peak-highlight-color orange                                                |
| Draw the cumulative ratio of histograms           | O                   | --hist-cumulative                                                                 |
| Change the cumulative ratio of histograms         | O                   | --hist-cumulative-color orange                                                    |
| Change bar width                                  | O                   | --bar-width 0.4                                                                   |

<a id="anchor6"></a>
## Other tmplot
tmplot (all written in Rust) https://github.com/th2ch-g/tmplot
