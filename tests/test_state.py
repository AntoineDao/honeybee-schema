import os
from honeybee_schema.radiance.state import RadianceSubFaceStateAbridged, \
    RadianceShadeStateAbridged


# target folder where all of the samples live
root = os.path.dirname(os.path.dirname(__file__))
target_folder = os.path.join(root, 'samples', 'state')


def test_aperture_state_abridged_bsdf():
    file_path = os.path.join(target_folder, 'aperture_state_abridged_bsdf.json')
    RadianceSubFaceStateAbridged.parse_file(file_path)


def test_shade_state_abridged_snow():
    file_path = os.path.join(target_folder, 'shade_state_abridged_snow.json')
    RadianceShadeStateAbridged.parse_file(file_path)