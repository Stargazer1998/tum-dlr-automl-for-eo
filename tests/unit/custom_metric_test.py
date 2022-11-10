import numpy as np

from src.tum_dlr_automl_for_eo.utils import custom_metrics

random_acc_list = np.array([
    [17, 74, 77, 81, 61, 84, 10, 82, 56, 66, 44, 40, 72, 23, 6, 59,
     98, 34, 26, 5],
    [15, 67, 3, 47, 8, 82, 36, 81, 29, 37, 37, 95, 67, 6, 44, 4,
     79, 27, 12, 60],
    [30, 57, 47, 29, 23, 92, 93, 90, 55, 95, 59, 38, 1, 93, 55, 97,
     96, 86, 53, 18],
    [52, 57, 78, 86, 47, 39, 66, 59, 69, 83, 24, 95, 66, 15, 20, 10,
     32, 77, 89, 96],
    [41, 21, 28, 84, 81, 33, 85, 0, 14, 87, 98, 74, 95, 79, 20, 56,
     25, 44, 30, 37],
    [53, 87, 57, 26, 10, 74, 59, 12, 88, 82, 16, 77, 35, 19, 9, 91,
     3, 59, 55, 55],
    [37, 39, 13, 83, 81, 1, 79, 97, 10, 56, 21, 33, 13, 79, 30, 48,
     48, 22, 87, 58],
    [74, 75, 63, 16, 65, 56, 87, 76, 48, 66, 27, 17, 24, 0, 71, 4,
     63, 99, 15, 5],
    [43, 15, 44, 97, 86, 12, 16, 14, 67, 11, 21, 37, 75, 80, 31, 12,
     59, 68, 84, 26],
    [50, 31, 28, 3, 49, 66, 1, 19, 91, 51, 61, 54, 2, 80, 23, 78,
     96, 80, 31, 89],
    [25, 11, 29, 96, 7, 63, 88, 61, 74, 57, 83, 34, 53, 34, 34, 39,
     51, 64, 96, 19],
    [74, 87, 90, 59, 10, 85, 30, 27, 45, 80, 15, 31, 29, 24, 19, 81,
     35, 44, 97, 77],
    [41, 28, 15, 89, 77, 40, 63, 3, 37, 12, 99, 41, 43, 86, 98, 5,
     69, 8, 95, 74],
    [49, 99, 26, 3, 77, 86, 66, 79, 67, 15, 26, 76, 70, 97, 0, 42,
     26, 36, 15, 61],
    [29, 56, 69, 53, 17, 97, 23, 35, 99, 51, 81, 59, 2, 80, 76, 81,
     33, 65, 38, 51],
    [91, 45, 63, 17, 66, 16, 40, 41, 10, 25, 57, 16, 35, 74, 77, 63,
     63, 29, 39, 85],
    [80, 81, 61, 14, 3, 49, 50, 95, 75, 82, 66, 86, 26, 33, 76, 54,
     73, 36, 71, 57],
    [41, 50, 61, 25, 74, 34, 77, 53, 37, 30, 46, 64, 41, 63, 59, 88,
     56, 96, 34, 26],
    [24, 38, 29, 66, 2, 85, 56, 23, 74, 14, 31, 75, 20, 90, 68, 22,
     94, 60, 17, 10],
    [68, 74, 69, 31, 54, 3, 52, 6, 32, 84, 52, 91, 3, 6, 20, 9,
     23, 74, 89, 77],
    [12, 24, 37, 33, 27, 78, 75, 19, 73, 44, 1, 87, 74, 95, 95, 96,
     96, 43, 22, 49],
    [72, 59, 68, 19, 93, 68, 7, 1, 56, 92, 21, 66, 48, 48, 70, 86,
     16, 95, 38, 38],
    [21, 25, 41, 58, 49, 2, 20, 23, 9, 59, 18, 29, 18, 43, 77, 28,
     92, 79, 75, 87],
    [33, 82, 7, 75, 96, 66, 79, 64, 25, 55, 75, 86, 16, 6, 94, 9,
     27, 77, 26, 34],
    [14, 13, 96, 38, 56, 35, 18, 45, 50, 19, 42, 66, 80, 98, 86, 91,
     35, 21, 0, 53],
    [2, 63, 41, 25, 69, 56, 80, 49, 9, 88, 9, 52, 0, 21, 83, 65,
     0, 89, 34, 53],
    [23, 36, 89, 28, 70, 24, 9, 35, 41, 30, 15, 56, 2, 50, 59, 63,
     53, 42, 72, 24],
    [53, 73, 37, 48, 41, 93, 7, 26, 80, 69, 51, 83, 22, 69, 23, 31,
     79, 13, 23, 17],
    [56, 24, 72, 59, 23, 42, 37, 62, 12, 80, 94, 97, 70, 51, 38, 91,
     42, 97, 42, 7],
    [97, 63, 34, 49, 75, 63, 11, 32, 78, 8, 5, 10, 77, 58, 21, 12,
     99, 68, 70, 9],
    [5, 20, 3, 39, 57, 8, 89, 79, 53, 64, 72, 12, 7, 88, 18, 42,
     81, 18, 56, 90],
    [21, 17, 67, 80, 46, 46, 75, 29, 16, 42, 14, 45, 98, 22, 34, 39,
     14, 96, 5, 66]])
