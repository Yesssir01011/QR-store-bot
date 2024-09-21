import random

a = [random.randint(1, 2000) for i in range(500)]
b = len(a)
print(a)
print(b)


#Көпіршік әдісі
"""import datetime
start_time = datetime.datetime.now()
def bubble_sort(nums):
    # swapped True, цикл 1 рет орындалуы үшін
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Элементтерді ауыстыру
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # swapped True келесі итерация үшін
                swapped = True
# тексеру
random_list_of_nums = [421, 29, 1275, 1169, 1020, 862, 1877,
                       639, 885, 1702, 1557, 37, 518, 1790,
                       924, 1092, 1038, 218, 1529, 1879, 1704,
                       1242, 919, 1150, 927, 1155, 931, 698,
                       308, 183, 701, 313, 1876, 486, 1921, 305,
                       376, 1839, 1950, 210, 413, 1564, 728, 1070,
                       1558, 1705, 1500, 883, 748, 159, 1651, 1748,
                       80, 1324, 728, 305, 252, 1110, 815, 591, 4,
                       1578, 1669, 1225, 1028, 910, 1775, 206, 146,
                       1695, 1769, 1436, 1465, 1774, 307, 1238, 843,
                       729, 1113, 959, 1016, 1304, 453, 789,
                       672, 101, 937, 1364, 434, 511, 136, 91, 499,
                       313, 662, 1090, 894, 1160, 180, 1512, 1520,
                       1954, 1979, 15, 1312, 1428, 76, 634, 1395,
                       1970, 1516, 1627, 1861, 476, 409, 161, 301,
                       621, 1718, 1321, 1088, 1452, 606, 597, 1370,
                       1867, 257, 192, 1814, 1986, 1902, 1719, 751,
                       1932, 757, 1555, 499, 1766, 738, 698, 1432,
                       136, 416, 1343, 406, 622, 31, 489, 1421, 1896,
                       442, 1745, 892, 749, 1000, 84, 1930, 280, 1191,
                       26, 90, 571, 357, 835, 1734, 1949, 705, 1625,
                       1748, 528, 1894, 1443, 1211, 1525, 1691, 1309,
                       1386, 1122, 177, 1617, 1653, 1911, 911, 635,
                       281, 1098, 1144, 299, 71, 1070, 1472, 340, 1697,
                       428, 539, 448, 197, 721, 322, 20, 685, 493, 752,
                       697, 1923, 945, 1616, 1317, 1154, 428, 1702, 1843,
                       328, 1769, 144, 416, 293, 1774, 781, 940, 1025,
                       1978, 1529, 1517, 404, 887, 1522, 74, 1228, 583,
                       221, 1135, 1150, 1233, 1693, 1512, 1357, 74, 1805,
                       1595, 845, 1472, 493, 1378, 1145, 1663, 1543, 808,
                       711, 492, 33, 297, 795, 1208, 1958, 917, 557, 800,
                       1477, 163, 847, 801, 681, 1900, 1098, 1802, 613,
                       273, 1945, 1496, 1340, 2, 425, 1430, 504, 1356,
                       1026, 761, 901, 1197, 1515, 620, 443, 1419, 537,
                       765, 1136, 1233, 116, 1242, 1785, 499, 1073, 1414,
                       1667, 466, 1344, 837, 1993, 96, 205, 1150, 1771,
                       1646, 552, 581, 1736, 1051, 1890, 1534, 622, 710,
                       665, 1896, 1565, 1167, 284, 97, 303, 1156, 1158,
                       377, 310, 615, 1656, 824, 1511, 326, 583, 1009,
                       864, 708, 661, 132, 115, 81, 761, 1869, 893, 1693,
                       601, 1581, 936, 1653, 438, 1393, 578, 1582, 1412,
                       196, 319, 1424, 1795, 1285, 1796, 1271, 686, 1461,
                       259, 337, 1361, 1987, 853, 1984, 1569, 1150, 1157,
                       1882, 758, 1011, 805, 1025, 298, 265, 88, 1815,
                       1074, 1515, 257, 1683, 845, 1650, 1996, 1290, 449,
                       813, 187, 1228, 635, 231, 136, 1738, 1868, 930, 411,
                       16, 1331, 500, 1565, 774, 859, 1885, 832, 29, 1417,
                       1364, 1338, 739, 476, 424, 628, 765, 1195, 1865, 1281,
                       441, 401, 1365, 1832, 1682, 162, 767, 1092, 835, 96,
                       637, 196, 625, 988, 793, 1827, 1376, 1579, 541, 944,
                       107, 1746, 1393, 1375, 1171, 627, 1166, 111, 1504,
                       153, 1637, 783, 1576, 1645, 1035, 331, 27, 685, 280,
                       543, 1907, 828, 667, 1827, 1939, 915, 1167, 391, 469,
                       396, 1022, 663, 628, 853, 194, 1166, 1492, 108, 1971,
                       196, 456, 916, 586, 1938, 275, 39, 931, 1842, 796, 1168,
                       440, 1651, 1336, 1723, 416, 1959, 878, 678, 661, 25, 585,
                       1768, 627, 353, 714]
bubble_sort(random_list_of_nums)
print(datetime.datetime.now()-start_time)"""

