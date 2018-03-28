SELECT funcionario.nome, registro.data, to_char(registro.hora, 'HH24:MI'), tipo_reg.nome AS tipo
FROM registro
INNER JOIN funcionario ON (funcionario.matricula = registro.matricula)
INNER JOIN tipo_reg ON (tipo_reg.cod_tiporeg = registro.cod_tiporeg)
