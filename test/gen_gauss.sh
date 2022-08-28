echo "" | awk -v mu=$1 -v sigma=$2 -v size=$3 '{for(i=0; i<size; i++) { print mu+ sigma * sqrt(-2 * log(rand())) * cos(2 * 3.14 * rand()) } }'
