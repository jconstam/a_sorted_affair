SORT=Merge

ffmpeg \
-i output/${SORT}_1000_random.mkv \
-i output/${SORT}_1000_saw4.mkv \
-i output/${SORT}_1000_saw8.mkv \
-i output/${SORT}_1000_sin.mkv \
-i output/${SORT}_1000_sin4.mkv \
-i output/${SORT}_1000_reverse.mkv \
-i output/${SORT}_1000_saw4rev.mkv \
-i output/${SORT}_1000_saw8rev.mkv \
-i output/${SORT}_1000_sin2.mkv \
-filter_complex \
"[0:v][1:v][2:v]hstack=inputs=3[top];\
[3:v][4:v][5:v]hstack=inputs=3[middle];\
[6:v][7:v][8:v]hstack=inputs=3[bottom];\
[top][middle][bottom]vstack=inputs=3[v]" \
-map "[v]" \
output/${SORT}_1000_composite.mkv

# DATA_TYPE=sin4

# ffmpeg \
# -i output/Bubble_1000_${DATA_TYPE}.mkv \
# -i output/Comb_1000_${DATA_TYPE}.mkv \
# -i output/Gnome_1000_${DATA_TYPE}.mkv \
# -i output/Heap_1000_${DATA_TYPE}.mkv \
# -i output/Insertion_1000_${DATA_TYPE}.mkv \
# -i output/Merge_1000_${DATA_TYPE}.mkv \
# -i output/Pancake_1000_${DATA_TYPE}.mkv \
# -i output/Quick_1000_${DATA_TYPE}.mkv \
# -i output/Radix_1000_${DATA_TYPE}.mkv \
# -filter_complex \
# "[0:v][1:v][2:v]hstack=inputs=3[top];\
# [3:v][4:v][5:v]hstack=inputs=3[middle];\
# [6:v][7:v][8:v]hstack=inputs=3[bottom];\
# [top][middle][bottom]vstack=inputs=3[v]" \
# -map "[v]" \
# output/${DATA_TYPE}_1000_composite.mkv
