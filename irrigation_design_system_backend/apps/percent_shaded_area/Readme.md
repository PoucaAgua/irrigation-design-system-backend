# Percent Shaded Area Service

This module provides two methods to calculate the percent shaded area and the shaded crop projection by a plant.

## Methods

### `calculate_shaded_area(sa_entity: SAEntity) -> Decimal`

Calculates the shaded area of the plant, projected by the diameter of the plant's canopy.

**Parameters:**

- `sa_entity`: An instance of the `SAEntity` class containing the following attributes:
  - `diameter_of_the_plants_canopy_projection`: Diameter of the plants' canopy projection.
  - `space_between_plants`: Space between plants.
  - `strip_shaded_by_the_plant`: Strip shaded by the plant.

**Returns:**

- `Decimal`: The calculated shaded area in decimal format.

### `calculate_crop_projection(cp_entity: CPEntity) -> Decimal`

Calculates the shaded crop projection by the plant.

**Parameters:**

- `cp_entity`: An instance of the `CPEntity` class containing the following attributes:
  - `shaded_strip_plant`: Shaded strip by the plant.
  - `strip_shaded_by_the_plant`: Strip shaded by the plant.

**Returns:**

- `Decimal`: The calculated shaded crop projection by the plant in decimal format.
