-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 12-05-2020 a las 23:11:43
-- Versión del servidor: 10.4.10-MariaDB
-- Versión de PHP: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `regis_clients_pano`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `grd_erh_texin_2020`
--

DROP TABLE IF EXISTS `grd_erh_texin_2020`;
CREATE TABLE IF NOT EXISTS `grd_erh_texin_2020` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_table` tinyint(4) DEFAULT NULL,
  `num_photo` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `6x9` tinyint(4) DEFAULT NULL,
  `8x12` tinyint(4) DEFAULT NULL,
  `cost` smallint(6) DEFAULT NULL,
  `payment` smallint(6) DEFAULT NULL,
  `seller` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `grd_erh_texin_2020`
--

INSERT INTO `grd_erh_texin_2020` (`id`, `name`, `id_table`, `num_photo`, `6x9`, `8x12`, `cost`, `payment`, `seller`) VALUES
(6, 'JUAN DOMINGUEZ PEREZ LAGUNES', 59, '8945', 2, 1, 340, 200, 'JORGE GABRIEL'),
(8, 'PEDRITO DOMINGUEZ GUZMAN', 12, '2345', 2, 2, 340, 340, 'JORGE GABRIEL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `lastnames` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `adress` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `pass` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `level` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `lastnames`, `adress`, `pass`, `level`) VALUES
(1, 'JORGE GABRIEL', 'VELASCO PALE', 'paleta663@gmail.com', '$2b$12$uAwDb.PyFpHo360Te97p2upL4grtpPVQYhRmRQ3K4Beq/zDU3dX0G', 'ADMIN'),
(6, 'ANDRES', 'VARGAS CHACON', 'andres@gmail.com', '$2b$12$K/xhUM9RnM55t3YRovPIJeD7nFLhmjp.iBy/eNxDdWwW47yY3OEL6', 'SELLER');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
regis_clients_pano