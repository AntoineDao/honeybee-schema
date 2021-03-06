from honeybee_schema.energy.constructionset import ConstructionSetAbridged, \
    WallSetAbridged, RoofCeilingSetAbridged, FloorSetAbridged, ApertureSetAbridged, \
    DoorSetAbridged
import os

# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'samples', 'construction_set')


def test_constructionset_complete():
    file_path = os.path.join(target_folder, 'constructionset_complete.json')
    ConstructionSetAbridged.parse_file(file_path)


def test_constructionset_partial_exterior():
    file_path = os.path.join(target_folder, 'constructionset_partial_exterior.json')
    ConstructionSetAbridged.parse_file(file_path)
