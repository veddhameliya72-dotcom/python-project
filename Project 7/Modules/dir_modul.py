from . import date_time
from . import mathemetic
from . import random_num
from . import file_op
from . import uuid_gene

def module_attributes():
    modules = {
        "date_time": date_time,
        "mathemetic": mathemetic,
        "random_num": random_num,
        "file_op": file_op,
        "uuid": uuid_gene
    }
    
    print("\n--- Available Module Attributes ---")
    for name, module in modules.items():
        print(f"\nFunctions In '{name}':")
        for attribute in dir(module):
            if not attribute.startswith("__"):
                print(f" - {attribute}")