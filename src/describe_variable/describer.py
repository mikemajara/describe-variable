from typing import Union
from .helpers import type_of_components

START_INDENT = -1

DEFAULT_DEPTH = 0
DEFAULT_SPACES = 4
DEFAULT_PRINT_VALUES = True
DEFAULT_PRINT_COMPONENTS_MAX = 4
DEFAULT_PRINT_COMPONENTS_TYPE = True


def get_indent(spaces, indent):
    return (" " * spaces * indent)


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
                     indent=START_INDENT,
                     ) -> None:
        res = ''
        if isinstance(v, dict) or isinstance(v, list):
            res += self.describe_object(v, depth=depth-1, indent=indent +
                                        1)
        else:
            if self.print_values:
                res += str(v) + ", "
            res += "type: " + type(v).__name__ + "\n"
        return res

    def describe_object(self, d: Union[dict, list],
                        depth: int = DEFAULT_DEPTH,
                        indent=START_INDENT,
                        ) -> None:
        res = ''
        dtype = type(d)
        if dtype is dict or dtype is list:
            res += "type: " + type(d).__name__ + ", size: " + str(len(d))
            if self.print_components_types:
                res += ", components: " + type_of_components(d) + "\n"
            if depth >= 0:
                rng = range(0, len(d)) if dtype is list else list(d.keys())
                for idx in rng:
                    if rng.index(idx) >= self.print_components_max:
                        res += get_indent(self.spaces, indent) + "...\n"
                        break
                    res += get_indent(self.spaces, indent) + str(idx) + " -> "
                    res += self.describe_object(d[idx], depth=depth-1, indent=indent + 1)
        else:
            res += self.describe_var(d, depth=depth-1, indent=indent + 1)
        return res
