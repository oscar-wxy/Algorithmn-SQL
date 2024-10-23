import re
from pyspark.sql.types import *

# Define the mapping from Redshift types to Spark types
type_mapping = {
    'INTEGER': IntegerType(),
    'BIGINT': LongType(),
    'DECIMAL': lambda p, s: DecimalType(int(p), int(s)),
    'VARCHAR': StringType(),
    'CHAR': StringType(),
    'BOOLEAN': BooleanType(),
    'TIMESTAMP': TimestampType(),
    'DATE': DateType(),
    'DOUBLE': DoubleType(),
    'FLOAT': FloatType()
}

# Regex pattern to match the column definitions in the DDL
ddl_pattern = re.compile(r'(\w+)\s+(\w+)(?:\((\d+),?\s?(\d+)?\))?', re.IGNORECASE)

def parse_ddl(ddl):
    columns = []
    
    # Extract column definitions using regex
    matches = ddl_pattern.findall(ddl)
    
    for match in matches:
        col_name = match[0]
        col_type = match[1].upper()
        precision = match[2]
        scale = match[3]
        
        # Map Redshift data types to Spark data types
        if col_type in type_mapping:
            if col_type == 'DECIMAL' and precision and scale:
                spark_type = type_mapping[col_type](precision, scale)
            else:
                spark_type = type_mapping[col_type]
        else:
            raise ValueError(f"Unsupported Redshift data type: {col_type}")
        
        # Add the column as a StructField (assuming nullable columns)
        columns.append(StructField(col_name, spark_type, True))
    
    return StructType(columns)

# Example DDL
ddl = """
CREATE TABLE example_table (
    id INTEGER,
    name VARCHAR(255),
    created_at TIMESTAMP,
    amount DECIMAL(10, 2),
    is_active BOOLEAN
);
"""

# Parse the DDL and generate the Spark schema
schema = parse_ddl(ddl)

# Output the generated schema
print(schema)
