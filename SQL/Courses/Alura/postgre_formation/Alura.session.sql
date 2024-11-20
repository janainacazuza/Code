-- Creating tables

CREATE TABLE aluno(
    id SERIAL,
        nome VARCHAR(255),
        cpf CHAR(11),
        observacao TEXT,
        idade INTEGER,
        dinheiro NUMERIC(10,2),
        altura REAL,
        ativo BOOLEAN,
        data_nascimento DATE,
        hora_aula TIME,
        matriculado_em TIMESTAMP
);
SELECT * FROM aluno;

-- Inserting data

INSERT INTO aluno (
    nome,
    cpf,
    observacao,
    idade,
    dinheiro,
    altura,
    ativo,
    data_nascimento,
    hora_aula,
    matriculado_em
) VALUES (
    'Diogo',
    '12345678901',
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac dui et nisl vestibulum consequat. Integer vitae magna egestas, finibus libero dapibus, maximus magna. Fusce suscipit mi ut dui vestibulum, non vehicula felis fringilla. Vestibulum eget massa blandit, viverra quam non, convallis libero. Morbi ut nunc ligula. Duis tristique purus augue, nec sodales sem scelerisque dignissim. Sed vel rutrum mi. Nunc accumsan magna quis tempus rhoncus. Duis volutpat nulla a aliquet feugiat. Vestibulum rhoncus mi diam, eu consectetur sapien eleifend in. Donec sed facilisis velit. Duis tempus finibus venenatis. Mauris neque nisl, pulvinar eu volutpat eu, laoreet in massa. Quisque vestibulum eros ac tortor facilisis vulputate. Sed iaculis purus non sem tempus mollis. Curabitur felis lectus, aliquam id nunc ut, congue accumsan tellus.',
    35,
    100.50,
    1.81,
    TRUE,
    '1984-08-27',
    '17:30:00',
    '2020-02-08 12:32:45'
);

SELECT * FROM aluno WHERE id = 1;

-- Updating and deleting data

UPDATE aluno 
    SET nome = 'Nico',
    cpf = '10987654321',
    observacao = 'Teste',
    idade = 38,
    dinheiro = 15.23,
    altura = 1.90,
    ativo = FALSE,
    data_nascimento = '1980-01-15',
    hora_aula = '13:00:00',
    matriculado_em = '2020-01-02 15:00:00'
WHERE id = 1;

DELETE 
    FROM aluno 
WHERE nome = 'Nico';

-- Inserting data agais and giving alias to columns

INSERT INTO aluno (nome) VALUES ('Vinícius Dias');
INSERT INTO aluno (nome) VALUES ('Nico Steppat');
INSERT INTO aluno (nome) VALUES ('João Roberto');
INSERT INTO aluno (nome) VALUES ('Diego');


SELECT nome AS "Nome do Aluno", 
       idade,
       matriculado_em AS quando_se_matriculou
    FROM aluno;

-- Using Filters

SELECT * 
    FROM aluno
WHERE nome = 'Diogo';

SELECT * 
    FROM aluno
WHERE nome LIKE 'Di_go';

SELECT * 
    FROM aluno
WHERE nome NOT LIKE 'Di_go';

SELECT * 
    FROM aluno
WHERE nome LIKE 'D%';

SELECT *
    FROM aluno
 WHERE cpf IS NULL;

SELECT *
    FROM aluno
WHERE idade <= 35;

SELECT *
    FROM aluno
WHERE idade BETWEEN 20 AND 35;

-- Using logical operators

SELECT *
    FROM aluno
WHERE nome LIKE 'D%' 
    AND idade > 30;

SELECT *
    FROM aluno
WHERE nome LIKE 'Diogo' 
  OR nome LIKE 'Nico Steppat';

SELECT *
    FROM aluno
WHERE nome LIKE 'D%'
    AND cpf IS NOT NULL;

-- Creating a new table with PRIMARY KEY

CREATE TABLE curso (
    id INTEGER PRIMARY KEY,
        nome VARCHAR(255) NOT NULL
);

SELECT * FROM curso;

-- Inserting data into the new table

INSERT INTO curso (id, nome) VALUES (1, 'HTML');
INSERT INTO curso (id, nome) VALUES (2, 'Javascript');


-- Creating a new table with a FOREIGN KEY

DROP TABLE aluno;

CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL
);

INSERT INTO aluno (nome) VALUES ('Diogo');
INSERT INTO aluno (nome) VALUES ('Vinícius');

SELECT * FROM aluno;

CREATE TABLE aluno_curso (
    aluno_id INTEGER,
        curso_id INTEGER,
        PRIMARY KEY (aluno_id, curso_id),

        FOREIGN KEY (aluno_id)
         REFERENCES aluno (id),

        FOREIGN KEY (curso_id)
         REFERENCES curso (id)

);

INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (1,1);
INSERT INTO aluno_curso (aluno_id, curso_id) VALUES (2,1);

-- Joining tables

SELECT *
    FROM aluno
JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
JOIN curso       ON curso.id             = aluno_curso.aluno_id;

INSERT INTO aluno_curso VALUES (2,2);

INSERT INTO aluno (nome) VALUES ('Nico');
INSERT INTO curso (id, nome) VALUES (3, 'CSS');

SELECT aluno.nome as "Nome do Aluno",
       curso.nome as "Nome do Curso"
    FROM aluno
LEFT JOIN aluno_curso ON aluno_curso.aluno_id = aluno.id
LEFT JOIN curso ON curso.id = aluno_curso.curso_id

