import dlt
from pyspark.sql import SparkSession
from schemas import get_schemas

# 获取schema定义
schemas = get_schemas()

# 初始化Spark Session
spark = SparkSession.builder.getOrCreate()

# 定义CSV和GZIP文件列表和路径
file_details = {
    'csv': {
        'path': "s3://your-bucket-name/path/to/csv/",
        'delimiter': ',',
        'format': 'csv',
        'codec': None
    },
    'gzip': {
        'path': "s3://your-bucket-name/path/to/gzip/",
        'delimiter': '|',
        'format': 'csv',
        'codec': 'gzip'
    }
}

csv_file_list = ['APDRG', 'claimcodetype', 'diabetescodes', 'dischargestatuscodes',
                 'MSDRG', 'payertypecodes', 'placeofservicecodes', 'providertypecodes',
                 'typeofbillcodes', 'ubrevenuecodes', 'zip3sociodemographiccollapse']
gzip_file_list = ['member', 'memberenrollment', 'memberenrollment_adjusted', 'provider',
                  'providersupplemental', 'claim', 'claimcode', 'rxclaim', 'labclaim',
                  'upkmemberkeys', 'consolidated_claim_price', 'consolidated_claimxref',
                  'consolidated_enrollment_monthly', 'consolidated_rxclaim_price',
                  'consolidated_rxclaimxref', 'consolidated_labclaim', 'consolidated_labclaimxref',
                  'claim_price', 'rxclaim_price', 'consolidated_provider']

# 定义表加载函数
def define_dlt_table(table_name, file_type):
    details = file_details[file_type]
    path = f"{details['path']}{table_name}.{file_type if file_type == 'gzip' else 'csv'}"

    @dlt.table(name=table_name)
    def table_loader():
        return (
            spark.read
            .format(details['format'])
            .option("header", True)
            .option("delimiter", details['delimiter'])
            .option("dateFormat", "yyyy-MM-dd")
            .option("emptyValue", None)
            .option("treatEmptyValuesAsNulls", "true")
            .option("codec", details['codec'])
            .schema(schemas[table_name])
            .load(path)
        )
    return table_loader

# 使用函数定义所有表
for table_name in schemas.keys():
    file_type = 'gzip' if table_name in gzip_file_list else 'csv'
    define_dlt_table(table_name, file_type)
