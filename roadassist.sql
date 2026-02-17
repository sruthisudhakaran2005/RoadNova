-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 17, 2026 at 11:34 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `roadassist`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `last_login` datetime DEFAULT NULL,
  `status` varchar(10) DEFAULT 'active',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `name`, `email`, `password`, `phone`, `image`, `last_login`, `status`, `created_at`) VALUES
(1, 'Admin', 'admin@gmail.com', 'admin123', '7788995566', 'admin.jpg', NULL, 'active', '2024-10-20 04:31:00');

-- --------------------------------------------------------

--
-- Table structure for table `mechanics`
--

CREATE TABLE `mechanics` (
  `mech_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `mail` varchar(40) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `specialization` varchar(20) DEFAULT NULL,
  `experience` varchar(10) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `dob` date DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `idproof` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mechanics`
--

INSERT INTO `mechanics` (`mech_id`, `name`, `phone`, `mail`, `address`, `specialization`, `experience`, `created_at`, `dob`, `gender`, `shop_id`, `image`, `idproof`) VALUES
(1, 'Rahul', '7788995566', 'user@gmail.com', 'palakkad,kerala', 'engine', '1', '2025-08-25 17:50:55', '2003-03-12', 'Male', 1, 'owner1.jpg', 'id2.jpg'),
(2, 'Neha', '9867545623', 'neha@gmail.com', 'coimbatore,thamilnadu', 'general', '1', '2025-08-26 09:15:45', '2001-04-06', 'Female', 5, NULL, NULL),
(4, 'Arun Das', '9867545623', 'arundas@gmail.com', '15/212, Kalpathy, Palakkad, Kerala - 678003', 'brakes', '6', '2025-08-31 11:44:54', '1996-06-06', 'Male', 1, 'owner2.jpg', 'idm2.webp'),
(7, 'rohan', '7788995566', 'rohan@gmail.com', 'palakkad,kerala', 'electrical', '3', '2025-08-31 12:05:53', '2000-03-12', 'Male', 1, 'owner4.jpg', 'idm2.webp'),
(8, 'Aravind', '7897442818', 'aravind@gmail.com', 'Sreekrishna Nagar, Olavakkode\r\n\r\n\r\n\r\nPalakkad � 678002', 'transmission', '5', '2025-09-02 06:45:49', '1998-06-30', 'Male', 1, 'owner4.jpg', 'id2.jpg'),
(9, 'Ramesh', '7788995566', 'ramesh@gmail.com', 'palakkad,kerala', 'general', '12', '2025-09-02 07:03:09', '1982-04-12', 'Male', 1, '20250902123309_mechm.jpg', '20250902123309_idm1.webp'),
(10, 'Anoop Mathew', '7788995566', 'anoop@gmail.com', 'Vellayil Lane, Kadavanthra, Ernakulam, Kerala', 'electrical', '3', '2025-09-11 05:48:57', '1996-06-27', 'Male', 2, '20250911111857_owner4.jpg', '20250911111857_idm3.jpg'),
(12, 'Rahul', '9867545623', 'rahul@gmail.com', 'kerala', 'engine', '1', '2025-09-11 06:23:21', '2001-03-12', 'Male', 2, '20250911115321_user.jpg', '20250911115321_id2.jpg'),
(13, 'jithin', '9867545623', 'jithin@mail.com', 'kochi, Ernakulam', 'brakes', '1', '2025-09-16 05:16:52', '2000-06-03', 'Male', 2, '20250916104652_user.jpg', '20250916104652_idm3.jpg'),
(14, 'ajith', '9867545623', 'ajith@gmail.com', 'kochi,kerala', 'brakes', '0', '2025-09-16 05:19:55', '1999-04-10', 'Male', 3, '20250916104955_owner4.jpg', '20250916104955_idm3.jpg'),
(15, 'sreya', '9867545634', 'sreya@gmail.com', 'kochi,kerala', 'general', '1', '2025-09-16 05:20:59', '2001-04-12', 'Female', 3, '20250916105059_mechw.png', '20250916105059_id1.png'),
(16, 'mahesh', '7897442818', 'mahesh@gmail.com', 'chennai,thamilnadu', 'engine', '5', '2025-09-16 05:23:41', '1890-06-05', 'Male', 4, '20250916105341_owner3.jpg', '20250916105341_idm3.jpg'),
(17, 'kavya', '7788995561', 'kavya@gmail.com', 'chennai', 'general', '2', '2025-09-16 05:25:22', '2001-01-31', 'Female', 4, '20250916105522_profile.jpg', '20250916105522_id1.png'),
(18, 'ravi', '7897442818', 'ravi@gmail.com', 'chennai', 'brakes', '6', '2025-09-16 05:29:04', '1895-03-12', 'Male', 6, '20250916105904_owner3.jpg', '20250916105904_idm1.webp'),
(19, 'Adarsh', '9867545623', 'adarsh@gmail.com', 'chennai,thamilnadu', 'general', '3', '2025-09-19 15:26:33', '2000-03-12', 'Male', 7, '20250919205633_user.jpg', '20250919205633_idm2.webp'),
(20, 'mohan', '7788995566', 'mohank@gmail.com', 'chennai,india', 'electrical', '4', '2025-09-20 03:03:05', '2000-02-11', 'Male', 6, '20250920083305_owner3.jpg', '20250920083305_idm3.jpg'),
(21, 'manu', '9867545623', 'manu@gmail.com', 'chennai,thamilnadu', 'electrical', '5', '2025-09-25 02:36:45', '1890-03-12', 'Male', 13, '20250925080645_owner3.jpg', '20250925080645_idm1.webp');

-- --------------------------------------------------------

--
-- Table structure for table `mechanicshops`
--

CREATE TABLE `mechanicshops` (
  `id` int(11) NOT NULL,
  `owner_name` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `gender` enum('male','female','other') NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` text NOT NULL,
  `adhar_proof` varchar(255) NOT NULL,
  `state` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `owner_image` varchar(255) NOT NULL,
  `shop_name` varchar(100) NOT NULL,
  `shop_address` text NOT NULL,
  `shop_image` varchar(255) NOT NULL,
  `license_proof` varchar(255) NOT NULL,
  `operating_hours` varchar(50) NOT NULL,
  `status` varchar(50) DEFAULT 'Pending',
  `registration_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `owner_email` varchar(100) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `availability` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `mechanicshops`
--

INSERT INTO `mechanicshops` (`id`, `owner_name`, `dob`, `gender`, `phone`, `address`, `adhar_proof`, `state`, `city`, `owner_image`, `shop_name`, `shop_address`, `shop_image`, `license_proof`, `operating_hours`, `status`, `registration_date`, `owner_email`, `password`, `availability`) VALUES
(1, 'Rajesh Kumar', '1990-03-12', 'male', '7788995562', 'palakkad,kerala', 'idm1.webp', 'kerala', 'palakkad', 'owner3.jpg', 'Speed Auto Garage', 'near ksrtc bus stand,palakkad', 'shop9.avif', 'proof1.webp', '9.00am-6.00pm', 'Approved', '2025-08-23 05:42:41', 'productr051@gmail.com', 'shop123', 'Open'),
(2, 'Anjali', '2000-04-23', 'female', '7788225566', 'House No. 14, Vyttila, Ernakulam', 'id1.png', 'kerala', 'Ernakulam', 'ownerw1.jpg', 'Anjali\'s Auto Garage', 'NH Bypass Road, Near Vyttila Mobility Hub, Ernakulam', 'shop11.jpg', 'proof1.webp', '9.00am-6.00pm', 'Approved', '2025-08-23 06:21:03', 'vinusruthi000@gmail.com', 'shop222', 'Open'),
(3, 'Asha Varghese', '2000-04-21', 'female', '9867545623', '77, Naval Guardian Road, Vyttila, Kochi – 682019, Kerala', 'id1.png', 'kerala', 'Ernakulam', 'ownerw1.jpg', 'Kochi Multibrand Automotive', 'Chakkamadam, Moulana Azad Road, Mattancherry, Kochi, Kerala ', 'shop3.jpg', 'proof1.webp', '10am-10pm', 'Approved', '2025-08-23 12:08:03', 'vinusruthi@gmail.com', 'shop111', 'Open'),
(4, 'Rahul', '2001-03-12', 'male', '9867545621', 'chennai,thamilnadu', 'id2.jpg', 'Tamil Nadu', 'chennai', 'owner4.jpg', 'Rahul-auto care', 'chennai,Tamil Nadu', 'shop2.jpg', 'proof1.webp', '7am-10pm', 'Approved', '2025-08-30 06:14:35', 'sumayasudhakaran@gmail.com', 'Ra867Tm', 'Open'),
(5, 'Anitha Das', '1994-08-12', 'female', '7897442818', 'Stadium Bypass Road, Palakkad, Kerala', 'id1.png', 'kerala', 'palakkad', 'ownerw1.jpg', 'Anitha s Auto Fix', 'Stadium Bypass, Near Malabar Hospital, Palakkad', 'shop1.jpg', 'proof1.webp', '9am-9pm', 'Approved', '2025-08-30 06:44:36', 'anithasgarage@gmail.com', 'An897XD', 'Open'),
(6, 'Ravi Kumar', '1882-05-16', 'male', '9867545623', '123, Mount Road\r\nTeynampet, Chennai', 'idm1.webp', 'Tamil Nadu', 'chennai', 'owner1.jpg', 'Chennai Auto Care', ' Mount Road, Teynampet, Chennai', 'shop4.jpg', 'proof1.webp', '9am-9pm', 'Rejected', '2025-09-10 06:41:00', 'ravikumar@gmail.com', NULL, 'Open'),
(7, 'arun', '1994-03-12', 'male', '7897442818', 'chennai,thamilnadu', 'id2.jpg', 'Tamil Nadu', 'chennai', 'owner4.jpg', 'arun auto care', 'chennai,thamilnadu', 'shop5.webp', 'proof1.webp', '10am-10pm', 'Blocked', '2025-09-10 06:43:42', 'arun@gmail.com', 'Jo2347G', 'Open'),
(8, 'John', '2001-09-11', 'male', '1234567890', 'Sai ram towers', 'idm1.webp', 'kerala', 'palakkad', 'cartoon.jpg', 'John Vehicle Service', 'sai ram towers', 'shop2.jpg', 'id1.png', '9am-9pm', 'Pending', '2025-09-10 08:43:16', 'techvolt.devisri@gmail.com', NULL, 'Open'),
(10, 'diya', '1999-03-12', 'female', '9867545623', 'chennai,tamilnadu', 'id1.png', 'Tamil Nadu', 'Coimbatore', 'profile.jpg', 'diya\'s auto care', 'chennai,thamilnadu', 'shop6.avif', 'proof1.webp', '7-10', 'Blocked', '2025-09-10 15:49:20', 'diya@gmail.com', 'X6kzDO7T', 'Open'),
(11, 'aswin', '2000-02-12', 'male', '7788995566', 'palakkad,kerala', 'id2.jpg', 'Kerala', 'Palakkad', 'user.jpg', 'aswin auto care', 'palakkad,kerala', 'shop7.jpg', 'proof1.webp', '7-10', 'Pending', '2025-09-16 08:28:22', 'aswin@gmail.com', 'An788QY', 'Open'),
(12, 'Aneesh', '1980-02-11', 'male', '7788995566', 'West Yakkara\r\nPalakkad – 678012', 'id2.jpg', 'Kerala', 'Palakkad', 'owner3.jpg', 'Aneesh auto care', 'West Yakkara,Near govt school \r\nPalakkad – 678012', 'shop8.jpg', 'proof1.webp', '7am-10pm', 'Pending', '2025-09-20 02:10:14', 'aneesh@gmail.com', NULL, NULL),
(13, 'vishnu', '2000-02-11', 'male', '6223233434', 'chennai,thamilnadu', 'id2.jpg', 'Tamil Nadu', 'Chennai', 'owner1.jpg', 'DriveLine Workshop', 'Chennai,thamilnadu', 'shop8.jpg', 'proof1.webp', '7-10', 'Approved', '2025-09-23 05:49:55', 'vishnu@gmail.com', 'dh7881s', 'Open'),
(14, 'dhdfcfidf', '1900-01-11', 'male', '7788995566', 'zzxvfgng', 'idm1.webp', 'Gujarat', 'Surat', 'mechm.jpg', 'flwjfew', ' lfcjjewf', 'shop4.jpg', 'img17.jpg', '10-10', 'Rejected', '2025-09-23 05:54:47', 'aff@gmail.com', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `notifications`
--

CREATE TABLE `notifications` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `request_id` int(11) NOT NULL,
  `message` text DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `shop_name` varchar(200) DEFAULT NULL,
  `status` varchar(10) DEFAULT 'unseen'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `notifications`
--

INSERT INTO `notifications` (`id`, `user_id`, `request_id`, `message`, `created_at`, `shop_name`, `status`) VALUES
(1, 1, 81, 'Yout request for Brake Failure has been approved. A mechanic is on their way', '2025-09-24 16:34:42', 'Speed Auto Garage', 'seen'),
(2, 1, 82, 'sorry we cant approve service now', '2025-09-24 16:41:52', 'Speed Auto Garage', 'seen'),
(3, 2, 84, 'we are on the way\r\n\r\n\r\n', '2025-09-24 16:47:51', 'Speed Auto Garage', 'seen'),
(4, 2, 85, 'Your service request has been approved.', '2025-09-24 16:52:24', 'Speed Auto Garage', 'seen'),
(5, 2, 86, 'Your service request has been approved.', '2025-09-24 16:55:57', 'Anjali\'s Auto Garage', 'seen'),
(6, 1, 87, 'Your service request has been approved.', '2025-09-24 17:01:10', 'Kochi Multibrand Automotive', 'seen'),
(7, 3, 90, 'Your service request has been rejected due to unforeseen circumstances or scheduling conflicts.', '2025-09-24 17:11:42', 'Anitha s Auto Fix', 'unseen'),
(8, 3, 89, 'Your service request has been approved.', '2025-09-24 17:11:55', 'Anitha s Auto Fix', 'unseen'),
(9, 4, 91, 'Your service request has been rejected due to unforeseen circumstances or scheduling conflicts.', '2025-09-24 17:15:47', 'Speed Auto Garage', 'unseen'),
(10, 1, 92, 'Your service request has been approved.', '2025-09-25 08:07:06', 'DriveLine Workshop', 'seen'),
(11, 3, 93, 'Your service request has been approved.', '2025-09-25 08:10:12', 'Speed Auto Garage', 'unseen'),
(12, 1, 95, 'Your service request has been approved.', '2025-09-25 09:52:11', 'Speed Auto Garage', 'seen'),
(13, 6, 99, 'Your service request has been rejected due to unforeseen circumstances or scheduling conflicts.', '2025-09-25 09:57:44', 'Speed Auto Garage', 'unseen'),
(14, 6, 98, 'Your service request has been approved.', '2025-09-25 09:57:56', 'Speed Auto Garage', 'unseen'),
(15, 6, 98, 'Your service request has been approved.', '2025-09-25 09:58:04', 'Speed Auto Garage', 'unseen'),
(16, 7, 100, 'Your service request has been approved.', '2025-09-25 10:02:34', 'Anitha s Auto Fix', 'unseen'),
(17, 9, 102, 'Your service request has been approved.', '2025-09-25 10:34:47', 'Kochi Multibrand Automotive', 'unseen'),
(18, 1, 103, 'Your service request has been approved.', '2025-09-25 12:20:20', 'Speed Auto Garage', 'seen'),
(19, 1, 105, 'Your service request has been approved.', '2025-09-25 14:23:35', 'Rahul-auto care', 'seen'),
(20, 1, 105, 'Your service request has been approved.', '2025-09-25 14:23:41', 'Rahul-auto care', 'seen'),
(21, 1, 104, 'Your service request has been approved.', '2025-09-26 10:22:56', 'Speed Auto Garage', 'seen'),
(22, 1, 106, 'Your request regarding smoke from the engine has been approved.', '2025-09-26 10:30:01', 'Rahul-auto care', 'seen'),
(23, 1, 106, 'Your request regarding smoke from the engine has been approved.', '2025-09-26 10:30:10', 'Rahul-auto care', 'seen'),
(24, 1, 107, 'Towing service for the engine smoke issue has been approved. The tow truck is on the way and is expected to reach the mechanic by 20 minutes.', '2025-09-26 10:33:27', 'Anitha s Auto Fix', 'seen'),
(25, 2, 96, 'Your request regarding the brake failure issue has been approved. The mechanic is expected to reach your location by 15 minutes.', '2025-09-26 10:36:32', 'Speed Auto Garage', 'seen'),
(26, 10, 108, 'dear customer , your request has been approved .our mechanic sreya will reach you within 20 minutes', '2025-09-26 10:40:42', 'Kochi Multibrand Automotive', 'seen'),
(27, 10, 109, 'Your service request has been approved.', '2025-09-27 14:32:22', 'Speed Auto Garage', 'unseen'),
(28, 1, 112, 'Your service request has been approved.', '2025-09-29 10:09:17', 'Speed Auto Garage', 'seen'),
(29, 1, 113, 'Your service request has been approved.', '2025-09-30 11:53:19', 'Speed Auto Garage', 'seen');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `method` varchar(20) DEFAULT NULL,
  `paid_on` datetime DEFAULT NULL,
  `type` varchar(200) DEFAULT 'first'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `shop_id`, `service_id`, `user_id`, `amount`, `method`, `paid_on`, `type`) VALUES
(1, 1, 81, 1, 1000.00, 'UPI', '2025-09-24 16:35:09', 'first'),
(2, 1, 81, 1, 200.00, 'Cash', '2025-09-24 16:35:49', 'second'),
(3, 1, 84, 2, 1000.00, 'UPI', '2025-09-24 16:48:17', 'first'),
(4, 1, 84, 2, 300.00, 'Cash', '2025-09-24 16:49:24', 'second'),
(5, 1, 85, 2, 1200.00, 'UPI', '2025-09-24 16:53:02', 'first'),
(6, 2, 86, 2, 4000.00, 'UPI', '2025-09-24 16:56:24', 'first'),
(7, 3, 87, 1, 1100.00, 'UPI', '2025-09-24 17:02:11', 'first'),
(8, 3, 87, 1, 400.00, 'UPI', '2025-09-24 17:03:08', 'second'),
(9, 5, 89, 3, 1300.00, 'Cash', '2025-09-24 17:12:12', 'first'),
(10, 5, 89, 3, 200.00, 'UPI', '2025-09-24 17:12:58', 'second'),
(11, 13, 92, 1, 1200.00, 'UPI', '2025-09-25 08:07:33', 'first'),
(12, 13, 92, 1, 500.00, 'UPI', '2025-09-25 08:08:17', 'second'),
(13, 13, 92, 1, 500.00, 'UPI', '2025-09-25 08:08:18', 'second'),
(14, 1, 93, 3, 1000.00, 'UPI', '2025-09-25 08:10:36', 'first'),
(15, 1, 98, 6, 1200.00, 'UPI', '2025-09-25 09:58:52', 'first'),
(16, 5, 100, 7, 3500.00, 'UPI', '2025-09-25 10:03:04', 'first'),
(17, 5, 100, 7, 450.00, 'UPI', '2025-09-25 10:04:04', 'second'),
(18, 3, 102, 9, 3000.00, 'UPI', '2025-09-25 10:35:19', 'first'),
(19, 3, 102, 9, 500.00, 'UPI', '2025-09-25 10:36:13', 'second'),
(20, 1, 95, 1, 1200.00, 'UPI', '2025-09-25 11:19:21', 'first'),
(21, 1, 95, 1, 50.00, 'UPI', '2025-09-25 11:20:49', 'second'),
(22, 1, 103, 1, 1000.00, 'UPI', '2025-09-25 12:20:38', 'first'),
(23, 1, 103, 1, 300.00, 'UPI', '2025-09-25 12:21:13', 'second'),
(24, 4, 105, 1, 2000.00, 'UPI', '2025-09-25 14:24:09', 'first'),
(25, 1, 104, 1, 1200.00, 'Cash', '2025-09-26 10:25:01', 'first'),
(26, 1, 104, 1, 150.00, 'UPI', '2025-09-26 10:25:42', 'second'),
(27, 4, 106, 1, 2000.00, 'UPI', '2025-09-26 10:30:30', 'first'),
(28, 5, 107, 1, 3500.00, 'UPI', '2025-09-26 10:34:19', 'first'),
(29, 3, 108, 10, 1000.00, 'UPI', '2025-09-26 10:41:20', 'first'),
(30, 1, 96, 2, 1000.00, 'UPI', '2025-09-27 11:03:31', 'first'),
(31, 1, 96, 2, 100.00, 'UPI', '2025-09-27 11:06:52', 'second'),
(32, 1, 112, 1, 1200.00, 'UPI', '2025-09-29 10:09:43', 'first'),
(33, 1, 113, 1, 1000.00, 'UPI', '2025-09-30 11:53:42', 'first'),
(34, 1, 113, 1, 250.00, 'Cash', '2025-09-30 11:54:34', 'second');

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `review_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `request_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL,
  `review_text` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reviews`
--

INSERT INTO `reviews` (`review_id`, `user_id`, `request_id`, `shop_id`, `rating`, `review_text`, `created_at`) VALUES
(18, 1, 81, 1, 5, '\"Excellent and quick service!\"', '2025-09-24 11:10:10'),
(19, 2, 84, 1, 4, 'good service\r\n', '2025-09-24 11:20:33'),
(20, 2, 86, 2, 5, 'nice service \r\n', '2025-09-24 11:28:03'),
(21, 1, 87, 3, 5, 'customer service was good\r\n', '2025-09-24 11:34:01'),
(22, 1, 92, 13, 5, NULL, '2025-09-25 02:39:03'),
(23, 7, 100, 5, 4, 'overall good service\r\n', '2025-09-25 04:35:49'),
(24, 3, 89, 5, 5, NULL, '2025-09-25 04:36:18'),
(25, 3, 93, 1, 5, NULL, '2025-09-25 04:36:32'),
(26, 9, 102, 3, 4, NULL, '2025-09-25 05:07:15'),
(27, 1, 105, 4, 5, '\r\n', '2025-09-25 08:54:55'),
(28, 1, 95, 1, 3, NULL, '2025-09-25 09:25:47'),
(29, 1, 104, 1, 4, NULL, '2025-09-29 05:27:08');

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `service_id` int(11) NOT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `service_name` varchar(255) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `added` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`service_id`, `shop_id`, `service_name`, `price`, `added`) VALUES
(1, 3, 'Flat Tire ', 1000.00, '2025-09-24 09:33:17'),
(2, 3, 'Towing Service', 3000.00, '2025-09-24 09:33:25'),
(3, 3, 'overheating', 3000.00, '2025-09-24 09:33:55'),
(4, 3, 'Car Key Locked Inside', 1000.00, '2025-09-24 09:34:16'),
(5, 1, 'Battery Jump Start', 1000.00, '2025-09-24 09:34:30'),
(6, 1, 'Vehicle Wont Start', 1000.00, '2025-09-24 09:35:46'),
(7, 1, 'Brake Failure', 1000.00, '2025-09-24 09:35:58'),
(8, 1, 'Flat Tire', 1200.00, '2025-09-24 10:49:06'),
(9, 2, 'Flat Tire', 1500.00, '2025-09-24 10:49:33'),
(10, 2, 'Towing', 4000.00, '2025-09-24 10:49:56'),
(11, 2, 'Jump Start', 2000.00, '2025-09-24 10:50:26'),
(12, 2, 'Brake Failure', 900.00, '2025-09-24 10:50:59'),
(13, 3, 'Smoke from engine', 1100.00, '2025-09-24 10:51:17'),
(14, 3, 'Brake Failure', 1000.00, '2025-09-24 10:51:35'),
(15, 4, 'Flat Tire', 1000.00, '2025-09-24 10:53:04'),
(16, 4, 'overheating', 1500.00, '2025-09-24 10:53:27'),
(17, 4, 'Brake Inspection', 800.00, '2025-09-24 10:53:48'),
(18, 4, 'Smoke from engine', 2000.00, '2025-09-24 10:54:04'),
(19, 4, 'Towing', 4000.00, '2025-09-24 10:54:14'),
(20, 5, 'Towing', 3500.00, '2025-09-24 10:54:30'),
(21, 5, 'Flat Tire', 1300.00, '2025-09-24 10:54:39'),
(22, 5, 'Brake Failure', 1200.00, '2025-09-24 10:54:54'),
(23, 6, 'Flat Tire', 1000.00, '2025-09-24 10:55:10'),
(24, 6, 'Towing', 4500.00, '2025-09-24 10:55:23'),
(25, 6, 'Smoke from engine', 2500.00, '2025-09-24 10:55:35'),
(26, 7, 'Flat Tire', 2000.00, '2025-09-24 10:55:50'),
(27, 7, 'Towing', 5000.00, '2025-09-24 10:56:00'),
(28, 8, 'Flat Tire', 800.00, '2025-09-24 10:56:15'),
(29, 8, 'Towing', 3200.00, '2025-09-24 10:56:22'),
(30, 8, 'Smoke from engine', 2000.00, '2025-09-24 10:56:34'),
(31, 13, 'Engine Failure', 1200.00, '2025-09-25 04:49:52'),
(32, 13, 'Flat Tire', 800.00, '2025-09-25 04:50:06');

-- --------------------------------------------------------

--
-- Table structure for table `service_requests`
--

CREATE TABLE `service_requests` (
  `request_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `shop_id` int(11) NOT NULL,
  `problem_type` varchar(255) NOT NULL,
  `request_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` varchar(50) DEFAULT NULL,
  `mech_id` int(11) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `payment_status` varchar(20) DEFAULT NULL,
  `location` varchar(120) DEFAULT NULL,
  `vehicle_type` varchar(20) DEFAULT NULL,
  `vehicle_brand` varchar(20) DEFAULT NULL,
  `reg_no` varchar(30) DEFAULT NULL,
  `completed_date` timestamp NULL DEFAULT NULL,
  `extra_charge` decimal(10,2) DEFAULT NULL,
  `extra_charge_status` varchar(20) DEFAULT NULL,
  `cancelled_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `refund` decimal(10,2) DEFAULT NULL,
  `pay_status` varchar(20) DEFAULT 'None',
  `total_charge` decimal(10,2) GENERATED ALWAYS AS (coalesce(`price`,0) + coalesce(`extra_charge`,0)) STORED,
  `refund_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `refund_status` varchar(20) DEFAULT NULL,
  `cancellation_fee` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `service_requests`
--

INSERT INTO `service_requests` (`request_id`, `user_id`, `shop_id`, `problem_type`, `request_date`, `status`, `mech_id`, `price`, `payment_status`, `location`, `vehicle_type`, `vehicle_brand`, `reg_no`, `completed_date`, `extra_charge`, `extra_charge_status`, `cancelled_date`, `refund`, `pay_status`, `refund_date`, `refund_status`, `cancellation_fee`) VALUES
(81, 1, 1, 'Brake Failure', '2025-09-24 10:59:41', 'Completed', 8, 1000.00, 'Paid', 'near bus stand', 'Four Wheeler', 'Volkswagen', 'KL09BM1212', '2025-09-24 11:06:16', 200.00, 'Paid', '2025-09-23 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(82, 1, 1, 'Flat Tire', '2025-09-24 11:11:06', 'Rejected', NULL, NULL, 'Pending', ' stedium bus stand,palakkad', 'Two Wheeler', 'TVS', 'KL09BM1234', NULL, NULL, NULL, '2025-09-23 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(83, 1, 5, 'Flat Tire', '2025-09-24 11:15:48', 'Cancelled', NULL, NULL, 'Pending', 'near railyway station ', 'Two Wheeler', 'TVS', 'KL09BM1234', NULL, NULL, NULL, '2025-09-23 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(84, 2, 1, 'Brake Failure', '2025-09-24 11:17:14', 'Completed', 1, 1000.00, 'Paid', 'near bus stand', 'Four Wheeler', 'Volkswagen', 'KL09BM1111', '2025-09-24 11:19:49', 300.00, 'Paid', '2025-09-23 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(85, 2, 1, 'Flat Tire', '2025-09-24 11:21:57', 'Cancelled', 8, 1200.00, 'Paid', 'near ksrtc bus stand', 'Four Wheeler', 'maruti suzuki', 'KL09BM1111', NULL, NULL, NULL, '2025-09-23 18:30:00', 900.00, 'paid', '2025-09-28 14:48:25', 'Paid', 300.00),
(86, 2, 2, 'Towing', '2025-09-24 11:25:36', 'Completed', 13, 4000.00, 'Paid', 'near bus stand', 'Four Wheeler', 'Tesla', 'KL09BM1111', '2025-09-24 11:26:46', NULL, NULL, '2025-09-23 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(87, 1, 3, 'Smoke from engine', '2025-09-24 11:30:21', 'Completed', 15, 1100.00, 'Paid', 'near bus stand', 'Four Wheeler', 'Volkswagen', 'KL09BM1234', '2025-09-24 11:33:31', 400.00, 'Paid', '2025-09-23 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(88, 3, 5, 'Flat Tire', '2025-09-24 11:39:23', 'Cancelled', NULL, NULL, 'Pending', 'near bus stand', 'Two Wheeler', 'Honda', 'KL09BM7777', NULL, NULL, NULL, '2025-09-23 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(89, 3, 5, 'Flat Tire', '2025-09-24 11:40:18', 'Completed', 2, 1300.00, 'Paid', 'near bus stand', 'Two Wheeler', 'TVS', 'KL09BM7777', '2025-09-24 11:43:11', 200.00, 'Paid', '2025-09-23 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(90, 3, 5, 'Flat Tire', '2025-09-24 11:40:48', 'Rejected', NULL, NULL, 'Pending', 'near bus stand', 'Two Wheeler', 'Honda', 'KL09BM7777', NULL, NULL, NULL, '2025-09-23 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(91, 4, 1, 'Vehicle Wont Start', '2025-09-24 11:44:54', 'Rejected', NULL, NULL, 'Pending', 'near bus stand', 'Two Wheeler', 'TVS', 'KL09BM0007', NULL, NULL, NULL, '2025-09-23 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(92, 1, 13, 'other', '2025-09-25 02:13:34', 'Completed', 21, 1200.00, 'Paid', 'near bus stand', 'Two Wheeler', ' suzuki', 'KL09BM0207', '2025-09-25 02:38:37', 500.00, 'Paid', '2025-09-24 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(93, 3, 1, 'Vehicle Wont Start', '2025-09-25 02:39:45', 'Completed', 7, 1000.00, 'Paid', 'near ksrtc bus stand', 'Two Wheeler', ' suzuki', 'KL09BM0707', '2025-09-25 02:41:01', NULL, NULL, '2025-09-24 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(94, 3, 1, 'Flat Tire', '2025-09-25 02:41:52', 'Pending', NULL, NULL, 'Pending', 'near ksrtc bus stand', 'Two Wheeler', 'Honda', 'KL09BM0707', NULL, NULL, NULL, '2025-09-24 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(95, 1, 1, 'Flat Tire', '2025-09-25 02:42:41', 'Completed', 8, 1200.00, 'Paid', 'near bus stand', 'Four Wheeler', 'Tesla', 'KL09BM1234', '2025-09-25 05:51:04', 50.00, 'Paid', '2025-09-24 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(96, 2, 1, 'Brake Failure', '2025-09-25 02:44:14', 'Completed', 1, 1000.00, 'Paid', ' stedium bus stand,palakkad', 'Four Wheeler', 'Volkswagen', 'KL09BM1111', '2025-09-27 05:37:55', 100.00, 'Paid', '2025-09-24 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(97, 5, 1, 'Brake Failure', '2025-09-25 04:24:43', 'Pending', NULL, NULL, 'Pending', 'near ksrtc bus stand', 'Two Wheeler', 'Honda', 'KL09BM1212', NULL, NULL, NULL, '2025-09-24 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(98, 6, 1, 'Flat Tire', '2025-09-25 04:26:53', 'Completed', 8, 1200.00, 'Paid', 'near bus stand', 'Two Wheeler', ' suzuki', 'KL09BM555', '2025-09-27 05:24:45', 250.00, 'Pending', '2025-09-24 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(99, 6, 1, 'Flat Tire', '2025-09-25 04:27:18', 'Rejected', NULL, NULL, 'Pending', 'near bus stand', 'Two Wheeler', 'Honda', 'KL09BM555', NULL, NULL, NULL, '2025-09-24 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(100, 7, 5, 'Towing', '2025-09-25 04:31:53', 'Completed', 2, 3500.00, 'Paid', 'near railyway station ', 'Three Wheeler', 'Bajaj', 'KL09BM4444', '2025-09-25 04:34:30', 450.00, 'Paid', '2025-09-24 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(101, 8, 5, 'Flat Tire', '2025-09-25 04:48:08', 'Pending', NULL, NULL, 'Pending', ' stedium bus stand,palakkad', 'Two Wheeler', 'Honda', 'KL09BM888', NULL, NULL, NULL, '2025-09-24 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(102, 9, 3, 'overheating', '2025-09-25 05:03:28', 'Completed', 15, 3000.00, 'Paid', 'kochi bus stand', 'Multi Wheeler', 'Mahindra', 'KL09BM1010', '2025-09-25 05:06:44', 500.00, 'Paid', '2025-09-24 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(103, 1, 1, 'Brake Failure', '2025-09-25 05:52:23', 'Cancelled', 4, 1000.00, 'Paid', 'near ksrtc bus stand', 'Two Wheeler', ' suzuki', 'KL09BM1122', NULL, 300.00, 'Paid', '2025-09-24 18:30:00', 975.00, 'paid', '2025-09-28 14:45:09', 'Paid', 325.00),
(104, 1, 1, 'Flat Tire', '2025-09-25 06:49:49', 'Completed', 4, 1200.00, 'Paid', 'near bus stand', 'Four Wheeler', 'Tesla', 'KL09BM1234', '2025-09-26 04:55:55', 150.00, 'Paid', '2025-09-24 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(105, 1, 4, 'Smoke from engine', '2025-09-25 08:51:32', 'Completed', 17, 2000.00, 'Paid', 'near railyway station chennai', 'Four Wheeler', 'maruti suzuki', 'KL09BM1234', '2025-09-25 08:54:24', NULL, NULL, '2025-09-24 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(106, 1, 4, 'Smoke from engine', '2025-09-26 04:57:17', 'Completed', 16, 2000.00, 'Paid', 'bus stand ,chennai', 'Four Wheeler', 'Tesla', 'KL09BM1234', '2025-09-26 05:00:56', NULL, NULL, '2025-09-25 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(107, 1, 5, 'Towing', '2025-09-26 05:01:54', 'Completed', 2, 3500.00, 'Paid', ' stedium bus stand,palakkad', 'Two Wheeler', 'Tvs', 'KL09BM1212', '2025-09-27 05:28:08', NULL, NULL, '2025-09-25 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(108, 10, 3, 'Brake Failure', '2025-09-26 05:08:53', 'Completed', 15, 1000.00, 'Paid', 'near govt hospital kochi', 'Two Wheeler', 'TVS', 'KL09BM0707', '2025-09-26 05:11:48', NULL, NULL, '2025-09-25 18:30:00', NULL, 'paid', '2025-09-27 08:55:18', NULL, NULL),
(109, 10, 1, 'Vehicle Wont Start', '2025-09-26 05:13:41', 'Approved', 7, 1000.00, 'Pending', 'near ksrtc bus stand', 'Four Wheeler', 'Volkswagen', 'KL09BM0707', NULL, NULL, NULL, '2025-09-25 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(110, 1, 3, 'Towing Service', '2025-09-27 05:29:33', 'Pending', NULL, NULL, 'Pending', 'infront of Mattancherry govt hss ', 'Four Wheeler', 'Volkswagen', 'KL09BM1234', NULL, NULL, NULL, '2025-09-26 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(111, 2, 1, 'Battery Jump Start', '2025-09-27 05:38:34', 'Pending', NULL, NULL, 'Pending', ' stedium bus stand,palakkad', 'Four Wheeler', 'maruti suzuki', 'KL09BM1111', NULL, NULL, NULL, '2025-09-26 18:30:00', NULL, 'pending', '2025-09-27 08:55:18', NULL, NULL),
(112, 1, 1, 'Flat Tire', '2025-09-29 04:38:45', 'Completed', 4, 1200.00, 'Paid', 'near bus stand', 'Two Wheeler', 'tvs', 'KL09BM0707', '2025-09-29 04:40:05', NULL, NULL, '2025-09-29 04:38:45', NULL, 'paid', '2025-09-29 04:38:45', NULL, NULL),
(113, 1, 1, 'Battery Jump Start', '2025-09-30 06:22:46', 'Completed', 8, 1000.00, 'Paid', 'near ksrtc bus stand', 'Four Wheeler', 'BMW', 'KL09BM1234', '2025-09-30 06:25:00', 250.00, 'Paid', '2025-09-30 06:22:46', NULL, 'None', '2025-09-30 06:22:46', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `gender` enum('Male','Female','Other') NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` text NOT NULL,
  `pincode` varchar(6) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `status` varchar(20) DEFAULT NULL,
  `otp` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `gender`, `email`, `phone`, `address`, `pincode`, `password`, `reg_date`, `status`, `otp`) VALUES
(1, 'sruthi', 'Female', 'sruthi@gmail.com', '7567275437', 'palakkad', '723452', 'sruthi123', '2025-08-21 09:32:38', 'Registered', '665203'),
(2, 'sumaya', 'Female', 'sumayasudhakaran@gmail.com', '7788995566', 'palakkad,kerala', '678502', 'sumaya123', '2025-08-22 07:23:46', 'Registered', NULL),
(3, 'vinu', 'Male', 'vinu@gmail.com', '9122334455', 'pathiripala,palakkad,kerala', '456213', 'vinu123', '2025-08-22 08:38:51', 'Registered', NULL),
(4, 'suji', 'Female', 'sujitha@gmail.com\n', '3322445566', 'palakkad,kerala', '456789', 'suji123', '2025-08-22 08:44:44', 'Registered', NULL),
(5, 'adarsh', 'Male', 'adarsh@gmail.com', '3322445577', 'chittur,palakkad,kerala', '678234', 'adarsh123', '2025-08-22 08:46:22', 'Registered', NULL),
(6, 'sujith', 'Male', 'sujith@gmail.com', '7788995588', 'kochi,kerala', '456789', 'sujith123', '2025-08-22 08:48:17', 'Registered', NULL),
(7, 'Divya', 'Female', 'divya@gmail.com', '4455667788', 'kannur,kerala', '789654', 'divya123', '2025-08-22 08:52:30', 'Registered', NULL),
(8, 'Akhila', 'Female', 'akhila@gmail.com', '7788995511', 'Chittoor Road, Ernakulam North\r\nKochi ,kerala', '234567', 'akhila123', '2025-08-22 08:55:22', 'Registered', NULL),
(9, 'mohan', 'Male', 'mohan@gmail.com', '9867545623', 'chennai,thamilnadu', '123456', 'mohan123', '2025-08-28 10:49:18', 'Registered', NULL),
(10, 'sujitha', 'Female', 'sujithasudhakran105@gmail.com', '9867545623', 'palakkad,kerala', '723451', 'sujitha123', '2025-09-08 15:20:42', 'Registered', NULL),
(13, 'Nithya', 'Female', 'nithya@gmail.com', '9867545623', 'chennai,thamilnadu', '723451', 'nithya123', '2025-09-10 06:33:47', 'Registered', NULL),
(14, 'John', 'Male', 'techvolt.devisri@gmail.com', '1234567890', 'sai bab colony', '124343', '1234567', '2025-09-10 08:38:34', 'Registered', NULL),
(20, 'sudhakaran', 'Male', 'sudhakaran@gmail.com', '9867545623', 'palakkad', '123456', 'S123456#', '2025-09-10 15:24:38', 'Registered', NULL),
(21, 'sahithya', 'Female', 'sahithya@gmail.com', '9867545623', 'palakkad,kerala', '123456', 'Sahithya123#', '2025-09-20 02:02:54', 'Registered', NULL),
(22, 'archana', 'Female', 'archana@gmail.com', '7234567890', 'chennai,thamilnadu', '123456', 'Archana1@', '2025-09-23 05:40:41', 'Registered', NULL);

--
-- Indexes for dumped tables


--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mechanics`
--
ALTER TABLE `mechanics`
  ADD PRIMARY KEY (`mech_id`),
  ADD KEY `fk_shop_id` (`shop_id`);

--
-- Indexes for table `mechanicshops`
--
ALTER TABLE `mechanicshops`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `owner_email` (`owner_email`);

--
-- Indexes for table `notifications`
--
ALTER TABLE `notifications`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `shop_id` (`shop_id`),
  ADD KEY `service_id` (`service_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`review_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `request_id` (`request_id`),
  ADD KEY `shop_id` (`shop_id`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`service_id`),
  ADD KEY `shop_id` (`shop_id`);

--
-- Indexes for table `service_requests`
--
ALTER TABLE `service_requests`
  ADD PRIMARY KEY (`request_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `shop_id` (`shop_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `mechanics`
--
ALTER TABLE `mechanics`
  MODIFY `mech_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `mechanicshops`
--
ALTER TABLE `mechanicshops`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `notifications`
--
ALTER TABLE `notifications`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `reviews`
--
ALTER TABLE `reviews`
  MODIFY `review_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `service_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `service_requests`
--
ALTER TABLE `service_requests`
  MODIFY `request_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=114;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `mechanics`
--
ALTER TABLE `mechanics`
  ADD CONSTRAINT `fk_shop_id` FOREIGN KEY (`shop_id`) REFERENCES `mechanicshops` (`id`);

--
-- Constraints for table `payments`
--
ALTER TABLE `payments`
  ADD CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`shop_id`) REFERENCES `mechanicshops` (`id`),
  ADD CONSTRAINT `payments_ibfk_2` FOREIGN KEY (`service_id`) REFERENCES `service_requests` (`request_id`),
  ADD CONSTRAINT `payments_ibfk_3` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`request_id`) REFERENCES `service_requests` (`request_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `reviews_ibfk_3` FOREIGN KEY (`shop_id`) REFERENCES `mechanicshops` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `services`
--
ALTER TABLE `services`
  ADD CONSTRAINT `services_ibfk_1` FOREIGN KEY (`shop_id`) REFERENCES `mechanicshops` (`id`);

--
-- Constraints for table `service_requests`
--
ALTER TABLE `service_requests`
  ADD CONSTRAINT `service_requests_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `service_requests_ibfk_2` FOREIGN KEY (`shop_id`) REFERENCES `mechanicshops` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
