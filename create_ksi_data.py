'''
We get the Killed and Seriously Injured (KSI) data from https://www.nyc.gov/html/dot/html/bicyclists/bikestats.shtml
'''

import pandas as pd
import numpy as np

from utils import unify_into_df

#BM is Bicyclist-Motorist
table14_Manhattan_BM = "Manhattan 1 73 74 0 0 0 \
Manhattan 5 84 84 0 1 0 \
Manhattan 6 53 54 0 0 0 \
Manhattan 7 50 49 1 0 0 \
Manhattan 9 85 86 0 0 0 \
Manhattan 10 41 41 0 0 0 \
Manhattan 13 129 129 0 1 0 \
Manhattan 14 95 95 0 2 0 \
Manhattan 17 62 62 0 0 0 \
Manhattan 18 76 76 0 0 0 \
Manhattan 19 93 93 0 1 0 \
Manhattan 20 40 40 0 0 0 \
Manhattan 22 7 7 0 0 0 \
Manhattan 23 24 22 2 0 0 \
Manhattan 24 47 46 1 0 0 \
Manhattan 25 26 26 0 1 0 \
Manhattan 26 36 36 0 0 0 \
Manhattan 28 50 49 1 3 0 \
Manhattan 30 21 21 0 0 0 \
Manhattan 32 24 25 0 0 0 \
Manhattan 33 24 24 0 0 0 \
Manhattan 34 48 48 0 0 0"

table14_Bronx_BM = "Bronx 40 43 43 0 1 0 \
Bronx 41 23 23 0 0 0 \
Bronx 42 31 31 0 0 0 \
Bronx 43 56 56 1 0 0 \
Bronx 44 42 42 0 0 0 \
Bronx 45 31 31 0 1 0 \
Bronx 46 34 34 0 0 0 \
Bronx 47 25 25 0 1 0 \
Bronx 48 39 39 0 0 0 \
Bronx 49 41 41 0 0 0 \
Bronx 50 19 19 0 0 0 \
Bronx 52 32 32 0 2 0"

table14_Brooklyn_BM = "Brooklyn 60 42 43 0 0 0 \
Brooklyn 61 69 72 1 1 0 \
Brooklyn 62 70 70 0 0 0 \
Brooklyn 63 32 32 0 0 0 \
Brooklyn 66 89 89 0 0 0 \
Brooklyn 67 59 61 0 2 0 \
Brooklyn 68 40 40 0 1 0 \
Brooklyn 69 19 19 0 0 0 \
Brooklyn 70 93 93 0 0 0 \
Brooklyn 71 46 45 1 0 0 \
Brooklyn 72 75 75 0 0 0 \
Brooklyn 73 31 30 1 0 0 \
Brooklyn 75 79 83 0 1 0 \
Brooklyn 76 17 17 0 1 0 \
Brooklyn 77 69 69 0 0 0 \
Brooklyn 78 81 81 0 0 0 \
Brooklyn 79 86 86 0 2 0 \
Brooklyn 81 45 44 1 3 0 \
Brooklyn 83 81 81 0 3 0 \
Brooklyn 84 54 53 1 0 0 \
Brooklyn 88 83 83 0 0 0 \
Brooklyn 90 177 176 1 3 0 \
Brooklyn 94 68 69 0 2 0"

table14_Queens_BM = "Queens 100 10 10 0 0 0 \
Queens 101 17 17 0 1 0 \
Queens 102 45 46 1 0 0 \
Queens 103 42 42 0 0 0 \
Queens 104 57 57 0 0 0 \
Queens 105 47 45 2 6 0 \
Queens 106 33 34 0 1 0 \
Queens 107 26 26 0 0 0 \
Queens 108 114 114 0 1 0 \
Queens 109 54 53 1 0 0 \
Queens 110 79 78 1 0 0 \
Queens 111 13 13 0 0 0 \
Queens 112 20 19 1 0 0 \
Queens 113 39 38 1 1 0 \
Queens 114 123 122 1 1 0 \
Queens 115 93 94 0 2 0"

table14_StatenIsland_BM = "StatenIsland 120 29 29 0 1 0 \
StatenIsland 121 15 15 0 0 0 \
StatenIsland 122 15 15 0 0 0 \
StatenIsland 123 1 1 0 0 0"

table15_Manhattan_BM = "Manhattan 1 90 91 0 0 0 \
Manhattan 5 73 75 0 3 0 \
Manhattan 6 58 60 0 0 0 \
Manhattan 7 51 51 0 1 0 \
Manhattan 9 86 87 0 1 0 \
Manhattan 10 51 51 0 0 0 \
Manhattan 13 136 136 0 0 0 \
Manhattan 14 94 94 0 0 0 \
Manhattan 17 108 108 0 0 0 \
Manhattan 18 104 106 0 0 0 \
Manhattan 19 111 111 0 2 0 \
Manhattan 20 50 51 0 0 0 \
Manhattan 22 5 5 0 0 0 \
Manhattan 23 37 37 0 1 0 \
Manhattan 24 40 40 0 0 0 \
Manhattan 25 38 37 1 1 0 \
Manhattan 26 19 20 0 0 0 \
Manhattan 28 42 42 0 1 0 \
Manhattan 30 27 28 0 0 0 \
Manhattan 32 29 30 1 0 0 \
Manhattan 33 28 28 0 0 0 \
Manhattan 34 36 36 0 0 0"

table15_Bronx_BM = "Bronx 40 58 59 0 3 0 \
Bronx 41 21 21 0 1 0 \
Bronx 42 32 32 0 0 0 \
Bronx 43 32 32 0 1 0 \
Bronx 44 60 59 1 0 0 \
Bronx 45 26 25 1 0 0 \
Bronx 46 43 45 0 0 0 \
Bronx 47 37 37 0 0 0 \
Bronx 48 42 42 0 1 0 \
Bronx 49 39 39 0 0 0 \
Bronx 50 29 29 0 0 0 \
Bronx 52 35 35 0 1 0"

table15_Brooklyn_BM = "Brooklyn 60 29 29 0 1 0 \
Brooklyn 61 73 73 0 0 0 \
Brooklyn 62 58 58 0 1 0 \
Brooklyn 63 20 20 0 0 0 \
Brooklyn 66 122 122 0 1 0 \
Brooklyn 67 79 80 0 2 0 \
Brooklyn 68 41 42 0 0 0 \
Brooklyn 69 19 19 0 2 0 \
Brooklyn 70 117 119 1 1 0 \
Brooklyn 71 51 52 0 0 0 \
Brooklyn 72 71 72 1 0 0 \
Brooklyn 73 39 39 0 0 0 \
Brooklyn 75 87 90 0 0 0 \
Brooklyn 76 34 33 1 0 0 \
Brooklyn 77 59 60 0 2 0 \
Brooklyn 78 74 73 1 8 0 \
Brooklyn 79 102 102 0 1 0 \
Brooklyn 81 64 64 0 0 0 \
Brooklyn 83 84 84 0 1 0 \
Brooklyn 84 55 55 0 0 0 \
Brooklyn 88 99 99 0 1 0 \
Brooklyn 90 177 177 0 3 0 \
Brooklyn 94 90 90 0 1 0"

table15_Queens_BM = "Queens 100 14 14 0 0 0 \
Queens 101 17 16 1 1 0 \
Queens 102 59 59 0 1 0 \
Queens 103 33 33 0 0 0 \
Queens 104 102 102 0 1 0 \
Queens 105 43 44 0 2 0 \
Queens 106 44 44 1 0 0 \
Queens 107 24 24 0 0 0 \
Queens 108 117 116 2 2 0 \
Queens 109 77 77 0 1 0 \
Queens 110 94 96 0 0 0 \
Queens 111 24 24 0 0 0 \
Queens 112 34 34 0 0 0 \
Queens 113 46 46 0 0 0 \
Queens 114 111 110 1 3 0 \
Queens 115 106 108 0 0 0"

table15_StatenIsland_BM = "StatenIsland 120 16 16 0 1 0 \
StatenIsland 121 21 21 0 0 0 \
StatenIsland 122 13 13 1 0 0 \
StatenIsland 123 5 5 0 0 0"

table16_Manhattan_BM = "Manhattan 1 88 87 1 2 0 \
Manhattan 5 81 81 0 0 0 \
Manhattan 6 60 60 0 1 0 \
Manhattan 7 45 46 0 0 0 \
Manhattan 9 84 84 0 3 0 \
Manhattan 10 53 53 0 0 0 \
Manhattan 13 121 121 0 4 0 \
Manhattan 14 115 116 0 1 0 \
Manhattan 17 94 94 0 1 0 \
Manhattan 18 104 103 1 1 0 \
Manhattan 19 111 112 0 1 0 \
Manhattan 20 46 46 0 0 0 \
Manhattan 22 6 6 0 0 0 \
Manhattan 23 27 27 0 0 0 \
Manhattan 24 48 48 0 0 0 \
Manhattan 25 39 39 0 1 0 \
Manhattan 26 25 25 0 0 0 \
Manhattan 28 39 39 0 0 0 \
Manhattan 30 26 26 0 0 0 \
Manhattan 32 50 50 0 3 0 \
Manhattan 33 23 23 0 0 0 \
Manhattan 34 42 42 0 0 0"

table16_Bronx_BM = "Bronx 40 79 79 0 0 0 \
Bronx 41 30 30 0 0 0 \
Bronx 42 30 30 0 6 0 \
Bronx 43 52 53 0 0 0 \
Bronx 44 47 48 0 3 0 \
Bronx 45 30 30 1 0 0 \
Bronx 46 33 35 0 2 0 \
Bronx 47 33 33 0 0 0 \
Bronx 48 32 33 0 0 0 \
Bronx 49 36 36 1 0 0 \
Bronx 50 18 18 0 1 0 \
Bronx 52 44 45 1 1 0"

table16_Brooklyn_BM = "Brooklyn 60 28 29 0 1 0 \
Brooklyn 61 74 72 2 3 0 \
Brooklyn 62 79 79 0 0 0 \
Brooklyn 63 27 27 0 0 0 \
Brooklyn 66 116 116 0 2 0 \
Brooklyn 67 81 82 0 3 0 \
Brooklyn 68 46 47 0 0 0 \
Brooklyn 69 26 26 0 0 0 \
Brooklyn 70 114 113 1 2 0 \
Brooklyn 71 71 70 1 0 0 \
Brooklyn 72 102 103 0 1 0 \
Brooklyn 73 47 47 0 3 0 \
Brooklyn 75 100 101 1 4 0 \
Brooklyn 76 35 36 0 0 0 \
Brooklyn 77 76 77 0 2 0 \
Brooklyn 78 89 89 1 0 0 \
Brooklyn 79 108 110 0 0 0 \
Brooklyn 81 55 55 0 1 0 \
Brooklyn 83 98 97 1 1 0 \
Brooklyn 84 63 63 0 0 0 \
Brooklyn 88 106 106 1 3 0 \
Brooklyn 90 198 199 1 2 0 \
Brooklyn 94 83 83 0 0 0"

table16_Queens_BM = "Queens 100 7 7 0 0 0 \
Queens 101 15 15 0 1 0 \
Queens 102 48 48 0 1 0 \
Queens 103 31 31 0 0 0 \
Queens 104 82 82 0 2 0 \
Queens 105 32 32 0 0 0 \
Queens 106 41 41 0 0 0 \
Queens 107 35 35 0 1 0 \
Queens 108 101 102 0 3 0 \
Queens 109 79 80 0 0 0 \
Queens 110 96 98 1 1 0 \
Queens 111 20 19 1 1 0 \
Queens 112 30 30 0 0 0 \
Queens 113 39 42 0 1 0 \
Queens 114 123 123 0 0 0 \
Queens 115 109 110 1 2 0"

