from .describer_list import describe_list
from .describer_var import describe_var

DEFAULT_DEPTH = 0
DEFAULT_SPACES = 4
DEFAULT_INDENT = 0


def describe_dict(d: dict,
                  depth=DEFAULT_DEPTH,
                  spaces=DEFAULT_SPACES,
                  indent=DEFAULT_INDENT,
                  print_values=False):
    for k in d.keys():
        print((" " * spaces * indent) + k + " -> ", end=' ')
        if isinstance(d[k], dict):
            print("type: " + type(d[k]).__name__ + ", size: " + str(len(d[k].keys())))
            if depth > 0:
                describe_dict(d[k], depth=depth-1, indent=indent+1, print_values=print_values)
        elif isinstance(d[k], list):
            print("type: " + type(d[k]).__name__ + ", size: " + str(len(d[k])))
            if depth > 0:
                describe_list(d[k], depth=depth-1, indent=indent+1, print_values=print_values)
        else:
            describe_var(d[k])
