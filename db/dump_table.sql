-- MySQL dump 10.13  Distrib 5.5.44, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: electrolab
-- ------------------------------------------------------
-- Server version	5.5.44-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add wp type',7,'add_wptype'),(20,'Can change wp type',7,'change_wptype'),(21,'Can delete wp type',7,'delete_wptype'),(22,'Can add workplace',8,'add_workplace'),(23,'Can change workplace',8,'change_workplace'),(24,'Can delete workplace',8,'delete_workplace'),(25,'Can add wp param type',9,'add_wpparamtype'),(26,'Can change wp param type',9,'change_wpparamtype'),(27,'Can delete wp param type',9,'delete_wpparamtype'),(28,'Can add wp param',10,'add_wpparam'),(29,'Can change wp param',10,'change_wpparam'),(30,'Can delete wp param',10,'delete_wpparam'),(40,'Can add course',14,'add_course'),(41,'Can change course',14,'change_course'),(42,'Can delete course',14,'delete_course'),(43,'Can add course state',15,'add_coursestate'),(44,'Can change course state',15,'change_coursestate'),(45,'Can delete course state',15,'delete_coursestate'),(46,'Can add user course state',16,'add_usercoursestate'),(47,'Can change user course state',16,'change_usercoursestate'),(48,'Can delete user course state',16,'delete_usercoursestate'),(49,'Can add question',17,'add_question'),(50,'Can change question',17,'change_question'),(51,'Can delete question',17,'delete_question'),(52,'Can add answer',18,'add_answer'),(53,'Can change answer',18,'change_answer'),(54,'Can delete answer',18,'delete_answer'),(55,'Can add user answer',19,'add_useranswer'),(56,'Can change user answer',19,'change_useranswer'),(57,'Can delete user answer',19,'delete_useranswer'),(61,'Can add field type',21,'add_fieldtype'),(62,'Can change field type',21,'change_fieldtype'),(63,'Can delete field type',21,'delete_fieldtype'),(64,'Can add course field',22,'add_coursefield'),(65,'Can change course field',22,'change_coursefield'),(66,'Can delete course field',22,'delete_coursefield'),(67,'Can add user field param',23,'add_userfieldparam'),(68,'Can change user field param',23,'change_userfieldparam'),(69,'Can delete user field param',23,'delete_userfieldparam'),(70,'Can add method',24,'add_method'),(71,'Can change method',24,'change_method'),(72,'Can delete method',24,'delete_method'),(73,'Can add user allowance',25,'add_userallowance'),(74,'Can change user allowance',25,'change_userallowance'),(75,'Can delete user allowance',25,'delete_userallowance');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$owTvMXveOLzJ$I/CG6XGZBNUsoKp9VgXd6bPjNirD6HMURz7267qdKz8=','2015-12-04 12:32:56',1,'admin','','','',1,1,'2015-08-20 13:01:19'),(2,'pbkdf2_sha256$20000$St9wKMrebnaO$mFLMWfmzBxy1lAdDXWql9n/37Jnaiyf4bTuOys9B6TQ=','2015-11-23 11:53:12',0,'1','','','',0,1,'2015-11-03 17:47:18'),(3,'pbkdf2_sha256$20000$I98qWKAN0mjf$D4Q3WjoVUhcCzFed41CJdGG6AvK/O6d5Z0G4NVLERh8=','2015-11-11 09:44:29',0,'KOS','Преподаватель','Преподавателевич','',1,1,'2015-11-03 18:51:06'),(4,'pbkdf2_sha256$20000$ZsLomRFSxY4X$wEQVVbPlcjRxqcf/ukFZLRz7qoD6eMrjMzrqRc5s2ks=','2015-11-10 16:12:25',0,'4keydach','Павел','Мерзляков','',0,1,'2015-11-09 17:22:44'),(5,'pbkdf2_sha256$20000$MToIrZxDOKPa$dkvp65GcNQxE/j5WAdTXAfP4M9LYKT1eiuit4W3U3wg=','2015-12-04 12:27:36',0,'test','Иван','Иванов','',0,1,'2015-11-10 16:22:11'),(6,'pbkdf2_sha256$20000$6YzW2WIPUGkx$vfG1ky8Q99XWbSXw87rt9wOSOgiEKrNaDd85Bnveo5w=',NULL,0,'test_prepod','Сидор','Сидоров','',1,1,'2015-11-10 16:24:26'),(7,'pbkdf2_sha256$20000$sXnknoeKr5RQ$uDF5OvDNEJFx0LZStGj4UhdZVxvLkOC3XA1Jr3WoIfA=','2015-12-02 11:42:33',0,'user1','Константин','Фёдоров','kaf_89@mail.ru',0,1,'2015-12-02 11:42:22');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-08-20 13:03:33','1','admin',2,'Changed username.',4,1),(2,'2015-12-03 10:20:36','6','test_prepod',2,'Изменен is_staff.',4,1),(3,'2015-12-03 17:38:26','1001','Лабораторная работа 310',1,'',14,1),(4,'2015-12-03 17:38:46','1001','Лабораторная работа 31',2,'Изменен name.',14,1),(5,'2015-12-03 17:39:03','1001','Лабораторная работа 31',2,'Ни одно поле не изменено.',14,1),(6,'2015-12-03 17:39:15','1001','Лабораторная работа 31',2,'Изменен duration.',14,1),(7,'2015-12-03 17:48:49','1001','Лабораторная работа 31',2,'Добавлен Поле лабораторной \"Схема 1 тип: Изображение сортировка: 1\".',14,1),(8,'2015-12-03 17:49:04','1001','Лабораторная работа 31',2,'Ни одно поле не изменено.',14,1),(9,'2015-12-03 17:50:52','1001','Лабораторная работа 31',2,'Изменены type для Поле лабораторной \"Схема 1 тип: Текст сортировка: 1\".',14,1),(10,'2015-12-03 19:39:38','1000','Лаботаторная работа 00',2,'Добавлен Поле лабораторной \"тест тип: Текст сортировка: 11\".',14,1),(11,'2015-12-03 19:46:23','1000','Лаботаторная работа 00',2,'Добавлен Поле лабораторной \"Тест2 тип: Текст сортировка: 12\".',14,1),(12,'2015-12-03 19:52:19','1001','Лабораторная работа 31',2,'Добавлен Поле лабораторной \"123 тип: Текст сортировка: 1\".',14,1),(13,'2015-12-03 19:53:15','1001','Лабораторная работа 31',2,'Ни одно поле не изменено.',14,1),(14,'2015-12-03 19:53:45','1001','Лабораторная работа 31',2,'Удален Поле лабораторной \"Схема 1 тип: Текст сортировка: 1\".',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(18,'main','answer'),(14,'main','course'),(22,'main','coursefield'),(15,'main','coursestate'),(21,'main','fieldtype'),(24,'main','method'),(17,'main','question'),(25,'main','userallowance'),(19,'main','useranswer'),(16,'main','usercoursestate'),(23,'main','userfieldparam'),(8,'main','workplace'),(10,'main','wpparam'),(9,'main','wpparamtype'),(7,'main','wptype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-08-20 13:00:40'),(2,'auth','0001_initial','2015-08-20 13:00:41'),(3,'admin','0001_initial','2015-08-20 13:00:41'),(4,'sessions','0001_initial','2015-08-20 13:00:42'),(5,'contenttypes','0002_remove_content_type_name','2015-11-03 17:47:01'),(6,'auth','0002_alter_permission_name_max_length','2015-11-03 17:47:01'),(7,'auth','0003_alter_user_email_max_length','2015-11-03 17:47:01'),(8,'auth','0004_alter_user_username_opts','2015-11-03 17:47:01'),(9,'auth','0005_alter_user_last_login_null','2015-11-03 17:47:01'),(10,'auth','0006_require_contenttypes_0002','2015-11-03 17:47:01'),(25,'main','0015_auto_20151203_1941','2015-12-03 19:42:21');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2eb1sfjdyv0hfuov4x83ctdblzeipe31','Njg2Mzc4MDY1NmIxZTEzZTZmZDYyYTE4ZTE4NGY0NTlkYTc3MTQ3NTp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzNDRiOGIyMDk5YjM1Mzg3Yjc4Mzc4MDZjYzRjYjQ3YWQ4MDE5OWQiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-12-18 12:32:56'),('5c7s9zegl4xmi1f0xl5pfu41i3zxk06k','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-12-06 15:11:48'),('6goyneb89v2bkmldkispriv0871p3cow','NzRhNTA5ZjI0ZmExMzNiNTc0MmE1YzQ2MTk3MTAzYmVhNDEyNDY1ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImEwYTQxNDFhYzI2YTRjZTk0ZGEzYWZjZTVkOTg1N2YyZTgxZGNhOTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-09-03 13:02:47'),('8rq78punyuetwervynzuvpabs3w6jgsv','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-12-06 12:10:56'),('96dw1iuw1q2m3wl1ggroqeo73qqswsk0','NzRhNTA5ZjI0ZmExMzNiNTc0MmE1YzQ2MTk3MTAzYmVhNDEyNDY1ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImEwYTQxNDFhYzI2YTRjZTk0ZGEzYWZjZTVkOTg1N2YyZTgxZGNhOTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-09-03 18:44:16'),('grw4z46m2qspz58ntkt2su8vvjpkr4rh','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-12-14 16:38:20'),('gzyefqh27zwckn9n5hze6vswxcv1a8sx','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-11-30 11:16:12'),('hezlii39t28ih63rr6nmnvx0ta7d1xhc','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-12-14 18:41:02'),('kz5cjhhv3yhta72fxmhj7xe0acoxh9t6','NzRhNTA5ZjI0ZmExMzNiNTc0MmE1YzQ2MTk3MTAzYmVhNDEyNDY1ODp7Il9hdXRoX3VzZXJfaGFzaCI6ImEwYTQxNDFhYzI2YTRjZTk0ZGEzYWZjZTVkOTg1N2YyZTgxZGNhOTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-09-23 14:48:40'),('lkqm8uzh6fednek0391x9gnv0xj92jw9','YWQ4MTA3MDg0MWNmZjFlMmY0Njk5YjVhMjViNGUwMThkNDEzOWQwMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzNDRiOGIyMDk5YjM1Mzg3Yjc4Mzc4MDZjYzRjYjQ3YWQ4MDE5OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-12-17 19:51:43'),('mhgxn7uqgw5yq9egi87rjm5yhbxnbx7h','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-11-29 14:42:40'),('n1nvx63exrln2go9jv9e7kysm31idk2n','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-12-18 08:14:46'),('n9y7rgwtbw10x96g6z2j9lmrfv6g6zyf','YWQ4MTA3MDg0MWNmZjFlMmY0Njk5YjVhMjViNGUwMThkNDEzOWQwMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzNDRiOGIyMDk5YjM1Mzg3Yjc4Mzc4MDZjYzRjYjQ3YWQ4MDE5OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-12-17 14:52:12'),('npiktke8wuqdzv1ox5olhq24iahchecf','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-12-13 09:43:12'),('ol6rskcaet1a7g2ykdd73xkmtdkd5j9m','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-12-12 07:15:27'),('qbqpr5as8u7z3ecnyk5bl81ti9tonhpo','YWQ4MTA3MDg0MWNmZjFlMmY0Njk5YjVhMjViNGUwMThkNDEzOWQwMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzNDRiOGIyMDk5YjM1Mzg3Yjc4Mzc4MDZjYzRjYjQ3YWQ4MDE5OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-12-17 14:55:10'),('w3u24hjrn2s967nrda2osug9aeapyr13','YWQ4MTA3MDg0MWNmZjFlMmY0Njk5YjVhMjViNGUwMThkNDEzOWQwMzp7Il9hdXRoX3VzZXJfaGFzaCI6IjEzNDRiOGIyMDk5YjM1Mzg3Yjc4Mzc4MDZjYzRjYjQ3YWQ4MDE5OWQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2015-12-17 16:36:55'),('yqblcfuktklagh3kvfklyh7ypqhzq5oy','NzY1NWNkYTIzODNiYzEyZDY4MTRkMzA5OTc4MGFiOWM1NDRhNTM2Mzp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2lkIjoiNSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2015-11-29 16:31:46'),('zaokpdkmeukq035il2tflrqwazfo1ymt','ODhjMjg4YmM0MjI3ZDdlMzRmMDM3MzllMjA0ZjhhMDEyYWEyOGNiODp7Il9hdXRoX3VzZXJfaGFzaCI6IjNjMjI5NTUyZmRjMjg4ZWEzNzc0YTk0Y2RiZDE3MDU3NGI0YjVjZmUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI1In0=','2015-11-24 18:44:26');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_answer`
--

