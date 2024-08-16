from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType, ArrayType, MapType

def class_to_schema(cls):
    fields = []
    for name, field_type in cls.__annotations__.items():
        if hasattr(field_type, '__annotations__'):
            # Recursive case: the field is a nested class
            field_schema = StructType(class_to_schema(field_type))
        elif isinstance(field_type, list):
            # Handle list/array types
            element_type = field_type.__args__[0]  # Get the type of the list elements
            if hasattr(element_type, '__annotations__'):
                field_schema = ArrayType(StructType(class_to_schema(element_type)))
            else:
                field_schema = ArrayType(_python_type_to_spark_type(element_type))
        elif isinstance(field_type, dict):
            # Handle dict/map types
            key_type, value_type = field_type.__args__  # Get the types of the dict keys and values
            if hasattr(value_type, '__annotations__'):
                field_schema = MapType(_python_type_to_spark_type(key_type), StructType(class_to_schema(value_type)))
            else:
                field_schema = MapType(_python_type_to_spark_type(key_type), _python_type_to_spark_type(value_type))
        else:
            # Base case: convert Python type to Spark type
            field_schema = _python_type_to_spark_type(field_type)
        
        fields.append(StructField(name, field_schema))
    return fields

def _python_type_to_spark_type(py_type):
    """Helper function to convert Python types to Spark types."""
    if py_type == str:
        return StringType()
    elif py_type == int:
        return IntegerType()
    elif py_type == float:
        return FloatType()
    # Add more types as needed
    else:
        raise ValueError(f"Unsupported type: {py_type}")

# Example nested class structure
class Address:
    street: str
    city: str
    zip_code: int

class Person:
    name: str
    age: int
    salary: float
    address: Address

# Convert the Person class to a Spark schema
schema = StructType(class_to_schema(Person))
print(schema.simpleString())

# Output:
# struct<name:string,age:int,salary:float,address:struct<street:string,city:string,zip_code:int>>
