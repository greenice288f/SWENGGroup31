from roboflow import Roboflow
#if you get an error of Roboflow missing
#use pip install Roboflow, if pip is missing, welp then download pip, through pwsh

rf = Roboflow(api_key="Tao36WXLMwnYXJt3uFaj")
project = rf.workspace("cigarette-c6554").project("cigarette-ghnlk")
#currently we model 3 is the best we have
model = project.version(3).model

# infer on a local image
print(model.predict("155135c1-7f8d-49b3-9a91-2db7572842ae.jpg", confidence=40, overlap=30).json())

#visualize your prediction
model.predict("155135c1-7f8d-49b3-9a91-2db7572842ae.jpg", confidence=40, overlap=30).save("resultv3.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())