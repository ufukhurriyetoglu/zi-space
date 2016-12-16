import cPickle as pickle
import numpy as np


max_distance_1 = 0, 0
max_distance_2 = 0, 0

def find_max_distances():
    with open("tsne.pickle", 'rb') as f:
        data = pickle.load(f)
        # xs = []
        # ys = []
        # for pair in data:
        #     xs.append(np.abs(pair[0]))
        #     ys.append(np.abs(pair[1]))
        # x = np.median(xs)
        # y = np.median(ys)
        # clump_y = -1.5 * y, 1.5 * y
        # clump_x = -1.5 * x, 1.5 * x
        x, y = np.std(data, axis=0)
        x = np.sqrt(x)
        y = np.sqrt(y)
        # x, y = np.std(data, axis=0)
        clump_x = -2*x, 2*x
        clump_y = -2 * y, 2 * y
        print clump_x, clump_y
        global max_distance_1, max_distance_2
        max_distance_1 = x, y
        # for index1 in range(len(data)):
        #     # break
        #     if data[index1][0] > clump_x[1] or data[index1][0] < clump_x[0] or data[index1][1] > clump_y[1] or \
        #                     data[index1][1] < clump_y[0]:
        #         continue
        #     for index2 in range(index1, len(data)):
        #         if data[index2][0] > clump_x[1] or data[index2][0] < clump_x[0] or data[index2][1] > clump_y[1] or \
        #                         data[index2][1] < clump_y[0]:
        #                         continue
        #         max_distance_1 = max(max_distance_1,(data[index1][0] - data[index2][0])**2 + (data[index1][1] - data[index2][1])**2)

    with open("working_l2_tsne.pickle", 'rb') as f:
        data = pickle.load(f)
        # xs = []
        # ys = []
        # for pair in data:
        #     xs.append(np.abs(pair[0]))
        #     ys.append(np.abs(pair[1]))
        # x = np.median(xs)
        # y = np.median(ys)
        x, y = np.std(data, axis=0)
        x = np.sqrt(x)
        y = np.sqrt(y)
        max_distance_2 = x, y
        # clump_y = -2 * y, 2 * y
        # clump_x = -2 * x, 2*x
        # # clump_y = -1.5 * y, 1.5 * y
        # # clump_x = -1.5 * x, 1.5 * x
        # print clump_x, clump_y
        # max_distance_2 = 0
        # for index1 in range(len(data)):
        #     if data[index1][0] > clump_x[1] or data[index1][0] < clump_x[0] or data[index1][1] > clump_y[1] or \
        #                     data[index1][1] < clump_y[0]:
        #         continue
        #     for index2 in range(index1, len(data)):
        #         if data[index2][0] > clump_x[1] or data[index2][0] < clump_x[0] or data[index2][1] > clump_y[1] or \
        #                         data[index2][1] < clump_y[0]:
        #             continue
        #         max_distance_2 = max(max_distance_2,
        #                              (data[index1][0] - data[index2][0]) ** 2 + (data[index1][1] - data[index2][1]) ** 2)
    print max_distance_1, max_distance_2


def distance(index1, index2):
    global max_distance_1, max_distance_2
    if max_distance_1 == (0, 0) and max_distance_2 == (0, 0):
        find_max_distances()
    # Normalized distance with tsne alone:
    with open("tsne.pickle", 'rb') as f:
        data = pickle.load(f)
        x1 = data[index1][0]/max_distance_1[0]
        y1 = data[index1][1]/max_distance_1[1]
        x2 = data[index2][0]/max_distance_1[0]
        y2 = data[index2][1]/max_distance_1[1]
        distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
        print "Distance using tsne without cnet is: " + str(distance)
    with open("working_l2_tsne.pickle", 'rb') as f:
        data = pickle.load(f)
        x1 = data[index1][0]/max_distance_1[0]
        y1 = data[index1][1]/max_distance_1[1]
        x2 = data[index2][0]/max_distance_1[0]
        y2 = data[index2][1]/max_distance_1[1]
        distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
        # distance = (data[index1][0] - data[index2][0]) ** 2 + (data[index1][1] - data[index2][1]) ** 2
        print "Distance using tsne with cnet is: " + str(distance)
distance(12, 24)
distance(0, 1)