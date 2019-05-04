# AWS SageMaker Ground Truth - Build Highly Accurate Datasets and Train Them with ML models
Amazon SageMaker can make it easy for customers to to efficiently and accurately label the datasets required for training machine learning systems.

Labeling datasets is a critical phase of training any supervised machine learning models. Data scientists and developers can now easily train machine learning models on datasets labeled by Amazon SageMaker Ground Truth. Amazon SageMaker Training now accepts the labeled datasets produced in augmented manifest format as input through both AWS Management Console.

Steps involved in dataset labeling tasks:

- Store your data in Amazon S3,
- Create a labeling workforce,
- Create a labeling job,
- Get to work,
- Visualize results.

Steps involved in traiing the ML model and hosting it:

- Explore the dataset
- Create the SageMaker training job
- Deploy the model onto SageMaker Endpoint
- Setup an API Gateway to connect to the Model Hosting Endpoint


## Table of Contents
1. [Architecture](#architecture)
2. [Dataset labeling tasks with Amazon SageMaker Ground Truth ](#labelsteps)

## 1. Architecture <a id="architecture"></a>

## 2. Dataset labeling tasks with Ground Truth <a id="labelsteps"></a>

### 2.1 Create S3 bucket

1. Go to Amazon S3 in AWS Console at https://s3.console.aws.amazon.com/s3/
2. Click on Create bucket.
3. Under Name and region:

* Bucket name: Enter a bucket name-your-name-raw-data (example: lab1-raw-data)
* Choose US East (N. Virginia)
* Click Next

1. Leave default values for Configure Options screen and click Next
3. Click Next, and click Create bucket.

### 2.2 Download the raw data 
1. Donwload the raw data of images from the following link: [raw-data.zip](https://www.dropbox.com/s/irk9dnml01kjmzf/raw-data.zip?dl=0)
2. Save it on your machine and unzip it
### 2.3 Storing data in Amazon S3
1. Go to Amazon S3 in AWS Console at https://s3.console.aws.amazon.com/s3/
2. Click on the bucket you've created earlier
3. Click on Upload button on the top left corner of the console
4. Click on Add files button and select all the images that you unziped earlier and click on "*Upload*" button
### 2.4 Creating manifest file for the dataset
1. Go to Amazon SageMaker Ground Truth in AWS Console at https://console.aws.amazon.com/sagemaker/groundtruth?region=us-east-1
2. Click on "*Create labeling job*"
3. In the Specify Job Details page provide the following information:
    - Because you don't have a manifest file yet, you'll create on:
        - under the section "*Input dataset location*" click on the link "*Create manifest file*"
        ![](./img/create_manifest.png)
        - In the "*Create manifest file*" popup windows provide the path to your S3 bucket and folder for the raw-data that you've created previously. Leave the "images" for data type and click on Create button.
        ![](./img/create_manifest_1.png)



