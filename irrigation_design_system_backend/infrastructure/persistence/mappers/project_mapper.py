from typing import List

from core.domain.entity.project_input import ProjectInput, DerivationLineInput, LateralLineInput
from infrastructure.persistence.models import Project, DerivationLine, LateralLine


class ProjectMapper:
    @staticmethod
    def model_from_input(project_input: ProjectInput) -> Project:
        field_mappings = dict(
            id=project_input.id,
            user_id=project_input.user_id,
            group_id=project_input.group_id,
            description=project_input.description,
            status=project_input.status,
            crop=project_input.crop,
            maximum_actual_irrigation_required=project_input.maximum_actual_irrigation_required,
            crop_evapotranspiration=project_input.crop_evapotranspiration,
            total_irrigation_required=project_input.total_irrigation_required,
            lateral_line=[
                LateralLineMapper.model_from_input(line, project_input.id)
                for line in project_input.lateral_line
            ],
            derivation_line=[
                DerivationLineMapper.model_from_input(line, project_input.id)
                for line in project_input.derivation_line
            ],
        )

        return Project(**field_mappings)

    @staticmethod
    def model_from_input_and_persisted(
        project_input: ProjectInput, project_persisted: Project
    ) -> Project:
        field_mappings = dict(
            id=project_input.id,
            user_id=project_input.user_id or project_persisted.user_id,
            group_id=project_input.group_id or project_persisted.group_id,
            description=project_input.description or project_persisted.description,
            status=project_input.status or project_persisted.status,
            crop=project_input.crop or project_persisted.crop,
            maximum_actual_irrigation_required=(
                project_input.maximum_actual_irrigation_required
                or project_persisted.maximum_actual_irrigation_required
            ),
            crop_evapotranspiration=(
                project_input.crop_evapotranspiration or project_persisted.crop_evapotranspiration
            ),
            total_irrigation_required=(
                project_input.total_irrigation_required
                or project_persisted.total_irrigation_required
            ),
            lateral_line=[
                LateralLineMapper.model_from_input_and_persisted(
                    line, project_persisted.lateral_line, project_input.id
                )
                for line in project_input.lateral_line
            ],
            derivation_line=[
                DerivationLineMapper.model_from_input_and_persisted(
                    line, project_persisted.derivation_line, project_input.id
                )
                for line in project_input.derivation_line
            ],
        )

        return Project(**field_mappings)


class DerivationLineMapper:
    @staticmethod
    def model_from_input(line: DerivationLineInput, project_id: int) -> DerivationLine:
        field_mappings = {**line.model_dump(), "project_id": project_id}
        return DerivationLine(**field_mappings)

    @staticmethod
    def model_from_input_and_persisted(
        line: DerivationLineInput, lines_persisted: List[DerivationLine], project_id: int
    ) -> DerivationLine:
        for line_persisted in lines_persisted:
            if line.type == line_persisted.type:
                field_mappings = dict(
                    id=line_persisted.id,
                    project_id=project_id,
                    pipe_type=line.pipe_type or line_persisted.pipe_type,
                    inlet_pressure=line.inlet_pressure or line_persisted.inlet_pressure,
                    length=line.length or line_persisted.length,
                    diameter=line.diameter or line_persisted.diameter,
                    localized_loss=line.localized_loss or line_persisted.localized_loss,
                    type=line.type,
                )
                return DerivationLine(**field_mappings)
        return DerivationLineMapper.model_from_input(line, project_id)


class LateralLineMapper:
    @staticmethod
    def model_from_input(line: LateralLineInput, project_id: int) -> LateralLine:
        field_mappings = {**line.model_dump(), "project_id": project_id}
        return LateralLine(**field_mappings)

    @staticmethod
    def model_from_input_and_persisted(
        line: LateralLineInput, lines_persisted: List[LateralLine], project_id: int
    ) -> LateralLine:
        for line_persisted in lines_persisted:
            if line.type == line_persisted.type:
                field_mappings = dict(
                    id=line_persisted.id,
                    project_id=project_id,
                    dripper=line.dripper or line_persisted.dripper,
                    decline=line.decline or line_persisted.decline,
                    inlet_pressure=line.inlet_pressure or line_persisted.inlet_pressure,
                    separation_between_issuers=line.separation_between_issuers
                    or line_persisted.separation_between_issuers,
                    length_max=line.length_max or line_persisted.length_max,
                    diameter=line.diameter or line_persisted.diameter,
                    localized_loss=line.localized_loss or line_persisted.localized_loss,
                    type=line.type,
                )
                return LateralLine(**field_mappings)
        return LateralLineMapper.model_from_input(line, project_id)
