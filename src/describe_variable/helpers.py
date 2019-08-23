from typing import Union


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
