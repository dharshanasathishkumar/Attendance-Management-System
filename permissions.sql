-- 1. Get rid of the old version if it exists
DROP USER IF EXISTS 'attendance_dev'@'localhost';

-- 2. Create it fresh with your new password
CREATE USER 'attendance_dev'@'localhost' IDENTIFIED BY '!Attendance047$';

-- 3. Give it the permissions to your project database
-- (Replace 'your_project_db' with your actual database name)
GRANT ALL PRIVILEGES ON attendance_system.* TO 'attendance_dev'@'localhost';

-- 4. Finalize
FLUSH PRIVILEGES;