#2 Таңдау әдісі
"""import datetime
start_time = datetime.datetime.now()
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
                nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]

random_list_of_nums = [167, 1945, 158, 287, 1265, 496, 624, 436,
                       1808, 828, 958, 266, 1418, 1665, 1189, 1356,
                       425, 176, 251, 940, 1549, 242, 232, 1687, 1293,
                       997, 161, 646, 393, 1063, 587, 133, 1354, 934,
                       595, 805, 530, 168, 1805, 861, 431, 1673, 132,
                       441, 259, 291, 851, 598, 961, 1212, 1318, 786,
                       1463, 1236, 845, 1844, 989, 341, 1282, 118, 1531,
                       127, 1099, 1098, 389, 1135, 1212, 567, 1705, 231,
                       1647, 1660, 423, 1905, 60, 543, 1208, 80, 1223,
                       87, 223, 237, 536, 271, 604, 855, 2, 707, 379,
                       1824, 1402, 139, 842, 62, 1124, 1644, 436, 295,
                       968, 1752, 1608, 804, 1190, 567, 254, 1134, 1346,
                       1232, 840, 1756, 1074, 90, 1903, 1865, 326, 697,
                       1795, 217, 391, 1671, 1778, 1832, 352, 472, 108,
                       1640, 1186, 429, 310, 1732, 130, 1191, 1619, 1249,
                       427, 720, 244, 763, 108, 1851, 1396, 953, 1480,
                       254, 979, 1788, 590, 1863, 1350, 996, 1774, 1336,
                       342, 1593, 426, 268, 898, 746, 299, 999, 1467,
                       757, 1098, 969, 304, 550, 1491, 1404, 1522, 1480,
                       1906, 707, 1370, 779, 1191, 249, 780, 1340, 1116,
                       620, 1534, 282, 1506, 1111, 272, 317, 849, 1570,
                       229, 1503, 1941, 1325, 601, 1087, 430, 1606, 1853,
                       1428, 1772, 1372, 1032, 1538, 15, 1441, 1139, 481,
                       1109, 1962, 145, 731, 979, 820, 1442, 1719, 887,
                       1668, 1, 646, 615, 1319, 1474, 1130, 289, 1210,
                       1371, 467, 1882, 1002, 1495, 391, 658, 949, 243,
                       489, 1215, 548, 1603, 1196, 1262, 1599, 492, 1088,
                       1043, 1648, 861, 25, 1905, 30, 1623, 277, 1323, 390,
                       735, 264, 1316, 182, 1368, 1912, 477, 433, 438, 1555,
                       767, 1581, 617, 49, 1116, 1041, 236, 1309, 1492,
                       1022, 1687, 1681, 1813, 1390, 1363, 1868, 1952, 1837,
                       1758, 56, 1464, 344, 545, 919, 1316, 1439, 501, 702,
                       1062, 579, 1399, 285, 1880, 1759, 492, 788, 152,
                       1062, 151, 1008, 1551, 46, 957, 659, 934, 1636, 478,
                       1175, 1294, 1064, 1662, 1507, 100, 40, 416, 1686,
                       414, 1440, 313, 1927, 278, 1943, 1465, 1153, 1301,
                       1585, 1377, 1403, 1353, 121, 1617, 1764, 1179, 453,
                       1114, 1453, 1914, 916, 983, 1282, 1125, 269, 1175,
                       405, 1699, 945, 527, 458, 1142, 961, 662, 864, 1435,
                       1792, 1935, 505, 1013, 620, 394, 244, 271, 1275,
                       1713, 331, 905, 881, 1339, 1585, 1816, 1252, 976,
                       84, 226, 1744, 955, 1043, 904, 1666, 898, 391, 1289,
                       1659, 1080, 1161, 1480, 1938, 1747, 1464, 1116,
                       372, 1233, 45, 1360, 1118, 59, 471, 1793, 1672,
                       1362, 1633, 1651, 1088, 1731, 157, 1602, 1885,
                       481, 1676, 1269, 338, 1061, 948, 1200, 1250, 1645,
                       1014, 385, 954, 770, 352, 834, 842, 1097, 904,
                       893, 1013, 627, 459, 557, 236, 294, 1359, 1057,
                       188, 1684, 151, 816, 543, 478, 71, 1610, 1771, 717,
                       943, 533, 1509, 1213, 1014, 642, 1982, 814, 999,
                       422, 1020, 1715, 1856, 5, 1914, 1308, 276, 40,
                       993, 484, 815, 1858, 261, 623, 695, 984, 1183,
                       583, 1252, 1446, 1302, 1416, 449, 259, 32, 555,
                       290, 1063, 192, 659, 970, 1781, 673, 991, 150,
                       1490, 940, 1152, 1011, 1684, 1838, 386, 1884, 934,
                       1702]

selection_sort(random_list_of_nums)
print(random_list_of_nums)
print(datetime.datetime.now()-start_time)"""



