DROP DATABASE IF EXISTS techservice;

CREATE DATABASE techservice
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE techservice;

SET SESSION sql_mode = 'STRICT_TRANS_TABLES,NO_ZERO_DATE,NO_ZERO_IN_DATE,ERROR_FOR_DIVISION_BY_ZERO';

CREATE TABLE clientes (
    id_cliente      INT AUTO_INCREMENT,
    tipo_cliente    ENUM('FISICA', 'JURIDICA') NOT NULL DEFAULT 'FISICA',
    nome            VARCHAR(150)    NOT NULL,
    telefone        VARCHAR(20)     NOT NULL,
    email           VARCHAR(150)    NOT NULL,
    nif             VARCHAR(20)     NULL,
    morada          VARCHAR(200)    NULL,
    cidade          VARCHAR(100)    NULL,
    codigo_postal   VARCHAR(20)     NULL,
    observacoes     VARCHAR(255)    NULL,
    ativo           TINYINT(1)      NOT NULL DEFAULT 1,
    criado_em       DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em   DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP
                                     ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id_cliente),
    UNIQUE KEY uq_clientes_nif (nif),
    KEY idx_clientes_nome (nome)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;