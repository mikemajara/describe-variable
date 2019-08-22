from .describer_var import describe_var

DEFAULT_DEPTH = 0
DEFAULT_SPACES = 4
DEFAULT_INDENT = 0


def describe_object(d: dict,
                    depth=DEFAULT_DEPTH,
                    spaces=DEFAULT_SPACES,
                    indent=DEFAULT_INDENT,
                    print_values=False):
    for k in d.keys():
        print((" " * spaces * indent) + k + " -> ", end=' ')
        if isinstance(d[k], dict) or isinstance(d[k], list):
            print("type: " + type(d[k]).__name__ + ", size: " + str(len(d[k])), end=' ')
            if depth > 0:
                describe_object(d[k], depth=depth-1, indent=indent+1, print_values=print_values)
        else:
            describe_var(d[k])