#Жылдам сұрыптау
"""import datetime
start_time = datetime.datetime.now()
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    v = nums[len(nums) // 2]
    left = [x for x in nums if x < v]
    middle = [x for x in nums if x == v]
    right = [x for x in nums if x > v]
    return quick_sort(left) + middle + quick_sort(right)

random_list_of_nums = [496, 465, 923, 699, 1918, 439, 228, 877,
                       848, 965, 795, 1011, 748, 1410, 360, 1998,
                       692, 183, 829, 1336, 143, 180, 223, 1403,
                       1726, 972, 243, 1259, 1740, 1329, 1964,
                       1071, 485, 1534, 1360, 395, 1673, 1905,
                       319, 1182, 1003, 982, 1816, 1760, 1527,
                       1301, 1676, 508, 1199, 1897, 1933, 1685,
                       973, 983, 795, 1342, 1202, 1729, 1347,
                       423, 1468, 286, 1729, 136, 977, 1398, 1784,
                       1853, 1034, 1784, 482, 1110, 859, 712, 302,
                       1140, 955, 1915, 44, 570, 1253, 1531, 1604,
                       1669, 710, 1326, 502, 1994, 113, 731, 906, 743,
                       1445, 586, 1112, 159, 754, 1647, 1946, 1263, 1913,
                       263, 389, 1494, 1882, 596, 7, 1831, 651, 840,
                       144, 1657, 1163, 568, 780, 151, 930, 1337, 444,
                       242, 1711, 193, 1525, 1513, 1191, 1648, 843,
                       927, 725, 1474, 1951, 978, 23, 1737, 803, 60,
                       1447, 855, 1445, 1311, 1838, 1802, 3, 331,
                       173, 1069, 128, 1333, 495, 1952, 1328, 610,
                       928, 164, 302, 1954, 1423, 1879, 1546, 1288,
                       48, 433, 799, 1765, 1203, 1776, 833, 1042, 1558,
                       1007, 1910, 628, 1405, 274, 1104, 1688, 1718,
                       1844, 668, 861, 1079, 1847, 1627, 838, 786, 881,
                       1764, 363, 862, 900, 1915, 1339, 1823, 557,
                       623, 1125, 1815, 374, 193, 1302, 1275, 342,
                       424, 1413, 800, 982, 261, 759, 1349, 1163, 500,
                       1878, 164, 254, 644, 351, 1809, 1229, 449, 697,
                       1111, 1247, 1237, 1419, 1606, 834, 460, 704,
                       1504, 1092, 1799, 868, 1619, 794, 1923, 1661,
                       1478, 1438, 1934, 1275, 1775, 1011, 1431, 477,
                       1394, 657, 608, 384, 1055, 132, 1885, 856, 1178,
                       1748, 45, 1472, 1657, 983, 1400, 818, 703, 1411,
                       1301, 783, 644, 1649, 1790, 129, 1850, 32, 818,
                       1157, 281, 1879, 1862, 1697, 763, 366, 1250, 996,
                       978, 1408, 449, 1045, 357, 201, 875, 1191, 47,
                       1850, 1817, 102, 412, 879, 1578, 1693, 756, 328,
                       1149, 1725, 1758, 1267, 689, 595, 94, 164, 1188,
                       622, 1920, 956, 674, 1312, 714, 792, 1097, 322,
                       276, 1883, 719, 320, 1689, 250, 1195, 582, 1024,
                       1535, 1086, 682, 357, 514, 1690, 1085, 177, 1190,
                       214, 1875, 1156, 1020, 445, 1504, 208, 1367,
                       1194, 1170, 910, 1478, 1557, 1462, 1220, 1828,
                       332, 198, 799, 345, 1340, 611, 952, 1042, 921,
                       274, 15, 1108, 30, 805, 1550, 1628, 1258, 1551,
                       1449, 1513, 1360, 681, 37, 154, 480, 679, 174,
                       1898, 57, 1069, 1319, 1587, 1625, 1580, 368, 947,
                       582, 938, 744, 582, 232, 1380, 7, 1838, 1911,
                       1909, 202, 936, 1360, 1552, 986, 825, 703, 401,
                       660, 1069, 1063, 1298, 78, 1445, 1108, 1110, 317,
                       1692, 1891, 162, 1384, 1009, 1652, 1255, 234, 813,
                       537, 515, 985, 649, 1394, 1582, 1231, 1130, 1416,
                       250, 834, 9, 528, 1374, 1229, 419, 420, 1420, 621,
                       925, 1943, 1191, 1798, 56, 169, 991, 1670, 113,
                       1457, 1365, 948, 1514, 527, 1683, 1942, 998, 1865,
                       279, 507, 1991, 654, 1903, 1268, 1926, 879, 9,
                       1700, 103, 824, 748, 1504, 1400, 783, 1630, 500,
                       1230, 673, 1477, 1577, 716, 1811, 1549, 1681, 613,
                       1541, 1662, 378, 1305, 454, 82, 1092, 542, 1654,
                       693, 1686, 507, 1852, 977]

sorted_nums = quick_sort(random_list_of_nums)

print(datetime.datetime.now() - start_time)"""