table16_StatenIsland_BM = "StatenIsland 120 33 33 0 1 0 \
StatenIsland 121 19 19 0 2 0 \
StatenIsland 122 16 15 1 0 0 \
StatenIsland 123 5 5 0 0 0"


#BP is Bicyclist-Pedestrian
table14_Manhattan_BP = "Manhattan 1 13 13 0 2 0 \
Manhattan 5 10 10 0 1 0 \
Manhattan 6 17 17 0 3 0 \
Manhattan 7 7 7 1 1 0 \
Manhattan 9 8 8 0 1 0 \
Manhattan 10 3 3 0 0 0 \
Manhattan 13 20 21 0 3 0 \
Manhattan 14 12 12 0 1 0 \
Manhattan 17 8 8 0 0 0 \
Manhattan 18 8 8 0 0 0 \
Manhattan 19 6 6 0 0 0 \
Manhattan 20 4 4 0 0 0 \
Manhattan 22 34 32 2 12 0 \
Manhattan 23 3 3 0 1 0 \
Manhattan 24 8 8 0 1 0 \
Manhattan 25 2 2 0 0 0 \
Manhattan 26 4 4 0 1 0 \
Manhattan 28 2 2 0 0 0 \
Manhattan 30 1 1 0 0 0 \
Manhattan 32 1 1 0 0 0 \
Manhattan 33 3 3 0 0 0 \
Manhattan 34 4 4 0 3 0"

table14_Bronx_BP = "Bronx 40 2 2 0 1 0 \
Bronx 41 1 1 0 0 0 \
Bronx 42 1 1 0 0 0 \
Bronx 43 0 0 0 0 0 \
Bronx 44 0 0 0 0 0 \
Bronx 45 1 1 0 0 0 \
Bronx 46 0 0 0 0 0 \
Bronx 47 0 0 0 0 0 \
Bronx 48 1 1 0 0 0 \
Bronx 49 0 0 0 0 0 \
Bronx 50 2 2 0 1 0 \
Bronx 52 2 2 0 0 0"

table14_Brooklyn_BP = "Brooklyn 60 3 3 0 0 0 \
Brooklyn 61 2 2 0 0 0 \
Brooklyn 62 3 3 0 0 0 \
Brooklyn 63 1 1 0 0 0 \
Brooklyn 66 1 1 0 0 0 \
Brooklyn 67 1 1 0 0 0 \
Brooklyn 68 3 3 0 0 0 \
Brooklyn 69 0 0 0 0 0 \
Brooklyn 70 3 3 0 0 0 \
Brooklyn 71 4 4 0 2 0 \
Brooklyn 72 2 3 0 0 0 \
Brooklyn 73 2 2 0 0 0 \
Brooklyn 75 0 0 0 0 0 \
Brooklyn 76 2 2 0 0 0 \
Brooklyn 77 1 1 0 0 0 \
Brooklyn 78 13 13 0 6 0 \
Brooklyn 79 7 7 0 0 0 \
Brooklyn 81 1 1 0 0 0 \
Brooklyn 83 5 6 0 0 0 \
Brooklyn 84 10 10 0 2 0 \
Brooklyn 88 2 2 0 2 0 \
Brooklyn 90 11 12 0 2 0 \
Brooklyn 94 6 6 0 1 0"

table14_Queens_BP = "Queens 100 1 1 0 0 0 \
Queens 101 1 1 0 0 0 \
Queens 102 1 1 0 0 0 \
Queens 103 4 4 0 0 0 \
Queens 104 4 4 0 0 0 \
Queens 105 1 1 0 0 0 \
Queens 106 1 1 0 0 0 \
Queens 107 0 0 0 0 0 \
Queens 108 1 1 0 0 0 \
Queens 109 3 3 0 0 0 \
Queens 110 3 4 0 0 0 \
Queens 111 1 1 0 0 0 \
Queens 112 2 2 0 0 0 \
Queens 113 0 0 0 0 0 \
Queens 114 4 4 0 0 0 \
Queens 115 4 4 0 0 0"

table14_StatenIsland_BP = "StatenIsland 120 0 0 0 0 0 \
StatenIsland 121 0 0 0 0 0 \
StatenIsland 122 0 0 0 0 0 \
StatenIsland 123 0 0 0 0 0"

table15_Manhattan_BP = "Manhattan 1 12 13 0 0 0 \
Manhattan 5 12 12 0 0 0 \
Manhattan 6 8 8 0 1 0 \
Manhattan 7 6 6 0 0 0 \
Manhattan 9 9 9 0 0 0 \
Manhattan 10 1 1 0 0 0 \
Manhattan 13 17 17 0 0 0 \
Manhattan 14 22 22 0 0 0 \
Manhattan 17 15 15 0 1 0 \
Manhattan 18 14 15 0 0 0 \
Manhattan 19 21 22 0 0 0 \
Manhattan 20 10 10 0 0 0 \
Manhattan 22 14 14 0 3 0 \
Manhattan 23 5 5 0 0 0 \
Manhattan 24 13 13 0 2 0 \
Manhattan 25 3 3 0 1 0 \
Manhattan 26 5 5 0 1 0 \
Manhattan 28 3 3 0 0 0 \
Manhattan 30 3 3 0 0 0 \
Manhattan 32 1 1 0 0 0 \
Manhattan 33 0 0 0 0 0 \
Manhattan 34 2 2 0 0 0"

table15_Bronx_BP = "Bronx 40 4 4 0 0 0 \
Bronx 41 0 0 0 0 0 \
Bronx 42 0 0 0 0 0 \
Bronx 43 0 0 0 0 0 \
Bronx 44 3 3 0 0 0 \
Bronx 45 1 1 0 0 0 \
Bronx 46 3 3 0 0 0 \
Bronx 47 0 0 0 0 0 \
Bronx 48 4 4 0 0 0 \
Bronx 49 1 1 0 0 0 \
Bronx 50 1 1 0 1 0 \
Bronx 52 3 3 0 1 0"

table15_Brooklyn_BP = "Brooklyn 60 2 2 0 0 0 \
Brooklyn 61 1 1 0 0 0 \
Brooklyn 62 5 5 0 1 0 \
Brooklyn 63 0 0 0 0 0 \
Brooklyn 66 9 10 0 1 0 \
Brooklyn 67 1 2 0 0 0 \
Brooklyn 68 3 3 0 0 0 \
Brooklyn 69 0 0 0 0 0 \
Brooklyn 70 4 4 0 0 0 \
Brooklyn 71 3 3 0 1 0 \
Brooklyn 72 3 3 0 1 0 \
Brooklyn 73 0 0 0 0 0 \
Brooklyn 75 1 1 0 0 0 \
Brooklyn 76 3 3 0 0 0 \
Brooklyn 77 5 5 0 0 0 \
Brooklyn 78 10 11 0 1 0 \
Brooklyn 79 9 9 0 2 1 \
Brooklyn 81 1 1 0 0 0 \
Brooklyn 83 5 6 0 0 0 \
Brooklyn 84 9 9 0 0 0 \
Brooklyn 88 5 5 0 1 0 \
Brooklyn 90 12 13 0 3 0 \
Brooklyn 94 5 5 0 3 0"

table15_Queens_BP = "Queens 100 0 0 0 0 0 \
Queens 101 0 0 0 0 0 \
Queens 102 2 3 0 0 0 \
Queens 103 0 0 0 0 0 \
Queens 104 3 3 0 0 0 \
Queens 105 0 0 0 0 0 \
Queens 106 0 0 0 0 0 \
Queens 107 1 1 0 0 0 \
Queens 108 0 0 0 0 0 \
Queens 109 3 4 0 0 0 \
Queens 110 11 12 0 1 0 \
Queens 111 1 1 0 0 0 \
Queens 112 1 1 0 0 0 \
Queens 113 0 0 0 0 0 \
Queens 114 6 6 0 2 0 \
Queens 115 6 6 0 0 0"

table15_StatenIsland_BP = "StatenIsland 120 1 1 0 0 0 \
StatenIsland 121 0 0 0 0 0 \
StatenIsland 122 1 2 0 0 0 \
StatenIsland 123 1 1 0 0 0"

table16_Manhattan_BP = "Manhattan 1 9 10 0 2 0 \
Manhattan 5 7 7 0 0 0 \
Manhattan 6 8 7 0 1 0 \
Manhattan 7 4 4 0 3 0 \
Manhattan 9 11 11 0 1 0 \
Manhattan 10 9 7 0 2 0 \
Manhattan 13 20 20 0 2 0 \
Manhattan 14 25 24 0 1 0 \
Manhattan 17 8 9 0 0 0 \
Manhattan 18 12 12 0 1 0 \
Manhattan 19 19 15 0 4 0 \
Manhattan 20 7 5 0 2 0 \
Manhattan 22 29 14 0 16 0 \
Manhattan 23 5 4 0 1 0 \
Manhattan 24 7 7 0 0 0 \
Manhattan 25 3 3 0 0 0 \
Manhattan 26 3 3 0 0 0 \
Manhattan 28 1 1 0 0 0 \
Manhattan 30 5 4 0 0 0 \
Manhattan 32 1 1 0 0 0 \
Manhattan 33 3 3 0 0 0 \
Manhattan 34 2 2 0 1 0"

table16_Bronx_BP = "Bronx 40 3 3 0 1 0 \
Bronx 41 2 2 0 1 0 \
Bronx 42 1 1 0 0 0 \
Bronx 43 4 3 0 0 0 \
Bronx 44 0 0 0 0 0 \
Bronx 45 2 2 0 0 0 \
Bronx 46 0 0 0 0 0 \
Bronx 47 2 2 0 0 0 \
Bronx 48 1 1 0 0 0 \
Bronx 49 1 1 0 0 0 \
Bronx 50 2 2 0 0 0 \
Bronx 52 3 3 0 1 0"

table16_Brooklyn_BP = "Brooklyn 60 2 2 0 0 0 \
Brooklyn 61 4 4 0 1 0 \
Brooklyn 62 7 5 0 1 0 \
Brooklyn 63 1 0 0 0 0 \
Brooklyn 66 5 6 0 0 0 \
Brooklyn 67 4 4 0 0 0 \
Brooklyn 68 2 2 0 1 0 \
Brooklyn 69 0 0 0 0 0 \
Brooklyn 70 2 3 0 0 0 \
Brooklyn 71 4 3 0 0 0 \
Brooklyn 72 6 7 0 1 0 \
Brooklyn 73 2 2 0 0 0 \
Brooklyn 75 4 4 0 0 0 \
Brooklyn 76 1 1 0 0 0 \
Brooklyn 77 3 3 0 1 0 \
Brooklyn 78 7 5 0 5 0 \
Brooklyn 79 4 5 0 0 0 \
Brooklyn 81 1 1 0 0 0 \
Brooklyn 83 3 3 0 0 0 \
Brooklyn 84 17 13 0 6 0 \
Brooklyn 88 4 4 0 0 0 \
Brooklyn 90 6 4 0 3 0 \
Brooklyn 94 3 3 0 1 0"

