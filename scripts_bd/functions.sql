CREATE OR REPLACE FUNCTION verificar_estoque_critico(p_limite INT)
RETURNS VOID AS $$

DECLARE
    v_reg RECORD;
BEGIN
    
    FOR v_reg IN
        SELECT id_produto, nome, qnt
        FROM produto
        WHERE qnt < p_limite
    LOOP

        RAISE NOTICE 'ALERTA: Estoque em capacidade critica para produto %', v_reg.nome;
    
    END LOOP;
    
    RETURN;
END;
$$ 
LANGUAGE plpgsql;

SELECT verificar_estoque_critico(40);

CREATE OR REPLACE FUNCTION obter_categoria_cliente(p_id_cliente INT)
RETURNS VARCHAR AS $$
DECLARE 
    v_total_compra DECIMAL;
BEGIN
    SELECT COALESCE(sum(pp.quantidade_compra * pp.preco_unitario), 0) INTO v_total_compra
    FROM pedido p
    JOIN produto_pedido pp
    ON p.id_pedido = pp.id_pedido
    WHERE p_id_cliente = p.id_cliente;

    IF v_total_compra > 1000.00 THEN
        RETURN 'Cliente: VIP';
    ELSIF v_total_compra > 500 AND v_total_compra <= 1000 THEN
        RETURN 'Cliente: PLATINUM';
    ELSE 
        RETURN 'Cliente: STANDART';
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Teste 2
SELECT obter_categoria_cliente(1);

CREATE OR REPLACE FUNCTION calcular_total_pedido(p_id_pedido INT)
RETURNS DECIMAL AS $$
DECLARE
    v_total DECIMAL;
BEGIN
    SELECT
        COALESCE(SUM(pp.quantidade_compra * pp.preco_unitario), 0) + p.frete
    INTO v_total
    FROM produto_pedido pp
    LEFT JOIN pedido p ON p.id_pedido = pp.id_pedido 
    WHERE p.id_pedido = p_id_pedido
    GROUP BY p.frete;    

    RETURN v_total;
END;
$$ 

LANGUAGE plpgsql;

-- Teste 3
SELECT calcular_total_pedido(1);