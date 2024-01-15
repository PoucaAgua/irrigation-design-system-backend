from core.domain.entity.project.project_input import (
    ProjectInput,
    DerivationLineInput,
    LateralLineInput,
)
from infrastructure.persistence.models import Project, LateralLine, DerivationLine
from infrastructure.persistence.mappers.project_mapper import (
    ProjectMapper,
    DerivationLineMapper,
    LateralLineMapper,
)
from core.domain.enum.line_types import LineTypes


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
                    id=1,
                    pipe_type="Iron",
                    inlet_pressure=100,
                    length="100",
                    diameter="100",
                    localized_loss="100",
                    type=LineTypes.with_plc,
                )
            ],
            lateral_line=[
                LateralLineInput(
                    id=1,
                    dripper="Dripper",
                    decline=100,
                    inlet_pressure=100,
                    separation_between_issuers=100,
                    length_max=100,
                    diameter=100,
                    localized_loss=100,
                    type=LineTypes.with_plc,
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
                    type=LineTypes.with_plc,
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
                    type=LineTypes.with_plc,
                )
            ],
        )

        # result
        result = ProjectMapper.model_from_input(input_data)

        assert result == expected_output

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
                    id=1,
                    pipe_type="Iron",
                    inlet_pressure=100,
                    length="100",
                    diameter="100",
                    localized_loss="100",
                    type=LineTypes.with_plc,
                )
            ],
            lateral_line=[
                LateralLineInput(
                    id=1,
                    dripper="Dripper",
                    decline=100,
                    inlet_pressure=100,
                    separation_between_issuers=100,
                    length_max=100,
                    diameter=100,
                    localized_loss=100,
                    type=LineTypes.with_plc,
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
                    type=LineTypes.with_plc,
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
                    type=LineTypes.with_plc,
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
                    type=LineTypes.with_plc,
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
                    type=LineTypes.with_plc,
                )
            ],
        )

        result = ProjectMapper.model_from_input_and_persisted(input_data, project_persisted)

        assert result == expected_output


class TestDerivationLineMapper:
    def test_model_from_input(self):
        # input_data
        derivation_line_input = DerivationLineInput(
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type=LineTypes.with_plc,
        )

        # expected_output
        expected_output = DerivationLine(
            project_id=1,
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type=LineTypes.with_plc,
        )

        # result
        result = DerivationLineMapper.model_from_input(line=derivation_line_input, project_id=1)

        assert result == expected_output

    def test_model_from_input_persisted(self):
        # input_data
        line = DerivationLineInput(
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type=LineTypes.with_plc,
        )

        # input_data
        lines_persisted = [
            DerivationLine(
                project_id=1,
                pipe_type="Iron",
                inlet_pressure=10,
                length="150",
                diameter="100",
                localized_loss="240",
                type=LineTypes.with_plc,
            ),
            DerivationLine(
                project_id=1,
                pipe_type="Iron",
                inlet_pressure=10,
                length="150",
                diameter="100",
                localized_loss="240",
                type=LineTypes.with_plc,
            ),
        ]

        # expected_output
        expected_output = DerivationLine(
            project_id=1,
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type=LineTypes.with_plc,
        )

        result = DerivationLineMapper.model_from_input_and_persisted(
            line, lines_persisted, project_id=1
        )

        assert result == expected_output


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
            type=LineTypes.with_plc,
        )

        # expected_output
        expected_output = LateralLine(
            project_id=1,
            dripper="10mm",
            decline=10,
            inlet_pressure=10,
            separation_between_issuers=20,
            length_max=6,
            diameter=5,
            localized_loss=100,
            type=LineTypes.with_plc,
        )

        result = LateralLineMapper.model_from_input(lateral_line_input, project_id=1)

        assert result == expected_output

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
            type=LineTypes.with_plc,
        )

        # input_data
        lines_persisted = [
            LateralLine(
                project_id=1,
                dripper="10mm",
                decline=10,
                inlet_pressure=10,
                separation_between_issuers=20,
                length_max=6,
                diameter=5,
                localized_loss=100,
                type=LineTypes.with_plc,
            ),
            LateralLine(
                project_id=1,
                dripper="10mm",
                decline=10,
                inlet_pressure=10,
                separation_between_issuers=20,
                length_max=6,
                diameter=5,
                localized_loss=100,
                type=LineTypes.with_plc,
            ),
        ]

        # expected_output
        expected_output = LateralLine(
            project_id=1,
            dripper="10mm",
            decline=10,
            inlet_pressure=10,
            separation_between_issuers=20,
            length_max=6,
            diameter=5,
            localized_loss=100,
            type=LineTypes.with_plc,
        )

        result = LateralLineMapper.model_from_input_and_persisted(
            line, lines_persisted, project_id=1
        )

        assert result == expected_output
