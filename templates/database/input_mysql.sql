-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 20, 2020 at 05:11 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `phuong0`
--

-- --------------------------------------------------------

--
-- Table structure for table `p000account`
--

CREATE TABLE `p000account` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `password` varchar(255) NOT NULL DEFAULT '5f4dcc3b5aa765d61d8327deb882cf99',
  `img` varchar(255) NOT NULL,
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `role` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for table `p000account`
--
ALTER TABLE `p000account`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for table `p000account`
--
ALTER TABLE `p000account`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

--
-- Dumping data for table `p000account`
--

INSERT INTO `p000account` (`id`, `name`, `email`, `phone`, `address`, `password`, `img`, `created_date`, `role`) VALUES
(1, 'Lê Hồng Phương1', 'admin@gmail.com', '0379558185', '183 Quách Thị Trang, Đà Nẵng', '5f4dcc3b5aa765d61d8327deb882cf99', '../../../assets/images/logo-admin.png', '2020-08-13', 'phuong1');


phuong2
 
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
