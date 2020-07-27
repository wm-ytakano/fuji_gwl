reset
set terminal qt font ",16"
set datafile separator ","
set xdata time
set timefmt "%Y-%m-%d"
set format x "%Y"
set ylabel "水位(m)"
set xrange ["1998-01-01":"2020-01-01"]
set grid
plot "all_fix.csv" using 1:5 with lines lc rgb "#3333ff" lw 2 title "精進湖"
