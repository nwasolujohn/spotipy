from pyspark.sql import SparkSession as ss, functions as func


spark = ss.builder.appName('df_anal').getOrCreate()
df = spark.read.option('header', 'true').option('inferSchema', 'true').csv('rapCaviar_albums.csv')
df.groupBy('Artist', 'Year Released').agg(func.avg('Album Length').alias('Avg Year Album Length'))
df.sort(func.col('Album Length').desc()).show(30)

spark.stop()