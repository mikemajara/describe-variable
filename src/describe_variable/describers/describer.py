from typing import Union

DEFAULT_DEPTH = 0
DEFAULT_SPACES = 4
DEFAULT_INDENT = -1
DEFAULT_PRINT_VALUES = True
DEFAULT_PRINT_COMPONENTS_MAX = 4
DEFAULT_PRINT_COMPONENTS_TYPE = True


def type_of_components(obj: Union[dict, list]) -> str:
    if isinstance(obj, list):
        indices = list(range(0, len(obj)))
        first_type = type(obj[indices[0]])
    elif isinstance(obj, dict):
        indices = list(obj.keys())
        first_type = type(obj[indices[0]])
    else:
        raise TypeError(str(obj) + " must be a list or a dict")

    if all(isinstance(obj[idx], first_type) for idx in indices):
        return first_type.__name__
    else:
        return 'mixed'


def get_indent(spaces, indent):
    return (" " * spaces * indent)


def describe(v: any,
             depth=DEFAULT_DEPTH,
             indent=DEFAULT_INDENT,
             spaces=DEFAULT_SPACES,
             print_values=DEFAULT_PRINT_VALUES,
             print_components_types=DEFAULT_PRINT_COMPONENTS_TYPE,
             print_components_max=DEFAULT_PRINT_COMPONENTS_MAX) -> None:

    desc = Describer(spaces, print_values, print_components_types, print_components_max)
    desc.describe_var(v, depth, indent)


class Describer:
    def __init__(self,
                 spaces=DEFAULT_SPACES,
                 print_values=DEFAULT_PRINT_VALUES,
                 print_components_types=DEFAULT_PRINT_COMPONENTS_TYPE,
                 print_components_max=DEFAULT_PRINT_COMPONENTS_MAX):
        self.spaces = spaces
        self.print_values = print_values
        self.print_components_types = print_components_types
        self.print_components_max = print_components_max

    def describe_var(self, v: any,
                     depth=DEFAULT_DEPTH,
                     indent=DEFAULT_INDENT,
                     ) -> None:
        if isinstance(v, dict) or isinstance(v, list):
            self.describe_object(v, depth=depth-1, indent=indent +
                                 1)
        else:
            if self.print_values:
                print(str(v) + ", ", end='')
            print("type: " + type(v).__name__)

    def describe_object(self, d: Union[dict, list],
                        depth: int = DEFAULT_DEPTH,
                        indent=DEFAULT_INDENT,
                        ) -> None:
        dtype = type(d)
        if dtype is dict or dtype is list:
            print("type: " + type(d).__name__ + ", size: " + str(len(d)), end='')
            if self.print_components_types:
                print(", components: " + type_of_components(d))
            if depth >= 0:
                rng = range(0, len(d)) if dtype is list else list(d.keys())
                for idx in rng:
                    if rng.index(idx) >= self.print_components_max:
                        print(get_indent(self.spaces, indent) + "...")
                        break
                    print(get_indent(self.spaces, indent) + str(idx) + " -> ", end=' ')
                    self.describe_object(d[idx], depth=depth-1, indent=indent + 1)
        else:
            self.describe_var(d, depth=depth-1, indent=indent + 1)