DROP TABLE IF EXISTS `main_answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_answer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text_answer` longtext NOT NULL,
  `right` tinyint(1) NOT NULL,
  `question_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_answer_7aa0f6ee` (`question_id`),
  CONSTRAINT `main_answer_question_id_23e8620c3593ce07_fk_main_question_id` FOREIGN KEY (`question_id`) REFERENCES `main_question` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_answer`
--

LOCK TABLES `main_answer` WRITE;
/*!40000 ALTER TABLE `main_answer` DISABLE KEYS */;
INSERT INTO `main_answer` VALUES (1,'использовать схему соединения обмоток выпрямительного трансформатора Y/ Y0/0 и два лучевыми выпрямителями',1,1),(2,'использовать схему соединения обмоток выпрямительного трансформатора Y/0/ Y0  и два лучевыми выпрямителями ',0,1),(3,'использовать два трансформатора со схемой Y/ Y0 и два лучевых выпрямителя',0,1),(4,'включить один лучевой выпрямитель в первичную обмотку, а второй – во вторичную',0,1),(5,'г',1,2),(6,'а',0,2),(7,'б',0,2),(8,'в',0,2),(9,'<img src=\"/static/img/q3.1.jpg\" alt=\"q3.1.jpg\"/>',1,3),(10,'<img src=\"/static/img/q3.2.jpg\" alt=\"q3.2.jpg\"/>',0,3),(11,'<img src=\"/static/img/q3.3.jpg\" alt=\"q3.3.jpg\"/>',0,3),(12,'<img src=\"/static/img/q3.4.jpg\" alt=\"q3.4.jpg\"/>',0,3),(13,'0,25',1,4),(14,'1,57 ',0,4),(15,'0,667',0,4),(16,'0,05',0,4),(17,'использовать схему соединения обмоток выпрямительного трансформатора Y/ Y0/0 и два лучевыми выпрямителями',1,5),(18,'использовать схему соединения обмоток выпрямительного трансформатора Y/0/ Y0  и два лучевыми выпрямителями ',0,5),(19,'использовать два трансформатора со схемой Y/ Y0 и два лучевых выпрямителя',0,5),(20,'включить один лучевой выпрямитель в первичную обмотку, а второй – во вторичную',0,5),(21,'г',1,6),(22,'а',0,6),(23,'б',0,6),(24,'в',0,6),(25,'<img src=\"/static/img/q3.1.jpg\" alt=\"q3.1.jpg\"/>',1,7),(26,'<img src=\"/static/img/q3.2.jpg\" alt=\"q3.2.jpg\"/>',0,7),(27,'<img src=\"/static/img/q3.3.jpg\" alt=\"q3.3.jpg\"/>',0,7),(28,'<img src=\"/static/img/q3.4.jpg\" alt=\"q3.4.jpg\"/>',0,7),(29,'0,25',1,8),(30,'1,57 ',0,8),(31,'0,667',0,8),(32,'0,05',0,8),(33,'ответ 1',1,9),(34,'ответ 2',0,9),(35,'ответ 3',0,9),(36,'ответ 4',0,9),(37,'ответ 1',1,10),(38,'ответ 2',0,10),(39,'ответ 3',0,10),(40,'ответ 4',0,10);
/*!40000 ALTER TABLE `main_answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_course`
--

DROP TABLE IF EXISTS `main_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `duration` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `last_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_course_user_id_253fc4aadbcb4a2d_fk_auth_user_id` (`user_id`),
  CONSTRAINT `main_course_user_id_253fc4aadbcb4a2d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1002 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_course`
