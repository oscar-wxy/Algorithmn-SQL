import re

# Define a mapping from Redshift data types to Python types
REDSHIFT_TO_PYTHON_TYPE_MAP = {
    'smallint': 'int',
    'integer': 'int',
    'bigint': 'int',
    'decimal': 'float',
    'numeric': 'float',
    'real': 'float',
    'double precision': 'float',
    'boolean': 'bool',
    'char': 'str',
    'character': 'str',
    'varchar': 'str',
    'character varying': 'str',
    'date': 'str',
    'timestamp': 'str',
    'timestamp without time zone': 'str',
    'time': 'str',
    'time without time zone': 'str',
    'text': 'str'
}

def convert_ddl_to_model(ddl: str, class_name: str) -> str:
    # Regular expression to extract column name and data type
    pattern = re.compile(r'(\w+)\s+(\w+(\s+\w+)?)')

    # Extracting all columns and their data types
    matches = pattern.findall(ddl)

    # Start building the class definition
    class_def = f"class {class_name}:\n"

    # Add type annotations for each column
    for match in matches:
        column_name, data_type = match[0], match[1]
        python_type = REDSHIFT_TO_PYTHON_TYPE_MAP.get(data_type.lower(), 'Any')
        class_def += f"    {column_name}: {python_type}\n"

    # If no columns found, add a placeholder
    if not matches:
        class_def += "    pass\n"
    
    return class_def

# Example usage
ddl = """
CREATE TABLE users (
    id integer NOT NULL,
    username varchar(50) NOT NULL,
    created_at timestamp without time zone NOT NULL,
    is_active boolean
)
"""

class_name = "User"
model_class = convert_ddl_to_model(ddl, class_name)
print(model_class)