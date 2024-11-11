# Configure AWS Glue to use Iceberg from JAR files

<img width="275" alt="map-user" src="https://img.shields.io/badge/cloudformation template deployments-132-blue"> <img width="85" alt="map-user" src="https://img.shields.io/badge/views-968-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-130-green">

AWS Glue versions 3.0 and up are natively bundled with the dependencies required to run a version of Apache Iceberg. To use the natively bundled version of iceberg that is included with Glue reference the [Using the Iceberg framework in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-iceberg.html) documentation.

Additionally, AWS Glue offers market place connectors for Apache Iceberg which can afford you access to different versions of Iceberg.

If you do not want to use the natively bundled version of iceberg and you do not want to use market place connectors - you can configure a Glue job to use iceberg from JAR files directly downloaded from the [Apache Iceberg release page](https://iceberg.apache.org/releases/). This method allows the most flexibility with respect to choosing an iceberg version but requires so additional configurations.

The instructions below will provide step by step instructions on how you can use iceberg in your Glue job via. dependent JAR files

## Instructions

There are two ways to run the example either via. a [CloudFormation stack](https://github.com/ev2900/Iceberg_Glue_from_JARs/tree/main?tab=readme-ov-file#deploy-via-cloudformation-stack) or going [step by step in the AWS console](https://github.com/ev2900/Iceberg_Glue_from_JARs/tree/main?tab=readme-ov-file#deploy-via-aws-console)

### Deploy via. CloudFormation Stack

Click on the button below to deploy a CloudFormation stack.

> [!NOTE]
> The cloudformation template has been update to use Iceberg version 1.6.1

[![Launch CloudFormation Stack](https://sharkech-public.s3.amazonaws.com/misc-public/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=glue-iceberg-from-jars&templateURL=https://sharkech-public.s3.amazonaws.com/misc-public/glue_iceberg_jars.yaml)

The stack will create an S3 bucket with the required JARs files and a Glue job. After the deployment of the CloudFormation stack open the Glue console, click on the job and the run the job

<img width="900" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/Start.png">

### Deploy via. AWS Console

1. Identify and download the iceberg JAR file

The [release page](https://iceberg.apache.org/releases/) in the iceberg documentation allows you to download the JAR files for iceberg. Each version of iceberg has multiple JAR files avaiable for download. It is important we download the correct JARs.

We want to download the JAR files associated with spark. Ignore the JAR files for flink and hive. For spark, iceberg has different JARs depending on the version of spark. The version of Spark run by Glue is determined by the version of Glue you chose. Use [AWS Glue version](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html) documentation to determine which version of spark the Glue job will use. Once you determine the version of Spark download the corresponding JAR file for iceberg.

An example. If I am using Glue 4.0 the [AWS documentation](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html) informs us that Glue 4.0 uses Spark version 3.3 . Consequently, I would download the download the iceberg JAR for spark that corresponds with spark version 3.3

2. Identify and download the aws bundle JAR file

The [release page](https://iceberg.apache.org/releases/) in the iceberg documentation also includes the option to download an ```aws-bundle``` JAR file download the ```aws-bundle``` JAR file that corresponds with the version of the iceberg JAR you downloaded

An example. Working with Iceberg version 1.5.2 and AWS Glue 4.0 I would download the following JARS

<img width="400" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/JARS.png">

3. Upload the JAR files to S3

Upload both of the JAR files to S3

<img width="700" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/S3.png">

4. Create Glue Data Catalog Database

Navigate to the AWS Glue home page in the AWS console. Under the Glue Data Catalog section, select databases and click on add database

<img width="700" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/create_database_1.png">

Name the database ```iceberg```

<img width="500" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/create_database_2.png">

6. Create and configure a Glue job

Navigate to Glue studio and create a new Spark job via. script editor

<img width="600" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/Glue_studio_1.png">

After configuring the standard aspects of a Glue job such as choosing an IAM role, renaming and saving the job. Navigate to the job details button, specifically open the advanced properties section, then navigate to libraries sub-section.

Update the dependent JARs path section with the URI of each JAR file separate the two URIs with a comma no spaces.

For example, if I have my JAR files in a S3 bucket named ```<example-bucket>``` I would enter the following into the dependent JARs path section of the Glue job details

```s3://<example-bucket>/jars/iceberg-aws-bundle-1.5.2.jar,s3://<example-bucket>/jars/iceberg-spark-runtime-3.3_2.12-1.5.2.jar```

The example configuration is pictured below

<img width="500" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/DependJAR.png">

Additonally add a job ```--s3_bucket_name``` with the name of the S3 bucket that you want the job to write the sample iceberg data to

<img width="500" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/s3_bucket_name_param.png">

6. Add sample code to Glue job

Copy and paste the code from the [sample_job.py](https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/sample_job.py) into the Glue script section

7. Save and run the Glue job

<img width="900" alt="quick_setup" src="https://github.com/ev2900/Iceberg_Glue_from_JARs/blob/main/README/SaveStart.png">
