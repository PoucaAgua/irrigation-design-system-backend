from core.domain.entity.project_input import ProjectInput, DerivationLineInput, LateralLineInput
from infrastructure.persistence.models import Project, LateralLine, DerivationLine
from infrastructure.persistence.mappers.project_mapper import (
    ProjectMapper,
    DerivationLineMapper,
    LateralLineMapper,
)


class TestProjectMapper:
    def test_model_from_input(self):
        # input_data
        input_data = ProjectInput(
            id=1,
            user_id=1,
            group_id="1",
            description="Tomato plantation",
            status="draft",
            crop="Tomato",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=100,
            derivation_line=[
                DerivationLineInput(
                    pipe_type="Iron",
                    inlet_pressure=100,
                    length="100",
                    diameter="100",
                    localized_loss="100",
                    type="with_plc",
                )
            ],
            lateral_line=[
                LateralLineInput(
                    dripper="Dripper",
                    decline=100,
                    inlet_pressure=100,
                    separation_between_issuers=100,
                    length_max=100,
                    diameter=100,
                    localized_loss=100,
                    type="with_plc",
                )
            ],
        )

        # expected_output
        expected_output = Project(
            id=1,
            user_id=1,
            group_id="1",
            description="Tomato plantation",
            status="draft",
            crop="Tomato",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=100,
            derivation_line=[
                DerivationLine(
                    id=1,
                    project_id=1,
                    pipe_type="Iron",
                    inlet_pressure=100,
                    length="100",
                    diameter="100",
                    localized_loss="100",
                    type="with_plc",
                )
            ],
            lateral_line=[
                LateralLine(
                    id=1,
                    project_id=1,
                    dripper="Dripper",
                    decline=100,
                    inlet_pressure=100,
                    separation_between_issuers=100,
                    length_max=100,
                    diameter=100,
                    localized_loss=100,
                    type="with_plc",
                )
            ],
        )

        # result
        result = ProjectMapper.model_from_input(input_data)

        assert isinstance(result, Project)
        assert result.id == expected_output.id
        assert result.user_id == expected_output.user_id
        assert result.group_id == expected_output.group_id
        assert result.description == expected_output.description
        assert result.status.value == expected_output.status
        assert result.crop == expected_output.crop
        assert (
            result.maximum_actual_irrigation_required
            == expected_output.maximum_actual_irrigation_required
        )
        assert result.crop_evapotranspiration == expected_output.crop_evapotranspiration
        assert result.total_irrigation_required == expected_output.total_irrigation_required

        assert len(result.derivation_line) == len(expected_output.derivation_line)
        for i in range(len(result.derivation_line)):
            assert isinstance(result.derivation_line[i], DerivationLine)
            assert (
                result.derivation_line[i].project_id
                == expected_output.derivation_line[i].project_id
            )
            assert (
                result.derivation_line[i].pipe_type == expected_output.derivation_line[i].pipe_type
            )
            assert (
                result.derivation_line[i].inlet_pressure
                == expected_output.derivation_line[i].inlet_pressure
            )
            assert result.derivation_line[i].length == expected_output.derivation_line[i].length
            assert result.derivation_line[i].diameter == expected_output.derivation_line[i].diameter
            assert (
                result.derivation_line[i].localized_loss
                == expected_output.derivation_line[i].localized_loss
            )
            assert result.derivation_line[i].type.value == expected_output.derivation_line[i].type

        assert len(result.lateral_line) == len(expected_output.lateral_line)
        for i in range(len(result.lateral_line)):
            assert isinstance(result.lateral_line[i], LateralLine)
            assert result.lateral_line[i].project_id == expected_output.lateral_line[i].project_id
            assert result.lateral_line[i].dripper == expected_output.lateral_line[i].dripper
            assert result.lateral_line[i].decline == expected_output.lateral_line[i].decline
            assert (
                result.lateral_line[i].inlet_pressure
                == expected_output.lateral_line[i].inlet_pressure
            )
            assert (
                result.lateral_line[i].separation_between_issuers
                == expected_output.lateral_line[i].separation_between_issuers
            )
            assert result.lateral_line[i].length_max == expected_output.lateral_line[i].length_max
            assert result.lateral_line[i].diameter == expected_output.lateral_line[i].diameter
            assert (
                result.lateral_line[i].localized_loss
                == expected_output.lateral_line[i].localized_loss
            )
            assert result.lateral_line[i].type.value == expected_output.lateral_line[i].type

    def test_model_from_input_and_persisted(self):
        # input_data
        input_data = ProjectInput(
            id=1,
            user_id=1,
            group_id="1",
            description="Tomato plantation",
            status="draft",
            crop="Tomato",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=100,
            derivation_line=[
                DerivationLineInput(
                    pipe_type="Iron",
                    inlet_pressure=100,
                    length="100",
                    diameter="100",
                    localized_loss="100",
                    type="with_plc",
                )
            ],
            lateral_line=[
                LateralLineInput(
                    dripper="Dripper",
                    decline=100,
                    inlet_pressure=100,
                    separation_between_issuers=100,
                    length_max=100,
                    diameter=100,
                    localized_loss=100,
                    type="with_plc",
                )
            ],
        )

        # project_persisted
        project_persisted = Project(
            id=1,
            user_id=1,
            group_id="1",
            description="Tomato plantation",
            status="draft",
            crop="Tomato",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=100,
            derivation_line=[
                DerivationLine(
                    id=1,
                    project_id=1,
                    pipe_type="Iron",
                    inlet_pressure=100,
                    length="100",
                    diameter="100",
                    localized_loss="100",
                    type="with_plc",
                )
            ],
            lateral_line=[
                LateralLine(
                    id=1,
                    project_id=1,
                    dripper="Dripper",
                    decline=100,
                    inlet_pressure=100,
                    separation_between_issuers=100,
                    length_max=100,
                    diameter=100,
                    localized_loss=100,
                    type="with_plc",
                )
            ],
        )

        # expected_output
        expected_output = Project(
            id=1,
            user_id=1,
            group_id="1",
            description="Tomato plantation",
            status="draft",
            crop="Tomato",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=100,
            derivation_line=[
                DerivationLine(
                    id=1,
                    project_id=1,
                    pipe_type="Iron",
                    inlet_pressure=100,
                    length="100",
                    diameter="100",
                    localized_loss="100",
                    type="with_plc",
                )
            ],
            lateral_line=[
                LateralLine(
                    id=1,
                    project_id=1,
                    dripper="Dripper",
                    decline=100,
                    inlet_pressure=100,
                    separation_between_issuers=100,
                    length_max=100,
                    diameter=100,
                    localized_loss=100,
                    type="with_plc",
                )
            ],
        )

        result = ProjectMapper.model_from_input_and_persisted(input_data, project_persisted)
        assert isinstance(result, Project)
        assert result.user_id == expected_output.user_id
        assert result.group_id == expected_output.group_id
        assert result.description == expected_output.description
        assert result.status.value == expected_output.status
        assert result.crop == expected_output.crop
        assert (
            result.maximum_actual_irrigation_required
            == expected_output.maximum_actual_irrigation_required
        )
        assert result.crop_evapotranspiration == expected_output.crop_evapotranspiration
        assert result.total_irrigation_required == expected_output.total_irrigation_required

        assert len(result.derivation_line) == len(expected_output.derivation_line)
        for i in range(len(result.derivation_line)):
            assert isinstance(result.derivation_line[i], DerivationLine)
            assert result.derivation_line[i].id is None
            assert (
                result.derivation_line[i].project_id
                == expected_output.derivation_line[i].project_id
            )
            assert (
                result.derivation_line[i].pipe_type == expected_output.derivation_line[i].pipe_type
            )
            assert (
                result.derivation_line[i].inlet_pressure
                == expected_output.derivation_line[i].inlet_pressure
            )
            assert result.derivation_line[i].length == expected_output.derivation_line[i].length
            assert result.derivation_line[i].diameter == expected_output.derivation_line[i].diameter
            assert (
                result.derivation_line[i].localized_loss
                == expected_output.derivation_line[i].localized_loss
            )
            assert result.derivation_line[i].type.value == expected_output.derivation_line[i].type

        assert len(result.lateral_line) == len(expected_output.lateral_line)
        for i in range(len(result.lateral_line)):
            assert isinstance(result.lateral_line[i], LateralLine)
            assert result.lateral_line[i].id is None
            assert result.lateral_line[i].project_id == expected_output.lateral_line[i].project_id
            assert result.lateral_line[i].dripper == expected_output.lateral_line[i].dripper
            assert result.lateral_line[i].decline == expected_output.lateral_line[i].decline
            assert (
                result.lateral_line[i].inlet_pressure
                == expected_output.lateral_line[i].inlet_pressure
            )
            assert result.lateral_line[i].separation_between_issuers == (
                expected_output.lateral_line[i].separation_between_issuers
            )
            assert result.lateral_line[i].length_max == expected_output.lateral_line[i].length_max
            assert result.lateral_line[i].diameter == expected_output.lateral_line[i].diameter
            assert (
                result.lateral_line[i].localized_loss
                == expected_output.lateral_line[i].localized_loss
            )
            assert result.lateral_line[i].type.value == expected_output.lateral_line[i].type


