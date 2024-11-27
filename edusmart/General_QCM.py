import utils.constants.values as cv
from  utils.utils import * 
import os

relative_path = "exercices/exercice_1.txt"

full_path = cv.path_smcour + relative_path

try:
    with open(full_path, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"The file at {full_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


