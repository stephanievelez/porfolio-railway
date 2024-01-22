from django.apps import AppConfig
import html
import pathlib
import os, sys
import pickle

class AlzheimermodelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alzheimerModel'

# absolute_path = os.path.dirname(sys.argv[0])
# model_path = os.path.join(absolute_path, 'export.pkl')

# with open(model_path, 'rb') as f:
#     model = pickle.load(f)
# #learn_inf = load_learner(model_path)
    
# #predict = learn_inf.predict('C:\my-python-projects\learning_log\alzheimerModel\model\data\test\MildDemented\26 (19).jpg')



# class WebappConfig(AppConfig):
#     name = 'alzheimer Predictor'
#     MODEL_PATH = model #Path("model")
#     #BERT_PRETRAINED_PATH = Path("model/uncased_L-12_H-768_A-12/")
#     #LABEL_PATH = Path("label/")
#     predictor = MODEL_PATH.predict()