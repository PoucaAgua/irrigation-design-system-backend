from _decimal import Decimal

from core.domain.entity.special_parts_entity import SpecialPartsEntity

class SpecialPartsService:

    @staticmethod
    def special_parts_loadloss(special_parts_selected:SpecialPartsEntity) ->Decimal:
        
        diameter = special_parts_selected.DE
        diameter_pol = special_parts_selected.D
        sp1 = special_parts_selected.joelho_90
        sp2 = special_parts_selected.joelho_45
        sp3 = special_parts_selected.curva_90
        sp4 = special_parts_selected.curva_45
        sp5 = special_parts_selected.tê_90_passagem_direta
        sp6 = special_parts_selected.tê_90_saida_de_lado
        sp7 = special_parts_selected.tê_90_saida_bilateral
        sp8 = special_parts_selected.entrada_normal
        sp9 = special_parts_selected.entrada_de_borda
        sp10 = special_parts_selected.saida_canalização
        sp11 = special_parts_selected.valvula_pe_crivo
        sp12 = special_parts_selected.valvula_retenção_tipo_leve
        sp13 = special_parts_selected.valvula_retenção_tipo_pesado
        sp14 = special_parts_selected.registro_globo_aberto
        sp15 = special_parts_selected.registro_gaveta_aberto
        sp16 = special_parts_selected.registro_angulo_aberto

        return Decimal(200)
