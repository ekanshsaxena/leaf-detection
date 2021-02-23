#PLANT SPECIES IDENTIFICATION USING LEAF IMAGE

Collected dataset of three types of plant's leaves ("APPLE","BLUEBERRY", and "TOMATO") and trained a model using transfer
learning.

1. Divided the data into 80: 20 in which 80% data is used for training model and 20% is used
for testing the model.
2. Libraries like resnet50, sequential, globalaveragepooling2d, are imported
3. Complete data is divided into 3 classes ("apple", "blueberry", "tomato").
4. We have used pooling as average and activation function as softmax.
5. We have excluded top layer during the training.
6. We have used standard image size that is 224.

##FOR TRAINING
7. We have all total images of 1200 x 3(number of classes) = 3600 images and that’s why we
take batch_size as 12.
epoch=3600/12 =300

##FOR TESTING
8. We have all total images of 300 x 3(number of classes) = 900 images and that’s why we
take batch_size as 3.
epoch=900/3 =300

9. We get prediction by following the piece of code :
 		model.predict(test_data)
10. We can save our model by following the piece of code :
 		model.save(“keras_model.h5”)
