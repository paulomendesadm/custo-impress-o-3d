SELECT
    peca,
    ROUND(
        filamento_g / 1000.0 * preco_filamento_kg / quantidade_lote,
        2
    ) AS custo_filamento_por_peca
FROM impressoes;