table16_Queens_BP = "Queens 100 0 0 0 0 0 \
Queens 101 1 1 0 0 0 \
Queens 102 0 0 0 0 0 \
Queens 103 0 0 0 0 0 \
Queens 104 4 4 0 0 0 \
Queens 105 1 0 0 1 0 \
Queens 106 0 0 0 0 0 \
Queens 107 1 1 0 0 0 \
Queens 108 5 4 0 1 0 \
Queens 109 3 2 0 0 0 \
Queens 110 5 6 0 0 0 \
Queens 111 0 0 0 0 0 \
Queens 112 2 2 0 0 0 \
Queens 113 1 1 0 0 0 \
Queens 114 5 5 0 0 0 \
Queens 115 8 6 0 2 0"

table16_StatenIsland_BP = "StatenIsland 120 1 1 0 0 0 \
StatenIsland 121 0 0 0 0 0 \
StatenIsland 122 1 1 0 0 0 \
StatenIsland 123 0 0 0 0 0"

# BB is Bicyclist-Bicyclist
table14_Manhattan_BB = "Manhattan 1 2 2 0 \
Manhattan 5 1 2 0 \
Manhattan 6 0 0 0 \
Manhattan 7 0 0 0 \
Manhattan 9 4 5 0 \
Manhattan 10 1 1 0 \
Manhattan 13 2 1 0 \
Manhattan 14 1 2 0 \
Manhattan 17 1 2 0 \
Manhattan 18 2 1 0 \
Manhattan 19 5 2 0 \
Manhattan 20 1 1 0 \
Manhattan 22 29 28 0 \
Manhattan 23 0 0 0 \
Manhattan 24 2 2 0 \
Manhattan 25 0 0 0 \
Manhattan 26 1 1 0 \
Manhattan 28 0 0 0 \
Manhattan 30 1 1 0 \
Manhattan 32 1 0 0 \
Manhattan 33 0 0 0 \
Manhattan 34 0 0 0"

table14_Bronx_BB = "Bronx 40 0 0 0 \
Bronx 41 0 0 0 \
Bronx 42 0 0 0 \
Bronx 43 0 0 0 \
Bronx 44 0 0 0 \
Bronx 45 0 0 0 \
Bronx 46 0 0 0 \
Bronx 47 1 0 0 \
Bronx 48 0 0 0 \
Bronx 49 0 0 0 \
Bronx 50 0 0 0 \
Bronx 52 0 0 0"

table14_Brooklyn_BB = "Brooklyn 60 0 0 0 \
Brooklyn 61 0 0 0 \
Brooklyn 62 0 0 0 \
Brooklyn 63 0 0 0 \
Brooklyn 66 0 0 0 \
Brooklyn 67 1 0 0 \
Brooklyn 68 0 0 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 0 0 0 \
Brooklyn 71 2 2 0 \
Brooklyn 72 0 0 0 \
Brooklyn 73 2 2 0 \
Brooklyn 75 0 0 0 \
Brooklyn 76 0 0 0 \
Brooklyn 77 1 2 0 \
Brooklyn 78 12 15 0 \
Brooklyn 79 1 1 0 \
Brooklyn 81 1 1 0 \
Brooklyn 83 1 1 0 \
Brooklyn 84 1 2 0 \
Brooklyn 88 4 2 0 \
Brooklyn 90 5 7 0 \
Brooklyn 94 2 2 0"

table14_Queens_BB = "Queens 100 0 0 0 \
Queens 101 0 0 0 \
Queens 102 2 0 0 \
Queens 103 0 0 0 \
Queens 104 3 2 0 \
Queens 105 0 0 0 \
Queens 106 0 0 0 \
Queens 107 0 0 0 \
Queens 108 0 0 0 \
Queens 109 0 0 0 \
Queens 110 0 0 0 \
Queens 111 0 0 0 \
Queens 112 0 0 0 \
Queens 113 0 0 0 \
Queens 114 0 0 0 \
Queens 115 2 3 0"

table14_StatenIsland_BB = "StatenIsland 120 0 0 0 \
StatenIsland 121 0 0 0 \
StatenIsland 122 1 0 0 \
StatenIsland 123 0 0 0"

table15_Manhattan_BB = "Manhattan 1 5 5 0 \
Manhattan 5 4 5 0 \
Manhattan 6 3 4 0 \
Manhattan 7 4 3 0 \
Manhattan 9 7 2 0 \
Manhattan 10 2 1 0 \
Manhattan 13 2 2 0 \
Manhattan 14 1 0 0 \
Manhattan 17 2 1 0 \
Manhattan 18 2 2 0 \
Manhattan 19 0 0 0 \
Manhattan 20 2 1 0 \
Manhattan 22 17 19 0 \
Manhattan 23 0 0 0 \
Manhattan 24 1 1 0 \
Manhattan 25 2 3 0 \
Manhattan 26 0 0 0 \
Manhattan 28 0 0 0 \
Manhattan 30 1 1 0 \
Manhattan 32 0 0 0 \
Manhattan 33 0 0 0 \
Manhattan 34 1 0 0"

table15_Bronx_BB = "Bronx 40 1 0 0 \
Bronx 41 0 0 0 \
Bronx 42 0 0 0 \
Bronx 43 1 1 0 \
Bronx 44 0 0 0 \
Bronx 45 1 1 0 \
Bronx 46 0 0 0 \
Bronx 47 0 0 0 \
Bronx 48 0 0 0 \
Bronx 49 1 1 0 \
Bronx 50 0 0 0 \
Bronx 52 0 0 0"

table15_Brooklyn_BB = "Brooklyn 60 0 0 0 \
Brooklyn 61 0 0 0 \
Brooklyn 62 1 1 0 \
Brooklyn 63 0 0 0 \
Brooklyn 66 2 2 0 \
Brooklyn 67 1 0 0 \
Brooklyn 68 2 3 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 0 0 0 \
Brooklyn 71 0 0 0 \
Brooklyn 72 2 3 0 \
Brooklyn 73 0 0 0 \
Brooklyn 75 0 0 0 \
Brooklyn 76 1 0 0 \
Brooklyn 77 1 0 0 \
Brooklyn 78 4 6 0 \
Brooklyn 79 3 2 0 \
Brooklyn 81 0 0 0 \
Brooklyn 83 1 1 0 \
Brooklyn 84 2 2 0 \
Brooklyn 88 0 0 0 \
Brooklyn 90 4 3 0 \
Brooklyn 94 2 3 0"

table15_Queens_BB = "Queens 100 0 0 0 \
Queens 101 0 0 0 \
Queens 102 0 0 0 \
Queens 103 0 0 0 \
Queens 104 1 0 0 \
Queens 105 0 0 0 \
Queens 106 0 0 0 \
Queens 107 0 0 0 \
Queens 108 2 2 0 \
Queens 109 0 0 0 \
Queens 110 0 0 0 \
Queens 111 0 0 0 \
Queens 112 0 0 0 \
Queens 113 0 0 0 \
Queens 114 0 0 0 \
Queens 115 2 1 0"

table15_StatenIsland_BB = "StatenIsland 120 0 0 0 \
StatenIsland 121 0 0 0 \
StatenIsland 122 0 0 0 \
StatenIsland 123 0 0 0"

table16_Manhattan_BB = "Manhattan 1 1 1 0 \
Manhattan 5 3 8 0 \
Manhattan 6 4 3 0 \
Manhattan 7 1 1 0 \
Manhattan 9 0 0 0 \
Manhattan 10 2 1 0 \
Manhattan 13 1 1 0 \
Manhattan 14 1 2 0 \
Manhattan 17 0 0 0 \
Manhattan 18 1 0 0 \
Manhattan 19 2 2 0 \
Manhattan 20 3 3 0 \
Manhattan 22 44 62 0 \
Manhattan 23 0 0 0 \
Manhattan 24 0 0 0 \
Manhattan 25 0 0 0 \
Manhattan 26 0 0 0 \
Manhattan 28 1 1 0 \
Manhattan 30 0 0 0 \
Manhattan 32 0 0 0 \
Manhattan 33 1 1 0 \
Manhattan 34 0 0 0"

table16_Bronx_BB = "Bronx 40 0 0 0 \
Bronx 41 0 0 0 \
Bronx 42 0 0 0 \
Bronx 43 0 0 0 \
Bronx 44 0 0 0 \
Bronx 45 0 0 0 \
Bronx 46 0 0 0 \
Bronx 47 0 0 0 \
Bronx 48 0 0 0 \
Bronx 49 0 0 0 \
Bronx 50 0 0 0 \
Bronx 52 0 0 0"

table16_Brooklyn_BB = "Brooklyn 60 0 0 0 \
Brooklyn 61 0 0 0 \
Brooklyn 62 2 2 0 \
Brooklyn 63 0 0 0 \
Brooklyn 66 0 0 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 0 0 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 0 0 0 \
Brooklyn 71 1 2 0 \
Brooklyn 72 2 3 0 \
Brooklyn 73 0 0 0 \
Brooklyn 75 0 0 0 \
Brooklyn 76 0 0 0 \
Brooklyn 77 0 0 0 \
Brooklyn 78 6 10 0 \
Brooklyn 79 2 3 0 \
Brooklyn 81 0 0 0 \
Brooklyn 83 0 0 0 \
Brooklyn 84 0 0 0 \
Brooklyn 88 2 1 0 \
Brooklyn 90 1 1 0 \
Brooklyn 94 2 4 0"

table16_Queens_BB = "Queens 100 2 2 0 \
Queens 101 0 0 0 \
Queens 102 0 0 0 \
Queens 103 0 0 0 \
Queens 104 0 0 0 \
Queens 105 0 0 0 \
Queens 106 0 0 0 \
Queens 107 0 0 0 \
Queens 108 1 2 0 \
Queens 109 0 0 0 \
Queens 110 0 0 0 \
Queens 111 0 0 0 \
Queens 112 0 0 0 \
Queens 113 0 0 0 \
Queens 114 2 3 0 \
Queens 115 1 2 0"

table16_StatenIsland_BB = "StatenIsland 120 0 0 0 \
StatenIsland 121 0 0 0 \
StatenIsland 122 0 0 0 \
StatenIsland 123 0 0 0"

#SB is Single Bicycle
table14_Manhattan_SB = "Manhattan 1 7 6 0 \
Manhattan 5 6 4 0 \
Manhattan 6 2 0 0 \
Manhattan 7 12 11 0 \
Manhattan 9 15 12 0 \
Manhattan 10 7 5 0 \
Manhattan 13 6 5 0 \
Manhattan 14 1 1 0 \
Manhattan 17 3 3 0 \
Manhattan 18 9 4 0 \
Manhattan 19 12 6 0 \
Manhattan 20 9 6 0 \
Manhattan 22 114 99 0 \
Manhattan 23 6 3 0 \
Manhattan 24 6 6 0 \
Manhattan 25 2 2 0 \
Manhattan 26 2 1 0 \
Manhattan 28 2 2 0 \
Manhattan 30 5 3 0 \
Manhattan 32 2 1 0 \
Manhattan 33 4 3 0 \
Manhattan 34 1 1 0"

table14_Bronx_SB = "Bronx 40 4 3 0 \
Bronx 41 1 1 0 \
Bronx 42 1 1 0 \
Bronx 43 2 2 0 \
Bronx 44 0 0 0 \
Bronx 45 3 3 0 \
Bronx 46 2 2 0 \
Bronx 47 0 0 0 \
Bronx 48 0 0 0 \
Bronx 49 2 2 0 \
Bronx 50 2 2 0 \
Bronx 52 6 6 0"

