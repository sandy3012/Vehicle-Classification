# Vehicle-Classification
Hello Everyone!!


Mode of Transport: Air, Water, Road and Amphibious 

This Project classifies Vehicles based on different modes of transport. The Mode of transport includes Air, Water, Road & Amphibious.


The Dataset is having 2778 images and It's trained on MobileNetV2 model using transfer learning. After Fine tuning, I am able to achieve 89.99% Validation Accuracy & 84% Training Accuracy.

Below are the parameters:
1) Learning rate = 0.0001
2) Optimizer = Adam
3) Activation = Softmax
4)fine_tune_at = 145 ( out of 155 layers)
