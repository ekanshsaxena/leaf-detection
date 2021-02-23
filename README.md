#PLANT SPECIES IDENTIFICATION USING LEAF IMAGE

Collected dataset of three types of plant's leaves ("APPLE","BLUEBERRY", and "TOMATO") and trained a model using transfer
learning.

1. Divided the data into 80: 20 in which 80% data is used for training model and 20% is used
for testing the model.
2. Libraries like resnet50, sequential, globalaveragepooling2d, are imported
3. Complete data is divided into 3 classes ("apple", "blueberry", "tomato").
4. Set pooling as "average" and activation function as "softmax".
5. Excluded top layer for the training.
6. Set image size as "224" during the pre-processing of the image.

##FOR TRAINING
7. There are total 1200 x 3(number of classes) = 3600 images for training and batch_size is set at 12: Epoch=3600/12 = 300

##FOR TESTING
8. There are total 300 x 3(number of classes) = 900 images for testing and batch_size is set at 3: Epoch=900/3 =300

9. We get prediction by following the piece of code :
 		model.predict(test_data)
10. We can save our model by following the piece of code :
 		model.save(“keras_model.h5”)
