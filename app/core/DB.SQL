CREATE DATABASE `api_dados` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
use `api_dados`;

-- api_dados.tipo_juego definition

CREATE TABLE `tipo_juego` (
  `id_tipo_juego` int(11) NOT NULL AUTO_INCREMENT,
  `clave` varchar(150) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `JSONCONFIG` text NOT NULL,
  `activo` int(1) NOT NULL DEFAULT 1,
  `create_at` datetime DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id_tipo_juego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- api_dados.usuario definition

CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(150) NOT NULL,
  `nombre` varchar(150) NOT NULL,
  `apellidos` varchar(150) NOT NULL,
  `correo` varchar(150) NOT NULL,
  `correo_alt` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `2FA` text NOT NULL,
  `frase_recuperacion` text NOT NULL,
  `sesion_activa` int(1) NOT NULL,
  `activo` int(1) NOT NULL,
  `ultima_actividad` datetime NOT NULL,
  `create_at` datetime NOT NULL DEFAULT current_timestamp(),
  `update_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `nombre_usuario` (`nombre_usuario`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `apellidos` (`apellidos`),
  UNIQUE KEY `correo` (`correo`),
  UNIQUE KEY `correo_alt` (`correo_alt`),
  UNIQUE KEY `password` (`password`),
  UNIQUE KEY `frase_recuperacion` (`frase_recuperacion`) USING HASH,
  UNIQUE KEY `usuario_un` (`2FA`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- api_dados.configsala definition

CREATE TABLE `configsala` (
  `id_config_sala` int(11) NOT NULL AUTO_INCREMENT,
  `clave` varchar(150) NOT NULL,
  `tipo_juego` int(11) DEFAULT NULL,
  `cantjugadores` int(11) DEFAULT NULL,
  `activo` int(1) NOT NULL DEFAULT 1,
  `create_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id_config_sala`),
  KEY `configsala_FK` (`tipo_juego`),
  CONSTRAINT `configsala_FK` FOREIGN KEY (`tipo_juego`) REFERENCES `tipo_juego` (`id_tipo_juego`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- api_dados.sala definition

CREATE TABLE `sala` (
  `id_sala` int(11) NOT NULL AUTO_INCREMENT,
  `clave` varchar(150) NOT NULL,
  `password` varchar(150) DEFAULT NULL,
  `configsala` int(11) DEFAULT NULL,
  `owner` int(11) DEFAULT NULL,
  `ganador` int(11) NOT NULL,
  `activo` int(1) NOT NULL DEFAULT 1,
  `create_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id_sala`),
  KEY `sala_FK` (`configsala`),
  KEY `sala_FK_1` (`owner`),
  KEY `sala_FK_2` (`ganador`),
  CONSTRAINT `sala_FK` FOREIGN KEY (`configsala`) REFERENCES `configsala` (`id_config_sala`) ON UPDATE CASCADE,
  CONSTRAINT `sala_FK_1` FOREIGN KEY (`owner`) REFERENCES `usuario` (`id_usuario`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `sala_FK_2` FOREIGN KEY (`ganador`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- api_dados.movimientos definition

CREATE TABLE `movimientos` (
  `id_movimiento` int(11) NOT NULL AUTO_INCREMENT,
  `clave` varchar(150) NOT NULL,
  `usuario` int(11) DEFAULT NULL,
  `registro` text NOT NULL,
  `sala` int(11) DEFAULT NULL,
  `activo` int(1) NOT NULL DEFAULT 1,
  `create_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id_movimiento`),
  KEY `movimientos_FK` (`sala`),
  KEY `movimientos_FK_1` (`usuario`),
  CONSTRAINT `movimientos_FK` FOREIGN KEY (`sala`) REFERENCES `sala` (`id_sala`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `movimientos_FK_1` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`id_usuario`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- api_dados.participantes definition

CREATE TABLE `participantes` (
  `id_participantes` int(11) NOT NULL AUTO_INCREMENT,
  `clave` varchar(150) NOT NULL,
  `sala` int(11) DEFAULT NULL,
  `usuario` int(11) DEFAULT NULL,
  `activo` int(1) NOT NULL DEFAULT 1,
  `create_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id_participantes`),
  UNIQUE KEY `participantes_un` (`clave`),
  KEY `participantes_FK` (`usuario`),
  KEY `participantes_FK_2` (`sala`),
  CONSTRAINT `participantes_FK` FOREIGN KEY (`usuario`) REFERENCES `usuario` (`id_usuario`) ON UPDATE CASCADE,
  CONSTRAINT `participantes_FK_2` FOREIGN KEY (`sala`) REFERENCES `sala` (`id_sala`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;