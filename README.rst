=================
describe-variable
=================


Describe variables in python. Most useful for complex dicts or arrays.


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
            "prop1": { "this": "that" }
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
            "prop1": { "this": "that" }
        }
        }
    ]
    }

    describe

    describe(d2, 3)

    diff(d1, d2, 4)
