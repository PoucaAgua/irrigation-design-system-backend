# Percent Wetted Area Service

This module provides a collection of methods for calculating the percent wetted area and related parameters for irrigation purposes.

## Methods

### `calculate_irrigation_by_tree(ibt_entity: IBTEntity) -> Decimal`

Calculates the irrigation required for a single tree based on the given parameters.

**Parameters:**

- `ibt_entity`: An instance of the `IBTEntity` class containing the following attributes:
  - `drippers_number`: Number of drippers for the tree.
  - `value_of_z`: Z value.
  - `value_of_q`: Q value.
  - `hydraulic_conductivity_of_saturated_soil`: Hydraulic conductivity of saturated soil.
  - `space_between_lines`: Space between lines.
  - `space_between_plants`: Space between plants.

**Returns:**

- `Decimal`: The calculated irrigation required in decimal format.

### `dw_calculate(ibt_entity: IBTEntity) -> Decimal`

Calculates the maximum wetted diameter by the dripper based on the given parameters.

**Parameters:**

- `ibt_entity`: An instance of the `IBTEntity` class (same as above).

**Returns:**

- `Decimal`: The calculated maximum wetted diameter in decimal format.

### `calculate_twice_saturated_wetted_radius(tsw_entity: TSWEntity) -> Decimal`

Calculates the saturated wetted radius based on the given parameters.

**Parameters:**

- `tsw_entity`: An instance of the `TSWEntity` class containing the following attributes:
  - `parameter_model_unsaturated_hydraulic`: Parameter model unsaturated hydraulic.
  - `hydraulic_conductivity_of_saturated_soil`: Hydraulic conductivity of saturated soil.
  - `value_of_q`: Q value.

**Returns:**

- `Decimal`: The calculated saturated wetted radius in decimal format.

### `calculate_continuous_strip(cp_entity: CPEntity) -> Decimal`

Calculates the irrigation required to form a continuous strip based on the given parameters.

**Parameters:**

- `cp_entity`: An instance of the `CPEntity` class containing the following attributes:
  - `space_between_plants`: Space between plants.
  - `wetted_zone`: Wetted zone.
  - `row_spacing_plants`: Row spacing of plants.

**Returns:**

- `Decimal`: The calculated irrigation required to form a continuous strip in decimal format.

### `moistened_area_calculate(cp_entity: CPEntity) -> Decimal`

Calculates the moistened area based on the given parameters.

**Parameters:**

- `cp_entity`: An instance of the `CPEntity` class (same as above).

**Returns:**

- `Decimal`: The calculated moistened area in decimal format.

### `area_occupied_plant_calculate(cp_entity: CPEntity) -> Decimal`

Calculates the area occupied by a single plant based on the given parameters.

**Parameters:**

- `cp_entity`: An instance of the `CPEntity` class (same as above).

**Returns:**

- `Decimal`: The calculated area occupied by a single plant in decimal format.
