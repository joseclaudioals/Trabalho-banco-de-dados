CREATE DATABASE ecommerce;

CREATE TABLE cargo(
id_cargo serial,
nome_cargo varchar(50) not null,
descricao_cargo varchar(255),
salario decimal(8,2), 

constraint pk_cargo primary key (id_cargo)
);

CREATE TABLE funcionario(
id_funcionario serial,
nome_funcionario varchar(150) not null,
cpf_funcionario varchar(11),
email_funcionario varchar(150),
telefone_funcionario varchar(11),
id_cargo int,

constraint pk_funcionario primary key (id_funcionario),
constraint uk_cpf_funcionario unique(cpf_funcionario),
constraint uk_email_funcionario unique(email_funcionario),
constraint chk_telefone_funcionario check(telefone_funcionario ~ '^\d{10,11}$'),
constraint fk_funcionario_cargo foreign key (id_cargo) references cargo(id_cargo)
);

CREATE TABLE produto(
id_produto serial,
descricao varchar(150),
foto varchar(255),
cor varchar(20) not null,
nome varchar(30) not null,
tamanho varchar(2) not null,
preco_unitario decimal (8,2) not null,
qnt integer,

constraint pk_produto primary key (id_produto),
constraint chk_tamanho check (tamanho in('pp', 'p', 'm', 'g', 'gg')),
constraint chk_preco check(preco_unitario>=0),
constraint chk_qnt check(qnt>=0)
);

CREATE TABLE auditoria(
id_auditoria serial,
id_funcionario int,
id_produto int,
descricao_auditoria varchar(120),
data_auditoria timestamp,

constraint pk_auditoria primary key(id_auditoria),
constraint fk_produto_auditoria foreign key (id_produto)
	references produto(id_produto),
constraint fk_auditoria_adm foreign key(id_funcionario)
	references funcionario(id_funcionario)
);

CREATE TABLE cliente(
id_cliente serial not null,
email VARCHAR(30) not null,
senha VARCHAR(30) not null,
nome_cliente VARCHAR(30) not null,
data_nascimento DATE not null,
telefone CHAR(11) not null,
cep CHAR(8) not null,
numero_casa VARCHAR(10) not null,

constraint pk_cliente primary key(id_cliente),
constraint uk_email unique(email),
constraint chk_telefone_cliente check(telefone ~ '^\d{10,11}$'),
constraint chk_cep_client check(cep ~ '^\d{8}$')
);

CREATE TABLE forma_pagamento(
id_forma_pagamento serial,
id_cliente INT not null,
numero_banco CHAR(16) not null,
endereco_cobranca VARCHAR(10) not null,

constraint pk_cartao primary key(id_forma_pagamento),
constraint fk_cartao_cliente foreign key (id_cliente)
	references cliente(id_cliente)
	on delete cascade
	on update cascade
);

CREATE TABLE carrinho(
id_carrinho serial,
id_cliente INT not null,
data_criacao TIMESTAMP not null,

constraint pk_carrinho1 primary key(id_carrinho),
constraint fk_carrinho_cliente foreign key (id_cliente)
	references cliente(id_cliente)
	on delete cascade
	on update cascade 
);

CREATE TABLE carrinho_produto(
id_carrinho INT,
id_produto INT,
qtd_produto_carrinho int not null,

constraint chk_qtd_produto_carrinho check(qtd_produto_carrinho>0),
constraint pk_carrinho_produto primary key (id_carrinho, id_produto),
constraint fk_produto1 foreign key (id_produto) 
	references produto(id_produto)
	on delete cascade 
	on update  cascade,
constraint fk_carrinho2 foreign key (id_carrinho) 
	references carrinho(id_carrinho)
	on delete  cascade 
	on update  cascade
);

CREATE TABLE pedido(
id_pedido serial,
id_cliente INT not null,
data_pedido TIMESTAMP not null,
frete decimal(5, 2),

constraint pk_pedido1 primary key (id_pedido),
constraint fk_pedido_cliente foreign key (id_cliente) 
	references cliente(id_cliente)
	on delete restrict 
	on update cascade 
);

CREATE TABLE produto_pedido(
id_pedido INT,
id_produto INT,
quantidade_compra int not null,
preco_unitario decimal(8,2) not null,
constraint pk_pedido_produto primary key (id_pedido, id_produto),
constraint fk_pedido_produto foreign key (id_pedido) 
	references pedido(id_pedido)
	on update cascade
	on delete cascade,
constraint fk_produto_pedido foreign key (id_produto) 
	references produto(id_produto)
	on delete restrict
	on update cascade
);