table14_Brooklyn_SB = "Brooklyn 60 3 3 0 \
Brooklyn 61 1 1 0 \
Brooklyn 62 3 3 0 \
Brooklyn 63 4 4 0 \
Brooklyn 66 4 3 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 1 1 0 \
Brooklyn 69 1 1 0 \
Brooklyn 70 4 4 0 \
Brooklyn 71 3 3 0 \
Brooklyn 72 9 9 0 \
Brooklyn 73 1 1 0 \
Brooklyn 75 2 2 0 \
Brooklyn 76 2 2 0 \
Brooklyn 77 4 3 0 \
Brooklyn 78 21 20 0 \
Brooklyn 79 4 4 0 \
Brooklyn 81 0 0 0 \
Brooklyn 83 2 1 0 \
Brooklyn 84 7 7 0 \
Brooklyn 88 9 9 0 \
Brooklyn 90 18 16 0 \
Brooklyn 94 6 5 1"

table14_Queens_SB = "Queens 100 0 0 0 \
Queens 101 2 2 0 \
Queens 102 2 2 0 \
Queens 103 0 0 0 \
Queens 104 1 0 0 \
Queens 105 0 0 0 \
Queens 106 3 2 0 \
Queens 107 0 0 0 \
Queens 108 8 8 0 \
Queens 109 3 2 0 \
Queens 110 3 2 0 \
Queens 111 2 2 0 \
Queens 112 1 1 0 \
Queens 113 1 0 0 \
Queens 114 3 2 0 \
Queens 115 6 6 0"

table14_StatenIsland_SB = "StatenIsland 120 1 1 0 \
StatenIsland 121 0 0 0 \
StatenIsland 122 0 0 0 \
StatenIsland 123 3 3 0"

table15_Manhattan_SB = "Manhattan 1 10 10 0 \
Manhattan 5 10 7 0 \
Manhattan 6 5 5 0 \
Manhattan 7 6 5 0 \
Manhattan 9 5 4 0 \
Manhattan 10 7 6 0 \
Manhattan 13 13 11 0 \
Manhattan 14 9 7 0 \
Manhattan 17 7 7 0 \
Manhattan 18 7 4 0 \
Manhattan 19 6 5 0 \
Manhattan 20 10 7 1 \
Manhattan 22 100 80 0 \
Manhattan 23 2 2 0 \
Manhattan 24 10 8 0 \
Manhattan 25 2 1 0 \
Manhattan 26 3 3 0 \
Manhattan 28 3 2 0 \
Manhattan 30 6 6 0 \
Manhattan 32 2 2 0 \
Manhattan 33 1 1 0 \
Manhattan 34 4 3 0"

table15_Bronx_SB = "Bronx 40 2 2 0 \
Bronx 41 1 1 0 \
Bronx 42 2 1 0 \
Bronx 43 3 2 0 \
Bronx 44 0 0 0 \
Bronx 45 1 1 0 \
Bronx 46 3 3 0 \
Bronx 47 1 1 0 \
Bronx 48 0 0 0 \
Bronx 49 3 3 0 \
Bronx 50 2 2 0 \
Bronx 52 4 4 0"

table15_Brooklyn_SB = "Brooklyn 60 5 4 0 \
Brooklyn 61 2 2 0 \
Brooklyn 62 1 1 0 \
Brooklyn 63 2 2 0 \
Brooklyn 66 10 9 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 3 3 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 2 1 0 \
Brooklyn 71 4 4 0 \
Brooklyn 72 8 8 0 \
Brooklyn 73 1 0 0 \
Brooklyn 75 3 3 0 \
Brooklyn 76 6 4 0 \
Brooklyn 77 4 3 0 \
Brooklyn 78 14 13 0 \
Brooklyn 79 10 8 0 \
Brooklyn 81 1 1 0 \
Brooklyn 83 2 2 0 \
Brooklyn 84 11 9 0 \
Brooklyn 88 6 5 0 \
Brooklyn 90 23 21 0 \
Brooklyn 94 11 9 0"

table15_Queens_SB = "Queens 100 1 1 0 \
Queens 101 2 1 0 \
Queens 102 4 4 0 \
Queens 103 0 0 0 \
Queens 104 6 6 0 \
Queens 105 0 0 0 \
Queens 106 1 0 0 \
Queens 107 1 1 0 \
Queens 108 5 5 0 \
Queens 109 2 2 0 \
Queens 110 4 3 0 \
Queens 111 2 2 0 \
Queens 112 2 1 0 \
Queens 113 0 0 0 \
Queens 114 4 4 0 \
Queens 115 5 4 0"

table15_StatenIsland_SB = "StatenIsland 120 0 0 0 \
StatenIsland 121 1 1 0 \
StatenIsland 122 0 0 0 \
StatenIsland 123 0 0 0"

table16_Manhattan_SB = "Manhattan 1 6 6 0 \
Manhattan 5 7 6 0 \
Manhattan 6 3 2 0 \
Manhattan 7 6 5 0 \
Manhattan 9 4 4 0 \
Manhattan 10 3 2 0 \
Manhattan 13 3 2 0 \
Manhattan 14 0 0 0 \
Manhattan 17 2 2 0 \
Manhattan 18 0 0 0 \
Manhattan 19 5 4 0 \
Manhattan 20 2 2 0 \
Manhattan 22 57 42 0 \
Manhattan 23 0 0 0 \
Manhattan 24 4 2 0 \
Manhattan 25 0 0 0 \
Manhattan 26 6 6 0 \
Manhattan 28 0 0 0 \
Manhattan 30 2 1 0 \
Manhattan 32 0 0 0 \
Manhattan 33 0 0 0 \
Manhattan 34 1 1 0"

table16_Bronx_SB = "Bronx 40 5 5 0 \
Bronx 41 0 0 0 \
Bronx 42 1 1 0 \
Bronx 43 2 1 0 \
Bronx 44 0 0 0 \
Bronx 45 2 2 0 \
Bronx 46 0 0 0 \
Bronx 47 1 1 0 \
Bronx 48 1 1 0 \
Bronx 49 2 2 0 \
Bronx 50 1 1 0 \
Bronx 52 0 0 0"

table16_Brooklyn_SB = "Brooklyn 60 0 0 0 \
Brooklyn 61 2 1 0 \
Brooklyn 62 1 1 0 \
Brooklyn 63 1 1 0 \
Brooklyn 66 0 0 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 2 2 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 1 1 0 \
Brooklyn 71 0 0 0 \
Brooklyn 72 9 8 0 \
Brooklyn 73 0 0 0 \
Brooklyn 75 3 2 0 \
Brooklyn 76 2 2 0 \
Brooklyn 77 4 4 0 \
Brooklyn 78 10 10 0 \
Brooklyn 79 5 5 0 \
Brooklyn 81 2 2 0 \
Brooklyn 83 2 2 0 \
Brooklyn 84 8 6 0 \
Brooklyn 88 4 4 0 \
Brooklyn 90 10 9 0 \
Brooklyn 94 6 6 0"

table16_Queens_SB = "Queens 100 2 2 0 \
Queens 101 0 0 0 \
Queens 102 2 2 0 \
Queens 103 0 0 0 \
Queens 104 0 0 0 \
Queens 105 1 1 0 \
Queens 106 0 0 0 \
Queens 107 1 0 0 \
Queens 108 4 4 0 \
Queens 109 0 0 0 \
Queens 110 5 4 0 \
Queens 111 0 0 0 \
Queens 112 1 1 0 \
Queens 113 0 0 0 \
Queens 114 1 1 0 \
Queens 115 8 8 0"

table16_StatenIsland_SB = "StatenIsland 120 3 3 0 \
StatenIsland 121 0 0 0 \
StatenIsland 122 2 1 0 \
StatenIsland 123 2 2 0"

table17_Manhattan_BM = "Manhattan 1 83 83 1 3 0 \
Manhattan 5 73 72 1 1 0 \
Manhattan 6 63 63 0 0 0 \
Manhattan 7 47 47 0 0 0 \
Manhattan 9 90 89 1 0 0 \
Manhattan 10 47 46 2 1 0 \
Manhattan 13 124 124 1 1 0 \
Manhattan 14 96 97 1 0 0 \
Manhattan 17 89 89 0 0 0 \
Manhattan 18 93 92 1 0 0 \
Manhattan 19 99 99 0 0 0 \
Manhattan 20 57 56 1 0 0 \
Manhattan 22 6 6 0 0 0 \
Manhattan 23 25 25 0 0 0 \
Manhattan 24 47 48 0 1 0 \
Manhattan 25 30 30 0 2 0 \
Manhattan 26 27 27 0 0 0 \
Manhattan 28 50 50 0 0 0 \
Manhattan 30 23 24 0 0 0 \
Manhattan 32 32 32 0 0 0 \
Manhattan 33 25 25 0 0 0 \
Manhattan 34 36 36 0 0 0"

table17_Bronx_BM = "Bronx 40 72 74 0 2 0 \
Bronx 41 24 24 0 1 0 \
Bronx 42 35 35 0 0 0 \
Bronx 43 44 44 0 1 0 \
Bronx 44 55 55 0 1 0 \
Bronx 45 19 19 0 0 0 \
Bronx 46 42 45 0 0 0 \
Bronx 47 32 35 0 0 0 \
Bronx 48 37 36 1 0 0 \
Bronx 49 35 35 0 0 0 \
Bronx 50 13 13 0 1 0 \
Bronx 52 36 36 0 0 0"

table17_Brooklyn_BM = "Brooklyn 60 31 31 0 0 0 \
Brooklyn 61 88 86 2 1 0 \
Brooklyn 62 67 68 0 0 0 \
Brooklyn 63 36 36 0 0 0 \
Brooklyn 66 119 120 2 0 0 \
Brooklyn 67 80 79 1 0 0 \
Brooklyn 68 44 45 0 0 0 \
Brooklyn 69 20 20 0 0 0 \
Brooklyn 70 99 101 0 0 0 \
Brooklyn 71 58 59 1 1 0 \
Brooklyn 72 89 89 0 0 0 \
Brooklyn 73 36 37 0 0 0 \
Brooklyn 75 98 99 0 1 0 \
Brooklyn 76 23 23 0 0 0 \
Brooklyn 77 56 56 0 0 0 \
Brooklyn 78 69 70 0 0 0 \
Brooklyn 79 117 117 0 1 0 \
Brooklyn 81 51 50 1 0 0 \
Brooklyn 83 110 110 1 4 0 \
Brooklyn 84 65 65 0 0 0 \
Brooklyn 88 77 77 0 0 0 \
Brooklyn 90 170 170 1 0 0 \
Brooklyn 94 83 83 1 0 0"

table17_Queens_BM = "Queens 100 13 13 0 0 0 \
Queens 101 13 13 0 0 0 \
Queens 102 54 56 0 2 0 \
Queens 103 46 46 0 1 0 \
Queens 104 93 93 0 0 0 \
Queens 105 28 28 0 0 0 \
Queens 106 33 34 0 0 0 \
Queens 107 23 23 0 0 0 \
Queens 108 108 109 1 0 0 \
Queens 109 88 89 1 0 0 \
Queens 110 97 97 0 2 0 \
Queens 111 17 17 0 0 0 \
Queens 112 33 32 1 0 0 \
Queens 113 25 25 0 1 0 \
Queens 114 137 139 1 1 0 \
Queens 115 97 99 0 1 0"

table17_StatenIsland_BM = "StatenIsland 120 34 34 0 0 0 \
StatenIsland 121 20 20 0 1 0 \
StatenIsland 122 19 19 0 0 0 \
StatenIsland 123 8 9 0 1 0"

