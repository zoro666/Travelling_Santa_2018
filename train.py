# Laod all the libraries
import numpy as np 
import pandas as pd 
from argparse import ArgumentParser
from model2 import model

def extract_data(file):
	""" Extract data from a csv file into a dataframe"""
	df = pd.read_csv(file)
	# Drop first column which is composed of indices of the file
	df = df.drop(df.columns[0], axis=1)
	return df

def train_model(path, verbose = False):
	""" Extract data and train model"""
	# Extract data from composite citis file
	composite_city_df = extract_data(path+"composite_city.csv")
	# Extract data from prime cities file
	prime_city_df = extract_data(path+"prime_city.csv")
	# Create arrays from dataframes
	comp_city_array = np.array(composite_city_df.iloc[0:50, 0:3])
	prime_city_array = np.array(prime_city_df.iloc[0:20, 0:3])
	# Find the start point
	start_pt = comp_city_array[0,:]
	# Delete the first point from array
	comp_city_array = np.delete(comp_city_array, 0, 0)
	# Find end point
	end_pt = start_pt
	# Find the route
	route, path_dist = model(start_pt,
									comp_city_array,
									prime_city_array,
									end_pt,
									verbose = verbose)
	print(route,path_dist)
	return route, path_dist

def save(filename, route, path_dist):
	""" Save the results in a file"""
	# Save output of model
	with open(filename, 'w') as f:
	    for s in route:
	        f.write(str(s) + '\n')
	    f.write(str(path_dist) + '\n')

def main(path, verbose = False):
	""" Run the main code"""
	route, path_dist = train_model(path, verbose = verbose)
	# Save the results
	save(path + "model2_output.txt", route, path_dist)

if __name__ == "__main__":
	# Read the filepath for csv files from command line
	parser = ArgumentParser()
	# First input path where files are stored
	parser.add_argument("-p",
						"--path", 
						help="input the filepath", 
						type = str)
	args = parser.parse_args()
	path = args.path
	# Execute main
	main(path, verbose = True)

