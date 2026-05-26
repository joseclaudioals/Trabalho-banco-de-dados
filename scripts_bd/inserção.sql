INSERT INTO cargo (nome_cargo, descricao_cargo, salario) VALUES
('Gerente de Loja', 'Gerencia a equipe comercial da boutique', 5500.00),
('Consultora de Vendas', 'Atendimento especializado e vendas', 2500.00),
('Estoquista', 'Organização e controle de peças delicadas', 2000.00),
('Caixa', 'Operação de pagamentos', 2100.00),
('Analista de TI', 'Suporte ao sistema do ecommerce', 4500.00),
('Coordenador de RH', 'Recrutamento e seleção', 4800.00),
('Assistente de Logística', 'Separação e embalagem de pacotes', 2200.00),
('Analista de Marketing', 'Criação de campanhas de moda íntima', 3800.00),
('Diretor Executivo', 'Gestão geral da marca', 12000.00),
('Jovem Aprendiz', 'Auxílio administrativo', 1200.00);

INSERT INTO funcionario (nome_funcionario, cpf_funcionario, email_funcionario, telefone_funcionario, id_cargo) VALUES
('Carlos Silva', '11122233344', 'carlos@lingerie.com', '11987654321', 1),
('Fernanda Souza', '22233344455', 'fernanda@lingerie.com', '21987654322', 2),
('Roberto Alves', '33344455566', 'roberto@lingerie.com', '31987654323', 3),
('Luciana Costa', '44455566677', 'luciana@lingerie.com', '41987654324', 4),
('Marcos Dias', '55566677788', 'marcos@lingerie.com', '51987654325', 5),
('Camila Rocha', '66677788899', 'camila@lingerie.com', '61987654326', 6),
('João Pedro', '77788899900', 'joao@lingerie.com', '71987654327', 7),
('Aline Nunes', '88899900011', 'aline@lingerie.com', '81987654328', 8),
('Ricardo Lima', '99900011122', 'ricardo@lingerie.com', '91987654329', 9),
('Paula Martins', '00011122233', 'paula@lingerie.com', '11987654330', 10);

INSERT INTO produto (descricao, foto, cor, nome, tamanho, preco_unitario, qnt) VALUES
('Sutiã com bojo e detalhes em renda', 'prod1.jpg', 'Preto', 'Sutiã de Renda', 'm', 79.90, 100),
('Calcinha fio dental dupla', 'prod2.jpg', 'Vermelho', 'Calcinha Fio Dental', 'p', 29.90, 150),
('Babydoll de seda com alças finas', 'prod3.jpg', 'Branco', 'Babydoll de Seda', 'g', 119.90, 40),
('Body todo em renda com transparência', 'prod4.jpg', 'Vinho', 'Body Rendado', 'm', 149.90, 25),
('Espartilho com barbatanas e cinta-liga', 'prod5.jpg', 'Preto', 'Espartilho Sensual', 'gg', 199.90, 15),
('Calcinha básica 100% algodão', 'prod6.jpg', 'Bege', 'Calcinha Conforto', 'g', 19.90, 200),
('Sutiã sem alças estruturado', 'prod7.jpg', 'Nude', 'Sutiã Tomara que Caia', 'm', 89.90, 60),
('Camisola longa com fenda', 'prod8.jpg', 'Azul Marinho', 'Camisola Longa', 'p', 159.90, 20),
('Robe de cetim com faixa', 'prod9.jpg', 'Rosa', 'Robe de Cetim', 'g', 129.90, 45),
('Conjunto sutiã e calcinha com tiras', 'prod10.jpg', 'Preto', 'Conjunto Strappy', 'm', 139.90, 50);

INSERT INTO auditoria (id_funcionario, id_produto, descricao_auditoria, data_auditoria) VALUES
(1, 1, 'Alteração de preço', '2026-05-01 10:00:00'),
(2, 2, 'Contagem de estoque', '2026-05-02 11:30:00'),
(3, 3, 'Entrada de lote', '2026-05-03 14:15:00'),
(5, 4, 'Correção de cadastro', '2026-05-04 09:45:00'),
(1, 5, 'Produto ativado', '2026-05-05 16:20:00'),
(8, 6, 'Campanha promocional Dia dos Namorados', '2026-05-06 08:10:00'),
(3, 7, 'Ajuste de cor', '2026-05-07 13:05:00'),
(1, 8, 'Baixa por avaria (renda rasgada)', '2026-05-08 17:50:00'),
(5, 9, 'Cadastro inicial', '2026-05-09 10:30:00'),
(8, 10, 'Atualização de foto de ensaio', '2026-05-10 15:40:00');

