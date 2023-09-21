from core.domain.entity.project_input import ProjectInput, DerivationLineInput, LateralLineInput
from infrastructure.persistence.models import Project, DerivationLine, LateralLine


class ProjectMapper:
    @staticmethod
    def entity_to_model(project_input: ProjectInput) -> Project:
        return Project(
            id=project_input.id,
            user_id=project_input.user_id,
            group_id=project_input.group_id,
            description=project_input.description,
            status=project_input.status,
            crop=project_input.crop,
            maximum_actual_irrigation_required=project_input.maximum_actual_irrigation_required,
            crop_evapotranspiration=project_input.crop_evapotranspiration,
            total_irrigation_required=project_input.total_irrigation_required,
        )


class DerivationLineMapper:
    @staticmethod
    def entity_to_model(line: DerivationLineInput, project_id: int) -> DerivationLine:
        return DerivationLine(
            project_id=project_id,
            pipe_type=line.pipe_type,
            inlet_pressure=line.inlet_pressure,
            length=line.length,
            diameter=line.diameter,
            localized_loss=line.localized_loss,
            type=line.type,
        )


class LateralLineMapper:
    @staticmethod
    def entity_to_model(line: LateralLineInput, project_id: int) -> LateralLine:
        return LateralLine(
            project_id=project_id,
            dripper=line.dripper,
            decline=line.decline,
            inlet_pressure=line.inlet_pressure,
            separation_between_issuers=line.separation_between_issuers,
            length_max=line.length_max,
            diameter=line.diameter,
            localized_loss=line.localized_loss,
            type=line.type,
        )
