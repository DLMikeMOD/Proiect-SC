from csv import reader


def import_csv_layout(path):
    terrain = []
    with open(path) as map_level:
        layout = reader(map_level, delimiter=',')
        for row in layout:
            terrain.append(list(row))
        return terrain


# print(import_csv_layout('../assets/map_objects/map_FloorAssets.csv'))
