DROP DATABASE IF EXISTS roblox_db;
CREATE DATABASE roblox_db;
USE roblox_db;

CREATE TABLE cadastro (
    nome VARCHAR(255),
    senha INT PRIMARY KEY AUTO_INCREMENT
);

CREATE TABLE perguntas (
    pergunta_1 TEXT,
    pergunta_2 TEXT,
    pergunta_3 TEXT
);

CREATE TABLE respostas (
    nome VARCHAR(80),
    resposta1 TEXT,
    resposta2 TEXT,
    resposta3 TEXT
);

INSERT INTO perguntas (pergunta_1, pergunta_2, pergunta_3) VALUES
('O que você mais gosta no Roblox e por quê?', 
'Na sua opinião, quais são os pontos positivos e negativos do Roblox?', 
'nota de 0 a 10 para o jogo');
