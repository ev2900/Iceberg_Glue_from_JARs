# Configure AWS Glue to use Iceberg from JAR files

AWS Glue versions 3.0 and up are natively bundled with the dependencies required to run a version of Apache Iceberg. To use the natively bundled version of iceberg that is included with Glue reference the [Using the Iceberg framework in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-iceberg.html) documentation. 

Additionally, AWS Glue offers market place connectors for Apache Iceberg which can afford you access to different versions of Iceberg.

If you do not want to use the natively bundled version of iceberg and you do not want to use market place connectors - you can configure a Glue job to use iceberg from JAR files directly downloaded from the [Apache Iceberg release page](https://iceberg.apache.org/releases/). This method allows the most flexibility with respect to choosing an iceberg version but requires so additional configurations.

The instructions below will provide step by step instructions on how you can use iceberg in your Glue job via. dependent JAR files

## Instructions

