-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-06-2020 a las 02:31:52
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.3.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
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
-- Estructura de tabla para la tabla `grd_art3_villa_2020`
--

CREATE TABLE `grd_art3_villa_2020` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `id_table` tinyint(4) DEFAULT NULL,
  `num_photo` varchar(10) DEFAULT NULL,
  `_6x9` tinyint(4) DEFAULT NULL,
  `_8x12` tinyint(4) DEFAULT NULL,
  `cost` smallint(6) DEFAULT NULL,
  `payment` smallint(6) DEFAULT NULL,
  `seller` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `grd_art3_villa_2020`
--

INSERT INTO `grd_art3_villa_2020` (`id`, `name`, `id_table`, `num_photo`, `_6x9`, `_8x12`, `cost`, `payment`, `seller`) VALUES
(2, 'JAVIER ALEJANDRO BENITEZ FLORES', 15, '7261', 1, 0, 100, 100, 'JORGE GABRIEL'),
(3, 'IVANA HAMPSHIRE GARCIA', 78, '5946', 3, 1, 410, 410, 'JORGE GABRIEL'),
(6, 'PEDRITO SANCHEZ PEREZ', 48, '5961', 2, 2, 440, 440, 'JORGE GABRIEL'),
(7, 'ANDRES VARGAS CHACON', 12, '2345', 2, 2, 440, 440, 'JORGE GABRIEL'),
(8, 'ZARATE MOTA', 12, '2345', 2, 1, 340, 340, 'JORGE GABRIEL'),
(9, 'MARIANA HERRERA', 4, '4004', 2, 0, 200, 200, 'FERNANDA '),
(10, 'LUPITA GUERRERO ', 25, '1945', 1, 2, 370, 370, 'DANIEL'),
(11, 'ANDRES VC', 20, '2222', 3, 3, 660, 460, 'ANDRES '),
(12, 'FATIMA DIAZ', 6, '3003', 0, 2, 400, 400, 'FERNANDA '),
(13, 'NIKI VEN LAU', 7, '5', 3, 2, 510, 400, 'ALEJANDRA'),
(14, 'PABLO DIAZ ', 5, '4', 5, 2, 650, 520, 'ALEJANDRA'),
(22, 'FREDDY DIAMANTE ', 11, '2567', 2, 1, 340, 200, 'DANIEL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `idSeller` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `lastname` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hashpsw` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `permissions` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`idSeller`, `name`, `lastname`, `email`, `hashpsw`, `permissions`) VALUES
(1, 'JORGE GABRIEL', 'VELASCO PALE', 'paleta663@gmail.com', '$2b$12$OdaiThDI6DosJS5.4fn7fObw8hOVl6N.5tfPpUkU/rMFFPJFFEmTa', 'ADMIN'),
(10, 'ANDRES ', 'VARGAS CHACON', 'andres.varcha12@gmail.com', '$2b$12$w15COyqu1NfvatYmOBB2Cu9CLfkHdsLWt5qgzeg4wBqwz2qmsrRGq', 'ADMIN'),
(11, 'ALEJANDRA', 'VENEGAS', 'aleveneguis@gmail.com', '$2b$12$w15COyqu1NfvatYmOBB2CuGDft6GXIpw.F3pScJxxtGz.Xe3T/bwm', 'SELLER'),
(12, 'FERNANDA ', 'MALDONADO', 'fermrojas97@gmail.com', '$2b$12$w15COyqu1NfvatYmOBB2CuGDft6GXIpw.F3pScJxxtGz.Xe3T/bwm', 'SELLER'),
(14, 'ALFREDO', 'RAMIREZ VELAZQUEZ', 'panoramicashd@gmail.com', '$2b$12$w15COyqu1NfvatYmOBB2CuGDft6GXIpw.F3pScJxxtGz.Xe3T/bwm', 'ADMIN');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `grd_art3_villa_2020`
--
ALTER TABLE `grd_art3_villa_2020`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`idSeller`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `grd_art3_villa_2020`
--
ALTER TABLE `grd_art3_villa_2020`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
