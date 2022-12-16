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
INSERT INTO `country` VALUES (1, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'AX', 'ALA', 'EUR', '€', 'ALAND ISLAND', '奥兰群岛', 'Europe', 'AX', 'N');
INSERT INTO `country` VALUES (3, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'AD', 'AND', 'EUR', '€', 'ANDORRA', '安道尔', 'Europe', 'AD', 'N');
INSERT INTO `country` VALUES (4, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'AT', 'AUT', 'EUR', '€', 'AUSTRIA', '奥地利', 'Europe', 'AT', 'N');
INSERT INTO `country` VALUES (5, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BY', 'BLR', 'BYN', 'Br', 'BELARUS', '白俄罗斯', 'Europe', 'BY', 'Y');
INSERT INTO `country` VALUES (6, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BE', 'BEL', 'EUR', '€', 'BELGIUM', '比利时', 'Europe', 'BE', 'Y');
INSERT INTO `country` VALUES (7, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BA', 'BIH', 'BAM', NULL, 'BOSNIA AND HERZEGOVINA', '波斯尼亚-黑塞哥维那共和国（波黑）', 'Europe', 'BA', 'N');
INSERT INTO `country` VALUES (8, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BG', 'BGR', 'BGN', 'лв', 'BULGARIA', '保加利亚', 'Europe', 'BG', 'N');
INSERT INTO `country` VALUES (9, '2022-12-15 02:55:54', '2022-12-15 06:58:25', 'BQ', 'BES', 'USD', '$', 'Caribbean Netherlands', '荷兰加勒比区', 'Europe', 'BQ', 'N');
INSERT INTO `country` VALUES (10, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'HR', 'HRV', 'HRK', 'kn', 'CROATIA', '克罗地亚', 'Europe', 'HR', 'N');
INSERT INTO `country` VALUES (11, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'CY', 'CYP', 'EUR', '€', 'CYPRUS', '塞浦路斯', 'Europe', 'CY', 'N');
INSERT INTO `country` VALUES (12, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'CZ', 'CZE', 'CZK', 'Kč', 'CZECH REPUBLIC', '捷克共和国', 'Europe', 'CZ', 'Y');
INSERT INTO `country` VALUES (13, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'DK', 'DNK', 'DKK', 'kr', 'DENMARK', '丹麦', 'Europe', 'DK', 'Y');
INSERT INTO `country` VALUES (14, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'EE', 'EST', 'EUR', '€', 'ESTONIA', '爱沙尼亚', 'Europe', 'EE', 'N');
INSERT INTO `country` VALUES (15, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'FO', 'FRO', 'DKK', 'kr', 'FAROE ISLANDS', '法罗群岛', 'Europe', 'FO', 'N');
INSERT INTO `country` VALUES (16, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'FI', 'FIN', 'EUR', '€', 'FINLAND', '芬兰', 'Europe', 'FI', 'Y');
INSERT INTO `country` VALUES (17, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'FR', 'FRA', 'EUR', '€', 'FRANCE', '法国', 'Europe', 'FR', 'Y');
INSERT INTO `country` VALUES (18, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'TF', 'ATF', 'EUR', '€', 'FRENCH SOUTHERN TERRITORIES', '法属南部领土', 'Europe', 'TF', 'N');
INSERT INTO `country` VALUES (19, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'DE', 'DEU', 'EUR', '€', 'GERMANY', '德国', 'Europe', 'DE', 'Y');
INSERT INTO `country` VALUES (20, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'GI', 'GIB', 'GIP', '£', 'GIBRALTAR', '直布罗陀', 'Europe', 'GI', 'N');
INSERT INTO `country` VALUES (21, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'GR', 'GRC', 'EUR', '€', 'GREECE', '希腊', 'Europe', 'GR', 'N');
INSERT INTO `country` VALUES (22, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'GG', 'GGY', 'GBP', '£', 'GUERNSEY', '根西岛', 'Europe', 'GGY', 'N');
INSERT INTO `country` VALUES (23, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'HU', 'HUN', 'HUF', 'Ft', 'HUNGARY', '匈牙利', 'Europe', 'HU', 'N');
INSERT INTO `country` VALUES (24, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'IS', 'ISL', 'ISK', 'kr', 'ICELAND', '冰岛', 'Europe', 'IS', 'N');
INSERT INTO `country` VALUES (25, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'IE', 'IRL', 'EUR', '€', 'IRELAND', '爱尔兰', 'Europe', 'IE', 'N');
INSERT INTO `country` VALUES (26, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'IM', 'IMN', 'GBP', '£', 'Isle of Man', '马恩岛', 'Europe', 'IM', 'N');
INSERT INTO `country` VALUES (27, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'IT', 'ITA', 'EUR', '€', 'ITALY', '意大利', 'Europe', 'IT', 'Y');
INSERT INTO `country` VALUES (28, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'JE', 'JEY', 'GBP', '£', 'JERSEY', '泽西岛(英属)', 'Europe', 'JEY', 'N');
INSERT INTO `country` VALUES (29, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'LV', 'LVA', 'EUR', '€', 'LATVIA', '拉脱维亚', 'Europe', 'LV', 'N');
INSERT INTO `country` VALUES (30, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'LI', 'LIE', 'CHF', 'Fr', 'LIECHTENSTEIN', '列支敦士登', 'Europe', 'LI', 'N');
INSERT INTO `country` VALUES (31, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'LT', 'LTU', 'EUR', '€', 'LITHUANIA', '立陶宛', 'Europe', 'LT', 'N');
INSERT INTO `country` VALUES (32, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'LU', 'LUX', 'EUR', '€', 'LUXEMBOURG', '卢森堡', 'Europe', 'LU', 'N');
INSERT INTO `country` VALUES (33, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MK', 'MKD', 'MKD', 'den', 'MACEDONIA', '马其顿', 'Europe', 'MK', 'N');
INSERT INTO `country` VALUES (34, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MT', 'MLT', 'EUR', '€', 'MALTA', '马耳他', 'Europe', 'MT', 'N');
INSERT INTO `country` VALUES (35, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MD', 'MDA', 'MDL', 'L', 'MOLDOVA', '摩尔多瓦', 'Europe', 'MD', 'N');
INSERT INTO `country` VALUES (36, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MC', 'MCO', 'EUR', '€', 'MONACO', '摩纳哥', 'Europe', 'MC', 'N');
INSERT INTO `country` VALUES (37, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'ME', 'MNE', 'EUR', '€', 'MONTENEGRO', '黑山共和国', 'Europe', 'MNE', 'N');
INSERT INTO `country` VALUES (38, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'NL', 'NLD', 'EUR', '€', 'NETHERLANDS', '荷兰', 'Europe', 'NL', 'Y');
INSERT INTO `country` VALUES (39, '2022-12-15 02:55:54', '2022-12-15 06:58:26', 'MK', 'MKD', 'MKD', 'den', 'NORTH MACEDONIA', '北马其顿', 'Europe', 'MK', 'N');
INSERT INTO `country` VALUES (40, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'NO', 'NOR', 'NOK', 'kr', 'NORWAY', '挪威', 'Europe', 'NO', 'Y');
INSERT INTO `country` VALUES (41, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'PS', 'PSE', 'EGP', 'E£', 'Palestinian territories', '巴勒斯坦', 'Europe', 'PS', 'N');
INSERT INTO `country` VALUES (42, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'PL', 'POL', 'PLN', 'zł', 'POLAND', '波兰', 'Europe', 'PL', 'Y');
INSERT INTO `country` VALUES (43, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'PT', 'PRT', 'EUR', '€', 'PORTUGAL', '葡萄牙', 'Europe', 'PT', 'N');
INSERT INTO `country` VALUES (44, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'RO', 'ROU', 'RON', 'lei', 'ROMANIA', '罗马尼亚', 'Europe', 'RO', 'N');
INSERT INTO `country` VALUES (45, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'RU', 'RUS', 'RUB', '₽', 'RUSSIA', '俄罗斯', 'Europe', 'RU', 'Y');
INSERT INTO `country` VALUES (46, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'MF', 'MAF', 'EUR', '€', 'SAINT MARTIN (FRENCH PART)', '法属圣马丁', 'Europe', 'MF', 'N');
INSERT INTO `country` VALUES (47, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'SM', 'SMR', 'EUR', '€', 'SAN MARINO', '圣马力诺', 'Europe', 'SM', 'N');
INSERT INTO `country` VALUES (48, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'RS', 'SRB', 'RSD', 'дин.', 'SERBIA, REPUBLIC OF', '塞尔维亚共和国', 'Europe', 'SRB', 'N');
INSERT INTO `country` VALUES (49, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'SL', 'SLE', 'SLL', 'Le', 'SIERRA LEONE', '塞拉利昂', 'Europe', 'SL', 'N');
INSERT INTO `country` VALUES (50, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'SK', 'SVK', 'EUR', '€', 'SLOVAKIA REPUBLIC', '斯洛伐克共和国', 'Europe', 'SK', 'N');
INSERT INTO `country` VALUES (51, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'SI', 'SVN', 'EUR', '€', 'SLOVENIA', '斯洛文尼亚', 'Europe', 'SI', 'N');
INSERT INTO `country` VALUES (52, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'GS', 'SGS', 'SHP', '£', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISL', '南乔治亚岛和南桑威奇群岛', 'Europe', 'SGS', 'N');
INSERT INTO `country` VALUES (53, '2022-12-15 02:55:55', '2022-12-15 06:58:26', 'ES', 'ESP', 'EUR', '€', 'SPAIN', '西班牙', 'Europe', 'ES', 'Y');
INSERT INTO `country` VALUES (54, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'SJ', 'SJM', 'NOK', 'kr', 'SVALBARD AND JAN MAYEN', '斯瓦尔巴岛和扬马延岛', 'Europe', 'SJ', 'N');
INSERT INTO `country` VALUES (55, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'SE', 'SWE', 'SEK', 'kr', 'SWEDEN', '瑞典', 'Europe', 'SE', 'Y');
INSERT INTO `country` VALUES (56, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'CH', 'CHE', 'CHF', 'Fr.', 'SWITZERLAND', '瑞士', 'Europe', 'CH', 'Y');
INSERT INTO `country` VALUES (57, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'UA', 'UKR', 'UAH', '₴', 'UKRAINE', '乌克兰', 'Europe', 'UA', 'Y');
INSERT INTO `country` VALUES (58, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GB', 'GBR', 'GBP', '£', 'UNITED KINGDOM', '英国', 'Europe', 'UK', 'Y');
INSERT INTO `country` VALUES (59, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'VA', 'VAT', 'EUR', '€', 'VATICAN CITY', '梵蒂冈', 'Europe', 'VA', 'N');
INSERT INTO `country` VALUES (60, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'AI', 'AIA', 'XCD', '$', 'ANGUILLA', '安圭拉岛', 'North America', 'AI', 'N');
INSERT INTO `country` VALUES (61, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'AG', 'ATG', 'XCD', '$', 'ANTIGUA AND BARBUDA', '安提瓜及巴布达', 'North America', 'AG', 'N');
INSERT INTO `country` VALUES (62, '2022-12-15 02:55:55', '2022-12-15 02:55:55', 'AA', '', NULL, NULL, 'APO/FPO', 'APO/FPO', 'North America', 'AA', 'N');
INSERT INTO `country` VALUES (63, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'AW', 'ABW', 'AWG', 'ƒ', 'ARUBA', '阿鲁巴岛', 'North America', 'AW', 'N');
INSERT INTO `country` VALUES (64, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'BS', 'BHS', 'BSD', '$', 'BAHAMAS', '巴哈马', 'North America', 'BS', 'N');
INSERT INTO `country` VALUES (65, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'BB', 'BRB', 'BBD', '$', 'BARBADOS', '巴巴多斯', 'North America', 'BB', 'N');
INSERT INTO `country` VALUES (66, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'BZ', 'BLZ', 'BZD', '$', 'BELIZE', '伯利兹', 'North America', 'BZ', 'N');
INSERT INTO `country` VALUES (67, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'BM', 'BMU', 'BMD', '$', 'BERMUDA', '百慕大', 'North America', 'BM', 'N');
INSERT INTO `country` VALUES (68, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'CA', 'CAN', 'CAD', '$', 'CANADA', '加拿大', 'North America', 'CA', 'Y');
INSERT INTO `country` VALUES (69, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'KY', 'CYM', 'KYD', '$', 'CAYMAN ISLANDS', '开曼群岛', 'North America', 'KY', 'N');
INSERT INTO `country` VALUES (70, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'CR', 'CRI', 'CRC', '₡', 'COSTA RICA', '哥斯达黎加', 'North America', 'CR', 'N');
INSERT INTO `country` VALUES (71, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'CU', 'CUB', 'CUC', '$', 'CUBA', '古巴', 'North America', 'CU', 'N');
INSERT INTO `country` VALUES (72, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'DM', 'DMA', 'XCD', '$', 'DOMINICA', '多米尼克', 'North America', 'DM', 'N');
INSERT INTO `country` VALUES (73, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'DO', 'DOM', 'DOP', '$', 'DOMINICAN REPUBLIC', '多米尼加共和国', 'North America', 'DO', 'N');
INSERT INTO `country` VALUES (74, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'SV', 'SLV', 'USD', '$', 'EL SALVADOR', '萨尔瓦多', 'North America', 'SV', 'N');
INSERT INTO `country` VALUES (75, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GL', 'GRL', 'DKK', 'kr.', 'GREENLAND', '格陵兰', 'North America', 'GL', 'N');
INSERT INTO `country` VALUES (76, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GD', 'GRD', 'XCD', '$', 'GRENADA', '格林纳达', 'North America', 'GD', 'N');
INSERT INTO `country` VALUES (77, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GP', 'GLP', 'EUR', '€', 'GUADELOUPE', '瓜德罗普', 'North America', 'GP', 'N');
INSERT INTO `country` VALUES (78, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'GT', 'GTM', 'GTQ', 'Q', 'GUATEMALA', '危地马拉', 'North America', 'GT', 'N');
INSERT INTO `country` VALUES (79, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'HT', 'HTI', 'HTG', 'G', 'HAITI', '海地', 'North America', 'HT', 'N');
INSERT INTO `country` VALUES (80, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'HN', 'HND', 'HNL', 'L', 'HONDURAS', '洪都拉斯', 'North America', 'HN', 'N');
INSERT INTO `country` VALUES (81, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'JM', 'JAM', 'JMD', '$', 'JAMAICA', '牙买加', 'North America', 'JM', 'N');
INSERT INTO `country` VALUES (82, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'MQ', 'MTQ', 'EUR', '€', 'MARTINIQUE', '马提尼克岛', 'North America', 'MQ', 'N');
INSERT INTO `country` VALUES (83, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'MX', 'MEX', 'MXN', '$', 'MEXICO', '墨西哥', 'North America', 'MX', 'Y');
INSERT INTO `country` VALUES (84, '2022-12-15 02:55:55', '2022-12-15 06:58:27', 'MS', 'MSR', 'XCD', '$', 'MONTSERRAT', '蒙特塞拉岛', 'North America', 'MS', 'N');
INSERT INTO `country` VALUES (85, '2022-12-15 02:55:56', '2022-12-15 02:55:56', 'AN', '', NULL, NULL, 'NETHERLANDS ANTILLES', '荷属安的列斯群岛', 'North America', 'AN', 'N');
INSERT INTO `country` VALUES (86, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'NI', 'NIC', 'NIO', 'C$', 'NICARAGUA', '尼加拉瓜', 'North America', 'NI', 'N');
INSERT INTO `country` VALUES (87, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'PA', 'PAN', 'PAB', 'B/.', 'PANAMA', '巴拿马', 'North America', 'PA', 'N');
INSERT INTO `country` VALUES (88, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'PR', 'PRI', 'USD', '$', 'PUERTO RICO', '波多黎各', 'North America', 'PR', 'Y');
INSERT INTO `country` VALUES (89, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'KN', 'KNA', 'XCD', '$', 'SAINT KITTS ', '圣基茨', 'North America', 'KN', 'N');
INSERT INTO `country` VALUES (90, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'PM', 'SPM', 'EUR', '€', 'SAINT PIERRE AND MIQUELON', '圣皮埃尔和密克隆群岛', 'North America', 'PM', 'N');
INSERT INTO `country` VALUES (91, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'VC', 'VCT', 'XCD', '$', 'SAINT VINCENT AND THE GRENADINES', '圣文森特和格林纳丁斯岛', 'North America', 'VC', 'N');
INSERT INTO `country` VALUES (92, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'LC', 'LCA', 'XCD', '$', 'ST. LUCIA', '圣卢西亚', 'North America', 'LC', 'N');
INSERT INTO `country` VALUES (93, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'TT', 'TTO', 'TTD', '$', 'TRINIDAD AND TOBAGO', '特立尼达和多巴哥', 'North America', 'TT', 'N');
INSERT INTO `country` VALUES (94, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'TC', 'TCA', 'USD', '$', 'TURKS AND CAICOS ISLANDS', '特克斯和凯科斯群岛', 'North America', 'TC', 'N');
INSERT INTO `country` VALUES (95, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'US', 'USA', 'USD', '$', 'UNITED STATES', '美国', 'North America', 'US', 'Y');
INSERT INTO `country` VALUES (96, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'UM', 'UMI', 'USD', '$', 'UNITED STATES MINOR OUTLYING ISLANDS', '美国本土外小岛屿', 'North America', 'UM', 'N');
INSERT INTO `country` VALUES (97, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'VG', 'VGB', 'USD', '$', 'VIRGIN ISLAND (GB)', '英属维尔京群岛', 'North America', 'VG', 'N');
INSERT INTO `country` VALUES (98, '2022-12-15 02:55:56', '2022-12-15 06:58:27', 'VI', 'VIR', 'USD', '$', 'VIRGIN ISLAND (US)', '美属维尔京群岛', 'North America', 'VI', 'N');
INSERT INTO `country` VALUES (99, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'AR', 'ARG', 'ARS', '$', 'ARGENTINA', '阿根廷', 'South America', 'AR', 'N');
INSERT INTO `country` VALUES (100, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BO', 'BOL', 'BOB', 'Bs.', 'BOLIVIA', '玻利维亚', 'South America', 'BO', 'N');
INSERT INTO `country` VALUES (101, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BR', 'BRA', 'BRL', 'R$', 'BRAZIL', '巴西', 'South America', 'BR', 'Y');
INSERT INTO `country` VALUES (102, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'CL', 'CHL', 'CLP', '$', 'CHILE', '智利', 'South America', 'CL', 'Y');
INSERT INTO `country` VALUES (103, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'CO', 'COL', 'COP', '$', 'COLOMBIA', '哥伦比亚', 'South America', 'CO', 'N');
INSERT INTO `country` VALUES (104, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'EC', 'ECU', 'USD', '$', 'ECUADOR', '厄瓜多尔', 'South America', 'EC', 'N');
INSERT INTO `country` VALUES (105, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'FK', 'FLK', 'FKP', '£', 'FALKLAND ISLAND', '福克兰群岛', 'South America', 'FK', 'N');
INSERT INTO `country` VALUES (106, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'GF', 'GUF', 'EUR', '€', 'FRENCH GUIANA', '法属圭亚那', 'South America', 'GF', 'N');
INSERT INTO `country` VALUES (107, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'GY', 'GUY', 'GYD', '$', 'GUYANA (BRITISH)', '圭亚那', 'South America', 'GY', 'N');
INSERT INTO `country` VALUES (108, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'PY', 'PRY', 'PYG', '₲', 'PARAGUAY', '巴拉圭', 'South America', 'PY', 'N');
INSERT INTO `country` VALUES (109, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'PE', 'PER', 'PEN', 'S/ ', 'PERU', '秘鲁', 'South America', 'PE', 'N');
INSERT INTO `country` VALUES (110, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'SR', 'SUR', 'SRD', '$', 'SURINAME', '苏里南', 'South America', 'SR', 'N');
INSERT INTO `country` VALUES (111, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'UY', 'URY', 'UYU', '$', 'URUGUAY', '乌拉圭', 'South America', 'UY', 'N');
INSERT INTO `country` VALUES (112, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'VE', 'VEN', 'VES', 'Bs.S', 'VENEZUELA', '委内瑞拉', 'South America', 'VE', 'N');
INSERT INTO `country` VALUES (113, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'HK', 'HKG', 'HKD', '$', '(China)HONG KONG', '中国香港', 'Asia', 'HK', 'N');
INSERT INTO `country` VALUES (114, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'MO', 'MAC', 'MOP', 'P', '(China)MACAU', '中国澳门', 'Asia', 'MO', 'N');
INSERT INTO `country` VALUES (115, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'TW', 'TWN', 'TWD', '$', '(China)TAIWAN', '中国台湾', 'Asia', 'TW', 'N');
INSERT INTO `country` VALUES (116, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'AF', 'AFG', 'AFN', '؋', 'AFGHANISTAN', '阿富汗', 'Asia', 'AF', 'N');
INSERT INTO `country` VALUES (117, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'AM', 'ARM', 'AMD', '֏', 'ARMENIA', '亚美尼亚', 'Asia', 'AM', 'N');
INSERT INTO `country` VALUES (118, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'AZ', 'AZE', 'AZN', '₼', 'AZERBAIJAN', '阿塞拜疆(独联体)', 'Asia', 'AZ', 'N');
INSERT INTO `country` VALUES (119, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BH', 'BHR', 'BHD', '.د.ب', 'BAHRAIN', '巴林', 'Asia', 'BH', 'N');
INSERT INTO `country` VALUES (120, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BD', 'BGD', 'BDT', '৳', 'BANGLADESH', '孟加拉国', 'Asia', 'BD', 'N');
INSERT INTO `country` VALUES (121, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BT', 'BTN', 'BTN', 'Nu.', 'BHUTAN', '不丹', 'Asia', 'BT', 'N');
INSERT INTO `country` VALUES (122, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'BN', 'BRN', 'BND', '$', 'BRUNEI', '文莱', 'Asia', 'BN', 'N');
INSERT INTO `country` VALUES (123, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'KH', 'KHM', 'KHR', '៛', 'CAMBODIA', '柬埔寨', 'Asia', 'KH', 'N');
INSERT INTO `country` VALUES (124, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'CN', 'CHN', 'CNY', '¥', 'CHINA', '中国', 'Asia', 'CN', 'N');
INSERT INTO `country` VALUES (127, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'TL', 'TLS', 'USD', '$', 'EAST TIMOR', '东帝汶', 'Asia', 'TLS', 'N');
INSERT INTO `country` VALUES (128, '2022-12-15 02:55:56', '2022-12-15 06:58:28', 'GE', 'GEO', 'GEL', '₾', 'GEORGIA', '格鲁吉亚', 'Asia', 'GE', 'N');
INSERT INTO `country` VALUES (129, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'IN', 'IND', 'INR', '₹', 'INDIA', '印度', 'Asia', 'IN', 'N');
INSERT INTO `country` VALUES (130, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'ID', 'IDN', 'IDR', 'Rp', 'INDONESIA', '印度尼西亚', 'Asia', 'ID', 'N');
INSERT INTO `country` VALUES (131, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'IR', 'IRN', 'IRR', '﷼', 'IRAN (ISLAMIC REPUBLIC OF)', '伊朗', 'Asia', 'IR', 'N');
INSERT INTO `country` VALUES (132, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'IQ', 'IRQ', 'IQD', 'ع.د', 'IRAQ', '伊拉克', 'Asia', 'IQ', 'N');
INSERT INTO `country` VALUES (133, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'IL', 'ISR', 'ILS', '₪', 'ISRAEL', '以色列', 'Asia', 'IL', 'Y');
INSERT INTO `country` VALUES (134, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'JP', 'JPN', 'JPY', '¥', 'JAPAN', '日本', 'Asia', 'JP', 'Y');
INSERT INTO `country` VALUES (135, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'JO', 'JOR', 'JOD', 'د.ا', 'JORDAN', '约旦', 'Asia', 'JO', 'N');
INSERT INTO `country` VALUES (136, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'KZ', 'KAZ', 'KZT', '₸', 'KAZAKHSTAN', '哈萨克斯坦', 'Asia', 'KZ', 'N');
INSERT INTO `country` VALUES (137, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'KW', 'KWT', 'KWD', 'د.ك', 'KUWAIT', '科威特', 'Asia', 'KW', 'N');
INSERT INTO `country` VALUES (138, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'KG', 'KGZ', 'KGS', 'с', 'KYRGYZSTAN', '吉尔吉斯斯坦', 'Asia', 'KG', 'N');
INSERT INTO `country` VALUES (139, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'LA', 'LAO', 'LAK', '₭', 'LAOS', '老挝', 'Asia', 'LA', 'N');
INSERT INTO `country` VALUES (140, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'LB', 'LBN', 'LBP', 'ل.ل', 'LEBANON', '黎巴嫩', 'Asia', 'LB', 'N');
INSERT INTO `country` VALUES (141, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'MY', 'MYS', 'MYR', 'RM', 'MALAYSIA', '马来西亚', 'Asia', 'MY', 'N');
INSERT INTO `country` VALUES (142, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'MV', 'MDV', 'MVR', '.ރ', 'MALDIVES', '马尔代夫', 'Asia', 'MV', 'N');
INSERT INTO `country` VALUES (143, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'MN', 'MNG', 'MNT', '₮', 'MONGOLIA', '蒙古', 'Asia', 'MN', 'N');
INSERT INTO `country` VALUES (144, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'MM', 'MMR', 'MMK', 'Ks', 'MYANMAR', '缅甸', 'Asia', 'MM', 'N');
INSERT INTO `country` VALUES (145, '2022-12-15 02:55:57', '2022-12-15 06:58:28', 'NP', 'NPL', 'NPR', '₨', 'NEPAL', '尼泊尔', 'Asia', 'NP', 'N');
INSERT INTO `country` VALUES (146, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'KP', 'PRK', 'KPW', '₩', 'NORTH KOREA', '朝鲜', 'Asia', 'KP', 'N');
INSERT INTO `country` VALUES (147, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'OM', 'OMN', 'OMR', 'ر.ع.', 'OMAN', '阿曼', 'Asia', 'OM', 'N');
INSERT INTO `country` VALUES (148, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'PK', 'PAK', 'PKR', '₨', 'PAKISTAN', '巴基斯坦', 'Asia', 'PK', 'N');
INSERT INTO `country` VALUES (149, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'PH', 'PHL', 'PHP', '₱', 'PHILIPPINES', '菲律宾', 'Asia', 'PH', 'Y');
INSERT INTO `country` VALUES (150, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'QA', 'QAT', 'QAR', 'ر.ق', 'QATAR', '卡塔尔', 'Asia', 'QA', 'N');
INSERT INTO `country` VALUES (151, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'SA', 'SAU', 'SAR', 'ر.س', 'SAUDI ARABIA', '沙特阿拉伯', 'Asia', 'SA', 'N');
INSERT INTO `country` VALUES (152, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'SG', 'SGP', 'SGD', '$', 'SINGAPORE', '新加坡', 'Asia', 'SG', 'N');
INSERT INTO `country` VALUES (153, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'KR', 'KOR', 'KRW', '₩', 'SOUTH KOREA', '韩国', 'Asia', 'KR', 'N');
INSERT INTO `country` VALUES (154, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'LK', 'LKA', 'LKR', 'Rs  ', 'SRI LANKA', '斯里兰卡', 'Asia', 'LK', 'N');
INSERT INTO `country` VALUES (156, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'SY', 'SYR', 'SYP', '£', 'SYRIA', '叙利亚', 'Asia', 'SY', 'N');
INSERT INTO `country` VALUES (157, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'TJ', 'TJK', 'TJS', 'ЅМ', 'TAJIKISTAN', '塔吉克斯坦', 'Asia', 'TJ', 'N');
INSERT INTO `country` VALUES (158, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'TH', 'THA', 'THB', '฿', 'THAILAND', '泰国', 'Asia', 'TH', 'N');
INSERT INTO `country` VALUES (159, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'TR', 'TUR', 'TRY', '₺', 'TURKEY', '土耳其', 'Asia', 'TR', 'Y');
INSERT INTO `country` VALUES (160, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'TM', 'TKM', 'TMT', 'm', 'TURKMENISTAN', '土库曼斯坦', 'Asia', 'TM', 'N');
INSERT INTO `country` VALUES (161, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'AE', 'ARE', 'AED', 'د.إ', 'UNITED ARAB EMIRATES', '阿拉伯联合酋长国', 'Asia', 'AE', 'N');
INSERT INTO `country` VALUES (162, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'UZ', 'UZB', 'UZS', 'so\'m', 'UZBEKISTAN', '乌兹别克斯坦', 'Asia', 'UZ', 'N');
INSERT INTO `country` VALUES (163, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'VN', 'VNM', 'VND', '₫', 'VIETNAM', '越南', 'Asia', 'VN', 'N');
INSERT INTO `country` VALUES (164, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'YE', 'YEM', 'YER', '﷼', 'YEMEN, REPUBLIC OF', '也门阿拉伯共合国', 'Asia', 'YE', 'N');
INSERT INTO `country` VALUES (165, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'AS', 'ASM', 'USD', '$', 'AMERICAN SAMOA', '美属萨摩亚群岛', 'Oceania', 'AS', 'N');
INSERT INTO `country` VALUES (166, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'AU', 'AUS', 'AUD', '$', 'AUSTRALIA', '澳大利亚', 'Oceania', 'AU', 'Y');
INSERT INTO `country` VALUES (167, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'CX', 'CXR', 'AUD', '$', 'CHRISTMAS ISLAND', '圣诞岛', 'Oceania', 'CX', 'N');
INSERT INTO `country` VALUES (168, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'CC', 'CCK', 'AUD', '$', 'COCOS(KEELING)ISLANDS', '科科斯群岛', 'Oceania', 'CC', 'N');
INSERT INTO `country` VALUES (169, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'CK', 'COK', 'CKD', '$', 'COOK ISLANDS', '库克群岛', 'Oceania', 'CK', 'N');
INSERT INTO `country` VALUES (170, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'FJ', 'FJI', 'FJD', '$', 'FIJI', '斐济', 'Oceania', 'FJ', 'N');
INSERT INTO `country` VALUES (171, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'PF', 'PYF', 'XPF', '₣', 'FRENCH POLYNESIA', '塔希堤岛(法属波利尼西亚)', 'Oceania', 'PF', 'N');
INSERT INTO `country` VALUES (172, '2022-12-15 02:55:57', '2022-12-15 06:58:29', 'GU', 'GUM', 'USD', '$', 'GUAM', '关岛', 'Oceania', 'GU', 'N');
INSERT INTO `country` VALUES (173, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'KI', 'KIR', 'AUD', '$', 'KIRIBATI REPUBILC', '基利巴斯共和国', 'Oceania', 'KI', 'N');
INSERT INTO `country` VALUES (174, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'MH', 'MHL', 'USD', '$', 'MARSHALL ISLANDS', '马绍尔群岛', 'Oceania', 'MH', 'N');
INSERT INTO `country` VALUES (175, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'FM', 'FSM', 'USD', '$', 'MICRONESIA', '密克罗尼西亚', 'Oceania', 'FM', 'N');
INSERT INTO `country` VALUES (176, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'NC', 'NCL', 'XPF', '₣', 'NEW CALEDONIA', '新喀里多尼亚', 'Oceania', 'NC', 'N');
INSERT INTO `country` VALUES (177, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'NZ', 'NZL', 'NZD', '$', 'NEW ZEALAND', '新西兰', 'Oceania', 'NZ', 'N');
INSERT INTO `country` VALUES (178, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'NU', 'NIU', 'NZD', '$', 'NIUE', '纽埃岛', 'Oceania', 'NU', 'N');
INSERT INTO `country` VALUES (179, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'NF', 'NFK', 'AUD', '$', 'NORFOLK ISLAND', '诺褔克岛', 'Oceania', 'NF', 'N');
INSERT INTO `country` VALUES (180, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'PW', 'PLW', 'USD', '$', 'PALAU', '帕劳', 'Oceania', 'PW', 'N');
INSERT INTO `country` VALUES (181, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'PG', 'PNG', 'PGK', 'K', 'PAPUA NEW GUINEA', '巴布亚新几内亚', 'Oceania', 'PG', 'N');
INSERT INTO `country` VALUES (182, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'PN', 'PCN', 'NZD', '$', 'PITCAIRN ISLANDS', '皮特凯恩群岛', 'Oceania', 'PN', 'N');
INSERT INTO `country` VALUES (183, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'MP', 'MNP', 'USD', '$', 'SAIPAN', '塞班岛', 'Oceania', 'MP', 'N');
INSERT INTO `country` VALUES (184, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'SB', 'SLB', 'SBD', '$', 'SOLOMON ISLANDS', '所罗门群岛', 'Oceania', 'SB', 'N');
INSERT INTO `country` VALUES (185, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'TK', 'TKL', 'NZD', '$', 'TOKELAU', '托克劳', 'Oceania', 'TK', 'N');
INSERT INTO `country` VALUES (186, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'TO', 'TON', 'TOP', 'T$', 'TONGA', '汤加', 'Oceania', 'TO', 'N');
INSERT INTO `country` VALUES (187, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'TV', 'TUV', 'AUD', '$', 'TUVALU', '图瓦卢', 'Oceania', 'TV', 'N');
INSERT INTO `country` VALUES (188, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'VU', 'VUT', 'VUV', 'Vt', 'VANUATU', '瓦努阿图', 'Oceania', 'VU', 'N');
INSERT INTO `country` VALUES (189, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'WF', 'WLF', 'XPF', '₣', 'WALLIS AND FUTUNA ISLANDS', '瓦利斯群岛和富图纳群岛', 'Oceania', 'WF', 'N');
INSERT INTO `country` VALUES (190, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'WS', 'WSM', 'WST', 'T', 'WESTERN SAMOA', '西萨摩亚', 'Oceania', 'WS', 'N');
INSERT INTO `country` VALUES (191, '2022-12-15 02:55:58', '2022-12-15 06:58:29', 'DZ', 'DZA', 'DZD', 'د.ج', 'ALGERIA', '阿尔及利亚', 'Africa', 'DZ', 'N');
INSERT INTO `country` VALUES (192, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'AO', 'AGO', 'AOA', 'Kz', 'ANGOLA', '安哥拉', 'Africa', 'AO', 'N');
INSERT INTO `country` VALUES (193, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'BJ', 'BEN', 'XOF', 'Fr', 'BENIN', '贝宁', 'Africa', 'BJ', 'N');
INSERT INTO `country` VALUES (194, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'BW', 'BWA', 'BWP', 'P', 'BOTSWANA', '博茨瓦纳', 'Africa', 'BW', 'N');
INSERT INTO `country` VALUES (195, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'IO', 'IOT', 'USD', '$', 'BRITISH INDIAN OCEAN TERRITORY', '英属印度洋地区(查各群岛)', 'Africa', 'IO', 'N');
INSERT INTO `country` VALUES (196, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'BF', 'BFA', 'XOF', 'Fr', 'BURKINA FASO', '布基纳法索', 'Africa', 'BF', 'N');
INSERT INTO `country` VALUES (197, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'BI', 'BDI', 'BIF', 'Fr', 'BURUNDI', '布隆迪', 'Africa', 'BI', 'N');
INSERT INTO `country` VALUES (198, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CM', 'CMR', 'XAF', 'Fr', 'CAMEROON', '喀麦隆', 'Africa', 'CM', 'N');
INSERT INTO `country` VALUES (199, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CV', 'CPV', 'CVE', 'Esc', 'CAPE VERDE', '佛得角群岛', 'Africa', 'CV', 'N');
INSERT INTO `country` VALUES (200, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CF', 'CAF', 'XAF', 'Fr', 'CENTRAL REPUBLIC', '中非共和国', 'Africa', 'CF', 'N');
INSERT INTO `country` VALUES (201, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'TD', 'TCD', 'XAF', 'Fr', 'CHAD', '乍得', 'Africa', 'TD', 'N');
INSERT INTO `country` VALUES (202, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'KM', 'COM', 'KMF', 'Fr', 'COMOROS', '科摩罗', 'Africa', 'KM', 'N');
INSERT INTO `country` VALUES (203, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CG', 'COG', 'XAF', 'Fr', 'CONGO', '刚果', 'Africa', 'CG', 'N');
INSERT INTO `country` VALUES (204, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CD', 'COD', 'CDF', 'FC', 'CONGO REPUBLIC ', '刚果民主共和国', 'Africa', 'CD', 'N');
INSERT INTO `country` VALUES (205, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'CI', 'CIV', 'XOF', 'Fr', 'COTE D\'LVOIRE(IVORY)', '科特迪瓦(象牙海岸) ', 'Africa', 'CI', 'N');
INSERT INTO `country` VALUES (206, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'DJ', 'DJI', 'DJF', 'Fr', 'DJIBOUTI', '吉布提', 'Africa', 'DJ', 'N');
INSERT INTO `country` VALUES (207, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'EG', 'EGY', 'EGP', '£', 'EGYPT', '埃及', 'Africa', 'EG', 'N');
INSERT INTO `country` VALUES (208, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GQ', 'GNQ', 'XAF', 'Fr', 'EQUATORIAL GUINEA ', '赤道几内亚', 'Africa', 'GQ', 'N');
INSERT INTO `country` VALUES (209, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'ER', 'ERI', 'ERN', 'Nfk', 'ERITREA', '厄里特立亚', 'Africa', 'ER', 'N');
INSERT INTO `country` VALUES (210, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'ET', 'ETH', 'ETB', 'Br', 'ETHIOPIA', '埃塞俄比亚', 'Africa', 'ET', 'N');
INSERT INTO `country` VALUES (211, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GA', 'GAB', 'XAF', 'Fr', 'GABON', '加蓬', 'Africa', 'GA', 'N');
INSERT INTO `country` VALUES (212, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GM', 'GMB', 'GMD', 'D', 'GAMBIA', '冈比亚', 'Africa', 'GM', 'N');
INSERT INTO `country` VALUES (213, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GH', 'GHA', 'GHS', '₵', 'GHANA', '加纳', 'Africa', 'GH', 'N');
INSERT INTO `country` VALUES (214, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GN', 'GIN', 'GNF', 'Fr', 'GUINEA ', '几内亚', 'Africa', 'GN', 'N');
INSERT INTO `country` VALUES (215, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'GW', 'GNB', 'XOF', 'Fr', 'GUINEA BISSAU', '几内亚比绍', 'Africa', 'GW', 'N');
INSERT INTO `country` VALUES (216, '2022-12-15 02:55:58', '2022-12-15 06:58:30', 'KE', 'KEN', 'KES', 'Sh', 'KENYA', '肯尼亚', 'Africa', 'KE', 'N');
INSERT INTO `country` VALUES (217, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'LS', 'LSO', 'LSL', 'L', 'LESOTHO', '莱索托', 'Africa', 'LS', 'N');
INSERT INTO `country` VALUES (218, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'LR', 'LBR', 'LRD', '$', 'LIBERIA', '利比里亚', 'Africa', 'LR', 'N');
INSERT INTO `country` VALUES (219, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'LY', 'LBY', 'LYD', 'ل.د', 'LIBYA', '利比亚', 'Africa', 'LY', 'N');
INSERT INTO `country` VALUES (220, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MG', 'MDG', 'MGA', 'Ar', 'MADAGASCAR', '马达加斯加', 'Africa', 'MG', 'N');
INSERT INTO `country` VALUES (221, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MW', 'MWI', 'MWK', 'MK', 'MALAWI', '马拉维', 'Africa', 'MW', 'N');
INSERT INTO `country` VALUES (222, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'ML', 'MLI', 'XOF', 'Fr', 'MALI', '马里', 'Africa', 'ML', 'N');
INSERT INTO `country` VALUES (223, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MR', 'MRT', 'MRU', 'UM', 'MAURITANIA', '毛里塔尼亚', 'Africa', 'MR', 'N');
INSERT INTO `country` VALUES (224, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MU', 'MUS', 'MUR', '₨', 'MAURITIUS', '毛里求斯', 'Africa', 'MU', 'N');
INSERT INTO `country` VALUES (225, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'YT', 'MYT', 'EUR', '€', 'MAYOTTE', '马约特', 'Africa', 'YT', 'N');
INSERT INTO `country` VALUES (226, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MA', 'MAR', 'MAD', 'د.م.', 'MOROCCO', '摩洛哥', 'Africa', 'MA', 'N');
INSERT INTO `country` VALUES (227, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'MZ', 'MOZ', 'MZN', 'MT', 'MOZAMBIQUE', '莫桑比克', 'Africa', 'MZ', 'N');
INSERT INTO `country` VALUES (228, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'NA', 'NAM', 'NAD', '$', 'NAMIBIA', '纳米比亚', 'Africa', 'NA', 'N');
INSERT INTO `country` VALUES (229, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'NE', 'NER', 'XOF', 'Fr', 'NIGER', '尼日尔', 'Africa', 'NE', 'N');
INSERT INTO `country` VALUES (230, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'NG', 'NGA', 'NGN', '₦', 'NIGERIA', '尼日利亚', 'Africa', 'NG', 'N');
INSERT INTO `country` VALUES (231, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'RE', 'REU', 'EUR', '€', 'REUNION ISLAND ', '留尼汪岛', 'Africa', 'RE', 'N');
INSERT INTO `country` VALUES (232, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'RW', 'RWA', 'RWF', 'Fr', 'RWANDA', '卢旺达', 'Africa', 'RW', 'N');
INSERT INTO `country` VALUES (233, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'ST', 'STP', 'STN', 'Db', 'SAO TOME AND PRINCIPE', '圣多美和普林西比', 'Africa', 'ST', 'N');
INSERT INTO `country` VALUES (234, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'SN', 'SEN', 'XOF', 'Fr', 'SENEGAL', '塞内加尔', 'Africa', 'SN', 'N');
INSERT INTO `country` VALUES (235, '2022-12-15 02:55:59', '2022-12-15 06:58:30', 'SC', 'SYC', 'SCR', '₨', 'SEYCHELLES', '塞舌尔', 'Africa', 'SC', 'N');
INSERT INTO `country` VALUES (236, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SO', 'SOM', 'SOS', 'Sh', 'SOMALIA', '索马里', 'Africa', 'SO', 'N');
INSERT INTO `country` VALUES (237, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XS', '', NULL, NULL, 'SOMALILAND', '索马里共和国', 'Africa', 'XS', 'N');
INSERT INTO `country` VALUES (238, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'ZA', 'ZAF', 'ZAR', 'R', 'SOUTH AFRICA', '南非', 'Africa', 'ZA', 'N');
INSERT INTO `country` VALUES (239, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SS', 'SSD', 'SSP', '£', 'SOUTH SUDAN', '南苏丹共和国', 'Africa', 'SS', 'N');
INSERT INTO `country` VALUES (240, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SH', 'SHN', 'GBP', '£', 'ST HELENA', '圣赫勒拿岛', 'Africa', 'SH', 'N');
INSERT INTO `country` VALUES (241, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SD', 'SDN', 'SDG', NULL, 'SUDAN', '苏丹', 'Africa', 'SD', 'N');
INSERT INTO `country` VALUES (242, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'SZ', 'SWZ', 'SZL', 'L', 'SWAZILAND', '斯威士兰', 'Africa', 'SZ', 'N');
INSERT INTO `country` VALUES (243, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'TZ', 'TZA', 'TZS', 'Sh', 'TANZANIA', '坦桑尼亚', 'Africa', 'TZ', 'N');
INSERT INTO `country` VALUES (244, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'TG', 'TGO', 'XOF', 'Fr', 'TOGO', '多哥', 'Africa', 'TG', 'N');
INSERT INTO `country` VALUES (245, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'TN', 'TUN', 'TND', 'د.ت', 'TUNISIA', '突尼斯', 'Africa', 'TN', 'N');
INSERT INTO `country` VALUES (246, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'UG', 'UGA', 'UGX', 'Sh', 'UGANDA', '乌干达', 'Africa', 'UG', 'N');
INSERT INTO `country` VALUES (247, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'EH', 'ESH', 'DZD', 'دج', 'WESTERN SAHARA ', '西撒哈拉', 'Africa', 'EH', 'N');
INSERT INTO `country` VALUES (248, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'ZM', 'ZMB', 'ZMW', 'ZK', 'ZAMBIA', '赞比亚', 'Africa', 'ZM', 'N');
INSERT INTO `country` VALUES (249, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'EAZ', '', NULL, NULL, 'ZANZIBAR', '桑给巴尔', 'Africa', 'EAZ', 'N');
INSERT INTO `country` VALUES (250, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'ZW', 'ZWE', 'ZWL', '$', 'ZIMBABWE', '津巴布韦', 'Africa', 'ZW', 'N');
INSERT INTO `country` VALUES (251, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'AL', 'ALB', 'ALL', 'L', 'ALBANIA', '阿尔巴尼亚', 'Other', 'AL', 'N');
INSERT INTO `country` VALUES (252, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XD', '', NULL, NULL, 'ASCENSION', '阿森松', 'Other', 'ASC', 'N');
INSERT INTO `country` VALUES (254, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XH', '', NULL, NULL, 'AZORES', '亚速尔群岛', 'Other', 'XH', 'N');
INSERT INTO `country` VALUES (255, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XJ', '', NULL, NULL, 'BALEARIC ISLANDS', '巴利阿里群岛', 'Other', 'XJ', 'N');
INSERT INTO `country` VALUES (256, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'XB', '', NULL, NULL, 'BONAIRE', '伯奈尔岛', 'Other', 'XB', 'N');
INSERT INTO `country` VALUES (257, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'BV', 'BVT', NULL, NULL, 'BOUVET ISLAND', '布维岛', 'Other', 'BV', 'N');
INSERT INTO `country` VALUES (258, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'IC', '', NULL, NULL, 'CANARY ISLANDS', '加那利群岛', 'Other', 'IC', 'N');
INSERT INTO `country` VALUES (259, '2022-12-15 02:55:59', '2022-12-15 06:58:31', 'XK', 'UNK', 'EUR', '€', 'CAROLINE ISLANDS', '加罗林群岛', 'Other', 'XK', 'N');
INSERT INTO `country` VALUES (260, '2022-12-15 02:55:59', '2022-12-15 02:55:59', 'ZR', '', NULL, NULL, 'CONGO-KINSHASA', '刚果(金)', 'Other', 'ZR', 'N');
INSERT INTO `country` VALUES (261, '2022-12-15 02:56:00', '2022-12-15 06:58:31', 'CW', 'CUW', 'ANG', 'ƒ', 'CURACAO', '库拉索岛(荷兰)', 'Other', 'CW', 'N');
INSERT INTO `country` VALUES (262, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'FX', '', NULL, NULL, 'FRANCE, METROPOLITAN', '法属美特罗波利坦', 'Other', 'FX', 'N');
INSERT INTO `country` VALUES (263, '2022-12-15 02:56:00', '2022-12-15 06:58:31', 'HM', 'HMD', NULL, NULL, 'HEARD ISLAND AND MCDONALD ISLANDS', '赫德岛和麦克唐纳岛', 'Other', 'HM', 'N');
INSERT INTO `country` VALUES (264, '2022-12-15 02:56:00', '2022-12-15 07:03:01', 'XK', 'UNK', 'Euro', '€', 'KOSOVO', '科索沃', 'Other', 'KS', 'N');
INSERT INTO `country` VALUES (265, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XI', '', NULL, NULL, 'MADEIRA', '马德拉岛', 'Other', 'XI', 'N');
INSERT INTO `country` VALUES (266, '2022-12-15 02:56:00', '2022-12-15 06:58:31', 'NR', 'NRU', 'AUD', '$', 'NAURU REPUBLIC ', '瑙鲁共和国', 'Other', 'NR', 'N');
INSERT INTO `country` VALUES (267, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XN', '', NULL, NULL, 'NEVIS', '尼维斯岛', 'Other', 'XN', 'N');
INSERT INTO `country` VALUES (268, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XY', '', NULL, NULL, 'Saint Barthélemy', '圣巴特勒米岛', 'Other', 'BLM', 'N');
INSERT INTO `country` VALUES (269, '2022-12-15 02:56:00', '2022-12-15 06:58:31', 'SX', 'SXM', 'ANG', 'ƒ', 'SINT MAARTEN (DUTCH PART)', '荷属圣马丁', 'Other', 'SX', 'N');
INSERT INTO `country` VALUES (270, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XG', '', NULL, NULL, 'SPANISH TERRITORIES OF N.AFRICA', '北非西班牙属土', 'Other', 'XG', 'N');
INSERT INTO `country` VALUES (272, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XE', '', NULL, NULL, 'ST. EUSTATIUS', '圣尤斯塔提马斯岛', 'Other', 'XE', 'N');
INSERT INTO `country` VALUES (273, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'XM', '', NULL, NULL, 'ST. MAARTEN', '圣马腾岛', 'Other', 'MAF', 'N');
INSERT INTO `country` VALUES (274, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'TA', '', NULL, NULL, 'TRISTAN DA CUNBA', '特里斯坦', 'Other', 'TA', 'N');
INSERT INTO `country` VALUES (275, '2022-12-15 02:56:00', '2022-12-15 02:56:00', 'JU', '', NULL, NULL, 'YUGOSLAVIA', '南斯拉夫', 'Other', 'YU', 'N');

SET FOREIGN_KEY_CHECKS = 1;
