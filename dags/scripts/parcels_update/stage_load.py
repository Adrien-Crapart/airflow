import pyspark
from pyspark.sql import SparkSession
from config.configparams import file_format, file_path


def sales_stage_load():
    spark = SparkSession.builder.master("sales_stage load") \
        .appName("SparkByExemples.com") \
        .getOrCreate()

    df = spark.read.format("csv") \
        .load(f"{file_path}/{file_format.get('sales')}")

    df.write.mode("overwrite") \
      .partitionBy("file_date") \
      .saveAsTable("sales_stage")


def stores_stage_load():
    spark = SparkSession.builder.master("stores_stage load") \
        .appName("SparkByExemples.com") \
        .getOrCreate()

    df = spark.read.format("csv") \
        .load(f"{file_path}/{file_format.get('stores_cities')}")

    df.write.mode("overwrite") \
      .partitionBy("file_date") \
      .saveAsTable("stores_stage")
