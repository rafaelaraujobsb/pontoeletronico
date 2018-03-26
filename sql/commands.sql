/*
	Criação do banco de dados pontoeletronico
	Autor: Rafael Araujo
	Data: 25/03/2018
*/

-- DROP DATABASE pontoeletronico;

/*CREATE DATABASE pontoeletronico
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
*/

--Tabela Acesso
CREATE TABLE acesso(
	cod_acesso SMALLSERIAL PRIMARY KEY,
	nome VARCHAR(15) NOT NULL
);

--Tabela Tipo Registro
CREATE TABLE tipo_reg(
	cod_tiporeg SMALLSERIAL PRIMARY KEY,
	nome VARCHAR(12) NOT NULL
);

--Tabela Funcionario 
CREATE TABLE funcionario(
	matricula SMALLSERIAL PRIMARY KEY,
	cod_acesso SMALLINT NOT NULL,
	nome VARCHAR(40) NOT NULL,
	cpf VARCHAR(11) NOT NULL,
	fone VARCHAR(9) NOT NULL,
	pin SMALLINT NOT NULL,
	carga_horaria SMALLINT NOT NULL,
	usuario VARCHAR(10) NOT NULL,
	senha VARCHAR(32) NOT NULL,
	FOREIGN KEY (cod_acesso) --foreign key da tabela acesso
	REFERENCES acesso (cod_acesso)
	ON UPDATE CASCADE ON DELETE CASCADE
);

--Tabela Registro
CREATE TABLE registro(
	cod_reg SMALLSERIAL PRIMARY KEY,
	matricula SMALLINT NOT NULL,
	cod_tiporeg SMALLINT NOT NULL,
	data DATE DEFAULT CURRENT_DATE, --data do sistema, preenchimento automatico 
	hora TIME DEFAULT CURRENT_TIME, --hora do sistema , preenchimento automatico
	foto BYTEA NOT NULL,
	loc VARCHAR(40) NOT NULL,
	FOREIGN KEY (matricula) --foreign key da tabela funcionario
		REFERENCES funcionario (matricula)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (cod_tiporeg) --foreign key da tabela tipo_reg
		REFERENCES tipo_reg (cod_tiporeg)
		ON UPDATE CASCADE ON DELETE CASCADE
);
