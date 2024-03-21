-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 11, 2023 at 07:15 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flaskfndb`
--

-- --------------------------------------------------------

--
-- Table structure for table `newsdata`
--

CREATE TABLE `newsdata` (
  `pid` varchar(50) DEFAULT NULL,
  `dated` varchar(50) DEFAULT NULL,
  `content` varchar(4000) DEFAULT NULL,
  `pred` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `newsdata`
--

INSERT INTO `newsdata` (`pid`, `dated`, `content`, `pred`) VALUES
('P72162', '30-05-2021', 'https://www.mygov.in/covid-19', 'FAKE'),
('P19572', '16-07-2021', '', 'FAKE'),
('P85845', '16-07-2021', '', 'FAKE'),
('P51876', '16-07-2021', '', 'FAKE'),
('P70433', '16-07-2021', '', 'FAKE'),
('P27722', '16-07-2021', '', 'FAKE'),
('P79699', '16-07-2021', '', 'FAKE'),
('P58820', '16-07-2021', '', 'FAKE'),
('P93333', '16-07-2021', '', 'FAKE'),
('P38537', '16-07-2021', 'https://timesofindia.indiatimes.com/india/the-case-for-and-against-a-uniform-civil-code/articleshow/84434255.cms', 'REAL'),
('P95175', '16-07-2021', 'https://timesofindia.indiatimes.com/india//articleshow/84434255.cms', 'REAL'),
('P18905', '16-07-2021', 'https://timesofindia.indiatimes.com/elections/assembly-elections/delhi/vijender-sole-bjp-mla-to-attend-event/articleshow/74168456.cms', 'REAL'),
('P64663', '16-07-2021', 'https://timesofindia.indiatimes.com/elections/assembly-elections/delhi/vijendeevent/articleshow/74168456.cms', 'REAL'),
('P15624', '16-07-2021', 'https://timesofindia.indiatimes.com/elections/assembly-elections/delhi/vijendeevent/articleshow/74167778456.cms', 'FAKE'),
('P92373', '16-07-2021', 'https://timesofindia.indiatimes.com/india/in-pictures-the-world-through-danish-siddiquis-eyes/articleshow/84472455.cms', 'REAL'),
('P49184', '16-07-2021', 'https://timesofindia.indiatimes.com/india/in-pictures-the-world-through-danish-siddiquis-eyes/articleshow/84472222455.cms', 'FAKE'),
('P61327', '16-07-2021', 'https://timesofindia.indiatimes.com/india/in-pictures-the-world-through-danish-siddiquis-eyes/articleshow/84472222455.cms', 'FAKE'),
('P27299', '16-07-2021', 'https://timesofindia.indiatimes.com/india/in-pictures-the-world-through-danish-siddiquis-eyes/articleshow/84472455.cms', 'REAL'),
('P93057', '16-07-2021', 'https://timesofindia.indiatimes.com/india/in-pictures-the-world-through-danish-siddiquis-eyes/articleshow/84472233455.cms', 'FAKE'),
('P9412', '16-07-2021', 'https://timesofindia.indiatimes.com/india//articleshow/84472455.cms', 'REAL'),
('P79903', '16-07-2021', 'https://timesofindia.indiatimes.com/india/in-pictures-the-world-through-danish-siddiquis-eyes/articleshow/84472455.cms', 'REAL'),
('P48423', '16-07-2021', 'https://timesofindia.indiatimes.com/india/in-pictures-the-world-through-danish-siddiquis-eyes/articleshow/8447222455.cms', 'FAKE'),
('P11829', '20-07-2021', 'https://timesofindia.indiatimes.com/home/education/news/bag-in-demand-jobs-with-these-full-stack-programs/articleshow/84430000.cms', 'REAL'),
('P47900', '20-07-2021', 'https://timesofindia.indiatimes.com/home/education/news/bag-in-demand-jobs-with-these-full-stack-programs/articleshow/84430000.cms', 'REAL'),
('P4646', '28-07-2021', 'https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news/raj-kundra-case-live-updates-pornography-shilpa-shetty-sherlyn-chopra-poonam-pandey-gehana-vasisth-hotshots/liveblog/84780648.cms', 'REAL'),
('P83640', '28-07-2021', 'https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news/raj-kundra-case-live-updates-pornography-shilpa-shetty-/liveblog/84780648.cms', 'REAL'),
('P46085', '28-07-2021', 'https://timesofindia.indiatimes.com/entertainment/hindi/bollywood/news/raj-kundra-case-live-updates-pornography-shilpa-shetty-sherlyn-chopra-poonam-pandey-gehana-vasisth-hotshots/liveblog/8478064228.cms', 'FAKE'),
('P36170', '28-07-2021', '', 'FAKE'),
('P12685', '03-08-2021', 'https://timesofindia.indiatimes.com/spotlight/malaika-arora-shares-why-the-frame-tv-from-samsung-is-the-ultimate-addition-to-your-living-space/articleshow/84790333.cms', 'REAL');

-- --------------------------------------------------------

--
-- Table structure for table `tweets`
--

CREATE TABLE `tweets` (
  `email` varchar(255) DEFAULT NULL,
  `tweetss` varchar(255) DEFAULT NULL,
  `ids` int(11) NOT NULL,
  `results` varchar(255) DEFAULT NULL,
  `Dates` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tweets`
