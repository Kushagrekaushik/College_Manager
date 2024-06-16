-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 15, 2022 at 09:44 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `manage_data`
--

-- --------------------------------------------------------

--
-- Table structure for table `clerk_data`
--

CREATE TABLE `clerk_data` (
  `Clerk_Unique_ID` int(20) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Phone` varchar(25) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` date NOT NULL,
  `Address` text NOT NULL,
  `Pic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `clerk_data`
--

INSERT INTO `clerk_data` (`Clerk_Unique_ID`, `Name`, `Phone`, `Gender`, `DOB`, `Address`, `Pic`) VALUES
(1, 'jkhf', '5687941230', 'Male', '2010-07-13', 'njbmn \n', 'default_image.jpg'),
(2, 'zxvblfk', '0123456789', 'Female', '2010-07-20', 'zvnkxnvdf\n', '1657868032906943.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `course_data`
--

CREATE TABLE `course_data` (
  `Departments` varchar(50) NOT NULL,
  `Course` varchar(50) NOT NULL,
  `Duration` varchar(50) NOT NULL,
  `Fee` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course_data`
--

INSERT INTO `course_data` (`Departments`, `Course`, `Duration`, `Fee`) VALUES
('computer', 'COE', '4', '4 LPA'),
('computer', 'CSE', '4', '4.2 LPA'),
('eletronics', 'ECE', '4 years', '3.5 LPA'),
('electrical', 'EIC', '4 years', '1.5 LPA'),
('electrical', 'ELE', '4 years', '1.8 LPA'),
('eletronics', 'enc', '4 years', '2.5 LPA'),
('computer', 'IT Diploma', '2 years', '1 LPA');

-- --------------------------------------------------------

--
-- Table structure for table `department_data`
--

CREATE TABLE `department_data` (
  `Department_name` varchar(50) NOT NULL,
  `head_of_department` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department_data`
--

INSERT INTO `department_data` (`Department_name`, `head_of_department`) VALUES
('computer', 'Dr.hs pannu'),
('electrical', 'DR.jitender'),
('eletronics', 'Dr.Mayank');

-- --------------------------------------------------------

--
-- Table structure for table `student_data`
--

CREATE TABLE `student_data` (
  `Roll_number` int(10) NOT NULL,
  `Name` varchar(40) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `DOB` date NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Department` varchar(100) NOT NULL,
  `course` varchar(15) NOT NULL,
  `DayScholar_Hosteler` varchar(20) NOT NULL,
  `Pic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_data`
--

INSERT INTO `student_data` (`Roll_number`, `Name`, `Phone`, `Gender`, `DOB`, `Address`, `Department`, `course`, `DayScholar_Hosteler`, `Pic`) VALUES
(1, 'kushagre', '8872674973', 'Male', '2010-07-14', 'jalandhar\n\n\n\n', 'computer', 'COE', 'Hosteler', '1657867280784668.jpg'),
(2, 'himani', '1234567890', 'Female', '2010-07-07', 'delhi\n\n', 'eletronics', 'enc', 'Hosteler', 'default_image.jpg'),
(3, 'dfhdt', '1234567890', 'Male', '2010-06-29', 'kdfhsdf\n', 'electrical', 'ELE', 'Day scholar', '16578672611815.png');

-- --------------------------------------------------------

--
-- Table structure for table `teacher_data`
--

CREATE TABLE `teacher_data` (
  `Teacher_Unique_ID` int(20) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  `Gender` varchar(20) NOT NULL,
  `DOB` date NOT NULL,
  `Address` text NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Course_Taught` varchar(50) NOT NULL,
  `Pic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teacher_data`
--

INSERT INTO `teacher_data` (`Teacher_Unique_ID`, `Name`, `Phone`, `Gender`, `DOB`, `Address`, `Department`, `Course_Taught`, `Pic`) VALUES
(1, 'tejoprakash', '5698712340', 'Male', '2010-07-29', 'delhi\n', 'electrical', 'EIC', 'default_image.jpg'),
(2, 'hasika', '0123456789', 'Female', '2010-07-06', 'faridabad\n', 'Department', 'EIC', '1657867628906943.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `usertable`
--

CREATE TABLE `usertable` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `usertable`
--

INSERT INTO `usertable` (`username`, `password`, `usertype`) VALUES
('admin', '123', 'Admin'),
('kushagre', '123', 'Employee');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clerk_data`
--
ALTER TABLE `clerk_data`
  ADD PRIMARY KEY (`Clerk_Unique_ID`);

--
-- Indexes for table `course_data`
--
ALTER TABLE `course_data`
  ADD PRIMARY KEY (`Course`);

--
-- Indexes for table `department_data`
--
ALTER TABLE `department_data`
  ADD PRIMARY KEY (`Department_name`);

--
-- Indexes for table `student_data`
--
ALTER TABLE `student_data`
  ADD PRIMARY KEY (`Roll_number`);

--
-- Indexes for table `teacher_data`
--
ALTER TABLE `teacher_data`
  ADD PRIMARY KEY (`Teacher_Unique_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
