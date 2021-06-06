# shipping_calculator

A simple volumetric weight calculator with GUI.



This calculator is mostly used in the shipping/freight industry.

Basically, box dimensions (length, width, and height), all in inches, are given along with a shipping constant (usually unique to the shipping/freight company) and the volumetric weight of the item is calculated and returned using the provided values.


**Calculations usually take the form:**

Item (box) dimensions:

- length = 14"
- width = 12"
- height = 24"

shipping constant = 355

volume weight = (14 x 12 x 24) / 355 = 11kg



In shipping, weights are usually rounded up, so integers instead of floats are returned.



