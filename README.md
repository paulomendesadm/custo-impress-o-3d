# Análise de custos de impressão 3D

## Objetivo

Calcular o custo de filamento por peça a partir do peso do lote, do
preço do filamento por quilo e da quantidade de peças.

## Como rodar

Com o Python instalado, abra um terminal na pasta do projeto e execute:

```text
python executar_consulta.py
```

## Resultados

- Fidget estrela curva — R$ 8,30 por peça, com consumo medido.
- Fidget ovo de dragão — R$ 12,00 por peça, estimados para um lote de três.

## O que aprendi

Aprendi a calcular em SQL o custo de filamento por peça a partir do consumo total do lote. Primeiro, converti o peso de gramas para quilogramas e multipliquei pelo preço do filamento por quilo. Depois, dividi o custo do lote pela quantidade de peças.

A estrela curva foi impressa em uma única unidade, então o custo do lote e o custo por peça são iguais: R$ 8,30. Para os ovos de dragão, o consumo previsto de 360 g corresponde a um custo de R$ 36,00 para o lote. Dividindo esse valor por três, o custo estimado é de R$ 12,00 por peça, considerando que todas saiam em condições de venda.


