/*
	Criação do banco de dados para o Ponto Eletrônico
	Autor: Rafael Araujo
	Data: 25/03/2018
*/

/*DROP DATABASE ptoeletr;

CREATE DATABASE ptoeletr
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

--Tabela Tipo 
CREATE TABLE tipo(
	cod_tipo SMALLSERIAL PRIMARY KEY,
	nome VARCHAR(12) NOT NULL
);

--Tabela Funcionario 
CREATE TABLE funcionario(
	matricula SMALLSERIAL PRIMARY KEY,
	cod_acesso SMALLINT NOT NULL,
	nome VARCHAR(40) NOT NULL,
	usuario VARCHAR(10) NOT NULL,
	senha VARCHAR(32) NOT NULL,
	pin SMALLINT NOT NULL,
	carga_horaria SMALLINT NOT NULL,
	FOREIGN KEY (cod_acesso) --foreign key da tabela acesso
	REFERENCES acesso (cod_acesso)
	ON UPDATE CASCADE ON DELETE CASCADE
);

--Tabela Ponto
CREATE TABLE ponto(
	cod_ponto SMALLSERIAL PRIMARY KEY,
	matricula SMALLINT NOT NULL,
	cod_tipo SMALLINT NOT NULL,
	data DATE DEFAULT CURRENT_DATE, --data do sistema, preenchimento automatico 
	hora TIME DEFAULT CURRENT_TIME, --hora do sistema , preenchimento automatico
	localizacao VARCHAR(60) NOT NULL,
	FOREIGN KEY (matricula) --foreign key da tabela funcionario
		REFERENCES funcionario (matricula)
		ON UPDATE CASCADE ON DELETE CASCADE,
	FOREIGN KEY (cod_tipo) --foreign key da tabela tipo_reg
		REFERENCES tipo (cod_tipo)
		ON UPDATE CASCADE ON DELETE CASCADE
);