#Кірістіру
"""import datetime

start_time = datetime.datetime.now()

def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

random_list_of_nums =[61, 52, 429, 353, 148, 82, 41, 118, 382, 25,
                      132, 473, 235, 300, 470, 486, 13, 298, 409, 120,
                      71, 245, 381, 239, 1, 89, 266, 371, 51, 305, 274,
                      397, 479, 15, 190, 329, 383, 145, 231, 196, 40, 179,
                      12, 23, 96, 308, 312, 101, 341, 101, 482, 141, 360,
                      118, 234, 475, 10, 171, 277, 168, 1, 292, 421, 124,
                      319, 278, 486, 401, 92, 157, 28, 75, 96, 226, 449,
                      314, 165, 361, 286, 185, 260, 191, 450, 244, 397,
                      192, 34, 25, 85, 458, 52, 297, 108, 294, 352, 411,
                      484, 267, 32, 425, 206, 210, 200, 156, 13, 386, 177,
                      259, 246, 346, 326, 68, 103, 206, 388, 132, 147, 193,
                      259, 89, 361, 333, 211, 20, 140, 262, 181, 91, 374,
                      469, 466, 230, 388, 153, 388, 144, 96, 15, 324, 128,
                      340, 485, 222, 238, 358, 50, 476, 274, 362, 403, 199,
                      148, 79, 246, 156, 453, 316, 497, 214, 426, 53, 210,
                      70, 55, 119, 409, 107, 52, 74, 476, 88, 210, 333, 141,
                      417, 467, 194, 309, 478, 13, 372, 318, 146, 53, 434,
                      85, 360, 348, 215, 34, 244, 304, 310, 110, 313, 485,
                      50, 169, 256, 192, 146, 282, 47, 449, 24, 436, 25,
                      414, 206, 312, 57, 209, 266, 7, 60, 176, 460, 297,
                      288, 179, 141, 400, 121, 388, 174, 49, 178, 182,
                      196, 140, 175, 12, 46, 36, 210, 167, 422, 133, 408,
                      259, 456, 461, 366, 28, 56, 68, 285, 244, 172, 323,
                      259, 8, 372, 254, 168, 303, 117, 272, 30, 124, 366,
                      468, 3, 291, 115, 437, 204, 245, 327, 302, 99, 459,
                      93, 442, 490, 343, 134, 362, 430, 335, 420, 3, 359,
                      3, 277, 456, 331, 197, 153, 456, 138, 267, 281, 401,
                      214, 57, 120, 289, 3, 357, 333, 401, 272, 85, 87, 303,
                      185, 80, 364, 333, 81, 226, 483, 189, 169, 112, 418,
                      213, 372, 294, 138, 178, 21, 88, 343, 481, 467, 260,
                      243, 170, 336, 141, 397, 243, 358, 218, 267, 32, 23,
                      334, 120, 100, 500, 483, 115, 428, 197, 399, 495, 147,
                      38, 371, 31, 464, 230, 139, 62, 1, 157, 358, 98, 156,
                      376, 49, 103, 226, 186, 341, 493, 86, 332, 147, 227,
                      217, 471, 476, 462, 237, 63, 54, 145, 95, 222, 154,
                      497, 281, 207, 209, 45, 265, 409, 410, 42, 378, 420,
                      400, 276, 389, 279, 341, 62, 348, 67, 415, 67, 209,
                      453, 24, 163, 201, 94, 135, 71, 371, 482, 172, 122,
                      79, 93, 96, 342, 341, 483, 359, 234, 173, 437, 234,
                      453, 399, 386, 491, 314, 189, 322, 43, 215, 180, 488,
                      279, 411, 197, 171, 32, 187, 309, 230, 96, 210, 341,
                      142, 326, 309, 112, 94, 428, 106, 71, 251, 493, 106,
                      457, 349, 106, 217, 90, 290, 245, 363, 27, 46, 45,
                      213, 383, 450, 219, 129, 362, 332, 210, 478, 343,
                      305, 404, 99, 198, 138, 284, 22, 251, 207, 172, 413,
                      441, 437, 341, 158, 102, 59, 186]

insertion_sort(random_list_of_nums)
print(datetime.datetime.now() - start_time)"""