--

LOCK TABLES `main_course` WRITE;
/*!40000 ALTER TABLE `main_course` DISABLE KEYS */;
INSERT INTO `main_course` VALUES (1,'Лабораторная работа 1',12000000000,6,NULL),(4,'Лабораторная работа 4-b',1200000000,6,NULL),(8,'Лабораторная работа 8',10000000000,6,NULL),(1000,'Лаботаторная работа 00',10000000000,6,NULL),(1001,'Лабораторная работа 31',3600000000,6,NULL);
/*!40000 ALTER TABLE `main_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_coursefield`
--

DROP TABLE IF EXISTS `main_coursefield`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_coursefield` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `type_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `wp_param_id` int(11) DEFAULT NULL,
  `param1` longtext,
  `param2` longtext,
  `param3` longtext,
  PRIMARY KEY (`id`),
  KEY `main_coursefield_94757cae` (`type_id`),
  KEY `main_coursefield_ea134da7` (`course_id`),
  KEY `main_coursefield_e066dd38` (`wp_param_id`),
  CONSTRAINT `main_coursefield_course_id_25634fb33c9d9224_fk_main_course_id` FOREIGN KEY (`course_id`) REFERENCES `main_course` (`id`),
  CONSTRAINT `main_coursefield_type_id_69c436520fe12be3_fk_main_fieldtype_id` FOREIGN KEY (`type_id`) REFERENCES `main_fieldtype` (`id`),
  CONSTRAINT `main_coursefield_wp_param_id_2a0fd1701b523db6_fk_main_wpparam_id` FOREIGN KEY (`wp_param_id`) REFERENCES `main_wpparam` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_coursefield`
--
use electrolab;
LOCK TABLES `main_coursefield` WRITE;
/*!40000 ALTER TABLE `main_coursefield` DISABLE KEYS */;
INSERT INTO `main_coursefield` (
`id`,`name`,`type_id`,`course_id`,`wp_param_id`,`param1`,`param2`,`param3`)
VALUES (1,'Текстовое поле',7,1000,NULL,'Действенным способом подавления высших гармоник в электрических сетях является применение силовых резонансных фильтров. Однако, при значительных мощностях выпрямительных агрегатов такой путь крайне затратен. Иное, более практичное решение состоит в таком построении вентильного трансформатора, при котором, значительная несинусоидальность вторичных токов, не будет приводить к несинусоидальности – первичных. Возможность такого пути заложена в уравнении МДС трансформатора (8.1). Так, для трехобмоточного трансформатора',NULL,NULL),(2,'Картинка',8,1000,NULL,'<img src=\"/static/img/8.1.bmp\" alt=\"8.1.bmp\">',NULL,NULL),(3,'Таблица считываемых параметров',3,1000,5,'Заголовок1,Заголовок2,Заголовок3;ПодписьСлева1,ПодписьСлева2,ПодписьСлева3,ПодписьСлева4,ПодписьСлева5,ПодписьСлева6,ПодписьСлева7,ПодписьСлева8,ПодписьСлева9,ПодписьСлева10,','10;3','Считать значения'),(4,'Одиночный параметр',4,1000,1,NULL,NULL,NULL),(5,'Логический управляющий/считываемый параметр',2,1000,7,NULL,NULL,NULL),(6,'График',6,1000,1,'50',NULL,NULL),(7,'Многопозиционный дискретный параметр',5,1000,17,'16',NULL,NULL),(8,' ',7,8,NULL,'1. Экспериментальное определение гармонического состава первичного тока силового трансформатора, работающего на линейную нагрузку. Данный опыт проводится для сопоставления степени влияния на сеть силовых трансформаторов с линейной нагрузкой и выпрямительных. \nПодготовка экспериментальной установки.  Собрать  схему  по рис. 8.11 и установить аппараты управления стенда в исходные положения.',NULL,NULL),(9,' ',8,8,NULL,'<img src=\"/static/img/8.11.jpg\" alt=\"8.11.jpg\"> Рис. 8.11',NULL,NULL),(10,' ',7,8,NULL,'<ul>\n<li>Установить номинальное напряжение трансформатора, переключением SA2 в положение 3, SA4 - 1 . </li>\n<li>С помощью выключателей SA1 и SA3  установить схему соединений об-моток трансформатора Y/Y0 . </li>\n<li>С помощью ступенчато поворотной рукоятки R включить максимальную симметричную нагрузку трансформатора.</li>\n</ul>',NULL,NULL),(11,' ',5,8,10804,'16',NULL,NULL),(12,'Подключить регистрирующий амперметр к гнезду',7,8,NULL,'Последовательность проведения эксперимента:\n<ul>\n<li>Подать напряжение на стенд.</li> \n<li>Включить регистрирующий амперметр.</li>\n<li>Включить трансформатор ТС1. </li>\n<li>Записать кривую первичного тока трансформатора ТС1.</li> \n</ul>',NULL,NULL),(13,' ',6,8,10801,'400',NULL,NULL),(14,' ',3,8,10802,'40',NULL,'Считать амплитудные значения гармоник 0-40'),(15,' ',3,8,10803,'40',NULL,'Считать углы сдвига гармоник 0-40'),(16,' ',7,8,NULL,'2. Экспериментальное определение гармонического состава первич-ного тока выпрямительного трансформатора со схемой соединения об-моток Y/Y0 и трехфазной лучевой схемой выпрямления (3-пульсной). \nПодготовка экспериментальной установки.  Собрать  схему  по рис. 8.12. \n',NULL,NULL),(17,' ',8,8,NULL,'<img src=\"/static/img/8.12.jpg\" alt=\"8.12.jpg\"> Рис. 8.12',NULL,NULL),(18,' ',7,8,NULL,'Последовательность проведения эксперимента. Провести измерения, подобно предыдущим опытам. ',NULL,NULL),(19,' ',6,8,10801,'400',NULL,NULL),(20,' ',3,8,10802,'40',NULL,'читать амплитудные значения гармоник 0-40'),(21,' ',3,8,10803,'40',NULL,'Считать углы сдвига гармоник 0-40'),(22,' ',7,8,NULL,'3. Экспериментальное определение гармонического состава первич-ного тока выпрямительного трансформатора со схемой соединения об-моток Δ /Y0 и трехфазной лучевой  схемой выпрямления (3-пульсной). \nПодготовка экспериментальной установки.  Собрать  схему  по рис. 8.13. \n',NULL,NULL),(23,' ',8,8,NULL,'<img src=\"/static/img/8.13.jpg\" alt=\"8.13.jpg\"> Рис. 8.13',NULL,NULL),(24,' ',7,8,NULL,'Последовательность проведения эксперимента. Провести измерения, подобно предыдущим опытам. ',NULL,NULL),(25,'',6,8,10801,'400',NULL,NULL),(26,'',3,8,10802,'40','','читать амплитудные значения гармоник 0-40'),(27,'',3,8,10803,'40',NULL,'Считать углы сдвига гармоник 0-40'),(28,'',7,8,NULL,'4. Экспериментальное определение гармонического состава первич-ного тока выпрямительного трансформатора со схемой соединения об-моток Y/Z0 и трехфазной лучевой схемой выпрямления (3-пульсной). Подготовка экспериментальной установки.  Собрать  схему  по рис. 8.14.',NULL,NULL),(29,'',8,8,NULL,'<img src=\"/static/img/8.14.jpg\" alt=\"8.14.jpg\"> Рис. 8.14',NULL,NULL),(30,'',7,8,NULL,'Последовательность проведения эксперимента. Провести измерения, подобно предыдущим опытам.',NULL,NULL),(31,'',7,8,NULL,'5. Экспериментальное определение гармонического состава первич-ного тока выпрямительного трансформатора со схемой соединения об-моток Δ/Z0 и трехфазной лучевой схемой выпрямления (3-пульсной). Подготовка экспериментальной установки.  Собрать  схему  по рис. 8.15. ',NULL,NULL),(32,'',8,8,NULL,'<img src=\"/static/img/8.15.jpg\" alt=\"8.15.jpg\"> Рис. 8.15',NULL,NULL),(33,'',7,8,NULL,'Последовательность проведения эксперимента. Провести измерения, подобно предыдущим опытам.',NULL,NULL),(34,'',6,8,10801,'400',NULL,NULL),(35,'',3,8,10802,'40',NULL,'читать амплитудные значения гармоник 0-40'),(36,'',3,8,10803,'40',NULL,'Считать углы сдвига гармоник 0-40'),(37,'',7,8,NULL,'Экспериментальное определение гармонического состава первичного то-ка выпрямительного трансформатора со схемой соединения обмоток Y/Y0/     0    и трехфазной лучевой схемой выпрямления (6-пульсной). Подготовка экспериментальной установки.  Собрать  схему  по рис. 8.16. ',NULL,NULL),(38,'',8,8,NULL,'<img src=\"/static/img/8.16.jpg\" alt=\"8.16.jpg\"> Рис. 8.16',NULL,NULL),(39,'',7,8,NULL,'Последовательность проведения эксперимента. Провести измерения, подобно предыдущим опытам.',NULL,NULL),(40,'',6,8,10801,'400',NULL,NULL),(41,'',3,8,10802,'40','','читать амплитудные значения гармоник 0-40'),(42,'',3,8,10803,'40','','Считать углы сдвига гармоник 0-40'),(43,'',7,4,NULL,'1. Экспериментальное определение напряжения опрокидывания асинхронного двигателя.<br>\n<b>Подготовка экспериментальной установки.  Собрать  схему  по рис. 10.8 и установить аппараты управления стенда в исходные положения.</b><br>\nНа блоке силового трансформатора ТС1:.\nУстановить переключателем SA1 схему соединения первичной обмотки Y.\nУстановить переключателем SA3 схему соединения вторичной  обмот-ки Y0.\nУстановить номинальную величину напряжения трансформатора SA3 -3, SA4 -1.\n\nОпыт №1. Работа АД при номинальном напряжении.<br>\n<b>Последовательность проведения эксперимента.</b><br>\n<ul>\n<li>Подать напряжение на стенд, нажатием кнопки SB1 «ПУСК».</li>\n<li>Подать напряжение на трансформатор ТС1 .</li>\n<li>Запустить асинхронный двигатель (M1)  нажатием кнопки SB1 «ПУСК».</li>\n<li>Подать напряжение возбуждения на генератор постоянного тока (G2), включением SB3. </li>\n<li>Изменяя сопротивление нагрузочного реостата генератора постоянного тока (изменением положения R), установить номинальное значение тока АД.</li>\n</ul> ',NULL,NULL),(44,'',7,4,NULL,'Измереения: Положение SA2 - 3, положение SA4 - 1',NULL,NULL),(45,'Фазный ток АД',4,4,10001,NULL,NULL,NULL),(46,'Линейное напрядение АД',4,4,10002,NULL,NULL,NULL),(47,'Частота вращения АД',4,4,10001,NULL,NULL,NULL),(48,'',7,4,NULL,'Опыт №2. Работа АД при понижении напряжения на 20%.<br>\n<b>Последовательность проведения эксперимента.</b><br>\n<ul>\n<li>Подать напряжение на стенд, нажатием кнопки SB1 «ПУСК».</li>\n<li>Подать напряжение на трансформатор ТС1 .</li>\n<li>Запустить асинхронный двигатель (M1)  нажатием кнопки SB1 «ПУСК».</li>\n<li>Подать напряжение возбуждения на генератор постоянного тока (G2), включением SB3. </li>\n<li>Изменяя сопротивление нагрузочного реостата генератора постоянного тока (изменением положения R), установить номинальное значение тока АД. </li>\n<li>Переводя переключатель  SA4 из положения 1 в 2 понизить напряжение на АД до 0.8 UНОМ.</li>\n</ul>',NULL,NULL),(49,'',7,4,NULL,'Измереения: Положение SA2 - 3, положение SA4 - 2',NULL,NULL),(50,'Фазный ток АД',4,4,10001,NULL,NULL,NULL),(51,'Линейное напрядение АД',4,4,10002,NULL,NULL,NULL),(52,'Частота вращения АД',4,4,10001,NULL,NULL,NULL),(53,'',7,4,NULL,'Опыт №3. Работа АД при понижении напряжения на 40%.<br>\n<b>Последовательность проведения эксперимента.</b><br>\n<ul>\n<li>Подать напряжение на стенд, нажатием кнопки SB1 «ПУСК».</li>\n<li>Подать напряжение на трансформатор ТС1 .</li>\n<li>Запустить асинхронный двигатель (M1)  нажатием кнопки SB1 «ПУСК».</li>\n<li>Подать напряжение возбуждения на генератор постоянного тока (G2), включением SB3.</li>\n<li>Изменяя сопротивление нагрузочного реостата генератора постоянного тока (изменением положения R), установить номинальное значение тока АД. </li>\n<li>Переводя переключатель  SA4 из положения 1 в 3 понизить напряжение на АД до 0.6 UНОМ.</li>\n</ul>',NULL,NULL),(54,'',7,4,NULL,'Измереения: Положение SA2 - 3, положение SA4 - 3',NULL,NULL),(55,'Фазный ток АД',4,4,10001,NULL,NULL,NULL),(56,'Линейное напрядение АД',4,4,10002,NULL,NULL,NULL),(57,'Частота вращения АД',4,4,10001,NULL,NULL,NULL),(58,'',7,4,NULL,'Опыт №4. Экспериментальное определение энергетических харак-теристик асинхронного двигателя при симметрии напряжений пита-ющей сети.<br>\n<b>Подготовка экспериментальной установки.</b><br> Собрать  схему  по рис. 10.8 и установить аппараты управления стенда в исходные положения.<br>\nНа блоке силового трансформатора ТС1:.<br>\n<ul>\n<li>Установить переключателем SA1 схему соединения первичной обмотки Y.</li> \n<li>Установить переключателем SA3 схему соединения вторичной  обмот-ки Y0.</li> \n<li>Установить номинальную величину напряжения трансформатора SA3 -3, SA4 -1.</li> \n</ul>\n<b>Последовательность проведения эксперимента.</b><br>\n<ul>\n<li>Подать напряжение на стенд, нажатием кнопки SB1 «ПУСК». </li> \n<li>Подать напряжение на трансформатор ТС1 .</li> \n<li>Запустить асинхронный двигатель (M1)  нажатием кнопки SB1 «ПУСК».</li> \n<li>Подать напряжение возбуждения на генератор постоянного тока (G2), включением SB3. </li> \n<li>Изменяя сопротивление нагрузочного реостата генератора постоянного тока (изменением положения R, изменять нагрузку асинхронного двигателя. В этом опыте необходимо получить 8 - 9 точек, при значениях  тока асин-хронного двигателя от величины тока 1.2 - 1.3IНОМ  до тока холостого хода (реального) IО.</li>  \n</ul>',NULL,NULL),(59,'Ручной ввод таблицы с Листа \"Таблица1\"',9,4,NULL,'10',NULL,NULL),(60,'',7,4,NULL,'Опыт №5. Экспериментальное определение энергетических харак-теристик асинхронного двигателя при несимметрии напряжений пи-тающей сети.\n<b>Подготовка экспериментальной установки.</b><br> Для искусственного со-здания несимметрии трехфазной системы напряжений сети используется трансформаторный агрегат, состоящий из трехфазного силового ТС1  и вольтодобавочного  ТВ  трансформаторов. Собрать  схему  по рис. 10.8 и установить аппараты управления стенда в исходные положения.\nНа блоке силового трансформатора ТС1:.<br>\n<ul>\n<li>Установить переключателем SA1 схему соединения первичной обмотки Y.</li>\n<li>Установить переключателем SA3 схему соединения вторичной  обмот-ки Y0.</li>\n<li>Установить номинальную величину напряжения трансформатора SA3 -3, SA4 -1. </li>\n</ul>\n<b>Последовательность проведения эксперимента.</b><br>\n<ul>\n<li>Подать напряжение на стенд, нажатием кнопки SB1 «ПУСК».</li>\n<li>Подать напряжение на трансформатор ТС1 .</li>\n<li>Запустить асинхронный двигатель (M1)  нажатием кнопки SB1 «ПУСК».</li>\n<li>Подать напряжение возбуждения на генератор постоянного тока (G2), включением SB3. </li>\n<li>Изменяя сопротивление нагрузочного реостата генератора постоянного тока (изменением положения R, изменять нагрузку асинхронного двигателя. В этом опыте необходимо получить 8 - 9 точек, при значениях  тока асин-хронного двигателя от величины тока 1.2 - 1.3IНОМ  до тока холостого хода (реального) IО. </li>\n</ul>',NULL,NULL),(61,'Ручной ввод таблицы с Листа \"Таблица1\"',9,4,NULL,'10',NULL,NULL),(62,'5. Обработка результатов лабораторной работы',7,4,NULL,'5.1. Расчет   рабочих характеристик асинхронного двигателя.\nПо данным табл.\n- заполнить табл. для всех точек, полученных экспериментально.',NULL,NULL),(63,'Ручной ввод таблицы с Листа \"Таблица2\"',9,4,NULL,'10',NULL,NULL),(64,'Итоги лабораторной работы',10,8,NULL,NULL,NULL,NULL),(65,'Таблица вводимых параметров',11,1000,NULL,'Заголовок1,Заголовок2,Заголовок3;ПодписьСлева1,ПодписьСлева2,ПодписьСлева3,ПодписьСлева4,ПодписьСлева5,ПодписьСлева6,ПодписьСлева7,ПодписьСлева8,ПодписьСлева9,ПодписьСлева10,','10;3','Записать значения'),(66,'Таблица мульти-параметров',12,1000,NULL,'Заголовок1,Заголовок2,Заголовок3,заголовок4,Заголовок5,Заголовок6;ПодписьСлева1,ПодписьСлева2,ПодписьСлева3,ПодписьСлева4,ПодписьСлева5,ПодписьСлева6,ПодписьСлева7,ПодписьСлева8,ПодписьСлева9,ПодписьСлева10,','10;3;3','Считать занчения;Записать значения '),(67,'АВР',13,1000,NULL,NULL,NULL,NULL),(69,'тест',7,1000,NULL,'текст текст текст','',''),(70,'Тест2',7,1000,NULL,'Текст','',''),(71,'123',7,1001,NULL,'123','','');
/*!40000 ALTER TABLE `main_coursefield` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_coursestate`
--

DROP TABLE IF EXISTS `main_coursestate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_coursestate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_coursestate`
--

LOCK TABLES `main_coursestate` WRITE;
/*!40000 ALTER TABLE `main_coursestate` DISABLE KEYS */;
INSERT INTO `main_coursestate` VALUES (1,'Недоступно'),(2,'Активировано'),(3,'Выполнено');
/*!40000 ALTER TABLE `main_coursestate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_fieldtype`
--

DROP TABLE IF EXISTS `main_fieldtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_fieldtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `code` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_fieldtype`
--

LOCK TABLES `main_fieldtype` WRITE;
/*!40000 ALTER TABLE `main_fieldtype` DISABLE KEYS */;
INSERT INTO `main_fieldtype` VALUES (1,'Числовой управляющий/считываемый параметр','input_param'),(2,'Логический управляющий/считываемый параметр','bool'),(3,'Считываемая таблица значений','input_table'),(4,'Одиночный многократно считываемый параметр','onlineparam'),(5,'Многопозиционный дискретный параметр','select'),(6,'График','diagram'),(7,'Текст','text'),(8,'Изображение','img'),(9,'Ручная таблица значений','table'),(10,'Текстовое поле ввода','text_field'),(11,'Вводимая таблица значений','output_table'),(12,'Комплексная таблица значений\n','multi_table'),(13,'АВР','avr');
/*!40000 ALTER TABLE `main_fieldtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_method`
--

DROP TABLE IF EXISTS `main_method`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_method` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text_question` longtext NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_method_course_id_421433f3b71ff039_fk_main_course_id` (`course_id`),
  CONSTRAINT `main_method_course_id_421433f3b71ff039_fk_main_course_id` FOREIGN KEY (`course_id`) REFERENCES `main_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_method`
--

LOCK TABLES `main_method` WRITE;
/*!40000 ALTER TABLE `main_method` DISABLE KEYS */;
INSERT INTO `main_method` VALUES (1,'<h3>Лабораторная работа 8. ИССЛЕДОВАНИЕ ВЛИЯНИЯ ЧИСЛА ПУЛЬСНОСТИ (3 - 6) ВЕНТИЛЬНОГО ТРАНСФОРМАТОРА (Y/Y0, Δ/Y0, Y/Z0 , Δ/Z0, Y/Y0,Y0) НА ГАРМОНИЧЕСКИЙ СОСТАВ ПЕРВИЧНОГО ТОКА ПРИ ЛУЧЕВЫХ СХЕМАХ ВЫПРЯМИТЕЛЯ </h3><p>Цель работы Экспериментальное исследование влияния схем соединения обмоток, числа фаз выпрямительных трансформаторов с лучевыми выпрямителями на гармонический состав первичного тока.</p> <p>Программа работы 1. Экспериментальное определение гармонического состава первичного тока силового трансформатора, работающего на линейную нагрузку (тестовая задача). 2. Экспериментальное определение гармонического состава первичного тока выпрямительного трансформатора со схемами соединения обмоток Y/Y, Δ/Y, Y/Δ/Y и трехфазной лучевой схемой выпрямления. 3. Обработка экспериментальных данных.</p><p> Особенности вентильных трансформаторов Вентильные трансформаторы (ВТ) используются в составе выпрямительных агрегатов, предназначенных для преобразования переменного тока – в постоянный. Основной особенностью условий работы выпрямительных трансформаторов является значительная несинусоидальность токов вторичной обмотки, питающей выпрямители. Поэтому к выпрямительным трансформаторам предъявляются дополнительные требования: наряду с основным назначением силового трансформатора – преобразование параметров энергии переменного синусоидального тока (величин напряжения и тока), они должны обеспечивать и должное качество потребляемой из сети электроэнергии – при несинусоидальном вторичном токе создавать первичный ток, близкий к синусоидальному. Определим основные особенности вентильных трансформаторов, рассматривая структурную схему мощного выпрямительного агрегата </p><img src=\"/static/img/8.1.bmp\" alt=\"8.1.bmp\"/>\n<p>Такой агрегат получает питание от трехфазной сети ВН – А1, далее с помощью вентильного трансформатора А2 понижается величина переменного напряжения. Пониженное переменное напряжение преобразуется в выпрямленное с помощью трехфазного выпрямителя А3.</p><p> Выпрямленное напряжение имеет значительные пульсации, поэтому для получения постоянного тока используется фильтр А4. Отметим, что в мощных выпрямительных агрегатах используются исключительно индуктивные фильтры. Наличие индуктивного фильтра и выпрямителя (фактически ключа) приводит к тому, что вторичный ток вентильного трансформатора становится несинусоидальным, и его форма приближается к - прямоугольной. Рис.8.1. Для идеального трансформатора справедливо равенство МДС первичной и вторичной обмоток, причем, в каждый момент времени , (8.1) поэтому при прямоугольной форме вторичного тока, первичный ток вентильного трансформатора, будет иметь такую же форму. Таким образом, для питающей сети такой вентильный трансформатор с (m1 = m2) представляет собой источник высших гармоник тока, и как следствие высших гармоник напряжения.</p> <p>Действенным способом подавления высших гармоник в электрических сетях является применение силовых резонансных фильтров. Однако, при значительных мощностях выпрямительных агрегатов такой путь крайне затратен. Иное, более практичное решение состоит в таком построении вентильного трансформатора, при котором, значительная несинусоидальность вторичных токов, не будет приводить к несинусоидальности – первичных. Возможность такого пути заложена в уравнении МДС трансформатора (8.1). Так, для трехобмоточного трансформатора</p>\n<img src=\"/static/img/8.2а.jpg\" alt=\"8.2а.jpg\"/>\n<p>первичная МДС равна сумме МДС вторичной и третичной обмоток , (8.2) Предположим, что вторичный i2 и третичный i3 токи имеют прямоугольную форму, но при этом сдвинуты относительно друг друга по фазе </p><img src=\"/static/img/8.2б.jpg\" alt=\"8.2б.jpg\"/>\n <p>Тогда первичная МДС приобретет уже другую – ступенчатую форму, в большей степени приближаясь к синусоидальной. Очевидно, увеличивая число вторичных обмоток, и уменьшая угол сдвига фаз их токов, Рис. 8.2. Изменение формы первичного тока трансформатора относительно форм вторичных: а) – схема преобразования; б) – временные диаграммы МДС можно формировать ступенчатую форму первичного тока, приближающуюся к – синусоидальной.</p>\n<p>Отметим, что переход от прямоугольной формы первичного тока к -ступенчатой, снижает амплитуды низших гармоник, но увеличивает - высших. Однако такое смещение спектра в область высших гармоник крайне благоприятно, поскольку в этом случае, даже небольшая индуктивность питающей сети, представляет собой фильтр низших гармоник. Подведем итоги, - для получения вентильного трансформатора с пониженной несинусоидального первичного тока, необходимо увеличивать число вторичных обмоток, векторы напряжений которых, должны образовывать систему напряжений, с числом фаз большим, чем число фаз питающей сети .</p> <p> (8.3) Полученное соотношение между числом фаз первичной и вторичной обмоток для вентильных трансформаторов позволяет определять их как умножители фаз. Принципы умножения числа фаз устройствами трансформаторного типа Возможность увеличения фаз трехфазным трансформатором (в общем случае любым многофазным при m1 > 1 ) основывается на следующих положениях: - во-первых, для трансформаторов, первичные и вторичные напряжения имеют одинаковую фазу (условно); - во вторых, один и тот же трехфазный трансформатор может иметь различные группы соединений обмоток (например, Y/Y – 0, и Y/Y – 6, рис. 6.3) только за счет различного способа соединения фаз вторичных обмоток. </p>\n<img src=\"/static/img/8.3.jpg\" alt=\"8.3.jpg\"/>\n<p>Образование различных групп соединений трансформаторов: а) - Y/Y – 0; б) - Y/Y – 6 Таким образом, первый, наиболее очевидный способ увеличения числа фаз, состоит в увеличении числа вторичных обмоток одинакового номинального напряжения с различными группами соединений. Так, на рис. 8.4 показаны схема и векторные диаграммы трехобмоточного трансформатора Y/Y0-0/Y0-6. Видно, что в этом случае вторичные напряжения образуют шестифазную симметричную систему с α[6] = 600. </p>\n<img src=\"/static/img/8.4.jpg\" alt=\"8.4.jpg\"/>\n<p>Трехфазно-шестифазный преобразователь Y/Y0-0/Y0-6: а) – схема; б) – векторная диаграмма первичных напряжений; в) – векторная диаграмма вторичной шестифазной системы напряжений Для некоторых сложных схем выпрямителей требуются несимметричные многофазные системы с переменным углом сдвига фаз α[6]1 = 300- α[6]2 = 900.</p><p> Так, на рис.8.5 приведен такой преобразователь, представляющий собой трехобмоточный трансформатор со схемой соединения обмоток Y/YΔ. </p>\n<img src=\"/static/img/8.5.jpg\" alt=\"8.5.jpg\"/>\n<p> Трехфазно-шестифазный преобразователь Y/Y0-0/Δ-1: а) – схема; б) – векторные диаграммы напряжений вторичных обмоток Y и Δ; в) – векторная диаграмма вторичной шестифазной системы напряжений Описание лабораторной установки Лабораторная работа выполняется на стенде для исследования трансформаторов. Подача напряжения на стенд производится кнопкой SB1 «ПУСК» (зеленой), снятие напряжения - кнопкой SB2 «СТОП» (красной). В лабораторной работе используется следующее оборудование.</p><p> Объектом исследования являются выпрямительные агрегаты, состоящие из трехфазного многообмоточного трансформатора ТС1 и трехфазных лучевых выпрямителей UZ1, UZ2. Имеющееся оборудование позволяет реализовывать следующие схемы выпрямления: - 3-пульсную со схемой соединения обмоток выпрямительного трансформатора Y /Y и трехфазной лучевой схемой выпрямления (рис. 8.6 б); - 3-пульсную со схемой соединения обмоток выпрямительного трансформатора Δ/Z0 и трехфазной лучевой схемой выпрямления (рис. 8.6 в); - 3-пульсную со схемой соединения обмоток выпрямительного трансформатора Y/Z0 и трехфазной лучевой схемой выпрямления (рис. 8.6 в); - 6-пульсную со схемой соединения обмоток выпрямительного трансформатора Y/ Y0/0 и двумя лучевыми выпрямителями (рис. 8.6г). </p>\n<img src=\"/static/img/8.6.jpg\" alt=\"8.6.jpg\"/>\n<p> Трехфазный трансформатор (ТС1). В качестве вентильного трансформатора используется трехфазный многообмоточный трансформатор. Трансформатор снабжен коммутационным устройством, позволяющим изменять схемы соединений первичной и вторичной обмоток. Изменение схем соединений первичных обмоток (Y, Y0, Δ) осуществляется многопозиционным переключателем SA1, изменение схем соединений вторичных обмоток (Y0, Z0, Δ, Y0/0, Y/Δ) и их включение - переключателем SA3. Регулирование напряжения осуществляется переключением отпаек, как первичной обмотки (переключатель SA2), так и вторичной обмотки (переключатель SA4). Переключатели SA1, SA3 расположены на лицевой панели лабораторного стенда. Лицевая панель блока трансформатора Т1 приведены на рис. 8.7(б). Включение и отключение трансформатора ТС1 производится кнопками SB1«ПУСК» и SB2«СТОП».</p><p> Номинальные данные трансформатора приведены в табл. 8.1. Таблица 8.1 Номинальные данные исследуемого трансформатора ТС1 Схема соединения обмоток SНОМ, ВА U1НОМ, В I1НОМ , А U2НОМ, В I2НОМ , А Y(Δ)/Y0 380 380 0.58 220 1.0 Δ(Δ)/Y0 380 380 0.58 220 1.0 Y(Δ)/Z0 330 380 0.58 190 1.0 Y(Δ)/Δ 380 380 0.58 220/220 0.5/0.5 Y(Δ)/Y0/0 380 380 0.58 220/220 0.5/0.5 Рис. 8.7(а) Рис. 8.7(б) Полупроводниковые выпрямители. В работе используются полупроводниковые трехфазные выпрямители лучевой схемы UZ1– UZ2 и мостовой схемы UZ3 – UZ4. Эти выпрямители расположены на блоке ВТ (рис. 8.8). Уравнительный реактор (Lр).</p> <p>Расположены на блоке ПВ (рис. 8.8). Плечи уравнительного реактора могут быть шунтированы выключателем Q1. Нагрузка выпрямителя. В качестве нагрузки выпрямителя используется реостат и индуктивный фильтр (рис. 8.8). Изменение сопротивления реостата осуществляется ступенчато поворотной рукояткой R. Индуктивный фильтр может быть шунтирован выключателем Q2. Для измерения выпрямленного тока и напряжения в цепь нагрузки включены амперметр A1 и вольтметр V1. </p>\n<img src=\"/static/img/8.7-8.8.jpg\" alt=\"8.7-8.8.jpg\"/>\n<p> Нагрузочный реостат. В качестве линейной нагрузки трансформатора используется трехфазный нагрузочный реостат, схема которого приведена на </p>\n<img src=\"/static/img/8.9-8.10.jpg\" alt=\"8.9-8.10.jpg\"/>\n<p> Изменение сопротивления фаз осуществляется ступенчато поворотной рукояткой R. Рис. 8.9 Измерительный комплект. Для измерения первичных и вторичных линейных и фазных напряжений, линейных токов трансформатора на стенде имеется трехфазный измерительный комплект. Вид мнемосхемы комплекта приведен на рис. 8.10. </p>',8),(2,'<h3>Лабораторная работа ЛК4-b</h3>\n\n<p><b>\nМОЩНЫЙАСИНХРОННЫЙ ДВИГАТЕЛЬ В СИСТЕМЕ ЭЛЕКТРОСНАБЖЕНИЯ ПРЕДПРИЯТИЯ.\nИССЛЕДОВАНИЕ УСТОЙЧИВОСТИ РАБОТЫ АСИНХРОННОГО ДВИГАТЕЛЯ ПРИ СНИЖЕНИИ ПИТАЮЩЕГО НАПРЯЖЕНИЯ, \nВЛИЯНИЕ НЕСИММЕТРИИ ПРИЛОЖЕННОГО НАПРЯЖЕНИЯ</b></p>\n\n<p>Цель работы</p>\n\n<p>Экспериментальное исследование устойчивости работы асинхронного двигателя при  понижении напряжения питающей сети. </p>\n\n<p>Программа работы</p>\n<ul>\n<li>Экспериментальное определение напряжения опрокидывания асинхронного двигателя. </li>\n<li>Экспериментальное определение энергетических характеристик асинхронного двигателя при несимметрии напряжений питающей сети.</li>\n<li>Обработка результатов эксперимента.</li>\n<li>Анализ полученных результатов.</li>\n</ul>\n<p>Описание лабораторной установки</p>\n\n<p>Лабораторная работа выполняется на учебных лабораторных стендах №1, №2, №3. Основное оборудование размещено на стенде №1, на стенде №2 используется блок кабельной линии. Стенд №3 – используется только для связи стендов №2 и №3.</p>\n<p>Подача напряжения на стенд №1 производится кнопкой SB1 «ПУСК» (черной), снятие напряжения - кнопкой SB2  «СТОП» (красной), размещенных на блоке УЗО (рис.1.1).</p>\n<p>В лабораторной работе используется следующее оборудование.</p>\n<p>Исследуемый асинхронный двигатель (М1). Объектом исследования является асинхронный двигатель общепромышленного исполнения АДМ63А4У3. Поскольку в лабораторной работе этот двигатель включается на пониженное напряжение, то получаемые данные не совпадают с каталожными. При проведении экспериментов и расчетов характеристик следует руководствоваться паспортными данными машины, приведенными в табл. 1.1. </p>\n<p>Выводы статорной обмотки размещены на клеммной коробке асинхронного двигателя, показанное на рис. 1.2.</p>\n<p>Паспортные данные асинхронного двигателя АДМ63А4У3 (М1)</p>\n<p>Вспомогательная машина (G). Для создания момента сопротивления и добавочного момента на валу асинхронного двигателя используется коллекторная машина постоянного тока ПЛ-072У3 (рис. 1.3). В лабораторной работе эта машина используется в генераторном режиме (для создания тормозного момента). Технические данные машины постоянного тока приведены в табл. 1.2. Источник питания индуктора и нагрузочный реостат МПТ расположены на блоке МП1 (рис. 1.4). Изменение сопротивления осуществляется вращением рукоятки R.</p>\n<p>Паспортные данные машины постоянного тока ПЛ-072У3 (G ) </p>\n<p>Трехфазный трансформатор (ТС1). В качестве силового трансформатора используется трехфазный многообмоточный трансформатор. Трансформатор снабжен коммутационным устройством, позволяющим изменять схемы соединений первичной и вторичной обмоток. Изменение схем соединений первичных обмоток  (Y, Y0, Δ) осуществляется многопозиционным переключателем SA1, изменение схем соединений вторичных обмоток (Y0, Z0, Δ, Y0/0, Y/Δ) и их включение - переключателем SA3. Регулирование напряжения осуществляется переключением отпаек, как первичной обмотки (переключатель SA2) , так  и вторичной обмотки (переключатель SA4). Переключатели SA1, SA3 расположены на лицевой панели лабораторного стенда. Лицевая панель блока трансформатора  Т1  приведены на рис. 1.5.\nВключение и отключение трансформатора ТС1 производится кнопками SB1«ПУСК» и  SB2«СТОП».  \nНоминальные данные трансформатора приведены  в табл. 1.3. </p>',4);
/*!40000 ALTER TABLE `main_method` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_question`
--

DROP TABLE IF EXISTS `main_question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_question` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `text_question` longtext NOT NULL,
  `course_id` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_question_course_id_4d1914d324978fc4_fk_main_course_id` (`course_id`),
  CONSTRAINT `main_question_course_id_4d1914d324978fc4_fk_main_course_id` FOREIGN KEY (`course_id`) REFERENCES `main_course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_question`
--

LOCK TABLES `main_question` WRITE;
/*!40000 ALTER TABLE `main_question` DISABLE KEYS */;
INSERT INTO `main_question` VALUES (1,'Как при лучевых схемах выпрямителя получить 6 - пульсную кривую выпрямленного напряжения?',8,1),(2,'Схема лучевого выпрямителя изображена на рис. <br> <img src=\"/static/img/8.1.bmp\" alt=\"8.1.bmp\"/>',8,2),(3,'Величина среднего выпрямленного напряжения в лучевой схеме выпрямления равна …',8,3),(4,'Коэффицент пульсаций лучевой схемы выпрямления равен ….',8,4),(5,'Как при лучевых схемах выпрямителя получить 6 - пульсную кривую выпрямленного напряжения?',1000,1),(6,'Схема лучевого выпрямителя изображена на рис. <br> <img src=\"/static/img/8.1.bmp\" alt=\"8.1.bmp\"/>',1000,2),(7,'Величина среднего выпрямленного напряжения в лучевой схеме выпрямления равна …',1000,3),(8,'Коэффицент пульсаций лучевой схемы выпрямления равен ….',1000,4),(9,'Вопрос 1',4,1),(10,'Вопрос 2',4,2);
/*!40000 ALTER TABLE `main_question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_standtask_data`
--

DROP TABLE IF EXISTS `main_standtask_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_standtask_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `standtask_id` int(11) NOT NULL,
  `conn_json` linestring NOT NULL,
  `rope_json` linestring NOT NULL,
  `standtask_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_standtask_data`
--

LOCK TABLES `main_standtask_data` WRITE;
/*!40000 ALTER TABLE `main_standtask_data` DISABLE KEYS */;
INSERT INTO `main_standtask_data` VALUES (1,1,'','','Схема №1'),(2,2,'','','Схема №2'),(3,4,'','','Четвертая схема'),(4,5,'','','Схема номер 5');
/*!40000 ALTER TABLE `main_standtask_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_standtaskstate`
--

DROP TABLE IF EXISTS `main_standtaskstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_standtaskstate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activate` tinyint(1) NOT NULL,
  `complete` tinyint(1) NOT NULL,
  `error` tinyint(1) NOT NULL,
  `standtask_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `user_rope_json` linestring DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `main_standta_stand_task_id_5a1cb4f9652a5f4d_fk_main_standtask_id` (`standtask_id`),
  KEY `main_standtaskstate_user_id_7220ef5c62679744_fk_auth_user_id` (`user_id`),
  CONSTRAINT `main_standtaskstate_user_id_7220ef5c62679744_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_standtaskstate`
--

LOCK TABLES `main_standtaskstate` WRITE;
/*!40000 ALTER TABLE `main_standtaskstate` DISABLE KEYS */;
INSERT INTO `main_standtaskstate` VALUES (1,1,0,0,1,7,NULL),(2,1,0,0,4,5,NULL),(3,0,0,0,2,5,NULL),(4,0,1,0,2,5,NULL),(5,0,1,0,5,7,NULL),(6,0,1,0,5,7,NULL),(7,0,0,0,5,7,NULL);
/*!40000 ALTER TABLE `main_standtaskstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_userallowance`
--

DROP TABLE IF EXISTS `main_userallowance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_userallowance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `construct` tinyint(1) NOT NULL,
  `course_start` tinyint(1) NOT NULL,
  `report` tinyint(1) NOT NULL,
  `course_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_userallowance_course_id_41270f0109adae6a_fk_main_course_id` (`course_id`),
  KEY `main_userallowance_user_id_f27424ade70a97a_fk_auth_user_id` (`user_id`),
  CONSTRAINT `main_userallowance_course_id_41270f0109adae6a_fk_main_course_id` FOREIGN KEY (`course_id`) REFERENCES `main_course` (`id`),
  CONSTRAINT `main_userallowance_user_id_f27424ade70a97a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_userallowance`
--

LOCK TABLES `main_userallowance` WRITE;
/*!40000 ALTER TABLE `main_userallowance` DISABLE KEYS */;
INSERT INTO `main_userallowance` VALUES (2,1,1,0,8,5),(3,1,1,0,1000,5),(4,1,1,0,4,5),(5,0,0,0,4,1),(6,0,0,0,8,1);
/*!40000 ALTER TABLE `main_userallowance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_useranswer`
--

DROP TABLE IF EXISTS `main_useranswer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_useranswer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `answer_id` int(11) NOT NULL,
  `question_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_useranswer_answer_id_67a7cbcffce0e82c_fk_main_answer_id` (`answer_id`),
  KEY `main_useranswer_question_id_2c52fd250e105554_fk_main_question_id` (`question_id`),
  KEY `main_useranswer_user_id_3292f92dfbe9adc1_fk_auth_user_id` (`user_id`),
  CONSTRAINT `main_useranswer_answer_id_67a7cbcffce0e82c_fk_main_answer_id` FOREIGN KEY (`answer_id`) REFERENCES `main_answer` (`id`),
  CONSTRAINT `main_useranswer_question_id_2c52fd250e105554_fk_main_question_id` FOREIGN KEY (`question_id`) REFERENCES `main_question` (`id`),
  CONSTRAINT `main_useranswer_user_id_3292f92dfbe9adc1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_useranswer`
--

LOCK TABLES `main_useranswer` WRITE;
/*!40000 ALTER TABLE `main_useranswer` DISABLE KEYS */;
INSERT INTO `main_useranswer` VALUES (5,1,1,5),(6,5,2,5),(7,9,3,5),(8,13,4,5),(9,17,5,5),(10,21,6,5),(11,25,7,5),(12,29,8,5),(13,33,9,5),(14,37,10,5);
/*!40000 ALTER TABLE `main_useranswer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_usercoursestate`
--

DROP TABLE IF EXISTS `main_usercoursestate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_usercoursestate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) NOT NULL,
  `course_state_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_usercoursestat_course_id_5bc2f204c3df6b2c_fk_main_course_id` (`course_id`),
  KEY `main_use_course_state_id_70c0af107ab11438_fk_main_coursestate_id` (`course_state_id`),
  KEY `main_usercoursestate_user_id_52f10020c6549bd0_fk_auth_user_id` (`user_id`),
  CONSTRAINT `main_usercoursestate_user_id_52f10020c6549bd0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `main_usercoursestat_course_id_5bc2f204c3df6b2c_fk_main_course_id` FOREIGN KEY (`course_id`) REFERENCES `main_course` (`id`),
  CONSTRAINT `main_use_course_state_id_70c0af107ab11438_fk_main_coursestate_id` FOREIGN KEY (`course_state_id`) REFERENCES `main_coursestate` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_usercoursestate`
--

LOCK TABLES `main_usercoursestate` WRITE;
/*!40000 ALTER TABLE `main_usercoursestate` DISABLE KEYS */;
INSERT INTO `main_usercoursestate` VALUES (1,8,2,5,'2016-01-06'),(2,4,2,5,'2016-01-06'),(3,1,3,5,'2016-01-06'),(4,1000,2,5,'2016-01-06');
/*!40000 ALTER TABLE `main_usercoursestate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_userfieldparam`
--

DROP TABLE IF EXISTS `main_userfieldparam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_userfieldparam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` varchar(200) NOT NULL,
  `field_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_userfieldp_field_id_50aa7577f659dbac_fk_main_coursefield_id` (`field_id`),
  CONSTRAINT `main_userfieldp_field_id_50aa7577f659dbac_fk_main_coursefield_id` FOREIGN KEY (`field_id`) REFERENCES `main_coursefield` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_userfieldparam`
--

LOCK TABLES `main_userfieldparam` WRITE;
/*!40000 ALTER TABLE `main_userfieldparam` DISABLE KEYS */;
/*!40000 ALTER TABLE `main_userfieldparam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_workplace`
--

DROP TABLE IF EXISTS `main_workplace`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_workplace` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `wp_type_id` int(11) NOT NULL,
  `url` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_workplace_a1feea53` (`wp_type_id`),
  CONSTRAINT `main_workplace_wp_type_id_2c33c076dc691793_fk_main_wptype_id` FOREIGN KEY (`wp_type_id`) REFERENCES `main_wptype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_workplace`
--

LOCK TABLES `main_workplace` WRITE;
/*!40000 ALTER TABLE `main_workplace` DISABLE KEYS */;
INSERT INTO `main_workplace` VALUES (1,'test stand',1,'http://46.48.44.5/do?format=json&'),(2,'stand1',2,'http://212.193.85.65:8087/do?format=json&');
/*!40000 ALTER TABLE `main_workplace` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_wpparam`
--

DROP TABLE IF EXISTS `main_wpparam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_wpparam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `workplace_id` int(11) NOT NULL,
  `wp_param_type_id` int(11) NOT NULL,
  `code` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `main_wpparam_673bd72d` (`wp_param_type_id`),
  KEY `main_wpparam_workplace_id_3aaa7a4c950bea5_fk_main_workplace_id` (`workplace_id`),
  CONSTRAINT `main_wpparam_workplace_id_3aaa7a4c950bea5_fk_main_workplace_id` FOREIGN KEY (`workplace_id`) REFERENCES `main_workplace` (`id`),
  CONSTRAINT `main_wp_wp_param_type_id_679463265d6fcd2f_fk_main_wpparamtype_id` FOREIGN KEY (`wp_param_type_id`) REFERENCES `main_wpparamtype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10805 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_wpparam`
--

LOCK TABLES `main_wpparam` WRITE;
/*!40000 ALTER TABLE `main_wpparam` DISABLE KEYS */;
INSERT INTO `main_wpparam` VALUES (1,'param1',1,1,'uid=1'),(5,'param5',1,1,'uid=5'),(7,'param7',1,1,'uid=7'),(17,'param17',1,1,'uid=17'),(10001,'param10001',2,1,'uid=10001'),(10002,'param10002',2,1,'uid=10002'),(10003,'param10003',2,1,'uid=10003'),(10801,'param801',2,1,'uid=801'),(10802,'param802',2,1,'uid=802'),(10803,'param803',2,1,'uid=803'),(10804,'param804',2,1,'uid=804');
/*!40000 ALTER TABLE `main_wpparam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_wpparamtype`
--

DROP TABLE IF EXISTS `main_wpparamtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_wpparamtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_wpparamtype`
--

LOCK TABLES `main_wpparamtype` WRITE;
/*!40000 ALTER TABLE `main_wpparamtype` DISABLE KEYS */;
INSERT INTO `main_wpparamtype` VALUES (1,'int');
/*!40000 ALTER TABLE `main_wpparamtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `main_wptype`
--

DROP TABLE IF EXISTS `main_wptype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `main_wptype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `main_wptype`
--

LOCK TABLES `main_wptype` WRITE;
/*!40000 ALTER TABLE `main_wptype` DISABLE KEYS */;
INSERT INTO `main_wptype` VALUES (1,'test'),(2,'real'),(3,'3d');
/*!40000 ALTER TABLE `main_wptype` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-04 17:57:04
