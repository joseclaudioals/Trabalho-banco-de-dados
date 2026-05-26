CREATE OR REPLACE VIEW funcionario_cargo AS
	SELECT funcionario.nome_funcionario, cargo.nome_cargo
	FROM funcionario
	inner join cargo
	ON funcionario.id_cargo = cargo.id_cargo;

SELECT * FROM funcionario_cargo;

CREATE OR REPLACE VIEW tamanho_produto AS
	SELECT nome,
	id_produto,
	tamanho
	FROM produto
	where tamanho = 'gg';

SELECT * FROM tamanho_produto;

CREATE OR REPLACE VIEW fechamento_financeiro as
	select 
		pedido.id_pedido,
    	pedido.frete,
	SUM(produto_pedido.quantidade_compra * produto_pedido.preco_unitario) + pedido.frete AS valor_total_pedido
	FROM pedido inner join produto_pedido
	on pedido.id_pedido = produto_pedido.id_pedido
	GROUP BY pedido.id_pedido, pedido.frete;

SELECT * FROM fechamento_financeiro;