table18_Manhattan_BM = "Manhattan 1 112 87 0 3 0 \
Manhattan 5 95 67 0 0 0 \
Manhattan 6 69 46 0 1 0 \
Manhattan 7 54 41 0 0 0 \
Manhattan 9 122 93 0 0 0 \
Manhattan 10 78 39 0 0 0 \
Manhattan 13 163 111 0 3 0 \
Manhattan 14 152 94 0 1 0 \
Manhattan 17 131 97 1 1 0 \
Manhattan 18 188 103 0 0 0 \
Manhattan 19 143 90 0 2 0 \
Manhattan 20 66 42 1 0 0 \
Manhattan 22 9 6 0 0 0 \
Manhattan 23 63 40 0 0 0 \
Manhattan 24 68 43 0 0 0 \
Manhattan 25 45 34 0 1 0 \
Manhattan 26 30 21 1 0 0 \
Manhattan 28 66 52 0 2 0 \
Manhattan 30 32 28 0 0 0 \
Manhattan 32 54 38 0 4 0 \
Manhattan 33 51 42 0 0 0 \
Manhattan 34 52 43 0 0 0"

table18_Bronx_BM = "Bronx 40 97 71 0 2 0 \
Bronx 41 26 23 0 0 0 \
Bronx 42 46 29 0 0 0 \
Bronx 43 61 46 0 0 0 \
Bronx 44 67 58 0 0 0 \
Bronx 45 24 19 0 0 0 \
Bronx 46 62 49 1 2 0 \
Bronx 47 46 41 0 0 0 \
Bronx 48 55 42 1 0 0 \
Bronx 49 29 24 0 0 0 \
Bronx 50 28 27 0 0 0 \
Bronx 52 37 35 0 0 0"

table18_Brooklyn_BM = "Brooklyn 60 43 38 0 0 0 \
Brooklyn 61 95 89 0 0 0 \
Brooklyn 62 85 73 0 0 0 \
Brooklyn 63 39 30 0 0 0 \
Brooklyn 66 160 139 0 1 0 \
Brooklyn 67 92 76 0 2 0 \
Brooklyn 68 52 43 0 1 0 \
Brooklyn 69 38 32 0 0 0 \
Brooklyn 70 138 120 0 0 0 \
Brooklyn 71 86 73 0 21 0 \
Brooklyn 72 103 87 0 2 0 \
Brooklyn 73 67 53 1 5 0 \
Brooklyn 75 110 97 0 4 0 \
Brooklyn 76 30 23 0 1 0 \
Brooklyn 77 106 80 0 4 0 \
Brooklyn 78 89 73 0 1 0 \
Brooklyn 79 121 100 0 1 0 \
Brooklyn 81 51 44 1 1 0 \
Brooklyn 83 121 94 0 3 0 \
Brooklyn 84 88 66 0 1 0 \
Brooklyn 88 88 72 0 0 0 \
Brooklyn 90 186 156 0 2 0 \
Brooklyn 94 84 67 0 0 0"

table18_Queens_BM =  "Queens 100 19 16 0 0 0 \
Queens 101 15 12 0 1 0 \
Queens 102 41 37 0 0 0 \
Queens 103 49 46 0 0 0 \
Queens 104 92 75 0 0 0 \
Queens 105 34 32 0 0 0 \
Queens 106 31 25 0 0 0 \
Queens 107 27 26 0 0 0 \
Queens 108 91 78 1 2 0 \
Queens 109 75 70 0 0 0 \
Queens 110 113 91 0 1 0 \
Queens 111 14 10 0 0 0 \
Queens 112 35 29 0 1 0 \
Queens 113 38 28 0 0 0 \
Queens 114 152 127 1 3 0 \
Queens 115 106 94 1 0 0"

table18_StatenIsland_BM = "StatenIsland 120 41 33 0 0 0 \
StatenIsland 121 20 18 0 0 0 \
StatenIsland 122 9 5 0 0 0 \
StatenIsland 123 7 6 0 0 0"

table19_Manhattan_BM = "Manhattan 1 109 78 0 2 0 \
Manhattan 5 98 70 0 3 0 \
Manhattan 6 97 64 0 0 0 \
Manhattan 7 54 45 0 0 0 \
Manhattan 9 112 86 0 1 0 \
Manhattan 10 82 45 1 0 0 \
Manhattan 13 177 118 1 4 0 \
Manhattan 14 133 81 1 3 0 \
Manhattan 17 121 107 0 0 0 \
Manhattan 18 173 100 0 0 0 \
Manhattan 19 167 110 0 1 0 \
Manhattan 20 68 49 0 1 0 \
Manhattan 22 7 6 1 0 0 \
Manhattan 23 79 53 0 0 0 \
Manhattan 24 57 32 0 0 0 \
Manhattan 25 72 59 1 0 0 \
Manhattan 26 30 21 0 0 0 \
Manhattan 28 59 45 0 0 0 \
Manhattan 30 40 38 0 0 0 \
Manhattan 32 70 58 0 0 0 \
Manhattan 33 56 35 0 2 0 \
Manhattan 34 44 31 0 0 0"

table19_Bronx_BM = "Bronx 40 103 79 0 0 0 \
Bronx 41 35 21 0 0 0 \
Bronx 42 44 35 0 0 0 \
Bronx 43 66 59 0 0 0 \
Bronx 44 88 76 0 2 0 \
Bronx 45 34 28 0 1 0 \
Bronx 46 55 42 0 1 0 \
Bronx 47 44 35 0 1 0 \
Bronx 48 65 44 0 0 0 \
Bronx 49 39 30 0 1 0 \
Bronx 50 25 24 0 2 0 \
Bronx 52 63 53 0 0 0"

table19_Brooklyn_BM = "Brooklyn 60 46 43 0 0 0 \
Brooklyn 61 97 83 1 0 0 \
Brooklyn 62 76 66 1 1 0 \
Brooklyn 63 40 29 1 1 0 \
Brooklyn 66 150 119 3 3 0 \
Brooklyn 67 107 95 0 2 0 \
Brooklyn 68 66 57 0 1 0 \
Brooklyn 69 29 27 1 4 0 \
Brooklyn 70 127 113 1 0 0 \
Brooklyn 71 93 86 0 1 0 \
Brooklyn 72 117 100 2 0 0 \
Brooklyn 73 81 70 1 2 0 \
Brooklyn 75 112 10 0 14 0 \
Brooklyn 76 24 22 0 2 0 \
Brooklyn 77 111 87 1 2 0 \
Brooklyn 78 115 91 1 3 0 \
Brooklyn 79 118 99 0 2 0 \
Brooklyn 81 81 51 0 0 0 \
Brooklyn 83 115 97 0 0 0 \
Brooklyn 84 75 53 0 1 0 \
Brooklyn 88 115 91 0 0 0 \
Brooklyn 90 178 141 2 5 0 \
Brooklyn 94 73 60 1 3 0"

table19_Queens_BM = "Queens 100 26 16 2 0 0 \
Queens 101 21 15 0 1 0 \
Queens 102 61 50 0 0 0 \
Queens 103 48 43 0 0 0 \
Queens 104 94 88 0 0 0 \
Queens 105 35 30 0 1 0 \
Queens 106 50 42 0 0 0 \
Queens 107 26 26 0 0 0 \
Queens 108 104 87 2 0 0 \
Queens 109 94 89 0 1 0 \
Queens 110 143 110 0 0 0 \
Queens 111 29 23 0 0 0 \
Queens 112 31 23 0 0 0 \
Queens 113 41 37 0 0 0 \
Queens 114 150 140 0 2 0 \
Queens 115 107 92 0 1 0"

table19_StatenIsland_BM = "StatenIsland 120 28 24 1 0 0 \
StatenIsland 121 22 19 0 0 0 \
StatenIsland 122 16 14 0 0 0 \
StatenIsland 123 8 6 0 0 0"

table17_Manhattan_BP = "Manhattan 1 17 18 0 3 0 \
Manhattan 5 13 13 0 1 0 \
Manhattan 6 4 2 0 1 0 \
Manhattan 7 9 5 1 4 0 \
Manhattan 9 17 17 0 4 0 \
Manhattan 10 3 3 0 1 0 \
Manhattan 13 16 14 0 5 0 \
Manhattan 14 20 19 0 5 0 \
Manhattan 17 11 9 0 4 0 \
Manhattan 18 16 12 0 1 0 \
Manhattan 19 18 14 0 5 0 \
Manhattan 20 10 10 0 2 0 \
Manhattan 22 20 13 0 24 0 \
Manhattan 23 6 3 0 0 0 \
Manhattan 24 10 7 0 3 0 \
Manhattan 25 2 2 0 1 0 \
Manhattan 26 2 1 0 0 0 \
Manhattan 28 4 5 0 1 0 \
Manhattan 30 3 2 0 1 0 \
Manhattan 32 3 2 0 0 0 \
Manhattan 33 2 0 0 1 0 \
Manhattan 34 1 1 0 0 0"

table17_Bronx_BP = "Bronx 40 5 5 0 1 0 \
Bronx 41 2 2 0 0 0 \
Bronx 42 3 1 0 0 0 \
Bronx 43 2 2 0 0 0 \
Bronx 44 7 7 0 1 0 \
Bronx 45 0 0 0 0 0 \
Bronx 46 0 0 0 0 0 \
Bronx 47 1 1 0 0 0 \
Bronx 48 1 1 0 0 0 \
Bronx 49 1 1 0 0 0 \
Bronx 50 2 1 0 0 0 \
Bronx 52 1 1 0 0 0"

table17_Brooklyn_BP = "Brooklyn 60 1 1 0 0 0 \
Brooklyn 61 3 3 0 1 0 \
Brooklyn 62 4 4 0 0 0 \
Brooklyn 63 0 0 0 0 0 \
Brooklyn 66 5 5 0 1 0 \
Brooklyn 67 2 2 0 0 0 \
Brooklyn 68 5 4 0 1 0 \
Brooklyn 69 0 0 0 0 0 \
Brooklyn 70 3 3 0 0 0 \
Brooklyn 71 2 2 0 0 0 \
Brooklyn 72 7 7 0 1 0 \
Brooklyn 73 2 2 0 0 0 \
Brooklyn 75 2 2 0 0 0 \
Brooklyn 76 1 1 0 0 0 \
Brooklyn 77 3 3 0 0 0 \
Brooklyn 78 11 10 0 3 0 \
Brooklyn 79 3 2 0 1 0 \
Brooklyn 81 4 3 0 0 0 \
Brooklyn 83 5 4 0 1 0 \
Brooklyn 84 17 14 0 6 0 \
Brooklyn 88 1 1 0 0 0 \
Brooklyn 90 9 8 0 2 0 \
Brooklyn 94 3 3 0 0 0"

table17_Queens_BP = "Queens 100 0 0 0 0 0 \
Queens 101 0 0 0 0 0 \
Queens 102 1 1 0 0 0 \
Queens 103 1 1 0 0 0 \
Queens 104 3 3 0 1 0 \
Queens 105 0 0 0 0 0 \
Queens 106 0 0 0 0 0 \
Queens 107 1 1 0 0 0 \
Queens 108 5 4 0 0 0 \
Queens 109 8 8 0 0 0 \
Queens 110 9 8 0 0 0 \
Queens 111 0 0 0 0 0 \
Queens 112 1 1 0 0 0 \
Queens 113 1 1 0 0 0 \
Queens 114 4 4 0 1 0 \
Queens 115 5 4 0 0 0"

