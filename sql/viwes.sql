-- view para mostrar todos os registros
CREATE VIEW viewreg AS
	SELECT funcionario.nome AS funcionario, 
		to_char(ponto.data, 'DD Mon YYYY') AS data, 
		to_char(ponto.hora, 'HH24:MI') AS hora,
		ponto.localizacao AS local,
		tipo.nome AS tipo
	FROM ponto
		INNER JOIN funcionario ON (funcionario.matricula = ponto.matricula)
		INNER JOIN tipo ON (tipo.cod_tipo = ponto.cod_tipo)
	ORDER BY ponto.cod_ponto DESC;

--view gráfico
CREATE VIEW viewgraph AS
	SELECT
		to_char(ponto.data, 'DD Mon YYYY') AS data, 
		to_char(ponto.hora, 'HH24:MI') AS hora,
		tipo.cod_tipo AS tipo
	FROM ponto
		INNER JOIN funcionario ON (funcionario.matricula = ponto.matricula)
		INNER JOIN tipo ON (tipo.cod_tipo = ponto.cod_tipo)
	ORDER BY ponto.cod_ponto DESC;
