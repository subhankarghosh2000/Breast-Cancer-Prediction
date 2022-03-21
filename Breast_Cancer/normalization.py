import pandas as pd
from sklearn.preprocessing import LabelEncoder

def db():
    data=pd.read_csv("Breast_Cancer/data.csv")  #Importing .csv file into a DataFrame named data
    df=data.iloc[:,1:12]          # Cropping all rows and columns from 1 to 11
    return df

df_copy=db().copy() # coping the dataframe into a temp. variable df_copy

def get_radius_min(df_copy):
    radius_min= df_copy['radius_mean'].min()
    return radius_min

def get_radius_max(df_copy):
    radius_max= df_copy['radius_mean'].max()
    return radius_max

def get_texture_min(df_copy):
    texture_min= df_copy['texture_mean'].min()
    return texture_min

def get_texture_max(df_copy):
    texture_max= df_copy['texture_mean'].max()
    return texture_max

def get_perimeter_min(df_copy):
    perimeter_min= df_copy['perimeter_mean'].min()
    return perimeter_min

def get_perimeter_max(df_copy):
    perimeter_max= df_copy['perimeter_mean'].max()
    return perimeter_max

def get_area_min(df_copy):
    area_min= df_copy['area_mean'].min()
    return area_min

def get_area_max(df_copy):
    area_max= df_copy['area_mean'].max()
    return area_max

def get_smoothness_min(df_copy):
    smoothness_min= df_copy['smoothness_mean'].min()
    return smoothness_min

def get_smoothness_max(df_copy):
    smoothness_max= df_copy['smoothness_mean'].max()
    return smoothness_max

def get_compactness_min(df_copy):
    compactness_min= df_copy['compactness_mean'].min()
    return compactness_min

def get_compactness_max(df_copy):
    compactness_max= df_copy['compactness_mean'].max()
    return compactness_max

def get_concavity_min(df_copy):
    concavity_min= df_copy['concavity_mean'].min()
    return concavity_min

def get_concavity_max(df_copy):
    concavity_max= df_copy['concavity_mean'].max()
    return concavity_max

def get_concave_points_min(df_copy):
    concave_points_min= df_copy['concavity_mean'].min()
    return concave_points_min

def get_concave_points_max(df_copy):
    concave_points_max= df_copy['concavity_mean'].max()
    return concave_points_max

def get_symmetry_min(df_copy):
    symmetry_min= df_copy['symmetry_mean'].min()
    return symmetry_min

def get_symmetry_max(df_copy):
    symmetry_max= df_copy['symmetry_mean'].max()
    return symmetry_max

def get_fractal_dimension_min(df_copy):
    fractal_dimension_min= df_copy['fractal_dimension_mean'].min()
    return fractal_dimension_min

def get_fractal_dimension_max(df_copy):
    fractal_dimension_max= df_copy['fractal_dimension_mean'].max()
    return fractal_dimension_max

# new_value=(value-minimum value)/(maximum value - minimum value)

df_copy['radius_mean'] = (df_copy['radius_mean'] - get_radius_min(df_copy)) / (get_radius_max(df_copy)-get_radius_min(df_copy))
df_copy['texture_mean'] = (df_copy['texture_mean'] - get_texture_min(df_copy)) / (get_texture_max(df_copy)-get_texture_min(df_copy))
df_copy['perimeter_mean'] = (df_copy['perimeter_mean'] - get_perimeter_min(df_copy)) / (get_perimeter_max(df_copy)-get_perimeter_min(df_copy))
df_copy['area_mean'] = (df_copy['area_mean'] - get_area_min(df_copy)) / (get_area_max(df_copy)-get_area_min(df_copy))
df_copy['smoothness_mean'] = (df_copy['smoothness_mean'] - get_smoothness_min(df_copy)) / (get_smoothness_max(df_copy)-get_smoothness_min(df_copy))
df_copy['compactness_mean'] = (df_copy['compactness_mean'] - get_compactness_min(df_copy)) / (get_compactness_max(df_copy)-get_compactness_min(df_copy))
df_copy['concavity_mean'] = (df_copy['concavity_mean'] - get_concavity_min(df_copy)) / (get_concavity_max(df_copy)-get_concavity_min(df_copy))
df_copy['concave_points_mean'] = (df_copy['concave_points_mean'] - get_concave_points_min(df_copy)) / (get_concave_points_max(df_copy)-get_concave_points_min(df_copy))
df_copy['symmetry_mean'] = (df_copy['symmetry_mean'] - get_symmetry_min(df_copy)) / (get_symmetry_max(df_copy)-get_symmetry_min(df_copy))
df_copy['fractal_dimension_mean'] = (df_copy['fractal_dimension_mean'] - get_fractal_dimension_min(df_copy)) / (get_fractal_dimension_max(df_copy)-get_fractal_dimension_min(df_copy))

labelencoder_Y = LabelEncoder()
df_copy.iloc[:,0]=labelencoder_Y.fit_transform(df_copy.iloc[:,0].values) #convert M and B to 1 and 0 respectively

df_copy = df_copy.sample(frac=1).reset_index(drop=True) #shuffle 

#df_copy.to_csv('normalized_dataset.csv', index= False)  # importing updated dataframe back to a new csv file








