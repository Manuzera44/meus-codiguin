CREATE TABLE estudante(
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(250) NOT NULL,0
    dt_nascimento DATE, 
    cpf VARCHAR(12)
    
);

CREATE TABLE uc(
	id INT AUTO_INCREMENT PRIMARY KEY,
    título VARCHAR(20),
    sigla CHAR(4)

);

CREATE TABLE matrícula (
	id INT AUTO_INCREMENT PRIMARY KEY,
    id_estudante INT,
    id_uc INT NOT NULL,
    FOREIGN KEY(id_estudante) REFERENCES estudante(id),
    FOREIGN KEY(id_uc) REFERENCES uc(id)
);

CREATE TABLE avaliacao(
	id INT AUTO_INCREMENT PRIMARY KEY,
    materia VARCHAR(50),
    dt_aplicacao DATETIME,
	id_uc INT NOT NULL,
    FOREIGN KEY (id_uc) REFERENCES uc(id)

);

CREATE TABLE questao(
	id INT AUTO_INCREMENT PRIMARY KEY,
    numero INT,
    enunciado TEXT,
    id_avaliacao INT NOT NULL,
    FOREIGN KEY(id_avaliacao) REFERENCES avaliacao(id)
);

CREATE TABLE alternativa(
	id INT AUTO_INCREMENT PRIMARY KEY,
    letra CHAR(1),
    descricao TEXT,
    id_questao INT NOT NULL,
    FOREIGN KEY (id_questao) REFERENCES questao(id)
);
CREATE TABLE resposta(
	id INT AUTO_INCREMENT PRIMARY KEY,
    ud_estudante INT NOT NULL,
    id_questao INT NULL,
    id_alternativa INT NOT NULL,
    FOREIGN KEY (id_estudante) REFERENCES estudante(id),
	FOREIGN KEY (id_questao) REFERENCES qeustao(id),	
    FOREIGN KEY (id_alternativa) REFERENCES alternativa(id),
    UNIQUE KEY (id_estudante, id_alternativa)


);