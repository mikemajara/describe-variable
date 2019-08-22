from .describer_dict import describe_dict

DEFAULT_DEPTH = 0
DEFAULT_SPACES = 4
DEFAULT_INDENT = 0


def describe_list(a: list,
                  depth=DEFAULT_DEPTH,
                  spaces=DEFAULT_SPACES,
                  indent=DEFAULT_INDENT,
                  print_values=False):
    if len(a):
        if all(isinstance(n, type(a[0])) for n in a):
            print(type(a[0]).__name__ + "s")
        if isinstance(a[0], dict):
            describe_dict(a[0], depth=depth-1, indent=indent+1, print_values=print_values)
        elif isinstance(a[0], list):
            describe_list(a[0], depth=depth-1, indent=indent+1, print_values=print_values)
        else:
            describe_var(a[0])