table17_StatenIsland_BP = "StatenIsland 120 1 1 0 0 0 \
StatenIsland 121 0 0 0 0 0 \
StatenIsland 122 0 0 0 0 0 \
StatenIsland 123 0 0 0 0 0"

table18_Manhattan_BP = "Manhattan 1 12 12 0 1 0 \
Manhattan 5 14 13 0 4 0 \
Manhattan 6 10 10 0 0 0 \
Manhattan 7 3 3 0 0 0 \
Manhattan 9 7 7 0 1 0 \
Manhattan 10 5 4 0 1 0 \
Manhattan 13 18 16 0 4 0 \
Manhattan 14 11 9 0 0 0 \
Manhattan 17 9 9 0 1 0 \
Manhattan 18 9 7 0 0 0 \
Manhattan 19 12 8 0 1 0 \
Manhattan 20 5 5 0 0 0 \
Manhattan 22 9 4 0 4 0 \
Manhattan 23 5 4 0 0 0 \
Manhattan 24 12 10 0 3 0 \
Manhattan 25 2 2 0 2 0 \
Manhattan 26 3 4 0 1 0 \
Manhattan 28 1 1 0 0 0 \
Manhattan 30 4 3 0 2 0 \
Manhattan 32 0 0 0 0 0 \
Manhattan 33 0 0 0 0 0 \
Manhattan 34 4 3 0 0 0"

table18_Bronx_BP = "Bronx 40 6 6 0 2 0 \
Bronx 41 2 1 0 0 0 \
Bronx 42 0 0 0 0 0 \
Bronx 43 0 0 0 0 0 \
Bronx 44 0 0 0 0 0 \
Bronx 45 1 1 0 0 0 \
Bronx 46 2 2 0 0 0 \
Bronx 47 0 0 0 0 0 \
Bronx 48 2 1 0 0 0 \
Bronx 49 1 1 0 0 0 \
Bronx 50 3 3 0 1 0 \
Bronx 52 1 1 0 0 0"

table18_Brooklyn_BP = "Brooklyn 60 0 0 0 0 0 \
Brooklyn 61 5 5 0 1 0 \
Brooklyn 62 4 4 0 1 0 \
Brooklyn 63 0 0 0 0 0 \
Brooklyn 66 6 6 0 0 0 \
Brooklyn 67 0 0 0 0 0 \
Brooklyn 68 4 4 0 1 0 \
Brooklyn 69 0 0 0 0 0 \
Brooklyn 70 3 3 0 0 0 \
Brooklyn 71 9 9 0 2 0 \
Brooklyn 72 7 6 0 4 0 \
Brooklyn 73 2 2 0 0 0 \
Brooklyn 75 3 3 0 0 0 \
Brooklyn 76 4 3 0 0 0 \
Brooklyn 77 6 5 0 0 0 \
Brooklyn 78 6 6 0 4 0 \
Brooklyn 79 4 4 0 0 0 \
Brooklyn 81 3 3 0 1 0 \
Brooklyn 83 4 4 0 1 0 \
Brooklyn 84 13 11 0 4 0 \
Brooklyn 88 2 2 0 0 0 \
Brooklyn 90 8 8 0 2 0 \
Brooklyn 94 2 2 0 0 0"

table18_Queens_BP = "Queens 100 0 0 0 0 0 \
Queens 101 0 0 0 0 0 \
Queens 102 3 1 0 2 0 \
Queens 103 0 0 0 0 0 \
Queens 104 2 2 0 0 0 \
Queens 105 0 0 0 0 0 \
Queens 106 1 1 0 0 0 \
Queens 107 1 1 0 0 0 \
Queens 108 3 3 0 0 0 \
Queens 109 6 6 0 2 0 \
Queens 110 9 7 0 0 0 \
Queens 111 0 0 0 0 0 \
Queens 112 3 2 0 1 0 \
Queens 113 0 0 0 0 0 \
Queens 114 3 3 0 0 0 \
Queens 115 3 3 0 1 0"

table18_StatenIsland_BP = "StatenIsland 120 0 0 0 0 0 \
StatenIsland 121 0 0 0 0 0 \
StatenIsland 122 1 1 0 0 0 \
StatenIsland 123 0 0 0 0 0"

table19_Manhattan_BP = "Manhattan 1 5 5 0 1 0 \
Manhattan 5 10 7 0 2 0 \
Manhattan 6 17 16 0 2 0 \
Manhattan 7 7 6 0 1 0 \
Manhattan 9 14 13 0 3 0 \
Manhattan 10 4 3 0 2 0 \
Manhattan 13 17 17 1 3 0 \
Manhattan 14 19 16 0 2 0 \
Manhattan 17 16 16 0 2 0 \
Manhattan 18 23 22 1 2 0 \
Manhattan 19 14 11 0 1 0 \
Manhattan 20 10 9 0 0 0 \
Manhattan 22 23 12 0 11 1 \
Manhattan 23 2 1 0 0 0 \
Manhattan 24 7 6 0 0 0 \
Manhattan 25 4 4 0 0 0 \
Manhattan 26 1 0 0 1 0 \
Manhattan 28 5 5 0 1 0 \
Manhattan 30 3 3 0 0 0 \
Manhattan 32 4 3 0 1 0 \
Manhattan 33 3 2 0 0 0 \
Manhattan 34 1 0 0 0 0"

table19_Bronx_BP = "Bronx 40 5 5 0 1 0 \
Bronx 41 3 3 0 0 0 \
Bronx 42 0 0 0 0 0 \
Bronx 43 2 2 0 0 0 \
Bronx 44 6 7 0 0 0 \
Bronx 45 0 0 0 0 0 \
Bronx 46 5 5 0 0 0 \
Bronx 47 0 0 0 0 0 \
Bronx 48 2 2 0 0 0 \
Bronx 49 1 1 0 0 0 \
Bronx 50 0 0 0 0 0 \
Bronx 52 10 11 0 1 0"

table19_Brooklyn_BP = "Brooklyn 60 2 2 0 1 0 \
Brooklyn 61 3 3 0 0 0 \
Brooklyn 62 6 6 0 1 0 \
Brooklyn 63 2 2 0 0 0 \
Brooklyn 66 8 8 0 0 0 \
Brooklyn 67 1 1 0 0 0 \
Brooklyn 68 1 1 0 0 0 \
Brooklyn 69 0 0 0 0 0 \
Brooklyn 70 5 5 0 0 0 \
Brooklyn 71 5 4 0 2 0 \
Brooklyn 72 5 6 0 0 0 \
Brooklyn 73 2 2 0 0 0 \
Brooklyn 75 3 3 0 0 0 \
Brooklyn 76 1 0 0 1 0 \
Brooklyn 77 3 3 0 0 0 \
Brooklyn 78 17 18 0 6 0 \
Brooklyn 79 3 3 0 0 0 \
Brooklyn 81 1 1 0 0 0 \
Brooklyn 83 7 7 0 0 0 \
Brooklyn 84 12 9 0 5 0 \
Brooklyn 88 1 1 0 0 0 \
Brooklyn 90 10 8 0 1 0 \
Brooklyn 94 1 1 0 0 0"

table19_Queens_BP = "Queens 100 0 0 0 0 0 \
Queens 101 0 0 0 0 0 \
Queens 102 2 2 0 0 0 \
Queens 103 1 1 0 0 0 \
Queens 104 5 5 0 0 0 \
Queens 105 1 1 0 1 0 \
Queens 106 1 1 0 0 0 \
Queens 107 2 2 0 0 0 \
Queens 108 5 5 0 1 0 \
Queens 109 5 5 0 0 0 \
Queens 110 6 5 0 0 0 \
Queens 111 0 0 0 0 0 \
Queens 112 0 0 0 0 0 \
Queens 113 0 0 0 0 0 \
Queens 114 2 2 0 0 0 \
Queens 115 7 6 0 0 0"

table19_StatenIsland_BP = "StatenIsland 120 2 2 0 1 0 \
StatenIsland 121 0 0 0 0 0 \
StatenIsland 122 0 0 0 0 0 \
StatenIsland 123 0 0 0 0 0"

table17_Manhattan_BB = "Manhattan 1 0 0 0 \
Manhattan 5 0 0 0 \
Manhattan 6 2 2 0 \
Manhattan 7 0 0 0 \
Manhattan 9 1 1 0 \
Manhattan 10 1 1 0 \
Manhattan 13 1 2 0 \
Manhattan 14 0 0 0 \
Manhattan 17 0 0 0 \
Manhattan 18 0 0 0 \
Manhattan 19 2 1 0 \
Manhattan 20 3 4 0 \
Manhattan 22 31 56 0 \
Manhattan 23 0 0 0 \
Manhattan 24 0 0 0 \
Manhattan 25 1 2 0 \
Manhattan 26 0 0 0 \
Manhattan 28 0 0 0 \
Manhattan 30 0 0 0 \
Manhattan 32 0 0 0 \
Manhattan 33 0 0 0 \
Manhattan 34 0 0 0"

table17_Bronx_BB = "Bronx 40 0 0 0 \
Bronx 41 0 0 0 \
Bronx 42 0 0 0 \
Bronx 43 0 0 0 \
Bronx 44 0 0 0 \
Bronx 45 0 0 0 \
Bronx 46 0 0 0 \
Bronx 47 0 0 0 \
Bronx 48 0 0 0 \
Bronx 49 0 0 0 \
Bronx 50 0 0 0 \
Bronx 52 0 0 0"

table17_Brooklyn_BB = "Brooklyn 60 0 0 0 \
Brooklyn 61 0 0 0 \
Brooklyn 62 0 0 0 \
Brooklyn 63 0 0 0 \
Brooklyn 66 1 1 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 0 0 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 1 2 0 \
Brooklyn 71 0 0 0 \
Brooklyn 72 1 1 0 \
Brooklyn 73 2 3 0 \
Brooklyn 75 0 0 0 \
Brooklyn 76 0 0 0 \
Brooklyn 77 0 0 0 \
Brooklyn 78 5 10 0 \
Brooklyn 79 2 1 0 \
Brooklyn 81 0 0 0 \
Brooklyn 83 1 1 0 \
Brooklyn 84 3 3 0 \
Brooklyn 88 0 0 0 \
Brooklyn 90 2 4 0 \
Brooklyn 94 0 0 0"

table17_Queens_BB = "Queens 100 0 0 0 \
Queens 101 0 0 0 \
Queens 102 0 0 0 \
Queens 103 0 0 0 \
Queens 104 0 0 0 \
Queens 105 0 0 0 \
Queens 106 0 0 0 \
Queens 107 0 0 0 \
Queens 108 0 0 0 \
Queens 109 0 0 0 \
Queens 110 1 1 0 \
Queens 111 0 0 0 \
Queens 112 0 0 0 \
Queens 113 0 0 0 \
Queens 114 1 1 0 \
Queens 115 1 2 0"

table17_StatenIsland_BB = "StatenIsland 120 0 0 0 \
StatenIsland 121 0 0 0 \
StatenIsland 122 0 0 0 \
StatenIsland 123 0 0 0"

table18_Manhattan_BB = "Manhattan 1 0 0 0 \
Manhattan 5 2 4 0 \
Manhattan 6 2 3 0 \
Manhattan 7 4 5 0 \
Manhattan 9 2 1 0 \
Manhattan 10 2 1 0 \
Manhattan 13 2 2 0 \
Manhattan 14 0 0 0 \
Manhattan 17 0 0 0 \
Manhattan 18 3 5 0 \
Manhattan 19 3 2 0 \
Manhattan 20 3 4 0 \
Manhattan 22 15 13 0 \
Manhattan 23 0 0 0 \
Manhattan 24 0 0 0 \
Manhattan 25 1 2 0 \
Manhattan 26 1 1 0 \
Manhattan 28 0 0 0 \
Manhattan 30 0 0 0 \
Manhattan 32 0 0 0 \
Manhattan 33 0 0 0 \
Manhattan 34 0 0 0"

