-- Trigger 1
CREATE OR REPLACE FUNCTION validar_estoque_carrinho()
RETURNS TRIGGER AS $$
DECLARE
    estoque_atual INT;
BEGIN
    SELECT qnt INTO estoque_atual 
    FROM produto 
    WHERE id_produto = NEW.id_produto;

    IF NEW.qtd_produto_carrinho > estoque_atual THEN
        RAISE EXCEPTION 'Estoque insuficiente para (ID: %). Disponível: %, Solicitado: %.', 
            NEW.id_produto, estoque_atual, NEW.qtd_produto_carrinho;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_validar_estoque_carrinho
BEFORE INSERT OR UPDATE ON carrinho_produto
FOR EACH ROW
EXECUTE FUNCTION validar_estoque_carrinho();

-- Teste 1
INSERT INTO carrinho_produto (id_carrinho, id_produto, qtd_produto_carrinho) 
VALUES (1, 1, 200);

-- Trigger 2
CREATE OR REPLACE FUNCTION auditar_alteracoes_produto()
RETURNS TRIGGER AS $$
BEGIN

    IF (TG_OP = 'INSERT') THEN
        INSERT INTO auditoria (id_funcionario, id_produto, descricao_auditoria, data_auditoria)
        VALUES (NULL, NEW.id_produto, 'PRODUTO CADASTRADO: Nome: ' || NEW.nome || ' | Preço: R$ ' || NEW.preco_unitario, NOW());
        RETURN NEW;

    ELSIF (TG_OP = 'UPDATE') THEN
        IF (OLD.preco_unitario IS DISTINCT FROM NEW.preco_unitario OR OLD.qnt IS DISTINCT FROM NEW.qnt) THEN
            INSERT INTO auditoria (id_funcionario, id_produto, descricao_auditoria, data_auditoria)
            VALUES (
                NULL, 
                NEW.id_produto, 
                'PRODUTO ALTERADO -> Preço Antigo: R$ ' || OLD.preco_unitario || ' | Novo: R$ ' || NEW.preco_unitario ||
                ' -- Estoque Antigo: ' || OLD.qnt || ' | Novo: ' || NEW.qnt, 
                NOW()
            );
        END IF;
        RETURN NEW;

    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO auditoria (id_funcionario, id_produto, descricao_auditoria, data_auditoria)
        VALUES (NULL, OLD.id_produto, 'PRODUTO EXCLUÍDO DO SISTEMA -> Nome: ' || OLD.nome, NOW());
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_auditoria_produto
AFTER INSERT OR UPDATE OR DELETE ON produto
FOR EACH ROW
EXECUTE FUNCTION auditar_alteracoes_produto();

-- Teste 2
UPDATE produto SET preco_unitario = 55.00, qnt = 90 WHERE id_produto = 1;
SELECT * FROM auditoria;
