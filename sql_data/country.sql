/*
 Navicat Premium Data Transfer

 Source Server         : 123.57.238.105
 Source Server Type    : MySQL
 Source Server Version : 80031 (8.0.31)
 Source Host           : 123.57.238.105:3306
 Source Schema         : fengchuanxt

 Target Server Type    : MySQL
 Target Server Version : 80031 (8.0.31)
 File Encoding         : 65001

 Date: 16/12/2022 23:28:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for country
-- ----------------------------
DROP TABLE IF EXISTS `country`;
CREATE TABLE `country`  (
  `country_id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `country_code2` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `country_code3` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `currency_code` varchar(8) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `currency_symbol` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `name_en` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `name_cn` varchar(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `continent` enum('Europe','North America','South America','Asia','Oceania','Africa','Other') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `smt_code` char(3) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `is_hot` enum('Y','N') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT 'N',
  PRIMARY KEY (`country_id`) USING BTREE,
  INDEX `ix_country_country_code2`(`country_code2` ASC) USING BTREE,
  INDEX `ix_country_country_code3`(`country_code3` ASC) USING BTREE,
  INDEX `ix_country_currency_code`(`currency_code` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 277 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of country
-- ----------------------------
INSERT INTO `country` VALUES (1, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'AX', 'ALA', 'EUR', '???', 'ALAND ISLAND', '????????????', 'Europe', 'AX', 'N');
INSERT INTO `country` VALUES (3, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'AD', 'AND', 'EUR', '???', 'ANDORRA', '?????????', 'Europe', 'AD', 'N');
INSERT INTO `country` VALUES (4, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'AT', 'AUT', 'EUR', '???', 'AUSTRIA', '?????????', 'Europe', 'AT', 'N');
INSERT INTO `country` VALUES (5, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BY', 'BLR', 'BYN', 'Br', 'BELARUS', '????????????', 'Europe', 'BY', 'Y');
INSERT INTO `country` VALUES (6, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BE', 'BEL', 'EUR', '???', 'BELGIUM', '?????????', 'Europe', 'BE', 'Y');
INSERT INTO `country` VALUES (7, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BA', 'BIH', 'BAM', NULL, 'BOSNIA AND HERZEGOVINA', '????????????-????????????????????????????????????', 'Europe', 'BA', 'N');
INSERT INTO `country` VALUES (8, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BG', 'BGR', 'BGN', '????', 'BULGARIA', '????????????', 'Europe', 'BG', 'N');
INSERT INTO `country` VALUES (9, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BQ', 'BES', 'USD', '$', 'Caribbean Netherlands', '??????????????????', 'Europe', 'BQ', 'N');
INSERT INTO `country` VALUES (10, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'HR', 'HRV', 'HRK', 'kn', 'CROATIA', '????????????', 'Europe', 'HR', 'N');
INSERT INTO `country` VALUES (11, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'CY', 'CYP', 'EUR', '???', 'CYPRUS', '????????????', 'Europe', 'CY', 'N');
INSERT INTO `country` VALUES (12, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'CZ', 'CZE', 'CZK', 'K??', 'CZECH REPUBLIC', '???????????????', 'Europe', 'CZ', 'Y');
INSERT INTO `country` VALUES (13, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'DK', 'DNK', 'DKK', 'kr', 'DENMARK', '??????', 'Europe', 'DK', 'Y');
INSERT INTO `country` VALUES (14, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'EE', 'EST', 'EUR', '???', 'ESTONIA', '????????????', 'Europe', 'EE', 'N');
INSERT INTO `country` VALUES (15, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'FO', 'FRO', 'DKK', 'kr', 'FAROE ISLANDS', '????????????', 'Europe', 'FO', 'N');
INSERT INTO `country` VALUES (16, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'FI', 'FIN', 'EUR', '???', 'FINLAND', '??????', 'Europe', 'FI', 'Y');
INSERT INTO `country` VALUES (17, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'FR', 'FRA', 'EUR', '???', 'FRANCE', '??????', 'Europe', 'FR', 'Y');
INSERT INTO `country` VALUES (18, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'TF', 'ATF', 'EUR', '???', 'FRENCH SOUTHERN TERRITORIES', '??????????????????', 'Europe', 'TF', 'N');
INSERT INTO `country` VALUES (19, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'DE', 'DEU', 'EUR', '???', 'GERMANY', '??????', 'Europe', 'DE', 'Y');
INSERT INTO `country` VALUES (20, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'GI', 'GIB', 'GIP', '??', 'GIBRALTAR', '????????????', 'Europe', 'GI', 'N');
INSERT INTO `country` VALUES (21, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'GR', 'GRC', 'EUR', '???', 'GREECE', '??????', 'Europe', 'GR', 'N');
INSERT INTO `country` VALUES (22, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'GG', 'GGY', 'GBP', '??', 'GUERNSEY', '?????????', 'Europe', 'GGY', 'N');
INSERT INTO `country` VALUES (23, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'HU', 'HUN', 'HUF', 'Ft', 'HUNGARY', '?????????', 'Europe', 'HU', 'N');
INSERT INTO `country` VALUES (24, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'IS', 'ISL', 'ISK', 'kr', 'ICELAND', '??????', 'Europe', 'IS', 'N');
INSERT INTO `country` VALUES (25, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'IE', 'IRL', 'EUR', '???', 'IRELAND', '?????????', 'Europe', 'IE', 'N');
INSERT INTO `country` VALUES (26, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'IM', 'IMN', 'GBP', '??', 'Isle of Man', '?????????', 'Europe', 'IM', 'N');
INSERT INTO `country` VALUES (27, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'IT', 'ITA', 'EUR', '???', 'ITALY', '?????????', 'Europe', 'IT', 'Y');
INSERT INTO `country` VALUES (28, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'JE', 'JEY', 'GBP', '??', 'JERSEY', '?????????(??????)', 'Europe', 'JEY', 'N');
INSERT INTO `country` VALUES (29, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'LV', 'LVA', 'EUR', '???', 'LATVIA', '????????????', 'Europe', 'LV', 'N');
INSERT INTO `country` VALUES (30, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'LI', 'LIE', 'CHF', 'Fr', 'LIECHTENSTEIN', '???????????????', 'Europe', 'LI', 'N');
INSERT INTO `country` VALUES (31, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'LT', 'LTU', 'EUR', '???', 'LITHUANIA', '?????????', 'Europe', 'LT', 'N');
INSERT INTO `country` VALUES (32, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'LU', 'LUX', 'EUR', '???', 'LUXEMBOURG', '?????????', 'Europe', 'LU', 'N');
INSERT INTO `country` VALUES (33, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MK', 'MKD', 'MKD', 'den', 'MACEDONIA', '?????????', 'Europe', 'MK', 'N');
INSERT INTO `country` VALUES (34, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MT', 'MLT', 'EUR', '???', 'MALTA', '?????????', 'Europe', 'MT', 'N');
INSERT INTO `country` VALUES (35, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MD', 'MDA', 'MDL', 'L', 'MOLDOVA', '????????????', 'Europe', 'MD', 'N');
INSERT INTO `country` VALUES (36, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MC', 'MCO', 'EUR', '???', 'MONACO', '?????????', 'Europe', 'MC', 'N');
INSERT INTO `country` VALUES (37, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'ME', 'MNE', 'EUR', '???', 'MONTENEGRO', '???????????????', 'Europe', 'MNE', 'N');
INSERT INTO `country` VALUES (38, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'NL', 'NLD', 'EUR', '???', 'NETHERLANDS', '??????', 'Europe', 'NL', 'Y');
INSERT INTO `country` VALUES (39, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MK', 'MKD', 'MKD', 'den', 'NORTH MACEDONIA', '????????????', 'Europe', 'MK', 'N');
INSERT INTO `country` VALUES (40, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'NO', 'NOR', 'NOK', 'kr', 'NORWAY', '??????', 'Europe', 'NO', 'Y');
INSERT INTO `country` VALUES (41, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'PS', 'PSE', 'EGP', 'E??', 'Palestinian territories', '????????????', 'Europe', 'PS', 'N');
INSERT INTO `country` VALUES (42, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'PL', 'POL', 'PLN', 'z??', 'POLAND', '??????', 'Europe', 'PL', 'Y');
INSERT INTO `country` VALUES (43, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'PT', 'PRT', 'EUR', '???', 'PORTUGAL', '?????????', 'Europe', 'PT', 'N');
INSERT INTO `country` VALUES (44, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'RO', 'ROU', 'RON', 'lei', 'ROMANIA', '????????????', 'Europe', 'RO', 'N');
INSERT INTO `country` VALUES (45, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'RU', 'RUS', 'RUB', '???', 'RUSSIA', '?????????', 'Europe', 'RU', 'Y');
INSERT INTO `country` VALUES (46, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'MF', 'MAF', 'EUR', '???', 'SAINT MARTIN (FRENCH PART)', '???????????????', 'Europe', 'MF', 'N');
INSERT INTO `country` VALUES (47, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'SM', 'SMR', 'EUR', '???', 'SAN MARINO', '????????????', 'Europe', 'SM', 'N');
INSERT INTO `country` VALUES (48, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'RS', 'SRB', 'RSD', '??????.', 'SERBIA, REPUBLIC OF', '?????????????????????', 'Europe', 'SRB', 'N');
INSERT INTO `country` VALUES (49, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'SL', 'SLE', 'SLL', 'Le', 'SIERRA LEONE', '????????????', 'Europe', 'SL', 'N');
INSERT INTO `country` VALUES (50, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'SK', 'SVK', 'EUR', '???', 'SLOVAKIA REPUBLIC', '?????????????????????', 'Europe', 'SK', 'N');
INSERT INTO `country` VALUES (51, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'SI', 'SVN', 'EUR', '???', 'SLOVENIA', '???????????????', 'Europe', 'SI', 'N');
INSERT INTO `country` VALUES (52, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'GS', 'SGS', 'SHP', '??', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISL', '????????????????????????????????????', 'Europe', 'SGS', 'N');
INSERT INTO `country` VALUES (53, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'ES', 'ESP', 'EUR', '???', 'SPAIN', '?????????', 'Europe', 'ES', 'Y');
INSERT INTO `country` VALUES (54, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'SJ', 'SJM', 'NOK', 'kr', 'SVALBARD AND JAN MAYEN', '??????????????????????????????', 'Europe', 'SJ', 'N');
INSERT INTO `country` VALUES (55, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'SE', 'SWE', 'SEK', 'kr', 'SWEDEN', '??????', 'Europe', 'SE', 'Y');
INSERT INTO `country` VALUES (56, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'CH', 'CHE', 'CHF', 'Fr.', 'SWITZERLAND', '??????', 'Europe', 'CH', 'Y');
INSERT INTO `country` VALUES (57, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'UA', 'UKR', 'UAH', '???', 'UKRAINE', '?????????', 'Europe', 'UA', 'Y');
INSERT INTO `country` VALUES (58, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GB', 'GBR', 'GBP', '??', 'UNITED KINGDOM', '??????', 'Europe', 'UK', 'Y');
INSERT INTO `country` VALUES (59, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'VA', 'VAT', 'EUR', '???', 'VATICAN CITY', '?????????', 'Europe', 'VA', 'N');
INSERT INTO `country` VALUES (60, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'AI', 'AIA', 'XCD', '$', 'ANGUILLA', '????????????', 'North America', 'AI', 'N');
INSERT INTO `country` VALUES (61, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'AG', 'ATG', 'XCD', '$', 'ANTIGUA AND BARBUDA', '?????????????????????', 'North America', 'AG', 'N');
INSERT INTO `country` VALUES (62, '2022-12-15 02:55:55', '2022-12-15 02:55:55', 'AA', '', NULL, NULL, 'APO/FPO', 'APO/FPO', 'North America', 'AA', 'N');
INSERT INTO `country` VALUES (63, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'AW', 'ABW', 'AWG', '??', 'ARUBA', '????????????', 'North America', 'AW', 'N');
INSERT INTO `country` VALUES (64, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'BS', 'BHS', 'BSD', '$', 'BAHAMAS', '?????????', 'North America', 'BS', 'N');
INSERT INTO `country` VALUES (65, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'BB', 'BRB', 'BBD', '$', 'BARBADOS', '????????????', 'North America', 'BB', 'N');
INSERT INTO `country` VALUES (66, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'BZ', 'BLZ', 'BZD', '$', 'BELIZE', '?????????', 'North America', 'BZ', 'N');
INSERT INTO `country` VALUES (67, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'BM', 'BMU', 'BMD', '$', 'BERMUDA', '?????????', 'North America', 'BM', 'N');
INSERT INTO `country` VALUES (68, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'CA', 'CAN', 'CAD', '$', 'CANADA', '?????????', 'North America', 'CA', 'Y');
INSERT INTO `country` VALUES (69, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'KY', 'CYM', 'KYD', '$', 'CAYMAN ISLANDS', '????????????', 'North America', 'KY', 'N');
INSERT INTO `country` VALUES (70, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'CR', 'CRI', 'CRC', '???', 'COSTA RICA', '???????????????', 'North America', 'CR', 'N');
INSERT INTO `country` VALUES (71, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'CU', 'CUB', 'CUC', '$', 'CUBA', '??????', 'North America', 'CU', 'N');
INSERT INTO `country` VALUES (72, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'DM', 'DMA', 'XCD', '$', 'DOMINICA', '????????????', 'North America', 'DM', 'N');
INSERT INTO `country` VALUES (73, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'DO', 'DOM', 'DOP', '$', 'DOMINICAN REPUBLIC', '?????????????????????', 'North America', 'DO', 'N');
INSERT INTO `country` VALUES (74, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'SV', 'SLV', 'USD', '$', 'EL SALVADOR', '????????????', 'North America', 'SV', 'N');
INSERT INTO `country` VALUES (75, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GL', 'GRL', 'DKK', 'kr.', 'GREENLAND', '?????????', 'North America', 'GL', 'N');
INSERT INTO `country` VALUES (76, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GD', 'GRD', 'XCD', '$', 'GRENADA', '????????????', 'North America', 'GD', 'N');
INSERT INTO `country` VALUES (77, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GP', 'GLP', 'EUR', '???', 'GUADELOUPE', '????????????', 'North America', 'GP', 'N');
INSERT INTO `country` VALUES (78, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GT', 'GTM', 'GTQ', 'Q', 'GUATEMALA', '????????????', 'North America', 'GT', 'N');
INSERT INTO `country` VALUES (79, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'HT', 'HTI', 'HTG', 'G', 'HAITI', '??????', 'North America', 'HT', 'N');
INSERT INTO `country` VALUES (80, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'HN', 'HND', 'HNL', 'L', 'HONDURAS', '????????????', 'North America', 'HN', 'N');
INSERT INTO `country` VALUES (81, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'JM', 'JAM', 'JMD', '$', 'JAMAICA', '?????????', 'North America', 'JM', 'N');
INSERT INTO `country` VALUES (82, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'MQ', 'MTQ', 'EUR', '???', 'MARTINIQUE', '???????????????', 'North America', 'MQ', 'N');
INSERT INTO `country` VALUES (83, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'MX', 'MEX', 'MXN', '$', 'MEXICO', '?????????', 'North America', 'MX', 'Y');
INSERT INTO `country` VALUES (84, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'MS', 'MSR', 'XCD', '$', 'MONTSERRAT', '???????????????', 'North America', 'MS', 'N');
INSERT INTO `country` VALUES (85, '2022-12-15 02:55:56', '2022-12-15 02:55:56', 'AN', '', NULL, NULL, 'NETHERLANDS ANTILLES', '????????????????????????', 'North America', 'AN', 'N');
INSERT INTO `country` VALUES (86, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'NI', 'NIC', 'NIO', 'C$', 'NICARAGUA', '????????????', 'North America', 'NI', 'N');
INSERT INTO `country` VALUES (87, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'PA', 'PAN', 'PAB', 'B/.', 'PANAMA', '?????????', 'North America', 'PA', 'N');
INSERT INTO `country` VALUES (88, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'PR', 'PRI', 'USD', '$', 'PUERTO RICO', '????????????', 'North America', 'PR', 'Y');
INSERT INTO `country` VALUES (89, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'KN', 'KNA', 'XCD', '$', 'SAINT KITTS ', '?????????', 'North America', 'KN', 'N');
INSERT INTO `country` VALUES (90, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'PM', 'SPM', 'EUR', '???', 'SAINT PIERRE AND MIQUELON', '??????????????????????????????', 'North America', 'PM', 'N');
INSERT INTO `country` VALUES (91, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'VC', 'VCT', 'XCD', '$', 'SAINT VINCENT AND THE GRENADINES', '?????????????????????????????????', 'North America', 'VC', 'N');
INSERT INTO `country` VALUES (92, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'LC', 'LCA', 'XCD', '$', 'ST. LUCIA', '????????????', 'North America', 'LC', 'N');
INSERT INTO `country` VALUES (93, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'TT', 'TTO', 'TTD', '$', 'TRINIDAD AND TOBAGO', '????????????????????????', 'North America', 'TT', 'N');
INSERT INTO `country` VALUES (94, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'TC', 'TCA', 'USD', '$', 'TURKS AND CAICOS ISLANDS', '???????????????????????????', 'North America', 'TC', 'N');
INSERT INTO `country` VALUES (95, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'US', 'USA', 'USD', '$', 'UNITED STATES', '??????', 'North America', 'US', 'Y');
INSERT INTO `country` VALUES (96, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'UM', 'UMI', 'USD', '$', 'UNITED STATES MINOR OUTLYING ISLANDS', '????????????????????????', 'North America', 'UM', 'N');
INSERT INTO `country` VALUES (97, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'VG', 'VGB', 'USD', '$', 'VIRGIN ISLAND (GB)', '?????????????????????', 'North America', 'VG', 'N');
INSERT INTO `country` VALUES (98, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'VI', 'VIR', 'USD', '$', 'VIRGIN ISLAND (US)', '?????????????????????', 'North America', 'VI', 'N');
INSERT INTO `country` VALUES (99, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'AR', 'ARG', 'ARS', '$', 'ARGENTINA', '?????????', 'South America', 'AR', 'N');
INSERT INTO `country` VALUES (100, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BO', 'BOL', 'BOB', 'Bs.', 'BOLIVIA', '????????????', 'South America', 'BO', 'N');
INSERT INTO `country` VALUES (101, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BR', 'BRA', 'BRL', 'R$', 'BRAZIL', '??????', 'South America', 'BR', 'Y');
INSERT INTO `country` VALUES (102, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'CL', 'CHL', 'CLP', '$', 'CHILE', '??????', 'South America', 'CL', 'Y');
INSERT INTO `country` VALUES (103, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'CO', 'COL', 'COP', '$', 'COLOMBIA', '????????????', 'South America', 'CO', 'N');
INSERT INTO `country` VALUES (104, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'EC', 'ECU', 'USD', '$', 'ECUADOR', '????????????', 'South America', 'EC', 'N');
INSERT INTO `country` VALUES (105, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'FK', 'FLK', 'FKP', '??', 'FALKLAND ISLAND', '???????????????', 'South America', 'FK', 'N');
INSERT INTO `country` VALUES (106, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'GF', 'GUF', 'EUR', '???', 'FRENCH GUIANA', '???????????????', 'South America', 'GF', 'N');
INSERT INTO `country` VALUES (107, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'GY', 'GUY', 'GYD', '$', 'GUYANA (BRITISH)', '?????????', 'South America', 'GY', 'N');
INSERT INTO `country` VALUES (108, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'PY', 'PRY', 'PYG', '???', 'PARAGUAY', '?????????', 'South America', 'PY', 'N');
INSERT INTO `country` VALUES (109, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'PE', 'PER', 'PEN', 'S/ ', 'PERU', '??????', 'South America', 'PE', 'N');
INSERT INTO `country` VALUES (110, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'SR', 'SUR', 'SRD', '$', 'SURINAME', '?????????', 'South America', 'SR', 'N');
INSERT INTO `country` VALUES (111, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'UY', 'URY', 'UYU', '$', 'URUGUAY', '?????????', 'South America', 'UY', 'N');
INSERT INTO `country` VALUES (112, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'VE', 'VEN', 'VES', 'Bs.S', 'VENEZUELA', '????????????', 'South America', 'VE', 'N');
INSERT INTO `country` VALUES (113, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'HK', 'HKG', 'HKD', '$', '(China)HONG KONG', '????????????', 'Asia', 'HK', 'N');
INSERT INTO `country` VALUES (114, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'MO', 'MAC', 'MOP', 'P', '(China)MACAU', '????????????', 'Asia', 'MO', 'N');
INSERT INTO `country` VALUES (115, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'TW', 'TWN', 'TWD', '$', '(China)TAIWAN', '????????????', 'Asia', 'TW', 'N');
INSERT INTO `country` VALUES (116, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'AF', 'AFG', 'AFN', '??', 'AFGHANISTAN', '?????????', 'Asia', 'AF', 'N');
INSERT INTO `country` VALUES (117, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'AM', 'ARM', 'AMD', '??', 'ARMENIA', '????????????', 'Asia', 'AM', 'N');
INSERT INTO `country` VALUES (118, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'AZ', 'AZE', 'AZN', '???', 'AZERBAIJAN', '????????????(?????????)', 'Asia', 'AZ', 'N');
INSERT INTO `country` VALUES (119, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BH', 'BHR', 'BHD', '.??.??', 'BAHRAIN', '??????', 'Asia', 'BH', 'N');
INSERT INTO `country` VALUES (120, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BD', 'BGD', 'BDT', '???', 'BANGLADESH', '????????????', 'Asia', 'BD', 'N');
INSERT INTO `country` VALUES (121, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BT', 'BTN', 'BTN', 'Nu.', 'BHUTAN', '??????', 'Asia', 'BT', 'N');
INSERT INTO `country` VALUES (122, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BN', 'BRN', 'BND', '$', 'BRUNEI', '??????', 'Asia', 'BN', 'N');
INSERT INTO `country` VALUES (123, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'KH', 'KHM', 'KHR', '???', 'CAMBODIA', '?????????', 'Asia', 'KH', 'N');
INSERT INTO `country` VALUES (124, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'CN', 'CHN', 'CNY', '??', 'CHINA', '??????', 'Asia', 'CN', 'N');
INSERT INTO `country` VALUES (127, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'TL', 'TLS', 'USD', '$', 'EAST TIMOR', '?????????', 'Asia', 'TLS', 'N');
INSERT INTO `country` VALUES (128, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'GE', 'GEO', 'GEL', '???', 'GEORGIA', '????????????', 'Asia', 'GE', 'N');
INSERT INTO `country` VALUES (129, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'IN', 'IND', 'INR', '???', 'INDIA', '??????', 'Asia', 'IN', 'N');
INSERT INTO `country` VALUES (130, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'ID', 'IDN', 'IDR', 'Rp', 'INDONESIA', '???????????????', 'Asia', 'ID', 'N');
INSERT INTO `country` VALUES (131, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'IR', 'IRN', 'IRR', '???', 'IRAN (ISLAMIC REPUBLIC OF)', '??????', 'Asia', 'IR', 'N');
INSERT INTO `country` VALUES (132, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'IQ', 'IRQ', 'IQD', '??.??', 'IRAQ', '?????????', 'Asia', 'IQ', 'N');
INSERT INTO `country` VALUES (133, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'IL', 'ISR', 'ILS', '???', 'ISRAEL', '?????????', 'Asia', 'IL', 'Y');
INSERT INTO `country` VALUES (134, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'JP', 'JPN', 'JPY', '??', 'JAPAN', '??????', 'Asia', 'JP', 'Y');
INSERT INTO `country` VALUES (135, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'JO', 'JOR', 'JOD', '??.??', 'JORDAN', '??????', 'Asia', 'JO', 'N');
INSERT INTO `country` VALUES (136, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'KZ', 'KAZ', 'KZT', '???', 'KAZAKHSTAN', '???????????????', 'Asia', 'KZ', 'N');
INSERT INTO `country` VALUES (137, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'KW', 'KWT', 'KWD', '??.??', 'KUWAIT', '?????????', 'Asia', 'KW', 'N');
INSERT INTO `country` VALUES (138, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'KG', 'KGZ', 'KGS', '??', 'KYRGYZSTAN', '??????????????????', 'Asia', 'KG', 'N');
INSERT INTO `country` VALUES (139, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'LA', 'LAO', 'LAK', '???', 'LAOS', '??????', 'Asia', 'LA', 'N');
INSERT INTO `country` VALUES (140, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'LB', 'LBN', 'LBP', '??.??', 'LEBANON', '?????????', 'Asia', 'LB', 'N');
INSERT INTO `country` VALUES (141, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'MY', 'MYS', 'MYR', 'RM', 'MALAYSIA', '????????????', 'Asia', 'MY', 'N');
INSERT INTO `country` VALUES (142, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'MV', 'MDV', 'MVR', '.??', 'MALDIVES', '????????????', 'Asia', 'MV', 'N');
INSERT INTO `country` VALUES (143, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'MN', 'MNG', 'MNT', '???', 'MONGOLIA', '??????', 'Asia', 'MN', 'N');
INSERT INTO `country` VALUES (144, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'MM', 'MMR', 'MMK', 'Ks', 'MYANMAR', '??????', 'Asia', 'MM', 'N');
INSERT INTO `country` VALUES (145, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'NP', 'NPL', 'NPR', '???', 'NEPAL', '?????????', 'Asia', 'NP', 'N');
INSERT INTO `country` VALUES (146, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'KP', 'PRK', 'KPW', '???', 'NORTH KOREA', '??????', 'Asia', 'KP', 'N');
INSERT INTO `country` VALUES (147, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'OM', 'OMN', 'OMR', '??.??.', 'OMAN', '??????', 'Asia', 'OM', 'N');
INSERT INTO `country` VALUES (148, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'PK', 'PAK', 'PKR', '???', 'PAKISTAN', '????????????', 'Asia', 'PK', 'N');
INSERT INTO `country` VALUES (149, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'PH', 'PHL', 'PHP', '???', 'PHILIPPINES', '?????????', 'Asia', 'PH', 'Y');
INSERT INTO `country` VALUES (150, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'QA', 'QAT', 'QAR', '??.??', 'QATAR', '?????????', 'Asia', 'QA', 'N');
INSERT INTO `country` VALUES (151, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'SA', 'SAU', 'SAR', '??.??', 'SAUDI ARABIA', '???????????????', 'Asia', 'SA', 'N');
INSERT INTO `country` VALUES (152, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'SG', 'SGP', 'SGD', '$', 'SINGAPORE', '?????????', 'Asia', 'SG', 'N');
INSERT INTO `country` VALUES (153, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'KR', 'KOR', 'KRW', '???', 'SOUTH KOREA', '??????', 'Asia', 'KR', 'N');
INSERT INTO `country` VALUES (154, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'LK', 'LKA', 'LKR', 'Rs  ', 'SRI LANKA', '????????????', 'Asia', 'LK', 'N');
INSERT INTO `country` VALUES (156, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'SY', 'SYR', 'SYP', '??', 'SYRIA', '?????????', 'Asia', 'SY', 'N');
INSERT INTO `country` VALUES (157, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'TJ', 'TJK', 'TJS', '????', 'TAJIKISTAN', '???????????????', 'Asia', 'TJ', 'N');
INSERT INTO `country` VALUES (158, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'TH', 'THA', 'THB', '???', 'THAILAND', '??????', 'Asia', 'TH', 'N');
INSERT INTO `country` VALUES (159, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'TR', 'TUR', 'TRY', '???', 'TURKEY', '?????????', 'Asia', 'TR', 'Y');
INSERT INTO `country` VALUES (160, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'TM', 'TKM', 'TMT', 'm', 'TURKMENISTAN', '???????????????', 'Asia', 'TM', 'N');
INSERT INTO `country` VALUES (161, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'AE', 'ARE', 'AED', '??.??', 'UNITED ARAB EMIRATES', '????????????????????????', 'Asia', 'AE', 'N');
INSERT INTO `country` VALUES (162, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'UZ', 'UZB', 'UZS', 'so\'m', 'UZBEKISTAN', '??????????????????', 'Asia', 'UZ', 'N');
INSERT INTO `country` VALUES (163, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'VN', 'VNM', 'VND', '???', 'VIETNAM', '??????', 'Asia', 'VN', 'N');
INSERT INTO `country` VALUES (164, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'YE', 'YEM', 'YER', '???', 'YEMEN, REPUBLIC OF', '????????????????????????', 'Asia', 'YE', 'N');
INSERT INTO `country` VALUES (165, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'AS', 'ASM', 'USD', '$', 'AMERICAN SAMOA', '?????????????????????', 'Oceania', 'AS', 'N');
INSERT INTO `country` VALUES (166, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'AU', 'AUS', 'AUD', '$', 'AUSTRALIA', '????????????', 'Oceania', 'AU', 'Y');
INSERT INTO `country` VALUES (167, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'CX', 'CXR', 'AUD', '$', 'CHRISTMAS ISLAND', '?????????', 'Oceania', 'CX', 'N');
INSERT INTO `country` VALUES (168, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'CC', 'CCK', 'AUD', '$', 'COCOS(KEELING)ISLANDS', '???????????????', 'Oceania', 'CC', 'N');
INSERT INTO `country` VALUES (169, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'CK', 'COK', 'CKD', '$', 'COOK ISLANDS', '????????????', 'Oceania', 'CK', 'N');
INSERT INTO `country` VALUES (170, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'FJ', 'FJI', 'FJD', '$', 'FIJI', '??????', 'Oceania', 'FJ', 'N');
INSERT INTO `country` VALUES (171, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'PF', 'PYF', 'XPF', '???', 'FRENCH POLYNESIA', '????????????(?????????????????????)', 'Oceania', 'PF', 'N');
INSERT INTO `country` VALUES (172, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'GU', 'GUM', 'USD', '$', 'GUAM', '??????', 'Oceania', 'GU', 'N');
INSERT INTO `country` VALUES (173, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'KI', 'KIR', 'AUD', '$', 'KIRIBATI REPUBILC', '?????????????????????', 'Oceania', 'KI', 'N');
INSERT INTO `country` VALUES (174, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'MH', 'MHL', 'USD', '$', 'MARSHALL ISLANDS', '???????????????', 'Oceania', 'MH', 'N');
INSERT INTO `country` VALUES (175, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'FM', 'FSM', 'USD', '$', 'MICRONESIA', '??????????????????', 'Oceania', 'FM', 'N');
INSERT INTO `country` VALUES (176, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'NC', 'NCL', 'XPF', '???', 'NEW CALEDONIA', '??????????????????', 'Oceania', 'NC', 'N');
INSERT INTO `country` VALUES (177, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'NZ', 'NZL', 'NZD', '$', 'NEW ZEALAND', '?????????', 'Oceania', 'NZ', 'N');
INSERT INTO `country` VALUES (178, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'NU', 'NIU', 'NZD', '$', 'NIUE', '?????????', 'Oceania', 'NU', 'N');
INSERT INTO `country` VALUES (179, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'NF', 'NFK', 'AUD', '$', 'NORFOLK ISLAND', '????????????', 'Oceania', 'NF', 'N');
INSERT INTO `country` VALUES (180, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'PW', 'PLW', 'USD', '$', 'PALAU', '??????', 'Oceania', 'PW', 'N');
INSERT INTO `country` VALUES (181, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'PG', 'PNG', 'PGK', 'K', 'PAPUA NEW GUINEA', '?????????????????????', 'Oceania', 'PG', 'N');
INSERT INTO `country` VALUES (182, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'PN', 'PCN', 'NZD', '$', 'PITCAIRN ISLANDS', '??????????????????', 'Oceania', 'PN', 'N');
INSERT INTO `country` VALUES (183, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'MP', 'MNP', 'USD', '$', 'SAIPAN', '?????????', 'Oceania', 'MP', 'N');
INSERT INTO `country` VALUES (184, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'SB', 'SLB', 'SBD', '$', 'SOLOMON ISLANDS', '???????????????', 'Oceania', 'SB', 'N');
INSERT INTO `country` VALUES (185, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'TK', 'TKL', 'NZD', '$', 'TOKELAU', '?????????', 'Oceania', 'TK', 'N');
INSERT INTO `country` VALUES (186, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'TO', 'TON', 'TOP', 'T$', 'TONGA', '??????', 'Oceania', 'TO', 'N');
INSERT INTO `country` VALUES (187, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'TV', 'TUV', 'AUD', '$', 'TUVALU', '?????????', 'Oceania', 'TV', 'N');
INSERT INTO `country` VALUES (188, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'VU', 'VUT', 'VUV', 'Vt', 'VANUATU', '????????????', 'Oceania', 'VU', 'N');
INSERT INTO `country` VALUES (189, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'WF', 'WLF', 'XPF', '???', 'WALLIS AND FUTUNA ISLANDS', '?????????????????????????????????', 'Oceania', 'WF', 'N');
INSERT INTO `country` VALUES (190, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'WS', 'WSM', 'WST', 'T', 'WESTERN SAMOA', '????????????', 'Oceania', 'WS', 'N');
INSERT INTO `country` VALUES (191, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'DZ', 'DZA', 'DZD', '??.??', 'ALGERIA', '???????????????', 'Africa', 'DZ', 'N');
INSERT INTO `country` VALUES (192, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'AO', 'AGO', 'AOA', 'Kz', 'ANGOLA', '?????????', 'Africa', 'AO', 'N');
INSERT INTO `country` VALUES (193, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'BJ', 'BEN', 'XOF', 'Fr', 'BENIN', '??????', 'Africa', 'BJ', 'N');
INSERT INTO `country` VALUES (194, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'BW', 'BWA', 'BWP', 'P', 'BOTSWANA', '????????????', 'Africa', 'BW', 'N');
INSERT INTO `country` VALUES (195, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'IO', 'IOT', 'USD', '$', 'BRITISH INDIAN OCEAN TERRITORY', '?????????????????????(????????????)', 'Africa', 'IO', 'N');
INSERT INTO `country` VALUES (196, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'BF', 'BFA', 'XOF', 'Fr', 'BURKINA FASO', '???????????????', 'Africa', 'BF', 'N');
INSERT INTO `country` VALUES (197, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'BI', 'BDI', 'BIF', 'Fr', 'BURUNDI', '?????????', 'Africa', 'BI', 'N');
INSERT INTO `country` VALUES (198, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CM', 'CMR', 'XAF', 'Fr', 'CAMEROON', '?????????', 'Africa', 'CM', 'N');
INSERT INTO `country` VALUES (199, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CV', 'CPV', 'CVE', 'Esc', 'CAPE VERDE', '???????????????', 'Africa', 'CV', 'N');
INSERT INTO `country` VALUES (200, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CF', 'CAF', 'XAF', 'Fr', 'CENTRAL REPUBLIC', '???????????????', 'Africa', 'CF', 'N');
INSERT INTO `country` VALUES (201, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'TD', 'TCD', 'XAF', 'Fr', 'CHAD', '??????', 'Africa', 'TD', 'N');
INSERT INTO `country` VALUES (202, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'KM', 'COM', 'KMF', 'Fr', 'COMOROS', '?????????', 'Africa', 'KM', 'N');
INSERT INTO `country` VALUES (203, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CG', 'COG', 'XAF', 'Fr', 'CONGO', '??????', 'Africa', 'CG', 'N');
INSERT INTO `country` VALUES (204, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CD', 'COD', 'CDF', 'FC', 'CONGO REPUBLIC ', '?????????????????????', 'Africa', 'CD', 'N');
INSERT INTO `country` VALUES (205, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CI', 'CIV', 'XOF', 'Fr', 'COTE D\'LVOIRE(IVORY)', '????????????(????????????) ', 'Africa', 'CI', 'N');
INSERT INTO `country` VALUES (206, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'DJ', 'DJI', 'DJF', 'Fr', 'DJIBOUTI', '?????????', 'Africa', 'DJ', 'N');
INSERT INTO `country` VALUES (207, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'EG', 'EGY', 'EGP', '??', 'EGYPT', '??????', 'Africa', 'EG', 'N');
INSERT INTO `country` VALUES (208, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GQ', 'GNQ', 'XAF', 'Fr', 'EQUATORIAL GUINEA ', '???????????????', 'Africa', 'GQ', 'N');
INSERT INTO `country` VALUES (209, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'ER', 'ERI', 'ERN', 'Nfk', 'ERITREA', '???????????????', 'Africa', 'ER', 'N');
INSERT INTO `country` VALUES (210, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'ET', 'ETH', 'ETB', 'Br', 'ETHIOPIA', '???????????????', 'Africa', 'ET', 'N');
INSERT INTO `country` VALUES (211, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GA', 'GAB', 'XAF', 'Fr', 'GABON', '??????', 'Africa', 'GA', 'N');
INSERT INTO `country` VALUES (212, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GM', 'GMB', 'GMD', 'D', 'GAMBIA', '?????????', 'Africa', 'GM', 'N');
INSERT INTO `country` VALUES (213, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GH', 'GHA', 'GHS', '???', 'GHANA', '??????', 'Africa', 'GH', 'N');
INSERT INTO `country` VALUES (214, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GN', 'GIN', 'GNF', 'Fr', 'GUINEA ', '?????????', 'Africa', 'GN', 'N');
INSERT INTO `country` VALUES (215, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GW', 'GNB', 'XOF', 'Fr', 'GUINEA BISSAU', '???????????????', 'Africa', 'GW', 'N');
INSERT INTO `country` VALUES (216, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'KE', 'KEN', 'KES', 'Sh', 'KENYA', '?????????', 'Africa', 'KE', 'N');
INSERT INTO `country` VALUES (217, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'LS', 'LSO', 'LSL', 'L', 'LESOTHO', '?????????', 'Africa', 'LS', 'N');
INSERT INTO `country` VALUES (218, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'LR', 'LBR', 'LRD', '$', 'LIBERIA', '????????????', 'Africa', 'LR', 'N');
INSERT INTO `country` VALUES (219, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'LY', 'LBY', 'LYD', '??.??', 'LIBYA', '?????????', 'Africa', 'LY', 'N');
INSERT INTO `country` VALUES (220, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MG', 'MDG', 'MGA', 'Ar', 'MADAGASCAR', '???????????????', 'Africa', 'MG', 'N');
INSERT INTO `country` VALUES (221, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MW', 'MWI', 'MWK', 'MK', 'MALAWI', '?????????', 'Africa', 'MW', 'N');
INSERT INTO `country` VALUES (222, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'ML', 'MLI', 'XOF', 'Fr', 'MALI', '??????', 'Africa', 'ML', 'N');
INSERT INTO `country` VALUES (223, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MR', 'MRT', 'MRU', 'UM', 'MAURITANIA', '???????????????', 'Africa', 'MR', 'N');
INSERT INTO `country` VALUES (224, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MU', 'MUS', 'MUR', '???', 'MAURITIUS', '????????????', 'Africa', 'MU', 'N');
INSERT INTO `country` VALUES (225, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'YT', 'MYT', 'EUR', '???', 'MAYOTTE', '?????????', 'Africa', 'YT', 'N');
INSERT INTO `country` VALUES (226, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MA', 'MAR', 'MAD', '??.??.', 'MOROCCO', '?????????', 'Africa', 'MA', 'N');
INSERT INTO `country` VALUES (227, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MZ', 'MOZ', 'MZN', 'MT', 'MOZAMBIQUE', '????????????', 'Africa', 'MZ', 'N');
INSERT INTO `country` VALUES (228, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'NA', 'NAM', 'NAD', '$', 'NAMIBIA', '????????????', 'Africa', 'NA', 'N');
INSERT INTO `country` VALUES (229, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'NE', 'NER', 'XOF', 'Fr', 'NIGER', '?????????', 'Africa', 'NE', 'N');
INSERT INTO `country` VALUES (230, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'NG', 'NGA', 'NGN', '???', 'NIGERIA', '????????????', 'Africa', 'NG', 'N');
INSERT INTO `country` VALUES (231, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'RE', 'REU', 'EUR', '???', 'REUNION ISLAND ', '????????????', 'Africa', 'RE', 'N');
INSERT INTO `country` VALUES (232, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'RW', 'RWA', 'RWF', 'Fr', 'RWANDA', '?????????', 'Africa', 'RW', 'N');
INSERT INTO `country` VALUES (233, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'ST', 'STP', 'STN', 'Db', 'SAO TOME AND PRINCIPE', '????????????????????????', 'Africa', 'ST', 'N');
INSERT INTO `country` VALUES (234, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'SN', 'SEN', 'XOF', 'Fr', 'SENEGAL', '????????????', 'Africa', 'SN', 'N');
INSERT INTO `country` VALUES (235, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'SC', 'SYC', 'SCR', '???', 'SEYCHELLES', '?????????', 'Africa', 'SC', 'N');
INSERT INTO `country` VALUES (236, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SO', 'SOM', 'SOS', 'Sh', 'SOMALIA', '?????????', 'Africa', 'SO', 'N');
INSERT INTO `country` VALUES (237, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XS', '', NULL, NULL, 'SOMALILAND', '??????????????????', 'Africa', 'XS', 'N');
INSERT INTO `country` VALUES (238, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'ZA', 'ZAF', 'ZAR', 'R', 'SOUTH AFRICA', '??????', 'Africa', 'ZA', 'N');
INSERT INTO `country` VALUES (239, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SS', 'SSD', 'SSP', '??', 'SOUTH SUDAN', '??????????????????', 'Africa', 'SS', 'N');
INSERT INTO `country` VALUES (240, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SH', 'SHN', 'GBP', '??', 'ST HELENA', '???????????????', 'Africa', 'SH', 'N');
INSERT INTO `country` VALUES (241, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SD', 'SDN', 'SDG', NULL, 'SUDAN', '??????', 'Africa', 'SD', 'N');
INSERT INTO `country` VALUES (242, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SZ', 'SWZ', 'SZL', 'L', 'SWAZILAND', '????????????', 'Africa', 'SZ', 'N');
INSERT INTO `country` VALUES (243, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'TZ', 'TZA', 'TZS', 'Sh', 'TANZANIA', '????????????', 'Africa', 'TZ', 'N');
INSERT INTO `country` VALUES (244, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'TG', 'TGO', 'XOF', 'Fr', 'TOGO', '??????', 'Africa', 'TG', 'N');
INSERT INTO `country` VALUES (245, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'TN', 'TUN', 'TND', '??.??', 'TUNISIA', '?????????', 'Africa', 'TN', 'N');
INSERT INTO `country` VALUES (246, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'UG', 'UGA', 'UGX', 'Sh', 'UGANDA', '?????????', 'Africa', 'UG', 'N');
INSERT INTO `country` VALUES (247, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'EH', 'ESH', 'DZD', '????', 'WESTERN SAHARA ', '????????????', 'Africa', 'EH', 'N');
INSERT INTO `country` VALUES (248, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'ZM', 'ZMB', 'ZMW', 'ZK', 'ZAMBIA', '?????????', 'Africa', 'ZM', 'N');
INSERT INTO `country` VALUES (249, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'EAZ', '', NULL, NULL, 'ZANZIBAR', '????????????', 'Africa', 'EAZ', 'N');
INSERT INTO `country` VALUES (250, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'ZW', 'ZWE', 'ZWL', '$', 'ZIMBABWE', '????????????', 'Africa', 'ZW', 'N');
INSERT INTO `country` VALUES (251, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'AL', 'ALB', 'ALL', 'L', 'ALBANIA', '???????????????', 'Other', 'AL', 'N');
INSERT INTO `country` VALUES (252, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XD', '', NULL, NULL, 'ASCENSION', '?????????', 'Other', 'ASC', 'N');
INSERT INTO `country` VALUES (254, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XH', '', NULL, NULL, 'AZORES', '???????????????', 'Other', 'XH', 'N');
INSERT INTO `country` VALUES (255, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XJ', '', NULL, NULL, 'BALEARIC ISLANDS', '??????????????????', 'Other', 'XJ', 'N');
INSERT INTO `country` VALUES (256, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XB', '', NULL, NULL, 'BONAIRE', '????????????', 'Other', 'XB', 'N');
INSERT INTO `country` VALUES (257, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'BV', 'BVT', NULL, NULL, 'BOUVET ISLAND', '?????????', 'Other', 'BV', 'N');
INSERT INTO `country` VALUES (258, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'IC', '', NULL, NULL, 'CANARY ISLANDS', '???????????????', 'Other', 'IC', 'N');
INSERT INTO `country` VALUES (259, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'XK', 'UNK', 'EUR', '???', 'CAROLINE ISLANDS', '???????????????', 'Other', 'XK', 'N');
INSERT INTO `country` VALUES (260, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'ZR', '', NULL, NULL, 'CONGO-KINSHASA', '??????(???)', 'Other', 'ZR', 'N');
INSERT INTO `country` VALUES (261, '2022-12-15 02:56:00', '2022-12-15 06:58:31', 'CW', 'CUW', 'ANG', '??', 'CURACAO', '????????????(??????)', 'Other', 'CW', 'N');
INSERT INTO `country` VALUES (262, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'FX', '', NULL, NULL, 'FRANCE, METROPOLITAN', '????????????????????????', 'Other', 'FX', 'N');
INSERT INTO `country` VALUES (263, '2022-12-15 02:56:00', '2022-12-15 06:58:31', 'HM', 'HMD', NULL, NULL, 'HEARD ISLAND AND MCDONALD ISLANDS', '???????????????????????????', 'Other', 'HM', 'N');
INSERT INTO `country` VALUES (264, '2022-12-15 02:56:00', '2022-12-15 07:03:01', 'XK', 'UNK', 'Euro', '???', 'KOSOVO', '?????????', 'Other', 'KS', 'N');
INSERT INTO `country` VALUES (265, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XI', '', NULL, NULL, 'MADEIRA', '????????????', 'Other', 'XI', 'N');
INSERT INTO `country` VALUES (266, '2022-12-15 02:56:00', '2022-12-15 06:58:31', 'NR', 'NRU', 'AUD', '$', 'NAURU REPUBLIC ', '???????????????', 'Other', 'NR', 'N');
INSERT INTO `country` VALUES (267, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XN', '', NULL, NULL, 'NEVIS', '????????????', 'Other', 'XN', 'N');
INSERT INTO `country` VALUES (268, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XY', '', NULL, NULL, 'Saint Barth??lemy', '??????????????????', 'Other', 'BLM', 'N');
INSERT INTO `country` VALUES (269, '2022-12-15 02:56:00', '2022-12-15 06:58:31', 'SX', 'SXM', 'ANG', '??', 'SINT MAARTEN (DUTCH PART)', '???????????????', 'Other', 'SX', 'N');
INSERT INTO `country` VALUES (270, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XG', '', NULL, NULL, 'SPANISH TERRITORIES OF N.AFRICA', '?????????????????????', 'Other', 'XG', 'N');
INSERT INTO `country` VALUES (272, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XE', '', NULL, NULL, 'ST. EUSTATIUS', '????????????????????????', 'Other', 'XE', 'N');
INSERT INTO `country` VALUES (273, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XM', '', NULL, NULL, 'ST. MAARTEN', '????????????', 'Other', 'MAF', 'N');
INSERT INTO `country` VALUES (274, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'TA', '', NULL, NULL, 'TRISTAN DA CUNBA', '????????????', 'Other', 'TA', 'N');
INSERT INTO `country` VALUES (275, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'JU', '', NULL, NULL, 'YUGOSLAVIA', '????????????', 'Other', 'YU', 'N');

SET FOREIGN_KEY_CHECKS = 1;
