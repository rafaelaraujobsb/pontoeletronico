INSERT INTO acesso(nome) VALUES ('Administrador');
INSERT INTO acesso(nome) VALUES ('Funcionario');

INSERT INTO funcionario (cod_acesso, nome, usuario, senha, pin, carga_horaria) VALUES (1,'admin','admin','4badaee57fed5610012a296273158f5f',1010,0);

INSERT INTO tipo(nome) VALUES ('Entrada');
INSERT INTO tipo(nome) VALUES ('Saída Almoço');
INSERT INTO tipo(nome) VALUES ('Volta Almoço');
INSERT INTO tipo(nome) VALUES ('Saída');

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Breno Santos Gomes',2389,40,'breno','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Daniel Dias Azevedo',1254,40,'danielaz','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Vitoria Cardoso Oliveira',4589,40,'vitcard','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Martim Castro Rocha',9643,40,'martimc','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Kai Souza Martins',1245,40,'kais','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Joao Cardoso Cunha',9962,40,'joaocc','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Carlos Sousa Gomes',2296,40,'carlossou','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Raissa Santos Costa',7896,40,'raissas','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Amanda Sousa Cardoso',1123,40,'amand','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Clara Pinto Cardoso',7892,40,'clarapc','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Danilo Almeida Oliveira',1548,40,'danial','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Melissa Barros Azevedo',7830,40,'melss','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Matheus Rocha Barbosa',1234,40,'mthbr','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Renan Almeida Goncalves',1247,40,'rengon','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Ryan Barros Ribeiro',9942,40,'ryanbr','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Kauê Ribeiro Oliveira',2364,40,'kauerb','d5e369e3921fa4903862cc6461b24b97', 2);

INSERT INTO funcionario(nome,pin,carga_horaria,usuario,senha, cod_acesso)
	VALUES ('Enzo Pereira Ferreira',7931,40,'enzfer','d5e369e3921fa4903862cc6461b24b97', 2);


INSERT INTO ponto(data,hora,localizacaoalizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','08:51:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 1, 1);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','09:01:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 6, 1);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','09:10:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 7, 1);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','09:11:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 9, 1);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','09:20:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 4, 1);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','09:31:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 3, 1);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','11:51:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 1, 4);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','12:01:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 7, 2);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','12:20:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 10, 1);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','12:25:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 6, 2);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','12:31:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 9, 2);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','12:32:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 4, 2);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','12:41:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 3, 2);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','14:10:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 7, 3);

INSERT INTO ponto(data,hora,localizacao, matricula, cod_tipo)
	VALUES ('2018-02-01','15:30:02.746572-08','St. Comercial Norte Q 1 BL A Edifício Number One SL 201', 3, 4);


