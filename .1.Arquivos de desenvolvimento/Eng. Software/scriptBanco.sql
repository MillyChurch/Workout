drop database Academia;
CREATE DATABASE IF NOT EXISTS Academia;

USE Academia;

CREATE TABLE TiposDeUsuario (
    idTipo INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nomeTipo VARCHAR(100) NOT NULL
);
INSERT INTO TiposDeUsuario (nomeTipo)
VALUES ("Professor"),("Aluno");

CREATE TABLE TiposDePlano (
    idPlano INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nomePlano VARCHAR(100) NOT NULL
);
INSERT INTO TiposDePlano (nomePlano)
VALUES ("Mensal"),("Anual"), ("Trimestral");

CREATE TABLE Aluno (
    idAluno INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nomeAluno VARCHAR(100) NOT NULL,
    tipoDePlano INT NOT NULL,
	ultimoPagamentoAluno DATE NOT NULL,
	dataVencimentoAluno DATE NOT NULL,
	statusPagamentoAluno BOOLEAN NOT NULL,
    FOREIGN KEY (tipoDePlano) REFERENCES TiposDePlano(idPlano)
);

CREATE TABLE Professor (
    idProfessor INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nomeProfessor VARCHAR(100) NOT NULL
);

CREATE TABLE Usuario (
	idUsuario INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    loginUsuario VARCHAR(100) NOT NULL,
	senhaUsuario VARCHAR(100) NOT NULL,
	idTipo INT NOT NULL,
	idAluno INT NULL,
	idProfessor INT NULL,
	FOREIGN KEY (idTipo) REFERENCES TiposDePlano(idPlano),
	FOREIGN KEY (idAluno) REFERENCES Aluno(idAluno),
	FOREIGN KEY (idProfessor) REFERENCES Professor(idProfessor)
);
INSERT INTO Usuario (loginUsuario,senhaUsuario,idTipo)
VALUES ("Administrador", "@workout1234", -1);

CREATE TABLE PlanoDeTreino (
    idPlanoDeTreino INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    idAluno INT NOT NULL,
    idProfessor INT NOT NULL,
    dataInicio DATE,
    dataFim DATE,
    FOREIGN KEY (idAluno) REFERENCES Aluno(idAluno),
    FOREIGN KEY (idProfessor) REFERENCES Professor(idProfessor)
);

CREATE TABLE Musculos (
    idMusculo INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    nomeMusculo VARCHAR(100) NOT NULL
);

CREATE TABLE Exercicio (
    idExercicio INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    musculoTrabalhado INT NOT NULL,
    nomeExercicio VARCHAR(100) NOT NULL,
    FOREIGN KEY (musculoTrabalhado) REFERENCES Musculos(idMusculo)
);

CREATE TABLE Treino (
    idTreino INT NOT NULL PRIMARY KEY AUTO_INCREMENT, 
    exercicio INT NOT NULL,
    planoDeTreino INT NOT NULL,
    diaDaSemana INT,
    series INT,
    repeticoes INT,
    observacoes MEDIUMTEXT,
    FOREIGN KEY (exercicio) REFERENCES Exercicio(idExercicio),
    FOREIGN KEY (planoDeTreino) REFERENCES PlanoDeTreino(idPlanoDeTreino)
);
