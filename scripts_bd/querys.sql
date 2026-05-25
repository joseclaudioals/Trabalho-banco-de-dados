SELECT 
    c.nome_cliente,
    p.id_pedido,
    p.data_pedido,
    p.frete,
    SUM(pp.quantidade_compra * pp.preco_unitario) AS total_produtos,
    SUM(pp.quantidade_compra * pp.preco_unitario) + p.frete AS valor_total_pedido
FROM pedido p
JOIN cliente c ON p.id_cliente = c.id_cliente
JOIN produto_pedido pp ON p.id_pedido = pp.id_pedido
GROUP BY c.nome_cliente, p.id_pedido, p.data_pedido, p.frete
ORDER BY valor_total_pedido DESC;

SELECT 
    prod.nome,
    prod.tamanho,
    SUM(pp.quantidade_compra) AS total_unidades_vendidas
FROM produto prod
JOIN produto_pedido pp ON prod.id_produto = pp.id_produto
GROUP BY prod.nome, prod.tamanho
ORDER BY total_unidades_vendidas DESC;
