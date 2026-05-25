-- View 1
CREATE OR REPLACE VIEW funcionario_cargo AS
	SELECT funcionario.nome_funcionario, cargo.nome_cargo
	FROM funcionario
	inner join cargo
	ON funcionario.id_cargo = cargo.id_cargo;

-- Teste 1
SELECT * FROM funcionario_cargo;

-- View 2
CREATE OR REPLACE VIEW tamanho_produto AS
	SELECT nome,
	id_produto,
	tamanho
	FROM produto
	where tamanho = 'gg';

-- Teste 2
SELECT * FROM tamanho_produto;

-- View 3
CREATE OR REPLACE VIEW fechamento_financeiro as
	select 
		pedido.id_pedido,
    	pedido.frete,
	SUM(produto_pedido.quantidade_compra * produto_pedido.preco_unitario) + pedido.frete AS valor_total_pedido
	FROM pedido inner join produto_pedido
	on pedido.id_pedido = produto_pedido.id_pedido
	GROUP BY pedido.id_pedido, pedido.frete;

-- Teste 3
SELECT * FROM fechamento_financeiro;