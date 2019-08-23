=================
describe-variable
=================


Describe variables in python. Most useful for complex dicts or arrays.

==========
Motivation
==========

Provide simple methods that describe variables (mainly dicts) and allows to find small differences in highly nested objects.



Example:

.. code-block:: python
    
    from describe_variable import describe, diff

    d1 = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                        "coordinates": [102.0, 0.5]
                },
                "properties": {
                    "prop0": "value0"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
                    ]
                },
                "properties": {
                    "prop0": "value0",
                    "prop1": 0.0
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
                            [100.0, 1.0], [100.0, 0.0]
                        ]
                    ]
                },
                "properties": {
                    "prop0": "value0",
                    "prop1": {"this": "that"}
                }
            }
        ]
    }

    d2 = {
        "type": "FeatureCollectio",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                        "coordinates": [102.0, 0.5]
                },
                "properties": {
                    "prop0": "value0"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": [
                        [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
                    ]
                },
                "properties": {
                    "prop0": "value0",
                    "prop1": 0.1
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Polygn",
                    "coordinates": [
                        [
                            [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
                            [100.0, 1.0], [100.0, 0.0]
                        ]
                    ]
                },
                "properties": {
                    "prop0": "value0",
                    "prop1": {"this": "that"}
                }
            }
        ]
    }

    describe(d1, 3)
    #     type: dict, size: 2, components: mixed
    #     type -> FeatureCollection, type: str
    #     features -> type: list, size: 3, components: dict
    #         0 -> type: dict, size: 3, components: mixed
    #             type -> Feature, type: str
    #             geometry -> type: dict, size: 2, components: mixed
    #             properties -> type: dict, size: 1, components: str
    #         1 -> type: dict, size: 3, components: mixed
    #             type -> Feature, type: str
    #             geometry -> type: dict, size: 2, components: mixed
    #             properties -> type: dict, size: 2, components: mixed
    #         2 -> type: dict, size: 3, components: mixed
    #             type -> Feature, type: str
    #             geometry -> type: dict, size: 2, components: mixed
    #             properties -> type: dict, size: 2, components: mixed

    diff(d1, d2, 4)

    #       type: dict, size: 2, components: mixed
    # -     type -> FeatureCollection, type: str
    # ?                             -
    # +     type -> FeatureCollectio, type: str
    #       features -> type: list, size: 3, components: dict
    #           0 -> type: dict, size: 3, components: mixed
    #               type -> Feature, type: str
    #               geometry -> type: dict, size: 2, components: mixed
    #                   type -> Point, type: str
    #                   coordinates -> type: list, size: 2, components: float
    #               properties -> type: dict, size: 1, components: str
    #                   prop0 -> value0, type: str
    #           1 -> type: dict, size: 3, components: mixed
    #               type -> Feature, type: str
    #               geometry -> type: dict, size: 2, components: mixed
    #                   type -> LineString, type: str
    #                   coordinates -> type: list, size: 4, components: list
    #               properties -> type: dict, size: 2, components: mixed
    #                   prop0 -> value0, type: str
    # -                 prop1 -> 0.0, type: float
    # ?                            ^
    # +                 prop1 -> 0.1, type: float
    # ?                            ^
    #           2 -> type: dict, size: 3, components: mixed
    #               type -> Feature, type: str
    #               geometry -> type: dict, size: 2, components: mixed
    # -                 type -> Polygon, type: str
    # ?                              -
    # +                 type -> Polygn, type: str
    #                   coordinates -> type: list, size: 1, components: list
    #               properties -> type: dict, size: 2, components: mixed
    #                   prop0 -> value0, type: str
    #                   prop1 -> type: dict, size: 1, components: str

