import pytest

from core.domain.entity.project_input import ProjectInput, DerivationLineInput, LateralLineInput
from infrastructure.persistence.models import Project, LateralLine, DerivationLine
from infrastructure.persistence.mappers.project_mapper import ProjectMapper, DerivationLineMapper, LateralLineMapper


class TestProjectMapper:

    def test_output_instance(self):

        # input_data
        project_input = ProjectInput(
            id=1,
            user_id=1,
            group_id="1",
            description="Tomato plantation",
            status="draft",
            crop="Tomato",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=100,
            derivation_line=[],
            lateral_line=[],
        )

        # expected_output
        project = ProjectMapper.model_from_input(project_input)

        assert isinstance(project, Project)

    """
        Tested a valid mapper
    """
    def test_valid_mapping(self):

        # input_data
        project_input = ProjectInput(
            id=1,
            user_id=1,
            group_id="1",
            description="Tomato plantation",
            status="draft",
            crop="Tomato",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=100,
            derivation_line=[],
            lateral_line=[]
        )

        # expected_output
        project = ProjectMapper.model_from_input(project_input)

        assert project.id == project_input.id
        assert project.user_id == project_input.user_id
        assert project.group_id == project_input.group_id
        assert project.description == project_input.description
        assert project.status == project_input.status
        assert project.crop == project_input.crop
        assert project.maximum_actual_irrigation_required == project_input.maximum_actual_irrigation_required
        assert project.total_irrigation_required == project_input.total_irrigation_required
        assert project.derivation_line == project_input.derivation_line
        assert project.lateral_line == project_input.lateral_line

    def test_output_lines(self):

        # input_data
        project_input = ProjectInput(
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
                    type="with_plc"
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
                    type="with_plc"
                )
            ]
        )

        # expected_output
        project = ProjectMapper.model_from_input(project_input)

        assert isinstance(project.lateral_line[0], LateralLine)
        assert isinstance(project.derivation_line[0], DerivationLine)


class TestDerivationLineMapper:

    def test_output_instance(self):

        # input_data
        line = DerivationLineInput(
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type="with_plc"
        )

        # input_data
        project_id = 1

        # expected_output
        derivation_line = DerivationLineMapper.model_from_input(line, project_id)

        assert isinstance(derivation_line, DerivationLine)


class TestLateralLineMapper:

    def test_output_instance(self):

        # input_data
        line = LateralLineInput(
            dripper="10mm",
            decline=10,
            inlet_pressure=10,
            separation_between_issuers=20,
            length_max=6,
            diameter=5,
            localized_loss=100,
            type="with_plc"
        )

        # input_data
        project_id = 1

        lateral_line = LateralLineMapper.model_from_input(line, project_id)

        assert isinstance(lateral_line, LateralLine)
