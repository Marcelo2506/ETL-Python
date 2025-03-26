from pydantic import BaseModel, Field
from typing import Optional


class Planilha(BaseModel):
    Organizador: int = Field(..., description="Identificador do organizador")
    Ano_Mes: str = Field(..., description="Ano e mês do registro")
    Dia_da_Semana: str = Field(...,
                               description="Dia da semana correspondente à data")
    Tipo_Dia: str = Field(...,
                          description="Classificação do dia: útil, feriado, etc...")
    Objetivo: str = Field(..., description="Objetivo da campanha ou ação")
    Date: str = Field(...,
                      description="Data de entrada no formato: YYYY-MM-DD")
    AdSet_name: Optional[str] = Field(
        None, description="Nome do Conjunto de anúncios")
    Amount_spent: float = Field(
        0.0, ge=0, le=1200.00, description="Valor gasto no anúncio (mínimo 0, máximo 589.96)")
    Link_clicks: Optional[float] = Field(
        None, description="Número de clicks no link", nullable=True)
    Impressions: int = Field(
        0, description="Número de Impressões no anúncio", nullable=True)
    Conversions: Optional[float] = Field(
        None, description="Número de Conversões Registradas", nullable=True)
    Segmentação: Optional[str] = Field(
        None, description="Segmentação Usada no Anúncio")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de Anúncio")
    Fase: str = Field(..., description="Fase da Camapanha")
