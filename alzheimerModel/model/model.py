import json
import urllib.request
import numpy as np

import pathlib #you need all 3 requirements.txt


#adding due to posixerror
#posix_backup = pathlib.PosixPath
# try:
#     pathlib.PosixPath = pathlib.WindowsPath
#     learn_inf = load_learner(EXPORT_PATH)
# finally:
#     pathlib.PosixPath = posix_backup

temp = pathlib.PosixPath #otherwise you'll be an posixerror
pathlib.PosixPath = pathlib.PureWindowsPath  #when loading the fastai model
from django.shortcuts import render
import os
import fastbook
fastbook.setup_book()
from fastbook import *
from fastai.vision.widgets import *

def loading_path():
    absolute_path = os.path.dirname(sys.argv[0])
    model_path = os.path.join(absolute_path, 'export.pkl')

    #load model
    learner = load_learner(model_path)
    return learner

# def getRelativePath(relative_path):
#     absolute_path = os.path.dirname(sys.argv[0])
#     full_path = os.path.join(absolute_path, relative_path)
#     check_path_exists(full_path)



# # with open(model_path, 'rb') as f:
# #     #model = pickle.load(f)
# learn_inf = load_learner(model_path)
    
# predict = learn_inf.predict('C:\my-python-projects\learning_log\alzheimerModel\model\data\test\MildDemented\26 (19).jpg')
