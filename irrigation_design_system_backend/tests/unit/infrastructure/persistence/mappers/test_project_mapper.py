import pytest

from core.domain.entity.project_input import ProjectInput, DerivationLineInput, LateralLineInput
from infrastructure.persistence.models import Project, LateralLine, DerivationLine
from infrastructure.persistence.mappers.project_mapper import ProjectMapper, DerivationLineMapper, LateralLineMapper


class TestProjectMapper:

    @pytest.fixture
    def project_input(self):
        return ProjectInput(
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

    @pytest.fixture
    def project_persisted(self):
        return Project(
            id=1,
            user_id=1,
            group_id="1",
            description="Tomato plantation",
            status="draft",
            crop="Tomato",
            maximum_actual_irrigation_required=100,
            crop_evapotranspiration=100,
            total_irrigation_required=100
        )

    def test_model_from_input_with_matching_type(self, project_input):

        # expected_output
        project = ProjectMapper.model_from_input(project_input)

        assert isinstance(project, Project)

    def test_model_from_input_valid_mapping(self, project_input):

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

        for derivation_line_input, derivation_line in zip(project_input.derivation_line, project.derivation_line):
            assert derivation_line_input.pipe_type == derivation_line.pipe_type
            assert derivation_line_input.inlet_pressure == derivation_line.inlet_pressure
            assert derivation_line_input.length == derivation_line.length
            assert derivation_line_input.diameter == derivation_line.diameter
            assert derivation_line_input.localized_loss == derivation_line.localized_loss
            assert derivation_line_input.type == derivation_line.type

        for lateral_line_input, lateral_line in zip(project_input.lateral_line, project.lateral_line):
            assert lateral_line_input.dripper == lateral_line.dripper
            assert lateral_line_input.decline == lateral_line.decline
            assert lateral_line_input.inlet_pressure == lateral_line.inlet_pressure
            assert lateral_line_input.separation_between_issuers == lateral_line.separation_between_issuers
            assert lateral_line_input.length_max == lateral_line.length_max
            assert lateral_line_input.diameter == lateral_line.diameter
            assert lateral_line_input.localized_loss == lateral_line.localized_loss
            assert lateral_line_input.type == lateral_line.type

    def test_model_from_input_with_lines_matching_type(self, project_input):

        # expected_output
        output = ProjectMapper.model_from_input(project_input)

        assert isinstance(output.lateral_line[0], LateralLine)
        assert isinstance(output.derivation_line[0], DerivationLine)

    def test_model_from_input_and_persisted_with_valid_inputs(self, project_input, project_persisted):
        output = ProjectMapper.model_from_input_and_persisted(project_input, project_persisted)
        assert isinstance(output, Project)


class TestDerivationLineMapper:

    @pytest.fixture
    def derivation_line_input(self):
        return DerivationLineInput(
            pipe_type="Iron",
            inlet_pressure=10,
            length="150",
            diameter="100",
            localized_loss="240",
            type="with_plc"
        )

    @pytest.fixture
    def derivation_lines_persisted(self):
        return [
            DerivationLine(
                id=1,
                project_id=1,
                pipe_type="Iron",
                inlet_pressure=10,
                length="150",
                diameter="100",
                localized_loss="240",
                type="with_plc"
            )
        ]

    def test_from_input_with_matching_type(self, derivation_line_input):

        # expected_output
        output = DerivationLineMapper.model_from_input(line=derivation_line_input, project_id=1)

        assert isinstance(output, DerivationLine)

    def test_model_from_input_and_persisted_with_matching_type(self, derivation_line_input, derivation_lines_persisted):
        output = DerivationLineMapper.model_from_input_and_persisted(
            derivation_line_input, derivation_lines_persisted, project_id=1
        )

        assert isinstance(output, DerivationLine)


class TestLateralLineMapper:

    @pytest.fixture
    def lateral_line_input(self):
        return LateralLineInput(
            dripper="10mm",
            decline=10,
            inlet_pressure=10,
            separation_between_issuers=20,
            length_max=6,
            diameter=5,
            localized_loss=100,
            type="with_plc"
        )

    @pytest.fixture
    def lateral_lines_persisted(self):
        return [
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
                type="with_plc"
            )
        ]

    def test_model_from_input_with_matching_type(self, lateral_line_input):

        output = LateralLineMapper.model_from_input(line=lateral_line_input, project_id=1)

        assert isinstance(output, LateralLine)

    def test_model_from_input_and_persisted_with_matching_type(self, lateral_line_input, lateral_lines_persisted):
        output = LateralLineMapper.model_from_input_and_persisted(
            lateral_line_input, lateral_lines_persisted, project_id=1
        )

        assert isinstance(output, LateralLine)