--

INSERT INTO `tweets` (`email`, `tweetss`, `ids`, `results`, `Dates`) VALUES
('mithesh1122@gmail.com', 'demo', 34, NULL, '2022-08-18 13:27:48.762141'),
('', 'i will kill all', 35, NULL, '2022-08-18 13:30:32.087153'),
('', 'demo', 36, NULL, '2022-08-18 13:42:19.734668'),
('', 'demo', 37, NULL, '2022-08-18 13:43:03.181277'),
('mithesh1122@gmail.com', 'demo', 38, NULL, '2022-08-18 13:43:42.726882'),
('', 'demo', 39, NULL, '2022-08-18 13:44:31.338384'),
('mithesh1122@gmail.com', 'demo', 40, NULL, '2022-08-18 13:44:56.673828'),
('mithesh1122@gmail.com', 'i will kill', 41, NULL, '2022-08-18 13:45:09.386233'),
('mithesh1122@gmail.com', 'i will commit suicide and write your name', 42, NULL, '2022-08-18 13:46:16.287379'),
('mithesh1122@gmail.com', 'ill murder you\n', 43, NULL, '2022-08-18 13:47:12.664556'),
('mithesh1122@gmail.com', 'you will be killed if you complain to police', 44, NULL, '2022-08-18 13:48:21.182631'),
('mithesh1122@gmail.com', 'your going to be killed', 45, NULL, '2022-08-18 13:48:56.204515'),
('mithesh1122@gmail.com', 'your dead', 46, NULL, '2022-08-18 13:49:15.548859'),
('', 'your going to be killed', 47, NULL, '2023-07-07 21:37:26.538417'),
('', 'your going to be killed', 48, NULL, '2023-07-07 21:38:43.177192'),
('', 'your going to be killed', 49, NULL, '2023-07-07 21:39:34.591129'),
('thejas2@gmail.com', 'kill', 50, NULL, '2023-07-10 21:22:39.318623'),
('thejas2@gmail.com', 'kill', 51, NULL, '2023-07-10 21:23:19.870813'),
('thejas2@gmail.com', 'kill', 52, NULL, '2023-07-10 21:23:40.201482'),
('thejas2@gmail.com', 'kill', 53, NULL, '2023-07-10 21:25:04.256082'),
('thejas2@gmail.com', 'kill', 54, NULL, '2023-07-10 21:41:41.220329'),
('thejas2@gmail.com', 'kill', 55, NULL, '2023-07-10 21:42:30.959676'),
('', 'ddd', 56, NULL, '2023-07-11 21:38:29.426812'),
('', 'test', 57, NULL, '2023-07-11 21:39:58.910056'),
('', '', 58, NULL, '2023-07-11 21:43:16.211773'),
('', '', 59, NULL, '2023-07-11 21:44:13.863831'),
('', '3.jpeg', 60, NULL, '2023-07-11 21:57:09.340880'),
('', '3.jpeg', 61, NULL, '2023-07-11 21:58:08.852035'),
('', '3.jpeg', 62, NULL, '2023-07-11 21:58:51.170882'),
('', '3.jpeg', 63, NULL, '2023-07-11 21:59:39.409595'),
('siddanth@gmail.com', '3.jpeg', 64, NULL, '2023-07-11 22:00:28.183679'),
('', '3.jpeg', 65, NULL, '2023-07-11 22:02:37.267898'),
('siddanth@gmail.com', '3.jpeg', 66, NULL, '2023-07-11 22:03:33.917192'),
('', '3.jpeg', 67, NULL, '2023-07-11 22:04:06.212804'),
('', '3.jpeg', 68, NULL, '2023-07-11 22:05:25.843891'),
('siddanth@gmail.com', '1.jpeg', 69, NULL, '2023-07-11 22:11:52.782461'),
('siddanth@gmail.com', '3.jpeg', 70, NULL, '2023-07-11 22:19:22.697050'),
('siddanth@gmail.com', '5.jpeg', 71, NULL, '2023-07-11 22:22:26.112535'),
('siddanth@gmail.com', '1.jpeg', 72, NULL, '2023-07-11 22:22:35.492092'),
('siddanth@gmail.com', 'istockphoto-1301422911-170667a.jpg', 73, NULL, '2023-07-11 22:22:53.071132'),
('siddanth@gmail.com', 'Armillaria_ostoyae.jpg', 74, NULL, '2023-07-11 22:23:23.750175'),
('', 'istockphoto-1301422911-170667a.jpg', 75, NULL, '2023-07-11 22:26:02.244221'),
('', 'istockphoto-1301422911-170667a.jpg', 76, NULL, '2023-07-11 22:26:45.441983'),
('', 'istockphoto-1301422911-170667a.jpg', 77, NULL, '2023-07-11 22:27:25.624262'),
('siddanth@gmail.com', 'istockphoto-1301422911-170667a.jpg', 78, NULL, '2023-07-11 22:34:29.196444'),
('siddanth@gmail.com', 'istockphoto-1301422911-170667a.jpg', 79, NULL, '2023-07-11 22:35:33.826006'),
('tarun@gmail.com', 'istockphoto-1301422911-170667a.jpg', 80, NULL, '2023-07-11 22:37:58.504209'),
('tarun@gmail.com', '4.jpeg', 81, NULL, '2023-07-11 22:39:35.668271'),
('tarun@gmail.com', 'hgutuy', 82, NULL, '2023-07-11 22:39:43.921108'),
('tarun@gmail.com', 'kill', 83, NULL, '2023-07-11 22:40:19.549497'),
('tarun@gmail.com', 'hgutuy', 84, NULL, '2023-07-11 22:40:26.383677'),
('tarun@gmail.com', 'i will kill you', 85, NULL, '2023-07-11 22:40:53.873769');

