from csv import reader
from os import walk
import pygame


def import_csv_layout(path):
    terrain = []
    with open(path) as map_level:
        layout = reader(map_level, delimiter=',')
        for row in layout:
            terrain.append(list(row))
        return terrain


def import_folder(path):
    surface_list = []

    for mainfolder,emptylist,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surface)

    return surface_list



# print(import_folder("../assets/grass"))
# print(import_csv_layout('../assets/map_objects/map_FloorAssets.csv'))
