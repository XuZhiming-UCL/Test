# CEGE0096 Python Assignment_1 code
# 2021.11.19
class Geometry:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Point(Geometry):
    def __init__(self, name, x, y):
        super().__init__(name)
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class Line(Geometry):
    def __init__(self, name, point_1, point_2):
        super().__init__(name)
        self.__point_1 = point_1
        self.__point_2 = point_2


class Polygon(Geometry):
    def __init__(self, name, points):
        super().__init__(name)
        self.__points = points

    def get_points(self):
        return self.__points

    def lines(self):
        res = []
        points = self.get_points()
        point_a = points[0]
        for point_b in points[1:]:
            res.append(Line(point_a.get_name() + '-' + point_b.get_name(), point_a, point_b))
            point_a = point_b
        res.append(Line(point_a.get_name() + '-' + points[0].get_name(), point_a, points[0]))
        return res

# 1.read polygon.csv -----------------------------------------
print('read polygon.csv')
path_polygon =\
    "/Users/zmxu/Documents/GitHub/point-in-polygon-test-XuZhiming-UCL/polygon.csv"
import csv
polygon_data = list(csv.reader(open(path_polygon)))
len_row = len(polygon_data)
len_column = len(polygon_data[0])

polygon_point_series = []
for i in range(1, len_row):
    polygon_point_i = Point(int(polygon_data[1][0]), float(polygon_data[i][1]), float(polygon_data[i][2]))
    polygon_point_series.append(polygon_point_i)

polygon_test = Polygon('polygon_test', polygon_point_series)

polygon_point = polygon_test.get_points()

print(polygon_point)

# 2.read input.csv -------------------------------------------
print('read input.csv')
import csv
path_input =\
    "/Users/zmxu/Documents/GitHub/point-in-polygon-test-XuZhiming-UCL/input.csv"
input_data = list(csv.reader(open(path_input)))
len_row = len(input_data)
len_column = len(input_data[0])

point_series = []
for i in range(1, len_row):
    point_i = Point(int(input_data[i][0]), float(input_data[i][1]), float(input_data[i][2]))
    point_series.append(point_i)

# for point_id in range(1,len_row):
#    print(point_series[point_id-1].get_x(), point_series[point_id-1].get_y())

print('NOTE: Now, class \'Point\' is stored in a list called \'point_series\'.')










