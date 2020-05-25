from typing import Union


def type_of_components(obj: Union[dict, list]) -> str:
    if isinstance(obj, list):
        indices = list(range(0, len(obj)))
        if len(indices) <= 0:
            first_type = None
        else:
            first_type = type(obj[indices[0]])
    elif isinstance(obj, dict):
        indices = list(obj.keys())
        if len(indices) <= 0:
            first_type = None
        else:
            first_type = type(obj[indices[0]])
    else:
        raise TypeError(str(obj) + " must be a list or a dict")

    if all(isinstance(obj[idx], first_type) for idx in indices):
        return first_type.__name__ if first_type is not None else 'empty'
    else:
        return 'mixed'