class TestDerivationLineMapper:
    def test_model_from_input(self):
        # input_data
        derivation_line_input = DerivationLineInput(
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type="with_plc",
        )

        # expected_output
        expected_output = DerivationLine(
            id=1,
            project_id=1,
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type="with_plc",
        )

        # result
        result = DerivationLineMapper.model_from_input(line=derivation_line_input, project_id=1)

        assert isinstance(result, DerivationLine)
        # assert result.id == expected_output.id
        assert result.project_id == expected_output.project_id
        assert result.inlet_pressure == expected_output.inlet_pressure
        assert result.length == expected_output.length
        assert result.diameter == expected_output.diameter
        assert result.localized_loss == expected_output.localized_loss
        assert result.type.value == expected_output.type

    def test_model_from_input_persisted(self):
        # input_data
        line = DerivationLineInput(
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type="with_plc",
        )

        # input_data
        lines_persisted = [
            DerivationLine(
                id=1,
                project_id=1,
                pipe_type="Iron",
                inlet_pressure=10,
                length="150",
                diameter="100",
                localized_loss="240",
                type="with_plc",
            ),
            DerivationLine(
                id=1,
                project_id=1,
                pipe_type="Iron",
                inlet_pressure=10,
                length="150",
                diameter="100",
                localized_loss="240",
                type="without_plc",
            ),
        ]

        # expected_output
        expected_output = DerivationLine(
            id=1,
            project_id=1,
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type="with_plc",
        )

        result = DerivationLineMapper.model_from_input_and_persisted(
            line, lines_persisted, project_id=1
        )

        assert isinstance(result, DerivationLine)
        assert result.project_id == expected_output.project_id
        assert result.pipe_type == expected_output.pipe_type
        assert result.inlet_pressure == expected_output.inlet_pressure
        assert result.length == expected_output.length
        assert result.diameter == expected_output.diameter
        assert result.localized_loss == expected_output.localized_loss
        assert result.type.value == expected_output.type


