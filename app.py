import os

model = None
model_path = os.path.join(os.getcwd(),"house_model.pkl")

if os.path.exists(model_path):
    model = pickel.load(open(model_path,"rb"))
else:
    print("model file not found")

