from . import normalization as no
from . import XG_Boost as xg

def get_values(radius,texture,perimeter,area,smoothness,compactness,concavity,c_points,symmetry,f_dimension):

	radius_new=(float(radius) - no.get_radius_min(no.db())) / (no.get_radius_max(no.db())-no.get_radius_min(no.db()))
	texture_new=(float(texture) - no.get_texture_min(no.db())) / (no.get_texture_max(no.db())-no.get_texture_min(no.db()))
	perimeter_new=(float(perimeter) - no.get_perimeter_min(no.db())) / (no.get_perimeter_max(no.db())-no.get_perimeter_min(no.db()))
	area_new=(float(area) - no.get_area_min(no.db())) / (no.get_area_max(no.db())-no.get_area_min(no.db()))
	smoothness_new=(float(smoothness) - no.get_smoothness_min(no.db())) / (no.get_smoothness_max(no.db())-no.get_smoothness_min(no.db()))
	compactness_new=(float(compactness) - no.get_compactness_min(no.db())) / (no.get_compactness_max(no.db())-no.get_compactness_min(no.db()))
	concavity_new=(float(concavity) - no.get_concavity_min(no.db())) / (no.get_concavity_max(no.db())-no.get_concavity_min(no.db()))
	concave_points_new=(float(c_points) - no.get_concave_points_min(no.db())) / (no.get_concave_points_max(no.db())-no.get_concave_points_min(no.db()))
	symmetry_new=(float(symmetry) - no.get_symmetry_min(no.db())) / (no.get_symmetry_max(no.db())-no.get_symmetry_min(no.db()))
	fractal_dimension_new=(float(f_dimension) - no.get_fractal_dimension_min(no.db())) / (no.get_fractal_dimension_max(no.db())-no.get_fractal_dimension_min(no.db()))

	data_list=[radius_new,texture_new,perimeter_new,area_new,smoothness_new,compactness_new,concavity_new,concave_points_new,symmetry_new,fractal_dimension_new]

	return xg.input_fetch(data_list)
