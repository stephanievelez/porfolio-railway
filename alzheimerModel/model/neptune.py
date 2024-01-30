import neptune
import os


# model = neptune.init_model(
#     name="Prediction model",
#     key="AL-MOD", 
#     project="stephanievelez1986/alzheimer-model", 
#     api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI3NmJhZDY5Mi0wYjJlLTQ0YjItYmEwOS0yZjM2ODhkYjE0YmEifQ==", # your credentials
# )


model_version = neptune.init_model_version(
    model="AL-MOD",
    project="stephanievelez1986/alzheimer-model",
    api_token="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiI3NmJhZDY5Mi0wYjJlLTQ0YjItYmEwOS0yZjM2ODhkYjE0YmEifQ==", # your credentials
)

# assign the classification model metadata to model object
model_info = {"size_limit": 10, "size_units": "MB"}
model["model"] = model_info

# upload the model to registry
absolute_path = os.path.dirname(sys.argv[0])
model_path = os.path.join(absolute_path, 'export.pkl')
model["model/signature"].upload(model_path)

# track dataset version
#model["data/train_and_test"].track_files("test.data")

# top the session
#model.stop()