table18_Bronx_BB = "Bronx 40 0 0 0 \
Bronx 41 0 0 0 \
Bronx 42 0 0 0 \
Bronx 43 0 0 0 \
Bronx 44 0 0 0 \
Bronx 45 0 0 0 \
Bronx 46 0 0 0 \
Bronx 47 0 0 0 \
Bronx 48 0 0 0 \
Bronx 49 0 0 0 \
Bronx 50 0 0 0 \
Bronx 52 0 0 0"

table18_Brooklyn_BB = "Brooklyn 60 0 0 0 \
Brooklyn 61 1 1 0 \
Brooklyn 62 1 2 0 \
Brooklyn 63 0 0 0 \
Brooklyn 66 2 2 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 0 0 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 0 0 0 \
Brooklyn 71 1 1 0 \
Brooklyn 72 0 0 0 \
Brooklyn 73 1 1 0 \
Brooklyn 75 0 0 0 \
Brooklyn 76 0 0 0 \
Brooklyn 77 0 0 0 \
Brooklyn 78 3 5 0 \
Brooklyn 79 0 0 0 \
Brooklyn 81 0 0 0 \
Brooklyn 83 0 0 0 \
Brooklyn 84 0 0 0 \
Brooklyn 88 1 1 0 \
Brooklyn 90 3 1 0 \
Brooklyn 94 2 2 0"

table18_Queens_BB = "Queens 100 1 2 0 \
Queens 101 0 0 0 \
Queens 102 0 0 0 \
Queens 103 0 0 0 \
Queens 104 0 0 0 \
Queens 105 0 0 0 \
Queens 106 0 0 0 \
Queens 107 0 0 0 \
Queens 108 0 0 0 \
Queens 109 0 0 0 \
Queens 110 0 0 0 \
Queens 111 0 0 0 \
Queens 112 0 0 0 \
Queens 113 0 0 0 \
Queens 114 1 1 0 \
Queens 115 1 2 0"

table18_StatenIsland_BB = "StatenIsland 120 0 0 0 \
StatenIsland 121 0 0 0 \
StatenIsland 122 0 0 0 \
StatenIsland 123 0 0 0"

table19_Manhattan_BB = "Manhattan 1 0 0 0 \
Manhattan 5 2 2 0 \
Manhattan 6 5 5 0 \
Manhattan 7 1 2 0 \
Manhattan 9 5 5 0 \
Manhattan 10 2 1 0 \
Manhattan 13 5 4 0 \
Manhattan 14 1 1 0 \
Manhattan 17 2 3 0 \
Manhattan 18 1 0 0 \
Manhattan 19 3 3 0 \
Manhattan 20 2 2 0 \
Manhattan 22 15 12 0 \
Manhattan 23 3 2 0 \
Manhattan 24 0 0 0 \
Manhattan 25 0 0 0 \
Manhattan 26 0 0 0 \
Manhattan 28 0 0 0 \
Manhattan 30 1 2 0 \
Manhattan 32 0 0 0 \
Manhattan 33 1 0 0 \
Manhattan 34 0 0 0"

table19_Bronx_BB = "Bronx 40 0 0 0 \
Bronx 41 0 0 0 \
Bronx 42 0 0 0 \
Bronx 43 0 0 0 \
Bronx 44 0 0 0 \
Bronx 45 0 0 0 \
Bronx 46 1 1 0 \
Bronx 47 0 0 0 \
Bronx 48 1 1 0 \
Bronx 49 0 0 0 \
Bronx 50 0 0 0 \
Bronx 52 0 0 0"

table19_Brooklyn_BB = "Brooklyn 60 0 0 0 \
Brooklyn 61 0 0 0 \
Brooklyn 62 0 0 0 \
Brooklyn 63 0 0 0 \
Brooklyn 66 0 0 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 0 0 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 1 1 0 \
Brooklyn 71 0 0 0 \
Brooklyn 72 2 2 0 \
Brooklyn 73 1 1 0 \
Brooklyn 75 1 2 0 \
Brooklyn 76 0 0 0 \
Brooklyn 77 2 1 0 \
Brooklyn 78 6 10 0 \
Brooklyn 79 2 0 0 \
Brooklyn 81 0 0 0 \
Brooklyn 83 1 1 0 \
Brooklyn 84 2 2 0 \
Brooklyn 88 1 1 0 \
Brooklyn 90 5 4 0 \
Brooklyn 94 3 3 0"

table19_Queens_BB = "Queens 100 0 0 0 \
Queens 101 0 0 0 \
Queens 102 0 0 0 \
Queens 103 1 1 0 \
Queens 104 0 0 0 \
Queens 105 0 0 0 \
Queens 106 1 1 0 \
Queens 107 0 0 0 \
Queens 108 1 2 0 \
Queens 109 0 0 0 \
Queens 110 0 0 0 \
Queens 111 0 0 0 \
Queens 112 0 0 0 \
Queens 113 0 0 0 \
Queens 114 1 1 0 \
Queens 115 2 2 0"

table19_StatenIsland_BB = "StatenIsland 120 0 0 0 \
StatenIsland 121 0 0 0 \
StatenIsland 122 0 0 0 \
StatenIsland 123 0 0 0"

table17_Manhattan_SB = "Manhattan 1 2 2 0 \
Manhattan 5 5 5 0 \
Manhattan 6 4 4 0 \
Manhattan 7 6 5 0 \
Manhattan 9 4 4 0 \
Manhattan 10 1 1 0 \
Manhattan 13 5 5 0 \
Manhattan 14 0 0 0 \
Manhattan 17 5 4 0 \
Manhattan 18 4 3 0 \
Manhattan 19 5 4 0 \
Manhattan 20 2 2 0 \
Manhattan 22 53 45 1 \
Manhattan 23 2 2 0 \
Manhattan 24 1 1 0 \
Manhattan 25 3 3 0 \
Manhattan 26 1 1 0 \
Manhattan 28 1 1 0 \
Manhattan 30 2 2 0 \
Manhattan 32 0 0 0 \
Manhattan 33 1 1 0 \
Manhattan 34 1 1 0"

table17_Bronx_SB = "Bronx 40 1 1 0 \
Bronx 41 0 0 0 \
Bronx 42 1 1 0 \
Bronx 43 1 1 0 \
Bronx 44 0 0 0 \
Bronx 45 2 2 0 \
Bronx 46 1 1 0 \
Bronx 47 0 0 0 \
Bronx 48 0 0 0 \
Bronx 49 1 1 0 \
Bronx 50 2 2 0 \
Bronx 52 0 0 0"

table17_Brooklyn_SB = "Brooklyn 60 0 0 0 \
Brooklyn 61 2 2 0 \
Brooklyn 62 1 1 0 \
Brooklyn 63 0 0 0 \
Brooklyn 66 4 4 0 \
Brooklyn 67 1 1 0 \
Brooklyn 68 3 3 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 0 0 0 \
Brooklyn 71 0 0 0 \
Brooklyn 72 14 12 0 \
Brooklyn 73 0 0 0 \
Brooklyn 75 0 0 0 \
Brooklyn 76 1 0 0 \
Brooklyn 77 4 4 0 \
Brooklyn 78 11 9 0 \
Brooklyn 79 4 3 0 \
Brooklyn 81 2 2 0 \
Brooklyn 83 4 4 0 \
Brooklyn 84 8 7 0 \
Brooklyn 88 3 3 0 \
Brooklyn 90 14 13 0 \
Brooklyn 94 7 6 0"

table17_Queens_SB = "Queens 100 1 1 0 \
Queens 101 2 2 0 \
Queens 102 4 4 0 \
Queens 103 0 0 0 \
Queens 104 1 0 0 \
Queens 105 0 0 0 \
Queens 106 1 1 0 \
Queens 107 0 0 0 \
Queens 108 7 6 0 \
Queens 109 3 3 0 \
Queens 110 4 4 0 \
Queens 111 1 1 0 \
Queens 112 2 2 0 \
Queens 113 0 0 0 \
Queens 114 7 7 0 \
Queens 115 8 7 0"

table17_StatenIsland_SB = "StatenIsland 120 0 0 0 \
StatenIsland 121 1 1 0 \
StatenIsland 122 2 2 0 \
StatenIsland 123 1 1 0"

table18_Manhattan_SB = "Manhattan 1 3 3 0 \
Manhattan 5 8 7 0 \
Manhattan 6 3 3 0 \
Manhattan 7 5 5 0 \
Manhattan 9 2 1 0 \
Manhattan 10 1 0 0 \
Manhattan 13 5 4 0 \
Manhattan 14 1 1 0 \
Manhattan 17 7 6 0 \
Manhattan 18 4 3 0 \
Manhattan 19 15 12 0 \
Manhattan 20 5 5 0 \
Manhattan 22 94 88 0 \
Manhattan 23 1 0 0 \
Manhattan 24 2 2 0 \
Manhattan 25 3 3 0 \
Manhattan 26 2 1 0 \
Manhattan 28 1 1 0 \
Manhattan 30 3 3 0 \
Manhattan 32 1 1 0 \
Manhattan 33 1 0 0 \
Manhattan 34 1 1 0"

table18_Bronx_SB = "Bronx 40 1 1 0 \
Bronx 41 1 1 0 \
Bronx 42 1 1 0 \
Bronx 43 5 2 0 \
Bronx 44 2 2 0 \
Bronx 45 1 0 0 \
Bronx 46 0 0 0 \
Bronx 47 0 0 0 \
Bronx 48 1 1 0 \
Bronx 49 2 2 0 \
Bronx 50 0 0 0 \
Bronx 52 1 1 0"

table18_Brooklyn_SB = "Brooklyn 60 2 2 0 \
Brooklyn 61 2 2 0 \
Brooklyn 62 1 1 0 \
Brooklyn 63 5 5 0 \
Brooklyn 66 0 0 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 1 1 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 1 1 0 \
Brooklyn 71 0 0 0 \
Brooklyn 72 3 3 0 \
Brooklyn 73 2 2 0 \
Brooklyn 75 1 1 0 \
Brooklyn 76 0 0 0 \
Brooklyn 77 3 1 0 \
Brooklyn 78 25 23 0 \
Brooklyn 79 3 3 0 \
Brooklyn 81 3 3 0 \
Brooklyn 83 1 1 0 \
Brooklyn 84 6 6 0 \
Brooklyn 88 5 5 0 \
Brooklyn 90 5 5 0 \
Brooklyn 94 7 7 0"

table18_Queens_SB = "Queens 100 1 1 0 \
Queens 101 0 0 0 \
Queens 102 4 4 0 \
Queens 103 1 1 0 \
Queens 104 0 0 0 \
Queens 105 0 0 0 \
Queens 106 1 1 0 \
Queens 107 0 0 0 \
Queens 108 5 5 0 \
Queens 109 1 1 0 \
Queens 110 5 5 0 \
Queens 111 2 2 0 \
Queens 112 1 0 0 \
Queens 113 1 1 0 \
Queens 114 5 5 0 \
Queens 115 3 3 0"

table18_StatenIsland_SB = "StatenIsland 120 2 2 0 \
StatenIsland 121 1 1 0 \
StatenIsland 122 0 0 0 \
StatenIsland 123 0 0 0"

