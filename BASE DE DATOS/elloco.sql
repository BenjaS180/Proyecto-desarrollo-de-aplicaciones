-- MariaDB dump 10.19  Distrib 10.4.27-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: elloco
-- ------------------------------------------------------
-- Server version	10.4.27-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `autor`
--

DROP TABLE IF EXISTS `autor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `autor` (
  `ID_autor` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(15) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `mail` varchar(20) NOT NULL,
  `ID_editorial` int(11) NOT NULL,
  `ID_producto` int(11) NOT NULL,
  PRIMARY KEY (`ID_autor`),
  UNIQUE KEY `ID_autor__UNIQUE` (`ID_autor`),
  KEY `fk_editoriales_autor` (`ID_editorial`),
  KEY `fk_productos_autor` (`ID_producto`),
  CONSTRAINT `fk_editoriales_autor` FOREIGN KEY (`ID_editorial`) REFERENCES `editoriales` (`ID_editorial`),
  CONSTRAINT `fk_productos_autor` FOREIGN KEY (`ID_producto`) REFERENCES `productos` (`ID_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autor`
--

LOCK TABLES `autor` WRITE;
/*!40000 ALTER TABLE `autor` DISABLE KEYS */;
/*!40000 ALTER TABLE `autor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bodega`
--

DROP TABLE IF EXISTS `bodega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bodega` (
  `ID_bodega` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(10) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `ID_colaborador` int(11) NOT NULL,
  `capacidad` int(11) DEFAULT NULL,
  `nivel_ocupacion` int(11) DEFAULT NULL,
  `correo_bodegas` varchar(30) DEFAULT NULL,
  `numero_fijo` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_bodega`),
  UNIQUE KEY `ID_bodega__UNIQUE` (`ID_bodega`),
  KEY `fk_colaborador_bodega` (`ID_colaborador`),
  CONSTRAINT `fk_colaborador_bodega` FOREIGN KEY (`ID_colaborador`) REFERENCES `colaborador` (`ID_colaborador`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bodega`
--

LOCK TABLES `bodega` WRITE;
/*!40000 ALTER TABLE `bodega` DISABLE KEYS */;
INSERT INTO `bodega` VALUES (1,'b02','prueba',1,100,50,'b02@bodega.cl',123213123),(2,'b02','prueba2',1,150,75,'b02@b02.cl',2147483647),(3,'b03','prueba3',3,200,125,'b03@bodega.cl',2323232);
/*!40000 ALTER TABLE `bodega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colaborador`
--

DROP TABLE IF EXISTS `colaborador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `colaborador` (
  `ID_colaborador` int(11) NOT NULL AUTO_INCREMENT,
  `cargo` varchar(20) NOT NULL,
  `ID_usuarios` int(11) NOT NULL,
  PRIMARY KEY (`ID_colaborador`),
  UNIQUE KEY `ID_colaborador__UNIQUE` (`ID_colaborador`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colaborador`
--

LOCK TABLES `colaborador` WRITE;
/*!40000 ALTER TABLE `colaborador` DISABLE KEYS */;
INSERT INTO `colaborador` VALUES (1,'jefebodega',1),(2,'bodeguero',2),(3,'admin',3),(4,'admin',1),(5,'bodeguero',2),(6,'prueba3',3);
/*!40000 ALTER TABLE `colaborador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colaborador_credenciales`
--

DROP TABLE IF EXISTS `colaborador_credenciales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `colaborador_credenciales` (
  `ID_credencial` int(11) NOT NULL AUTO_INCREMENT,
  `ID_colaborador` int(11) NOT NULL,
  `usuario` varchar(12) NOT NULL,
  `contrasena` int(11) NOT NULL,
  `accesos` int(11) NOT NULL,
  PRIMARY KEY (`ID_credencial`),
  UNIQUE KEY `ID_credencial__UNIQUE` (`ID_credencial`),
  KEY `fk_colaborador_col_cred` (`ID_colaborador`),
  CONSTRAINT `fk_colaborador_col_cred` FOREIGN KEY (`ID_colaborador`) REFERENCES `colaborador` (`ID_colaborador`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colaborador_credenciales`
--

LOCK TABLES `colaborador_credenciales` WRITE;
/*!40000 ALTER TABLE `colaborador_credenciales` DISABLE KEYS */;
INSERT INTO `colaborador_credenciales` VALUES (1,1,'jefebodega',12345,1),(2,2,'bodeguero',12345,2),(3,3,'admin',12345,3),(5,1,'benja1122',12345,3),(6,2,'prueba2',12345,3),(7,3,'prueba3',12345,1);
/*!40000 ALTER TABLE `colaborador_credenciales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `editoriales`
--

DROP TABLE IF EXISTS `editoriales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `editoriales` (
  `ID_editorial` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(15) NOT NULL,
  `cantidad_libros` int(11) NOT NULL,
  PRIMARY KEY (`ID_editorial`),
  UNIQUE KEY `ID_editorial__UNIQUE` (`ID_editorial`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `editoriales`
--

LOCK TABLES `editoriales` WRITE;
/*!40000 ALTER TABLE `editoriales` DISABLE KEYS */;
/*!40000 ALTER TABLE `editoriales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movimiento_bodega`
--

DROP TABLE IF EXISTS `movimiento_bodega`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movimiento_bodega` (
  `ID_movimiento` int(11) NOT NULL AUTO_INCREMENT,
  `fecha` date NOT NULL,
  `ID_bodega_origen` int(11) NOT NULL,
  `ID_bodega_destino` int(11) NOT NULL,
  `ID_colaborador` int(11) NOT NULL,
  `ID_bodega` int(11) NOT NULL,
  PRIMARY KEY (`ID_movimiento`),
  UNIQUE KEY `ID_movimiento__UNIQUE` (`ID_movimiento`),
  KEY `fk_colaborador_mov_bodega` (`ID_colaborador`),
  KEY `fk_bodega_mov_bodega` (`ID_bodega`),
  CONSTRAINT `fk_bodega_mov_bodega` FOREIGN KEY (`ID_bodega`) REFERENCES `bodega` (`ID_bodega`),
  CONSTRAINT `fk_colaborador_mov_bodega` FOREIGN KEY (`ID_colaborador`) REFERENCES `colaborador` (`ID_colaborador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimiento_bodega`
--

LOCK TABLES `movimiento_bodega` WRITE;
/*!40000 ALTER TABLE `movimiento_bodega` DISABLE KEYS */;
/*!40000 ALTER TABLE `movimiento_bodega` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prod_editorial`
--

DROP TABLE IF EXISTS `prod_editorial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `prod_editorial` (
  `ID_prod_edi` int(11) NOT NULL AUTO_INCREMENT,
  `ID_producto` int(11) NOT NULL,
  `ID_editorial` int(11) NOT NULL,
  PRIMARY KEY (`ID_prod_edi`),
  UNIQUE KEY `ID_prod_edi__UNIQUE` (`ID_prod_edi`),
  KEY `fk_editoriales_prod_edi` (`ID_editorial`),
  KEY `fk_productos_prod_edi` (`ID_producto`),
  CONSTRAINT `fk_editoriales_prod_edi` FOREIGN KEY (`ID_editorial`) REFERENCES `editoriales` (`ID_editorial`),
  CONSTRAINT `fk_productos_prod_edi` FOREIGN KEY (`ID_producto`) REFERENCES `productos` (`ID_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prod_editorial`
--

LOCK TABLES `prod_editorial` WRITE;
/*!40000 ALTER TABLE `prod_editorial` DISABLE KEYS */;
/*!40000 ALTER TABLE `prod_editorial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `productos` (
  `ID_producto` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_ing` varchar(20) NOT NULL,
  `cantidades` int(11) NOT NULL,
  `tipo_producto` varchar(20) NOT NULL,
  PRIMARY KEY (`ID_producto`),
  UNIQUE KEY `ID_producto__UNIQUE` (`ID_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'2023-07-01 13:48:45.',50,'revistas'),(2,'2023-07-01 13:51:07.',30,'libros');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `ID_usuarios` int(11) NOT NULL AUTO_INCREMENT,
  `rut` varchar(20) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `apellido_p` varchar(20) DEFAULT NULL,
  `apellido_m` varchar(20) DEFAULT NULL,
  `correo` varchar(20) DEFAULT NULL,
  `direccion` varchar(50) DEFAULT NULL,
  `numero_c` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID_usuarios`),
  UNIQUE KEY `ID_usuarios__UNIQUE` (`ID_usuarios`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'202425607','benja1','soto1','gonzalez1','benjamin@s.com','dsdas',22),(2,'202425608','benja2','soto2','gonzalez2','benjamin@s.com','asdas',2),(3,'202425609','benja3','soto3','gonzalez3','benjamin@s.com','asdas',222);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-01 18:33:33
