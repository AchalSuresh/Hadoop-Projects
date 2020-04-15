# Utilizing Spark to identify Spam emails.

## The project utilizes Pyspark environment and AWS to check spam emails.

# The input folder contains 4 sets of test set to check for project

On training the model using the data set that I collected, the model was able to correctly predict whether the email was Spam or not spam.

Input
posTestExample = tf.transform("Achal Suresh,Enter your details & enjoy UPTO 70% Off on Car".split(" ")) #Positive Test Sample
negTestExample = tf.transform("Hi everyone,Instructions for uploading project #1 can be found in ".split(" "))

# Now use the learned model to predict spam/ham for new emails.
print ("Prediction for positive test example: %g" % model_test.predict(posTestExample))
print ("Prediction for negative test example: %g" % model_test.predict(negTestExample))

Output:
1
0

The model is able to rightly identify whether the email is spam or not spam is because the training data had content similar to the test samples and the appearance of similar words such as UPTO and off in the Postive Test Sample.