INSERT INTO cliente (email, senha, nome_cliente, data_nascimento, telefone, cep, numero_casa) VALUES
('cli1@email.com', '123', 'Calebe Oliveira', '2000-01-15', '11912345678', '64200000', '10A'),
('cli2@email.com', '123', 'Beatriz Souza', '1998-05-20', '21912345678', '01001000', '200'),
('cli3@email.com', '123', 'Diego Silva', '1985-08-10', '31912345678', '30110000', '55'),
('cli4@email.com', '123', 'Heloisa Rocha', '1995-12-05', '41912345678', '80010000', '102B'),
('cli5@email.com', '123', 'Gabriel Santos', '1992-04-22', '51912345678', '90010000', '33'),
('cli6@email.com', '123', 'Fernanda Costa', '1999-07-30', '61912345678', '70040000', '14'),
('cli7@email.com', '123', 'Lucas Almeida', '1988-11-12', '71912345678', '40010000', '90'),
('cli8@email.com', '123', 'Mariana Ribeiro', '1994-02-28', '81912345678', '50010000', '8A'),
('cli9@email.com', '123', 'Thiago Mendes', '1990-09-15', '85912345678', '60010000', '77'),
('cli10@email.com', '123', 'Juliana Castro', '1987-06-18', '92912345678', '69010000', '1200');

INSERT INTO forma_pagamento (id_cliente, numero_banco, endereco_cobranca) VALUES
(1, '1111222233334444', 'Rua A, 10'),
(2, '5555666677778888', 'Casa 200'),
(3, '9999000011112222', 'Apt 55'),
(4, '3333444455556666', 'Bloco B'),
(5, '7777888899990000', 'Rua C, 33'),
(6, '2222333344445555', 'Lote 14'),
(7, '6666777788889999', 'Casa 90'),
(8, '0000111122223333', 'Rua D, 8A'),
(9, '4444555566667777', 'Apt 77'),
(10, '8888999900001111', 'Galpao 1');

INSERT INTO carrinho (id_cliente, data_criacao) VALUES
(1, '2026-05-10 08:00:00'), (2, '2026-05-10 09:30:00'),
(3, '2026-05-10 10:15:00'), (4, '2026-05-10 11:45:00'),
(5, '2026-05-10 12:20:00'), (6, '2026-05-10 14:10:00'),
(7, '2026-05-10 15:05:00'), (8, '2026-05-10 16:50:00'),
(9, '2026-05-10 18:30:00'), (10, '2026-05-10 20:40:00');

INSERT INTO carrinho_produto (id_carrinho, id_produto, qtd_produto_carrinho) VALUES
(1, 1, 2), (2, 2, 1), (3, 3, 3), (4, 4, 1), (5, 5, 2),
(6, 6, 1), (7, 7, 1), (8, 8, 4), (9, 9, 2), (10, 10, 1);

INSERT INTO pedido (id_cliente, data_pedido, frete) VALUES
(1, '2026-05-11 08:30:00', 15.50), (2, '2026-05-11 09:45:00', 0.00),
(3, '2026-05-11 10:20:00', 20.00), (4, '2026-05-11 11:55:00', 12.00),
(5, '2026-05-11 12:30:00', 15.00), (6, '2026-05-11 14:40:00', 18.50),
(7, '2026-05-11 15:15:00', 0.00),  (8, '2026-05-11 17:00:00', 22.00),
(9, '2026-05-11 18:45:00', 10.00), (10, '2026-05-11 21:00:00', 0.00);

INSERT INTO produto_pedido (id_pedido, id_produto, quantidade_compra, preco_unitario) VALUES
(1, 1, 2, 79.90), 
(2, 2, 1, 29.90), 
(3, 3, 3, 119.90),
(4, 4, 1, 149.90), 
(5, 5, 2, 199.90), 
(6, 6, 1, 19.90),
(7, 7, 1, 89.90), 
(8, 8, 4, 159.90), 
(9, 9, 2, 129.90),
(10, 10, 1, 139.90);