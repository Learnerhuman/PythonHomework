---task1
CREATE TABLE Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
);
INSERT INTO Roster (Name, Species, Age) VALUES
('Benjamin Sisko', 'Human', 40),
('Jadzia Dax', 'Trill', 300),
('Kira Nerys', 'Bajoran', 29);
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';
DELETE FROM Roster
WHERE Age > 100;
ALTER TABLE Roster
ADD COLUMN Rank TEXT;
UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko';
UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax';
UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys';
SELECT *
FROM Roster
ORDER BY Age DESC;
---task2
CREATE TABLE Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
);
INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES
('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
('1984', 'George Orwell', 1949, 'Dystopian'),
('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic');
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984';
SELECT Title, Author
FROM Books
WHERE Genre = 'Dystopian';
DELETE FROM Books
WHERE Year_Published < 1950;
ALTER TABLE Books
ADD COLUMN Rating REAL;
SELECT *
FROM Books
ORDER BY Year_Published ASC;
