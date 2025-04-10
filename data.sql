-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: trading
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `data`
--

DROP TABLE IF EXISTS `data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `data` (
  `day` int DEFAULT NULL,
  `amount` decimal(10,3) DEFAULT NULL,
  `pnl` decimal(10,3) DEFAULT NULL,
  `withdrawal` decimal(10,3) DEFAULT NULL,
  `remarks` varchar(100) DEFAULT NULL,
  `date_time` varchar(50) DEFAULT NULL,
  `user` varchar(20) DEFAULT NULL,
  KEY `user` (`user`),
  CONSTRAINT `data_ibfk_1` FOREIGN KEY (`user`) REFERENCES `user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `data`
--

LOCK TABLES `data` WRITE;
/*!40000 ALTER TABLE `data` DISABLE KEYS */;
INSERT INTO `data` VALUES (0,150.000,0.000,NULL,'Deposit 120$ + Bonus 25%','Not Specified','demo'),(1,168.800,18.800,NULL,NULL,'Not Specified','demo'),(2,187.620,18.820,NULL,NULL,'Not Specified','demo'),(3,193.540,5.920,NULL,NULL,'Not Specified','demo'),(4,216.500,19.190,NULL,NULL,'Not Specified','demo'),(5,237.370,20.870,NULL,NULL,'Not Specified','demo'),(6,279.590,42.220,NULL,NULL,'Not Specified','demo'),(7,308.900,29.310,NULL,NULL,'Not Specified','demo'),(8,338.100,29.200,NULL,NULL,'Not Specified','demo'),(9,367.300,29.200,NULL,NULL,'Not Specified','demo'),(10,356.400,-10.900,NULL,NULL,'Not Specified','demo'),(11,400.010,43.610,NULL,NULL,'Not Specified','demo'),(12,435.300,35.290,NULL,NULL,'Not Specified','demo'),(13,465.400,121.100,61.000,'Bonus Amount Deducted $30 + Withdrawal $61','Not Specified','demo'),(14,488.400,23.000,NULL,NULL,'Not Specified','demo'),(15,506.430,18.030,NULL,'Shekh Session','Not Specified','demo'),(16,432.430,-74.000,NULL,'Shekh Session in OTC','Not Specified','demo'),(17,508.430,76.000,NULL,'Magic V,SnR,Bullish Engulfing and Ascending Wedge','Not Specified','demo'),(18,562.430,54.000,NULL,'Supply Zone,Magic V and Trend Continuation','Not Specified','demo'),(19,613.430,51.000,NULL,'Resistance level,Trend Continuation and Sideways Market','Not Specified','demo'),(20,174.000,-439.430,NULL,'Shekh Zoom Live Session','Not Specified','demo'),(21,209.640,35.640,NULL,'self trading','Not Specified','demo'),(22,188.300,-21.340,0.000,'Self Trading','Not Specified','demo'),(23,237.130,48.830,NULL,'self trading','Not Specified','demo'),(24,290.000,52.870,NULL,'self trading','Not Specified','demo'),(25,299.210,9.210,NULL,'self trading','Not Specified','demo'),(26,325.350,26.140,NULL,'self trading','Not Specified','demo'),(27,353.840,28.490,NULL,'self trading','Not Specified','demo'),(28,381.610,27.770,NULL,'Self trading','Not Specified','demo'),(29,413.560,31.950,NULL,'self trading','Not Specified','demo'),(30,444.460,30.900,NULL,'self trading','Not Specified','demo'),(31,467.490,23.030,NULL,'self trading','Not Specified','demo'),(32,512.550,45.060,NULL,'self trading','Not Specified','demo'),(33,553.270,40.720,NULL,'self trading','Not Specified','demo'),(34,587.350,34.080,NULL,'night recovery(self trading)','Not Specified','demo'),(35,550.000,107.580,144.930,'NFP loss(Night Recovery) + Withdrawal $144.93','Not Specified','demo'),(0,25.000,0.000,NULL,NULL,'Not Specified','trade5'),(1,33.850,8.850,NULL,'54%','Not Specified','trade5'),(2,40.540,6.690,NULL,'67%','Not Specified','trade5'),(3,50.790,10.250,NULL,'75%','Not Specified','trade5'),(36,632.600,82.600,NULL,'self trading - Tuesday','Not Specified','demo'),(4,0.000,-50.790,NULL,'Worst OTC','Not Specified','trade5'),(37,688.100,55.500,NULL,'self trading - Wednesday','Not Specified','demo'),(38,731.950,43.850,NULL,'self trading - Thrusday','Not Specified','demo'),(39,707.590,-24.360,NULL,'self trading - Friday','Not Specified','demo'),(40,421.790,-285.800,NULL,'5 sec trades - Saturady (very bad OTC)','Not Specified','demo'),(41,467.100,45.310,NULL,'self trading - Monday','Not Specified','demo'),(42,517.720,50.620,NULL,'self trading - Tuesday','Not Specified','demo'),(43,514.200,-3.520,NULL,'self trading - Wednesday','Not Specified','demo'),(44,551.030,36.830,NULL,'self trading','Thu Jun 15 ','demo'),(45,592.160,41.130,NULL,'self trading','Fri Jun 16 ','demo'),(46,635.450,43.290,NULL,'Tough Day for profit (Shekh Signals(Sureshot Group)-70% + Self trading-30%)','Mon Jun 19 ','demo'),(47,687.300,51.850,NULL,'self trading - good market','Tue Jun 20 ','demo'),(48,743.420,56.120,NULL,'self trading - very good market (FFLC on fire)','Wed Jun 21 ','demo'),(49,795.290,51.870,NULL,'self trading (-414 to 50+) - heartattack day','Thu Jun 22 ','demo'),(50,853.980,58.690,NULL,'self trading - average market','Fri Jun 23 ','demo'),(51,187.430,-766.550,NULL,'self trading - starting loss - recovery trade loss(error) - very bad market + Deposit $100','Mon Jun 26 ','demo'),(52,203.420,15.990,NULL,'self trading - average market','Tue Jun 27 ','demo'),(53,240.400,36.980,NULL,'Self trading - average market','Wed Jun 28 ','demo'),(54,254.970,14.570,NULL,'self trading - high volatile market','Fri Jun 30 ','demo'),(55,247.530,-7.440,NULL,'Shekh sureshot loss','Sun Jul  2 ','demo'),(56,255.950,8.420,NULL,'self trading','Mon Jul  3','demo'),(57,241.000,-14.950,NULL,'self trading  - OTC market','Tue Jul  4','demo'),(58,271.000,30.000,NULL,'self trading - accuracy 100%','Wed Jul  5 ','demo'),(59,252.470,-18.530,NULL,'self trading','Thu Jul  6 ','demo'),(60,260.550,8.080,NULL,'self trading','Fri Jul  7','demo'),(61,239.460,-21.090,NULL,'self trading','Mon Jul  10','demo'),(62,264.740,25.280,NULL,'self trading','Tue Jul 11 ','demo'),(63,170.530,-94.210,NULL,'self trading','Wed Jul 12 ','demo'),(64,187.700,17.170,NULL,'self Trading + Shekh Session','Thu Jul 13 ','demo'),(65,200.400,12.700,NULL,'self trading + Shekh Session','Fri Jul 14 ','demo'),(66,220.880,20.480,NULL,'self trading','Mon Jul 17 ','demo'),(67,254.500,33.620,NULL,'self trading','Tue Jul 18 ','demo'),(68,265.700,11.200,NULL,'self trading','Wed Jul 19 ','demo'),(69,0.000,-265.700,NULL,'self trading','Thu Jul 20 ','demo'),(70,220.000,0.000,NULL,'New start - Deposit $100 + Bonus $80 + Prev Bal - $40','Sat Nov 18 ','demo'),(71,226.580,6.580,NULL,'self trading','Mon Nov 20','demo'),(72,239.310,12.730,NULL,'self trading','Tue Nov 21 ','demo'),(73,257.060,17.750,NULL,'self trading','Wed Nov 22 ','demo'),(74,276.880,19.820,NULL,'self trading','Fri Nov 24 ','demo'),(75,300.520,23.640,NULL,'self trading','Mon Nov 27 ','demo'),(76,325.590,25.070,NULL,'self trading','Tue Nov 28 ','demo'),(77,321.830,-3.760,NULL,'self trading - more fluctuations ','Wed Nov 29 ','demo'),(78,328.180,6.350,NULL,'self trading','Thu Nov 30 ','demo'),(79,351.030,22.850,NULL,'self trading','Fri Dec  1 ','demo'),(80,345.360,-5.670,NULL,'self trading','Mon Dec  4','demo'),(81,375.850,30.490,NULL,'self trading','Tue Dec  5 ','demo'),(0,1000.000,0.000,NULL,'futures trading start','Mon Dec 11','futures'),(82,392.070,16.220,NULL,'self trading','Tue Dec 12 ','demo'),(83,340.790,-51.280,NULL,'self trading','Wed Dec 13 ','demo'),(84,373.140,32.350,NULL,'self trading - breakout and retest trades','Thu Dec 14','demo');
/*!40000 ALTER TABLE `data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `pswd` varchar(20) DEFAULT NULL,
  `user` varchar(30) NOT NULL,
  PRIMARY KEY (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('#demo','demo'),('#futures','futures'),('#trade5','trade5');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-15 15:53:06
