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

### 2.1 Create S3 buckets

1. Go to Amazon S3 in AWS Console at https://s3.console.aws.amazon.com/s3/
2. Click on Create bucket.
3. Under Name and region:

* Bucket name: Enter a bucket name-your-name-raw-data (example: lab1-raw-data)
* Choose US East (N. Virginia)
* Click Next

1. Leave default values for Configure Options screen and click Next
3. Click Next, and click Create bucket.
4. Go back to Amazon S3 in AWS Console at https://s3.console.aws.amazon.com/s3/ 
5. Click on Create bucket.
6. Under Name and region:

* Bucket name: Enter a bucket name-your-name-label-output (example: lab1-label-output)
* Choose US East (N. Virginia)
* Click Next

7. Leave default values for Configure Options screen and click Next
8. Click Next, and click Create bucket.

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
        - Once the manifest creation process completes it'll provide number of object found and option to use the manifest. Click on "*Use this manifest*" button
        ![](./img/create_manifest_2.png)

### 2.5 Creating the labeling Job
1. You'll be back on the main Job Details screen. Type the name of the job (example: lab1-labeling-job)
2. Under the "*Output dataset location*" put the path of the bucker you've created previsouly for the label output (example: s3://lab1-label-output)
3. Under "*IAM Role*" drop down the "*Choose option*" and select "*Create a new role*"
4. In the popup window select "*Any S3 bucket*" ![](./img/create_manifest_3.png) and click on Create button.
5. Under the "*Task type*" select Image Classification and click on next
6. Under the "*Select Workers and configure tool*" provide the following information:

Amazon SageMaker Ground Truth gives us different options:

- Public workforce, backed by Amazon Mechanical Turk,
- Private workforce, backed by internal resources,
- Vendor workforce, backed by third-party resources.

The first option is probably the most scalable one. However, the last two may be a better fit if your job requires confidentiality, service guarantees, or special skills.

7. Workers: Select Private as you will send the labeling task to an internal team to your organization. In this lab the team will be yourself:
- Team Name: put a name for your team (example: lab1-private-team)
- Under Invite private annotators add your email address and any other team member of your group in the lab/workshop
- (Optional) Under Organization put your company name and divison
- (Optional) Leave contact email address empty

8. Under "*Image classification labeling tool*" you'll see a preview of the object in the raw dataset. Add the following label. example:
    - RH
    - LH
    - Add some decription on the it as well: (example: Classify the below image using the part number as well as the label on the part.)
    - Click on "*Submit*" at the bottom of the page to send the labeling job to the worker. In this case yourself from the email address.
![](./img/create_manifest_5.png)

### 2.6 Start working on the labeling Job
Once the labeling job is sucessfully submitted you'll receive an email from Amazon SageMaker labeling project requesting to work on a labeling project:

1. In the email inviting you to work on a labeling project you'll receive a username and password to login into the labeling console. Follow the procedure provided in the email.
![](./img/create_manifest_6.png)

2. Logging into the URL you received by email, you'll see the list of jobs you're assigned to.
![](./img/create_manifest_7.png)

3. When I click on the ‘Start working’ button, You'll see instructions as well as a first image to work on. Using the toolbox, you can zoom in and out, etc. This is pretty intuitive. Select the correct "*Label*" (example: LH or RH) depending what you observe on the image. You can use reference images from the downloaded assets.

4. Once you complete the labeling you'll receive a window message:
![](./img/create_manifest_8.png)

Also, you're Amazon SageMaker console job lebeling screen will show completed:
![](./img/create_manifest_9.png)
5. Click on the job name and you can observe the output of the labeling process. As you're aware of it this was a human labeling job. For large datasets (more thant 1000 objects) Ground Truth can automatically label the dataset.

Of course, our purpose is to use this information to train machine learning models. you can find it in the augmented manifest file stored in your bucket. For example, your manifest will be located in s3://lab1-label-output/lab1-labeling-job/manifests/output/output.manifes. This manifest file contains information about the first image, where you labeled the objects.

Here is an example of the augmented manifest output file:
```json
{
    "source-ref": "s3://lab1-rawdata/IMG_0085.JPG",
    "lab1-labeling-job": 0,
    "lab1-labeling-job-metadata": {
        "confidence": 0.95,
        "job-name": "labeling-job/lab1-labeling-job",
        "class-name": "RH",
        "human-annotated": "yes",
        "creation-date": "2019-05-04T20:26:41.638095",
        "type": "groundtruth/image-classification"
    }
}

```

Now you're ready to train the model with this dataset.

## 3. 