-- Jake Hathaway and Kevin Kraatz
-- Portfolio Project Group 50 Official DDL File for CS340 project deliverables
-- MySQL Workbench Forward Engineering

SET UNIQUE_CHECKS=0;
SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- DROP OLD TABLES
-- -----------------------------------------------------

DROP TABLE IF EXISTS `Media_Transactions`;
DROP TABLE IF EXISTS `Media_Items`;
DROP TABLE IF EXISTS `Employees`;
DROP TABLE IF EXISTS `Patrons`;
DROP TABLE IF EXISTS `Suppliers`;
DROP TABLE IF EXISTS `Creators`;

-- -----------------------------------------------------
-- Table `Employees`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Employees` (
  `employee_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` NVARCHAR(50) NOT NULL,
  `last_name` NVARCHAR(50) NOT NULL,
  `phone_number` NVARCHAR(15) NULL DEFAULT NULL,
  `address` NVARCHAR(200) NOT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE INDEX `employee_id_UNIQUE` (`employee_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Patrons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Patrons` (
  `patron_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` NVARCHAR(50) NOT NULL,
  `last_name` NVARCHAR(50) NOT NULL,
  `phone_number` NVARCHAR(15) NOT NULL,
  `fine_amount` DECIMAL(19,2) NULL DEFAULT NULL,
  `address` NVARCHAR(200) NOT NULL,
  PRIMARY KEY (`patron_id`),
  UNIQUE INDEX `idpatrons_UNIQUE` (`patron_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Suppliers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Suppliers` (
  `supplier_id` INT NOT NULL AUTO_INCREMENT,
  `name` NVARCHAR(50) NOT NULL,
  `address` NVARCHAR(200) NOT NULL,
  `phone_number` NVARCHAR(20) NOT NULL,
  PRIMARY KEY (`supplier_id`),
  UNIQUE INDEX `idsuppliers_UNIQUE` (`supplier_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Creators`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Creators` (
  `creator_id` INT NOT NULL AUTO_INCREMENT,
  `full_name` NVARCHAR(50) NOT NULL,
  PRIMARY KEY (`creator_id`),
  UNIQUE INDEX `artist_id_UNIQUE` (`creator_id` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Media_Items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Media_Items` (
  `item_id` INT NOT NULL AUTO_INCREMENT,
  `media_type` NVARCHAR(20) NOT NULL,
  `supplier_id` INT NULL,
  `title` NVARCHAR(50) NOT NULL,
  `creator_id` INT NOT NULL,
  `release_date` DATE NOT NULL,
  `replacement_cost` DECIMAL(19,2) NULL DEFAULT NULL,
  `quantity_owned` INT NOT NULL,
  PRIMARY KEY (`item_id`, `creator_id`),
  INDEX `primary_supplier_idx` (`supplier_id` ASC),
  INDEX `artist_idx` (`creator_id` ASC),
  CONSTRAINT `primary_supplier`
    FOREIGN KEY (`supplier_id`)
    REFERENCES `Suppliers` (`supplier_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `artist`
    FOREIGN KEY (`creator_id`)
    REFERENCES `Creators` (`creator_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Media_Transactions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Media_Transactions` (
  `transaction_id` INT NOT NULL AUTO_INCREMENT,
  `patron_id` INT NOT NULL,
  `transaction_type` NVARCHAR(20) NOT NULL,
  `employee_id` INT NOT NULL,
  `item_id` INT NOT NULL,
  `transaction_date` DATETIME NOT NULL,
  INDEX `employee_id_idx` (`employee_id` ASC),
  INDEX `media_id_idx` (`item_id` ASC),
  PRIMARY KEY (`transaction_id`, `patron_id`, `employee_id`, `item_id`),
  UNIQUE INDEX `transaction_id_UNIQUE` (`transaction_id` ASC),
  CONSTRAINT `patron_id`
    FOREIGN KEY (`patron_id`)
    REFERENCES `Patrons` (`patron_id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `employee_id`
    FOREIGN KEY (`employee_id`)
    REFERENCES `Employees` (`employee_id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `media_id`
    FOREIGN KEY (`item_id`)
    REFERENCES `Media_Items` (`item_id`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Employees` Data Insert
-- -----------------------------------------------------
INSERT INTO `Employees` (
  `first_name`,
  `last_name`,
  `phone_number`,
  `address`
) VALUES (
  'Jaimie',
  'Melliard',
  '(702) 445-4215',
  '6 Eliot Point Las Vegas, NV 89115'
), (
  'Darian',
  'Labern',
  '(415) 391-7377',
  '08854 Armistice Junction San Francisco, CA 94110'
), (
  'Cathee',
  'Pluthero',
  '(407) 216-1318',
  '97 Del Mar Circle Pensacola, FL 32595'
), (
  'Lena',
  'Bausor',
  '(773) 616-9766',
  '3 Nelson Pass Chicago, IL 60657'
);

-- -----------------------------------------------------
-- Table `Patrons` Data Insert
-- -----------------------------------------------------
INSERT INTO `Patrons` (
  `first_name`,
  `last_name`,
  `phone_number`,
  `fine_amount`,
  `address`
) VALUES (
  'Dianna',
  'MacTrustie',
  '(979) 856-0499',
  '0.00',
  '2568 Mifflin Parkway Bryan, TX 77806'
), (
  'Lorain',
  'Burren',
  '(916) 468-6616',
  '2.75',
  '45 Melrose Way Sacramento, CA 94250'
), (
  'Mildrid',
  'McArte',
  '(212) 760-3859',
  '19.95',
  '1 Algoma Hill New York City, NY 10184'
), (
  'Jeramy',
  'McCann',
  '(503) 550-4845',
  '0.00',
  '68967 Stuart Alley Beaverton, OR 97075'
);

-- -----------------------------------------------------
-- Table `Creators` Data Insert
-- -----------------------------------------------------

INSERT INTO `Creators` (
  `full_name`
) VALUES (
  'Stephen King'
), (
  'Joanna Gaines'
), (
  'George R.R. Martin'
), (
  'Katy Perry'
), (
  'Quentin Tarantino'
);

-- -----------------------------------------------------
-- Table `Suppliers` Data Insert
-- -----------------------------------------------------
INSERT INTO `Suppliers` (
  `name`,
  `address`,
  `phone_number`
) VALUES (
  'Ingram Content Group, Inc.',
  'One Ingram Blvd. La Vergne, TN 37086',
  '(855) 867-1920'
), (
  'Publishers Group West',
  '1700 Fourth Street Berkeley, CA 94710',
  '(510) 809-3700'
), (
  'Media Solutions',
  '9632 Madison Blvd. Madison, AL 35758',
  '(800) 476-5872'
), (
  'Small Changes Inc.',
  '1418 NW 53rd Street Seattle, WA 98107',
  '(206) 382-1980'
);

-- -----------------------------------------------------
-- Table `Media_Items` Data Insert
-- -----------------------------------------------------
INSERT INTO `Media_Items` (
  `media_type`,
  `supplier_id`,
  `title`,
  `creator_id`,
  `release_date`,
  `replacement_cost`,
  `quantity_owned`
) VALUES (
  'Book',
  '1',
  'The Shining',
  '1',
  '1977-01-28',
  '7.99',
  '2'
), (
  'Book',
  '2',
  'A Game of Thrones',
  '3',
  '1996-08-01',
  '15.29',
  '4'
), (
  'Movie',
  '3',
  'Pulp Fiction',
  '5',
  '1994-10-14',
  '15.50',
  '1'
), (
  'Music',
  '3',
  'Teenage Dream',
  '4',
  '2010-08-24',
  '8.01',
  '1'
), (
  'Magazine',
  '4',
  'Magnolia Journal',
  '2',
  '2022-01-01',
  '20.00',
  '1'
);

-- -----------------------------------------------------
-- Table `Media_Transactions` Data Insert
-- -----------------------------------------------------

INSERT INTO `Media_Transactions` (
  `patron_id`,
  `transaction_type`,
  `employee_id`,
  `item_id`,
  `transaction_date`
) VALUES (
  '1',
  'checkout',
  '2',
  '4',
  '2022-04-25 15:21:34'
), (
  '4',
  'checkout',
  '3',
  '1',
  '2022-04-26 09:10:55'
), (
  '3',
  'checkin',
  '1',
  '5',
  '2022-04-26 11:46:34'
), (
  '2',
  'checkout',
  '4',
  '2',
  '2022-04-27 17:50:10'
);

SET FOREIGN_KEY_CHECKS=1;
SET UNIQUE_CHECKS=1;
