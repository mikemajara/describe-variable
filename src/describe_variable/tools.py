from difflib import ndiff
from .describer import Describer

START_INDENT = 0

DEFAULT_DEPTH = 0
DEFAULT_SPACES = 4
DEFAULT_PRINT_VALUES = True
DEFAULT_PRINT_COMPONENTS_MAX = 4
DEFAULT_PRINT_COMPONENTS_TYPE = True


def describe(v: any,
             depth=DEFAULT_DEPTH,
             spaces=DEFAULT_SPACES,
             indent=START_INDENT,
             print_values=DEFAULT_PRINT_VALUES,
             print_components_types=DEFAULT_PRINT_COMPONENTS_TYPE,
             print_components_max=DEFAULT_PRINT_COMPONENTS_MAX) -> None:
    """
    Print the description of a variable.
    :param v: the variable to be described.
    :type v: any
    :param depth: sets the depth of the description (for dicts).
    :type depth: int
    :param spaces: sets the number of spaces of the indent. (default: 4)
    :type spaces: int
    :param print_values: should the values of the variables be printed. (default: True)
    :type print_values: bool
    :param print_components_types: should the types of the variables be printed. (default: True)
    :type print_components_types: bool
    :param print_components_max: sets the number of spaces of the indent.
    :type print_components_max: bool
    """
    desc = Describer(spaces, print_values, print_components_types, print_components_max)
    print(desc.describe_var(v, depth, indent=START_INDENT))


def get_description(v: any,
                    depth=DEFAULT_DEPTH,
                    spaces=DEFAULT_SPACES,
                    indent=START_INDENT,
                    print_values=DEFAULT_PRINT_VALUES,
                    print_components_types=DEFAULT_PRINT_COMPONENTS_TYPE,
                    print_components_max=DEFAULT_PRINT_COMPONENTS_MAX) -> str:
    """
    Get the description of a variable as a string.
    :param v: the variable to be described.
    :type v: any
    :param depth: sets the depth of the description (for dicts).
    :type depth: int
    :param spaces: sets the number of spaces of the indent. (default: 4)
    :type spaces: int
    :param print_values: should the values of the variables be printed. (default: True)
    :type print_values: bool
    :param print_components_types: should the types of the variables be printed. (default: True)
    :type print_components_types: bool
    :param print_components_max: sets the number of spaces of the indent.
    :type print_components_max: bool
    """
    desc = Describer(spaces, print_values, print_components_types, print_components_max)
    return desc.describe_var(v, depth, indent=START_INDENT)


def diff(v1: any, v2: any,
         depth=DEFAULT_DEPTH,
         spaces=DEFAULT_SPACES,
         indent=START_INDENT,
         print_values=DEFAULT_PRINT_VALUES,
         print_components_types=DEFAULT_PRINT_COMPONENTS_TYPE,
         print_components_max=DEFAULT_PRINT_COMPONENTS_MAX) -> str:
    """
    Find differences between two variables description.
    This is specially useful using when values are printed out.
    Also note that differences are only found from description,
    so the differences found depend on the depth parameter.
    :param v: the variable to be described.
    :type v: any
    :param depth: sets the depth of the description (for dicts).
    :type depth: int
    :param spaces: sets the number of spaces of the indent. (default: 4)
    :type spaces: int
    :param print_values: should the values of the variables be printed. (default: True)
    :type print_values: bool
    :param print_components_types: should the types of the variables be printed. (default: True)
    :type print_components_types: bool
    :param print_components_max: sets the number of spaces of the indent.
    :type print_components_max: bool
    """
    desc = Describer(spaces, print_values, print_components_types, print_components_max)
    description_v1 = desc.describe_var(v1, depth, indent=START_INDENT)
    description_v2 = desc.describe_var(v2, depth, indent=START_INDENT)
    print(''.join(ndiff(description_v1.splitlines(1), description_v2.splitlines(1))))
