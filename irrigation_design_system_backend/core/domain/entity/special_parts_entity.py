from decimal import Decimal
from dataclasses import dataclass


@dataclass
class SpecialPartsEntity:
  
  DE : Decimal
  D: Decimal
  joelho_90: Decimal
  joelho_45: Decimal
  curva_90: Decimal
  curva_45: Decimal
  tê_90_passagem_direta: Decimal
  tê_90_saida_de_lado: Decimal
  tê_90_saida_bilateral: Decimal
  entrada_normal: Decimal
  entrada_de_borda: Decimal
  saida_canalização: Decimal
  valvula_pe_crivo: Decimal
  valvula_retenção_tipo_leve: Decimal
  valvula_retenção_tipo_pesado: Decimal
  registro_globo_aberto: Decimal
  registro_gaveta_aberto: Decimal
  registro_angulo_aberto: Decimal
