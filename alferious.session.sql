CREATE TABLE temp_members AS SELECT email,phone,understood,parent_name
FROM members;
DROP TABLE members;
ALTER TABLE temp_members RENAME to members
