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

CREATE TABLE equipamentos (
    id_equipamento  INT AUTO_INCREMENT,
    id_cliente      INT             NOT NULL,
    tipo            VARCHAR(50)     NOT NULL,
    marca           VARCHAR(50)     NOT NULL,
    modelo          VARCHAR(50)     NOT NULL,
    numero_serie    VARCHAR(100)    NOT NULL,
    data_compra     DATE            NULL,
    observacoes     VARCHAR(300)    NULL,
    ativo           TINYINT(1)      NOT NULL DEFAULT 1,
    criado_em       DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em   DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP
                                     ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id_equipamento)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE ordens_servico (
    id_ordem            INT AUTO_INCREMENT,
    id_equipamento      INT             NOT NULL,
    id_tecnico          INT             NULL,
    data_abertura        DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    data_conclusao       DATETIME        NULL,
    prazo_entrega        DATE            NULL,
    defeito_relatado     VARCHAR(500)    NOT NULL,
    diagnostico          VARCHAR(500)    NULL,
    solucao              VARCHAR(500)    NULL,
    status                ENUM('ABERTA', 'EM_ANDAMENTO', 'AGUARDANDO_PECAS',
                                'CONCLUIDA', 'CANCELADA')
                          NOT NULL DEFAULT 'ABERTA',
    prioridade            ENUM('BAIXA', 'MEDIA', 'ALTA', 'URGENTE')
                          NOT NULL DEFAULT 'MEDIA',
    valor_servico         DECIMAL(10,2)   NOT NULL DEFAULT 0.00,
    valor_pecas           DECIMAL(10,2)   NOT NULL DEFAULT 0.00,
    desconto              DECIMAL(10,2)   NOT NULL DEFAULT 0.00,
    valor_total           DECIMAL(10,2)
                          GENERATED ALWAYS AS
                          (valor_servico + valor_pecas - desconto) STORED,
    observacoes           VARCHAR(300)    NULL,
    criado_em             DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em         DATETIME        NOT NULL DEFAULT CURRENT_TIMESTAMP
                                          ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id_ordem),
    CONSTRAINT chk_os_valor_servico CHECK (valor_servico >= 0),
    CONSTRAINT chk_os_valor_pecas   CHECK (valor_pecas >= 0),
    CONSTRAINT chk_os_desconto      CHECK (desconto >= 0),
    CONSTRAINT chk_os_prazo         CHECK (prazo_entrega IS NULL
                                            OR prazo_entrega >= DATE(data_abertura))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;