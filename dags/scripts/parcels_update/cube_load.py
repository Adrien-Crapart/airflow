import pyspark
from pyspark.sql import SparkSession


def sales_monthly():
    spark = SparkSession.builder.master("sales_stage load") \
        .appName('SparkByExamples.com') \
        .getOrCreate()

    df = spark.sql("""
      select month_id, sum(sales)
      from sales_stage
      group by month_id
    
    """
                   )

    df.repartition(10).write.mode("overwrite") \
      .format("delta") \
      .saveAsTable("sales_monthly")