class TestLateralLineMapper:
    def test_model_from_input(self):
        # input_data
        lateral_line_input = LateralLineInput(
            dripper="10mm",
            decline=10,
            inlet_pressure=10,
            separation_between_issuers=20,
            length_max=6,
            diameter=5,
            localized_loss=100,
            type="with_plc",
        )

        # expected_output
        expected_output = LateralLine(
            id=1,
            project_id=1,
            dripper="10mm",
            decline=10,
            inlet_pressure=10,
            separation_between_issuers=20,
            length_max=6,
            diameter=5,
            localized_loss=100,
            type="with_plc",
        )

        result = LateralLineMapper.model_from_input(lateral_line_input, project_id=1)

        assert isinstance(result, LateralLine)
        # assert result.id == expected_output.id
        assert result.project_id == expected_output.project_id
        assert result.dripper == expected_output.dripper
        assert result.decline == expected_output.decline
        assert result.inlet_pressure == expected_output.inlet_pressure
        assert result.separation_between_issuers == expected_output.separation_between_issuers
        assert result.length_max == expected_output.length_max
        assert result.diameter == expected_output.diameter
        assert result.localized_loss == expected_output.localized_loss
        assert result.type.value == expected_output.type

    def test_model_from_input_persisted(self):
        # input_data
        line = LateralLineInput(
            dripper="10mm",
            decline=10,
            inlet_pressure=10,
            separation_between_issuers=20,
            length_max=6,
            diameter=5,
            localized_loss=100,
            type="with_plc",
        )

        # input_data
        lines_persisted = [
            LateralLine(
                id=1,
                project_id=1,
                dripper="10mm",
                decline=10,
                inlet_pressure=10,
                separation_between_issuers=20,
                length_max=6,
                diameter=5,
                localized_loss=100,
                type="with_plc",
            ),
            LateralLine(
                id=1,
                project_id=1,
                dripper="10mm",
                decline=10,
                inlet_pressure=10,
                separation_between_issuers=20,
                length_max=6,
                diameter=5,
                localized_loss=100,
                type="with_plc",
            ),
        ]

        # expected_output
        expected_output = LateralLine(
            id=1,
            project_id=1,
            dripper="10mm",
            decline=10,
            inlet_pressure=10,
            separation_between_issuers=20,
            length_max=6,
            diameter=5,
            localized_loss=100,
            type="with_plc",
        )

        result = LateralLineMapper.model_from_input_and_persisted(
            line, lines_persisted, project_id=1
        )

        assert isinstance(result, LateralLine)
        # assert result.id == expected_output.id
        assert result.project_id == expected_output.project_id
        assert result.dripper == expected_output.dripper
        assert result.decline == expected_output.decline
        assert result.inlet_pressure == expected_output.inlet_pressure
        assert result.separation_between_issuers == expected_output.separation_between_issuers
        assert result.length_max == expected_output.length_max
        assert result.diameter == expected_output.diameter
        assert result.localized_loss == expected_output.localized_loss
        assert result.type.value == expected_output.type
