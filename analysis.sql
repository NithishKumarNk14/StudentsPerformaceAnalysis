-- Average score by gender
SELECT gender, AVG(math_score) AS avg_math
FROM students
GROUP BY gender;

-- Effect of study hours
SELECT weekly_self_study_hours, AVG((math_score+english_score)/2) AS avg_score
FROM students
GROUP BY weekly_self_study_hours;

-- Attendance vs performance
SELECT absence_days, AVG(math_score) AS avg_math
FROM students
GROUP BY absence_days;
