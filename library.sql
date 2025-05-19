
CREATE TABLE people (

    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL
);

CREATE TABLE members (
    member_id INTEGER PRIMARY KEY,
    FOREIGN KEY (member_id) REFERENCES people(person_id)
);

CREATE TABLE librarians (
    employee_id INTEGER PRIMARY KEY,
    FOREIGN KEY (employee_id) REFERENCES people(person_id)
);

CREATE TABLE books (
    code TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    is_available INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE borrowed_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    book_code TEXT NOT NULL,
    borrowed_at TEXT DEFAULT CURRENT_TIMESTAMP,
    returned_at TEXT,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_code) REFERENCES books(code)
);


INSERT INTO people (person_id,name,age,gender) VALUES
('Alice', 30, 'F'),
('Bob', 25, 'M'),
('Charlie', 35, 'M'),
('Diana', 28, 'F');

INSERT INTO members (member_id) VALUES
(1),
(2), 
(3), 
(4), 




INSERT INTO librarians (employee_id) VALUES
(1), 
(2), 
(3), 
(4), 



INSERT INTO books (code,title,author,is_available) VALUES
('B001', 'The Great Gatsby', 'F. Scott Fitzgerald', 1),
('B002', 'To Kill a Mockingbird', 'Harper Lee', 1),
('B003', '1984', 'George Orwell', 1),
('B004', 'Pride and Prejudice', 'Jane Austen', 1),
('B005', 'The Catcher in the Rye', 'J.D. Salinger', 1);

INSERT INTO borrowed_books (member_id, book_code, borrowed_at) VALUES
(1, 'B001', '2023-10-01 10:00:00'), 
(2, 'B002', '2023-10-02 11:00:00'), 
(3, 'B003', '2023-10-03 12:00:00'), 
(4, 'B004', '2023-10-04 13:00:00'), 