-- --------------------------------------------------------

--
-- Table structure for table `userdata`
--

CREATE TABLE `userdata` (
  `Uid` varchar(50) NOT NULL,
  `Uname` varchar(80) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Pswd` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `Phone` varchar(50) NOT NULL,
  `Addr` varchar(500) NOT NULL,
  `Bullycount` int(11) NOT NULL,
  `Stat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `userdata`
--

INSERT INTO `userdata` (`Uid`, `Uname`, `Name`, `Pswd`, `Email`, `Phone`, `Addr`, `Bullycount`, `Stat`) VALUES
('User10565', 'mithesh', 'mithesh', 'mithes@1', 'mithesh1122@gmail.com', '9148599960', 'mysore', 6, 'Suspended'),
('User55741', 'dhyan', 'dhyan', 'dhyan01', 'dhyanchinnappa06@gmail.com', '8073939278', 'mysore', 0, 'Active'),
('User71361', 'Tarun', 'Nnnnnn', 'qazwsx', 'tarun@gmail.com', '9844921346', 'aedqefrw', 3, 'Active'),
('User86258', 'Siddanth1', 'Siddanth', '123456', 'siddanth@gmail.com', '9448059770', '24', 5, 'Suspended'),
('User66581', 'tejas2', 'thejas', '12345', 'thejas2@gmail.com', '9448059770', 'aeew', 6, 'Suspended');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tweets`
--
ALTER TABLE `tweets`
  ADD PRIMARY KEY (`ids`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tweets`
--
ALTER TABLE `tweets`
  MODIFY `ids` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
