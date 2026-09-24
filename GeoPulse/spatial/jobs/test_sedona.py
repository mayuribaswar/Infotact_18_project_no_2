from sedona.spark import SedonaContext

print("Starting GeoPulse Spatial Environment...")

config = (
    SedonaContext.builder()
    .master("local[*]")
    .appName("GeoPulse")
    .config(
        "spark.jars.packages",
        "org.apache.sedona:sedona-spark-shaded-3.5_2.12:1.9.1,"
        "org.datasyslab:geotools-wrapper:1.9.1-33.5"
    )
    .getOrCreate()
)

sedona = SedonaContext.create(config)

print("======================================")
print("GeoPulse Spatial Environment READY!")
print("Spark version:", config.version)
print("Apache Sedona started successfully!")
print("======================================")

# Test a spatial function
result = sedona.sql("""
    SELECT ST_AsText(ST_Point(77.5946, 12.9716)) AS location
""")

result.show(truncate=False)

sedona.stop()