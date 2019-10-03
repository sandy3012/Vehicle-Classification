# Vehicle-Classification
## Hello Everyone!!


Mode of Transport: Air, Water, Road and Amphibious 

This Project classifies Vehicles based on different modes of transport. The Mode of transport includes Air, Water, Road & Amphibious.


The Dataset is having 2778 images and It's trained on MobileNetV2 model using transfer learning. After Fine tuning, I am able to achieve 89.99% Validation Accuracy & 84% Training Accuracy.

Below are the parameters:
1) Learning rate = 0.0001
2) Optimizer = Adam
3) Activation = Softmax
4) fine_tune_at = 145(out of 155 layers) with learning rate = 0.001

Due to Github's file size limitation, the parameter h5 file and the dataset are not included in this repo. To test the Flask app yourself:

* Download the h5 file [Here!](https://drive.google.com/open?id=1v-lBpP1n28lwL3986pSp0NbJRt8QzSC-)
* Save the h5 file to static folder
* In your terminal, navigate to this folder then type python main.py

Note:

* This app is using Tensorflow 2.0. Make sure you install it instead of earlier versions: pip install --user tensorflow==2.0.0-beta1

# Previews of the Flask app:
![](https://i.imgur.com/wwsBKmJ.png)
![](https://i.imgur.com/6Piqygt.png)
![](https://i.imgur.com/gxLddW8.png)