table19_Manhattan_SB = "Manhattan 1 3 3 0 \
Manhattan 5 4 4 0 \
Manhattan 6 1 1 0 \
Manhattan 7 1 1 0 \
Manhattan 9 4 3 0 \
Manhattan 10 3 3 0 \
Manhattan 13 2 2 0 \
Manhattan 14 1 1 0 \
Manhattan 17 5 5 0 \
Manhattan 18 7 6 0 \
Manhattan 19 7 6 0 \
Manhattan 20 5 5 0 \
Manhattan 22 90 84 0 \
Manhattan 23 3 2 0 \
Manhattan 24 0 0 0 \
Manhattan 25 2 2 0 \
Manhattan 26 0 0 0 \
Manhattan 28 1 1 0 \
Manhattan 30 0 0 0 \
Manhattan 32 1 1 0 \
Manhattan 33 2 2 0 \
Manhattan 34 1 1 0"

table19_Bronx_SB = "Bronx 40 2 2 0 \
Bronx 41 0 0 0 \
Bronx 42 0 0 0 \
Bronx 43 3 3 0 \
Bronx 44 0 0 0 \
Bronx 45 0 0 0 \
Bronx 46 0 0 0 \
Bronx 47 3 2 0 \
Bronx 48 1 2 0 \
Bronx 49 0 0 0 \
Bronx 50 0 0 0 \
Bronx 52 1 1 0"

table19_Brooklyn_SB = "Brooklyn 60 0 0 0 \
Brooklyn 61 1 1 0 \
Brooklyn 62 0 0 0 \
Brooklyn 63 2 2 0 \
Brooklyn 66 1 1 0 \
Brooklyn 67 0 0 0 \
Brooklyn 68 0 0 0 \
Brooklyn 69 0 0 0 \
Brooklyn 70 1 1 0 \
Brooklyn 71 2 1 0 \
Brooklyn 72 1 1 0 \
Brooklyn 73 1 1 0 \
Brooklyn 75 4 4 0 \
Brooklyn 76 1 1 0 \
Brooklyn 77 2 1 0 \
Brooklyn 78 8 8 0 \
Brooklyn 79 2 0 0 \
Brooklyn 81 1 1 0 \
Brooklyn 83 3 3 0 \
Brooklyn 84 5 4 0 \
Brooklyn 88 2 2 0 \
Brooklyn 90 13 12 0 \
Brooklyn 94 3 3 0"

table19_Queens_SB = "Queens 100 2 2 0 \
Queens 101 1 3 0 \
Queens 102 3 3 0 \
Queens 103 1 1 0 \
Queens 104 2 2 0 \
Queens 105 0 0 0 \
Queens 106 1 1 0 \
Queens 107 0 0 0 \
Queens 108 7 7 0 \
Queens 109 0 0 0 \
Queens 110 2 1 0 \
Queens 111 2 2 0 \
Queens 112 4 3 0 \
Queens 113 0 0 0 \
Queens 114 3 3 0 \
Queens 115 4 3 0"

table19_StatenIsland_SB = "StatenIsland 120 2 2 0 \
StatenIsland 121 2 2 0 \
StatenIsland 122 3 3 0 \
StatenIsland 123 0 0 0"

columns = ['borough',
           'precinct',
           'crashes',
           'injuries',
           'fatalities',
           'injuries_car',
           'fatalities_car'
           ]

Table_14_BM = unify_into_df([
    table14_Manhattan_BM,
    table14_Bronx_BM,
    table14_Brooklyn_BM,
    table14_Queens_BM,
    table14_StatenIsland_BM
    ], columns)

Table_15_BM = unify_into_df([
    table15_Manhattan_BM,
    table15_Bronx_BM,
    table15_Brooklyn_BM,
    table15_Queens_BM,
    table15_StatenIsland_BM
    ], columns)

Table_16_BM = unify_into_df([
    table16_Manhattan_BM,
    table16_Bronx_BM,
    table16_Brooklyn_BM,
    table16_Queens_BM,
    table16_StatenIsland_BM
    ], columns)

Table_17_BM = unify_into_df([
    table17_Manhattan_BM,
    table17_Bronx_BM,
    table17_Brooklyn_BM,
    table17_Queens_BM,
    table17_StatenIsland_BM
    ], columns)

Table_18_BM = unify_into_df([
    table18_Manhattan_BM,
    table18_Bronx_BM,
    table18_Brooklyn_BM,
    table18_Queens_BM,
    table18_StatenIsland_BM
    ], columns)

Table_19_BM = unify_into_df([
    table19_Manhattan_BM,
    table19_Bronx_BM,
    table19_Brooklyn_BM,
    table19_Queens_BM,
    table19_StatenIsland_BM
    ], columns)

Table_14_BM.to_csv('data/KSI14_BM.csv', encoding='utf-8', index=False)
Table_15_BM.to_csv('data/KSI15_BM.csv', encoding='utf-8', index=False)
Table_16_BM.to_csv('data/KSI16_BM.csv', encoding='utf-8', index=False)
Table_17_BM.to_csv('data/KSI17_BM.csv', encoding='utf-8', index=False)
Table_18_BM.to_csv('data/KSI18_BM.csv', encoding='utf-8', index=False)
Table_19_BM.to_csv('data/KSI19_BM.csv', encoding='utf-8', index=False)

columns = ['borough',
           'precinct',
           'crashes',
           'injuries_pedestrian',
           'fatalities_pedestrian',
           'injuries',
           'fatalities',
           ]


Table_14_BP = unify_into_df([
    table14_Manhattan_BP,
    table14_Bronx_BP,
    table14_Brooklyn_BP,
    table14_Queens_BP,
    table14_StatenIsland_BP
    ], columns)

Table_15_BP = unify_into_df([
    table15_Manhattan_BP,
    table15_Bronx_BP,
    table15_Brooklyn_BP,
    table15_Queens_BP,
    table15_StatenIsland_BP
    ], columns)

Table_16_BP = unify_into_df([
    table16_Manhattan_BP,
    table16_Bronx_BP,
    table16_Brooklyn_BP,
    table16_Queens_BP,
    table16_StatenIsland_BP
    ], columns)

Table_17_BP = unify_into_df([
    table17_Manhattan_BP,
    table17_Bronx_BP,
    table17_Brooklyn_BP,
    table17_Queens_BP,
    table17_StatenIsland_BP
    ], columns)

Table_18_BP = unify_into_df([
    table18_Manhattan_BP,
    table18_Bronx_BP,
    table18_Brooklyn_BP,
    table18_Queens_BP,
    table18_StatenIsland_BP
    ], columns)

Table_19_BP = unify_into_df([
    table19_Manhattan_BP,
    table19_Bronx_BP,
    table19_Brooklyn_BP,
    table19_Queens_BP,
    table19_StatenIsland_BP
    ], columns)

Table_14_BP.to_csv('data/KSI14_BP.csv', encoding='utf-8', index=False)
Table_15_BP.to_csv('data/KSI15_BP.csv', encoding='utf-8', index=False)
Table_16_BP.to_csv('data/KSI16_BP.csv', encoding='utf-8', index=False)
Table_17_BP.to_csv('data/KSI17_BP.csv', encoding='utf-8', index=False)
Table_18_BP.to_csv('data/KSI18_BP.csv', encoding='utf-8', index=False)
Table_19_BP.to_csv('data/KSI19_BP.csv', encoding='utf-8', index=False)

columns = ['borough',
           'precinct',
           'crashes',
           'injuries',
           'fatalities',
           ]

Table_14_BB = unify_into_df([
    table14_Manhattan_BB,
    table14_Bronx_BB,
    table14_Brooklyn_BB,
    table14_Queens_BB,
    table14_StatenIsland_BB
    ], columns)

Table_15_BB = unify_into_df([
    table15_Manhattan_BB,
    table15_Bronx_BB,
    table15_Brooklyn_BB,
    table15_Queens_BB,
    table15_StatenIsland_BB
    ], columns)

Table_16_BB = unify_into_df([
    table16_Manhattan_BB,
    table16_Bronx_BB,
    table16_Brooklyn_BB,
    table16_Queens_BB,
    table16_StatenIsland_BB
    ], columns)

Table_17_BB = unify_into_df([
    table17_Manhattan_BB,
    table17_Bronx_BB,
    table17_Brooklyn_BB,
    table17_Queens_BB,
    table17_StatenIsland_BB
    ], columns)

Table_18_BB = unify_into_df([
    table18_Manhattan_BB,
    table18_Bronx_BB,
    table18_Brooklyn_BB,
    table18_Queens_BB,
    table18_StatenIsland_BB
    ], columns)

Table_19_BB = unify_into_df([
    table19_Manhattan_BB,
    table19_Bronx_BB,
    table19_Brooklyn_BB,
    table19_Queens_BB,
    table19_StatenIsland_BB
    ], columns)

Table_14_BB.to_csv('data/KSI14_BB.csv', encoding='utf-8', index=False)
Table_15_BB.to_csv('data/KSI15_BB.csv', encoding='utf-8', index=False)
Table_16_BB.to_csv('data/KSI16_BB.csv', encoding='utf-8', index=False)
Table_17_BB.to_csv('data/KSI17_BB.csv', encoding='utf-8', index=False)
Table_18_BB.to_csv('data/KSI18_BB.csv', encoding='utf-8', index=False)
Table_19_BB.to_csv('data/KSI19_BB.csv', encoding='utf-8', index=False)

columns = ['borough',
           'precinct',
           'crashes',
           'injuries',
           'fatalities'
           ]


Table_14_SB = unify_into_df([
    table14_Manhattan_SB,
    table14_Bronx_SB,
    table14_Brooklyn_SB,
    table14_Queens_SB,
    table14_StatenIsland_SB
    ], columns)

Table_15_SB = unify_into_df([
    table15_Manhattan_SB,
    table15_Bronx_SB,
    table15_Brooklyn_SB,
    table15_Queens_SB,
    table15_StatenIsland_SB
    ], columns)

Table_16_SB = unify_into_df([
    table16_Manhattan_SB,
    table16_Bronx_SB,
    table16_Brooklyn_SB,
    table16_Queens_SB,
    table16_StatenIsland_SB
    ], columns)

Table_17_SB = unify_into_df([
    table17_Manhattan_SB,
    table17_Bronx_SB,
    table17_Brooklyn_SB,
    table17_Queens_SB,
    table17_StatenIsland_SB
    ], columns)

Table_18_SB = unify_into_df([
    table18_Manhattan_SB,
    table18_Bronx_SB,
    table18_Brooklyn_SB,
    table18_Queens_SB,
    table18_StatenIsland_SB
    ], columns)

Table_19_SB = unify_into_df([
    table19_Manhattan_SB,
    table19_Bronx_SB,
    table19_Brooklyn_SB,
    table19_Queens_SB,
    table19_StatenIsland_SB
    ], columns)

Table_14_SB.to_csv('data/KSI14_SB.csv', encoding='utf-8', index=False)
Table_15_SB.to_csv('data/KSI15_SB.csv', encoding='utf-8', index=False)
Table_16_SB.to_csv('data/KSI16_SB.csv', encoding='utf-8', index=False)
Table_17_SB.to_csv('data/KSI17_SB.csv', encoding='utf-8', index=False)
Table_18_SB.to_csv('data/KSI18_SB.csv', encoding='utf-8', index=False)
Table_19_SB.to_csv('data/KSI19_SB.csv', encoding='utf-8', index=False)

