from core.domain.entity.project_input import ProjectInput, DerivationLineInput, LateralLineInput
from infrastructure.persistence.models import Project, DerivationLine, LateralLine


class ProjectMapper:
    @staticmethod
    def entity_to_model(project_entity: ProjectInput) -> Project:

        project = Project(
            user_id=project_entity.user_id,
            group_id=project_entity.group_id,
            description=project_entity.description,
            status=project_entity.status,
            crop=project_entity.crop,
            maximum_actual_irrigation_required=project_entity.maximum_actual_irrigation_required,
            crop_evapotranspiration=project_entity.crop_evapotranspiration,
            total_irrigation_required=project_entity.total_irrigation_required,
        )

        derivation_line = [DerivationLine(
            pipe_type=line.pipe_type,
            inlet_pressure=line.inlet_pressure,
            length=line.length,
            diameter=line.diameter,
            localized_loss=line.localized_loss,
            type=line.type
        ) for line in project_entity.derivation_line]

        lateral_line = [LateralLine(
            dripper=line.dripper,
            decline=line.decline,
            inlet_pressure=line.inlet_pressure,
            separation_between_issuers=line.separation_between_issuers,
            length_max=line.length_max,
            diameter=line.diameter,
            localized_loss=line.localized_loss,
            type=line.type

        ) for line in project_entity.lateral_line]

        project.derivation_line = derivation_line
        project.lateral_line = lateral_line

        return project


class DerivationLineMapper:
    @staticmethod
    def entity_to_model(derivation_entity: DerivationLineInput) -> DerivationLine:
        return DerivationLine(**derivation_entity.dict())


class LateralLineMapper:

    @staticmethod
    def entity_to_model(lateral_line_entity: LateralLineInput) -> LateralLine:
        return LateralLine(**lateral_line_entity.dict())
