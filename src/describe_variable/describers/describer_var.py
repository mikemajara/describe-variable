# from .describer_dict import describe_dict
# from .describer_list import describe_list
from .describer_object import describe_object

DEFAULT_PRINT_VALUES = True


def describe_var(v, print_values=DEFAULT_PRINT_VALUES, *args, **kwargs):
    if isinstance(v, dict) or isinstance(v, list):
        describe_object(v, print_values=print_values, *args, **kwargs)
    else:
        print("type: " + type(v).__name__, end='')
        if print_values:
            print(", value: " + str(v))
