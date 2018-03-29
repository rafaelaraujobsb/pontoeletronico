INSERT INTO acesso(nome) VALUES ('Administrador');
INSERT INTO acesso(nome) VALUES ('Funcionario');

INSERT INTO funcionario (cod_acesso, nome, usuario, senha, pin, carga_horaria) VALUES (1,'admin','admin','4badaee57fed5610012a296273158f5f',1010,0)

INSERT INTO tipo(nome) VALUES ('Entrada');
INSERT INTO tipo(nome) VALUES ('Saída Almoço');
INSERT INTO tipo(nome) VALUES ('Volta Almoço');
INSERT INTO tipo(nome) VALUES ('Saída');

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Zé 1',0000,40,'pth','d5e369e3921fa4903862cc6461b24b97', 1);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Zé 2',3258,45,'floop','d5e369e1921fa4203862ce6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Zé 3',1234,60,'op','d5e369e1921fa1489862ce6461b24b97', 2);


INSERT INTO ponto(loc, matricula, cod_tipo)
	VALUES ('Qnh Area Esp 86', 2, 1);

INSERT INTO ponto(loc, matricula, cod_tipo)
	VALUES ('Qnh Area Esp 86', 2, 2);

INSERT INTO ponto(loc, matricula, cod_tipo) 
	VALUES ('Qnh Area Esp 86', 1, 3);

INSERT INTO ponto(loc, matricula, cod_tipo) 
	VALUES ('Qnh Area Esp 86', 1, 4);

INSERT INTO ponto(loc, matricula, cod_tipo) 
	VALUES ('Qnh Area Esp 86', 3, 1);

INSERT INTO ponto(loc, matricula, cod_tipo) 
	VALUES ('Qnh Area Esp 86', 3, 2);