#sorted
"""import datetime
start_time = datetime.datetime.now()
def merge(left_list, right_list):

    sorted_list = []
left_list_index = right_list_index = [158, 1453, 393, 1834, 722, 1877,
                                      1408, 1076, 484, 18, 271, 903, 1097,
                                      1335, 1305, 1598, 277, 448, 1100, 
                                      1172, 26, 1371, 862, 1319, 1549, 
                                      1327, 808, 1886, 252, 964, 1034,
                                      307, 239, 1864, 1942, 1796, 623, 
                                      544, 1720, 1125, 1526, 1583, 162, 
                                      1271, 1348, 949, 1144, 445, 1552, 
                                      33, 1019, 681, 436, 151, 747, 1150,
                                      1733, 1072, 936, 28, 877, 256, 1222,
                                      1020, 1374, 1237, 575, 191, 1759, 
                                      1888, 1954, 1469, 1449, 1605, 342,
                                      233, 1908, 170, 294, 1622, 1782,
                                      926, 1599, 1974, 1339, 169, 275, 
                                      1009, 82, 1198, 1249, 811, 696, 
                                      1335, 360, 625, 1897, 880, 1874, 
                                      1410, 1311, 971, 820, 1522, 756,
                                      308, 867, 221, 1062, 1421, 1155, 
                                      1860, 1730, 971, 1757, 1785, 1372,
                                      331, 803, 697, 655, 74, 480, 1576,
                                      1913, 1873, 527, 9, 1941, 1912, 
                                      522, 1415, 177, 1420, 1981, 1435, 
                                      495, 687, 272, 644, 1549, 1938, 
                                      1311, 652, 949, 1390, 818, 45, 
                                      1874, 1294, 1828, 1395, 1229, 469,
                                      1287, 923, 1061, 837, 766, 87, 
                                      1652, 616, 1345, 220, 982, 1423,
                                      1921, 927, 1347, 1332, 299, 389, 
                                      770, 122, 316, 1783, 1608, 188, 
                                      1123, 719, 1953, 1627, 1104, 585, 
                                      1982, 1376, 383, 828, 1040, 401, 
                                      1647, 796, 390, 760, 581, 1552, 
                                      1103, 556, 1610, 120, 79, 153, 192,
                                      126, 1175, 1977, 1317, 1580, 1898,
                                      264, 1954, 1056, 270, 308, 1127,
                                      276, 1047, 1842, 187, 1771, 1670, 
                                      633, 927, 1773, 1582, 663, 110, 
                                      1469, 1476, 1732, 1907, 1442, 642,
                                      441, 1513, 1029, 1770, 1601, 1178,
                                      569, 165, 1994, 1995, 1461, 677, 
                                      1362, 1066, 403, 1416, 402, 1097, 
                                      1436, 504, 1134, 1892, 1329, 1990, 
                                      658, 767, 1832, 643, 1792, 48, 
                                      1197, 1066, 31, 594, 979, 1508, 
                                      1983, 212, 469, 231, 904, 1923, 
                                      1641, 784, 1701, 1864, 748, 1926, 
                                      1483, 1326, 189, 611, 675, 992, 
                                      1427, 44, 1066, 1538, 1059, 1941, 
                                      191, 679, 1292, 1332, 1985, 1467,
                                      667, 497, 1857, 1694, 1606, 1678, 
                                      1194, 1870, 1380, 1989, 732, 1003,
                                      1730, 469, 249, 1277, 738, 1096, 
                                      828, 1742, 1491, 761, 626, 1115, 
                                      1520, 10, 1671, 1444, 683, 1437, 
                                      1650, 168, 1937, 1001, 1775, 1215,
                                      323, 636, 1280, 917, 330, 838, 869,
                                      1993, 539, 1921, 171, 1741, 1561, 
                                      1918, 41, 803, 1657, 1180, 356, 1012,
                                      1270, 1472, 512, 474, 1074, 1012, 
                                      1861, 237, 332, 43, 1087, 1324, 355,
                                      1336, 1628, 1839, 510, 1299, 1867, 
                                      1204, 1002, 1317, 1250, 354, 1680, 
                                      1306, 747, 795, 157, 977, 1382, 1845,
                                      97, 557, 565, 856, 1783, 1271, 971,
                                      1303, 553, 398, 1837, 610, 1628, 494,
                                      676, 793, 1653, 1005, 744, 1026, 1195,
                                      1289, 1372, 201, 1982, 1160, 1014, 
                                      158, 1976, 320, 1811, 554, 776, 600, 
                                      1200, 746, 403, 1159, 1235, 381, 
                                      1380, 892, 1824, 1852, 732, 544, 
                                      94, 258, 28, 426, 595, 707, 926, 
                                      1556, 1100, 376, 1158, 74, 1609, 
                                      1254, 1532, 382, 780, 1242, 1551, 
                                      1223, 36, 962, 557, 1727, 336, 1302, 
                                      1808, 118, 247, 1612, 1607, 1820, 
                                      1968, 467, 1720, 1460, 1554, 1707, 
                                      115, 1946, 1372, 1347, 1141, 888, 
                                      337, 1441, 1339, 1770, 676, 739, 
                                      770, 191, 747, 1046, 950, 1378,
                                      983, 409, 1910, 1963, 800, 339, 
                                      2, 1089, 1326, 1598, 1853]
    left_list_length, right_list_length = len(left_list), len(right_list)



    for _ in range(left_list_length + right_list_length):

        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:

                sorted_list.append(left_list[left_list_index])

                left_list_index += 1

            else:

                sorted_list.append(right_list[right_list_index])

                right_list_index += 1
            
            elif left_list_index == left_list_length:

            sorted_list.append(right_list[right_list_index])

            right_list_index += 1


        elif right_list_index == right_list_length:

            sorted_list.append(left_list[left_list_index])

            left_list_index += 1


sort(random_list_of_nums)
print(datetime.datetime.now() - start_time)"""







#3
import random
a = [random.randint(150, 170) for i in range(15)]
print(a)
a.sort()
oqushy_10 = a[9]

print("10 шы оқушының бойы ", oqushy_10)