uniform_acc_list = np.array([
    [2.62694856, 2.22677609, 2.42496714, 1.66479449, 2.01615093,
     2.99399028, 0.53866163, 1.6874283, 1.40607651, 1.50406354,
     2.64354006, 2.40629568, 0.52519331, 2.20971825, 1.11381884,
     2.48761338, 1.69836191, 1.64219906, 1.47323245, 1.31408753],
    [4.99373382, 4.65334086, 3.28004878, 4.40886701, 3.78768322,
     3.45605175, 3.63156636, 3.24120605, 4.54964201, 5.93239494,
     3.88918873, 3.21846453, 5.15361905, 5.19580421, 4.9047772,
     5.46036787, 5.33425335, 5.64466818, 5.97497926, 5.368717],
    [8.44211613, 8.60947671, 6.43180949, 6.49527413, 7.58055252,
     8.58528741, 6.70361774, 6.27171213, 6.53506379, 7.96811442,
     8.61405635, 7.29780907, 7.03612388, 7.77247958, 8.70917466,
     9.24614829, 8.60282879, 8.6328314, 7.47502061, 6.34443171],
    [11.82124102, 10.85365425, 9.89590734, 12.3112366, 11.69760826,
     10.63769558, 10.41020123, 11.20915124, 11.9853197, 10.02525187,
     11.89678823, 10.51867329, 11.52716959, 11.41652158, 12.09080659,
     10.44706641, 10.65995974, 9.84641782, 11.72625304, 11.58969076],
    [15.38111806, 12.62046276, 12.74858514, 14.30148276, 12.53010866,
     14.80057355, 15.15501569, 15.35130491, 15.44675472, 15.61232909,
     14.05458281, 13.03671971, 15.26258685, 13.82796499, 13.78218509,
     13.03869664, 14.50106968, 12.89267253, 14.13344957, 13.70143561],
    [16.07151822, 16.70071773, 18.18107399, 18.41174881, 17.41532993,
     16.21339102, 17.82410479, 16.26790257, 16.31118918, 17.75247257,
     17.48919506, 18.61865529, 16.18069931, 17.74900957, 16.05578826,
     18.40174885, 18.66175767, 16.02270947, 16.9077742, 17.79064191],
    [19.6149682, 21.7278799, 21.71250428, 19.60860143, 20.06966241,
     20.99674565, 21.20881434, 21.56063789, 21.36006279, 21.70669263,
     21.333515, 19.78806753, 20.53799877, 19.51480538, 21.22781937,
     20.97889421, 20.05147341, 21.00225477, 21.34127016, 21.17463632],
    [24.78967656, 24.73879922, 24.02353685, 23.7598659, 24.44324635,
     21.96849467, 22.65749499, 23.91019792, 21.91731386, 24.36404336,
     22.4827557, 24.43440808, 23.83648908, 24.7329892, 22.22585826,
     24.50908367, 23.76134456, 24.02626722, 22.65087291, 22.80851312],
    [25.91271392, 26.32816365, 26.69539982, 25.47905973, 27.42096554,
     26.35479585, 26.80586813, 26.62240912, 26.52713205, 27.59676485,
     25.74682819, 26.65283346, 27.79943887, 26.01098776, 27.46647465,
     27.06741008, 27.83110195, 27.66628887, 27.11822473, 26.18354785],
    [30.09662312, 29.65009083, 29.00171557, 30.04681301, 30.64733,
     28.35625533, 28.96808557, 29.56767752, 28.68455785, 29.43599016,
     28.59467903, 28.67207352, 28.91593381, 30.53158926, 28.3825715,
     30.77695695, 30.5086813, 29.26775168, 28.23644901, 28.46774754],
    [32.49028052, 33.89528277, 34.29892101, 32.21186769, 32.92332633,
     33.24522119, 33.58678497, 33.62047527, 32.37939738, 32.13062953,
     33.62577732, 34.36874374, 32.45942574, 34.05004853, 31.37095745,
     34.28952269, 31.46600357, 34.13823617, 32.7310959, 31.60733823],
    [35.56638569, 37.1580977, 34.47743731, 37.24073276, 34.5236366,
     37.21539456, 36.64013847, 35.65328326, 35.9012558, 35.59219027,
     36.09995716, 34.78700595, 35.74375251, 36.46211372, 35.74649457,
     34.8312594, 35.85030723, 36.11872487, 34.4448791, 35.86628251],
    [38.13620709, 38.22232328, 37.86286638, 40.30555695, 40.18076114,
     37.66565619, 37.69013725, 37.8129216, 39.81964786, 38.33029582,
     39.04586218, 39.21323312, 39.91364615, 39.720874, 39.57382661,
     38.1496667, 39.98455332, 37.85415525, 40.06385516, 39.772336],
    [43.73343506, 43.41965093, 41.95688234, 42.0900047, 40.73355689,
     40.97260998, 42.53642844, 41.44305564, 41.80143582, 41.63466648,
     41.33663575, 43.08373224, 41.03959278, 43.30223655, 40.74238572,
     43.11949843, 43.06991181, 42.53426297, 40.71767159, 42.31086452],
    [45.91176944, 45.85743187, 44.11673682, 43.78215828, 46.21188229,
     46.84375043, 46.54333654, 43.89430005, 45.85062647, 44.57842212,
     46.82227998, 44.02418012, 46.20279088, 44.80144105, 46.86375563,
     46.28933133, 44.4923894, 44.50492328, 45.49442788, 45.98601116],
    [48.06128766, 48.14612443, 49.69356477, 48.62959122, 49.32368133,
     49.70833456, 49.29071231, 48.12414459, 47.50049488, 47.34549503,
     49.7681536, 48.14816228, 48.33791096, 49.04923439, 49.09555967,
     48.57331172, 48.90377012, 47.34695807, 46.95977603, 46.95804904],
    [51.7836747, 51.4420894, 52.78501669, 50.68962149, 51.78523335,
     51.14086572, 50.89235717, 51.81445601, 50.57802438, 52.12421816,
     50.27292254, 51.80347212, 52.80272069, 50.84803352, 51.57419826,
     51.32343812, 51.90062854, 51.99834212, 51.5742468, 50.59219123],
    [54.95998885, 54.93364258, 56.11955781, 54.25709691, 54.16812237,
     53.71543903, 55.7680241, 54.87777471, 54.63274423, 55.72268063,
     53.93239026, 53.8655792, 55.1504652, 54.29011446, 55.41148021,
     53.18577102, 56.17803448, 53.58142658, 54.67255944, 55.71685137],
    [56.94555656, 58.38317445, 58.71976199, 58.13504003, 56.31068609,
     56.86023851, 56.55728805, 56.53038272, 56.41677681, 59.00980848,
     59.26524368, 57.84970769, 58.98007043, 59.23427896, 58.55922383,
     57.1619349, 58.56762576, 56.80573856, 58.12101562, 58.33835984],
    [62.13542145, 61.85640828, 60.55407312, 59.47918095, 59.76724417,
     60.13522259, 60.93543514, 61.87307232, 59.69541024, 62.22305456,
     59.81600446, 59.67968981, 60.35438375, 61.45447246, 60.27020476,
     61.78379439, 60.7752565, 60.56580195, 60.87492423, 62.11828475],
    [64.62591455, 63.30312826, 62.58557204, 64.08872775, 63.94163446,
     64.16296138, 65.45279727, 65.03828606, 64.39484596, 65.25871994,
     62.89342806, 63.84735835, 64.12953624, 65.06458909, 63.13943829,
     63.78419357, 63.74481036, 63.93455759, 63.57721986, 62.60159886],
    [66.81790744, 66.27440172, 65.72507475, 68.25759963, 65.64764315,
     68.72111386, 65.64549381, 67.44913323, 66.10302265, 68.50445808,
     68.74820253, 66.20757767, 68.65384349, 66.66768727, 67.51366951,
     67.98173312, 67.18653809, 66.18874622, 67.64189262, 66.52058131],
    [71.86934322, 69.12254661, 71.04772096, 70.68478903, 71.64013385,
     70.93921886, 70.66095897, 70.07778371, 69.82516037, 71.03127507,
     71.45480261, 70.80781851, 71.02849778, 71.09124607, 68.85337709,
     70.70119961, 70.985337, 70.46801209, 70.18726479, 69.58083559],
    [74.21492011, 73.01399185, 73.433944, 74.34885144, 73.93228554,
     72.97334236, 72.96534395, 72.46791925, 74.48785051, 73.82988222,
     73.95220411, 73.37025419, 73.06166982, 72.25856969, 73.78580666,
     72.4663798, 73.2933816, 72.41464552, 72.27317699, 72.84930129],
    [75.38934128, 77.39252137, 75.44260394, 76.2015662, 75.57654452,
     75.91727364, 76.47164989, 76.45360605, 76.20699478, 76.21870407,
     76.647817, 77.76937733, 77.51786732, 76.45845147, 76.06767635,
     76.5599725, 78.08126908, 76.28022464, 77.66308341, 76.35620248],
    [78.48741086, 79.49876513, 78.88641581, 78.69623059, 79.69558691,
     79.22563508, 80.46343205, 79.27311173, 81.06986996, 80.52886123,
     80.54173795, 79.78535046, 81.13151268, 80.98191777, 80.33551826,
     78.60515446, 80.75298225, 80.69816715, 78.50610019, 80.01230687],
    [82.68640816, 84.34297893, 84.35886225, 83.31945374, 82.14159133,
     82.54840981, 81.55362754, 82.36326024, 81.40125093, 82.20337368,
     83.03870618, 81.25619496, 81.28284698, 84.2096345, 83.53089015,
     83.85370024, 83.7736363, 81.59334162, 82.05415603, 82.37960245],
    [86.0486093, 84.59766555, 85.94980791, 85.06772188, 87.12194188,
     86.54837407, 85.64374128, 85.44320975, 86.08822036, 86.18613162,
     84.56123514, 84.91332426, 87.46536205, 85.92873073, 86.23322455,
     86.3906087, 87.3464106, 84.51835698, 85.11826813, 85.22046879],
    [90.07579906, 90.14339094, 88.05683894, 89.61717468, 89.51558248,
     88.41364613, 90.06233122, 90.13582958, 90.59895589, 88.41927506,
     90.35826964, 89.35273486, 90.54875134, 90.11699121, 87.51787396,
     87.74867107, 88.26123373, 88.9383988, 89.92699684, 87.78619287],
    [92.08097992, 92.86051212, 91.57722664, 92.71749168, 93.32390613,
     90.83878932, 92.24464565, 92.50583094, 93.50027805, 93.42821321,
     91.91029783, 90.81826613, 91.01776114, 90.90017793, 91.36119593,
     90.95377985, 91.09951699, 91.12740645, 91.39828623, 92.35662448],
    [96.86434406, 94.09031581, 93.97205981, 94.81087958, 95.70471537,
     95.5276359, 96.02710857, 93.78269423, 95.19962957, 94.50047061,
     94.920006, 96.23143454, 96.11966797, 94.92692301, 93.85677534,
     94.36372756, 96.6986976, 95.7789533, 96.63599549, 95.88340607],
    [98.58224186, 98.49723628, 98.76602386, 98.95820234, 97.74299891,
     98.71714461, 99.22273247, 99.98304143, 99.63479503, 97.01294446,
     98.01170883, 97.44077768, 99.1688268, 97.47531859, 97.24602258,
     97.73384054, 97.51508132, 97.15074502, 97.72929575, 99.9925263]])


def test_positive_persistence():
    assert custom_metrics.positive_persistence(random_acc_list) == 0
    assert custom_metrics.positive_persistence(uniform_acc_list) == 3.637978807091713e-12


def test_negative_persistence():
    assert custom_metrics.negative_persistence(random_acc_list) == 0
    assert custom_metrics.negative_persistence(uniform_acc_list) == 3.637978807091713e-12
