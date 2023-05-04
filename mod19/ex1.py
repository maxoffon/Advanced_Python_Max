import sqlite3

hardest_ex = """
select full_name as teacher, avg(grade) as avg_grade
from assignments_grades
join (select * from assignments left join teachers on assignments.teacher_id = teachers.teacher_id) as t1
on assignments_grades.assisgnment_id = t1.assisgnment_id
group by teacher
order by avg_grade
limit 1"""

best_st = """
select full_name as student, avg(grade) as avg_grade
from assignments_grades
join students
on assignments_grades.student_id = students.student_id
group by student
order by avg_grade desc
limit 10"""

easiest_ex_students = """
select full_name as student 
from students
left join (select group_id, full_name as teacher_name from students_groups left join teachers on students_groups.teacher_id = teachers.teacher_id) as t1
on students.group_id = t1.group_id
where teacher_name = (select teacher from (select full_name as teacher, avg(grade) as avg_grade
from assignments_grades
join (select * from assignments left join teachers on assignments.teacher_id = teachers.teacher_id) as t1
on assignments_grades.assisgnment_id = t1.assisgnment_id
group by teacher
order by avg_grade
limit 1))"""

min_max_avg_expired_ex = """
select group_id, min(expired) as min_exp, avg(expired) as avg_exp, max(expired) as max_exp
from (
select student_id, count(date_cur) as expired
from (
select student_id, date as date_cur, due_date as date_to
from assignments_grades
join assignments
on assignments_grades.assisgnment_id = assignments.assisgnment_id
where date_to < date_cur)
group by student_id) as expired
left join students
on expired.student_id = students.student_id
group by group_id
"""

read_memorize = """
select avg(grade) as avg_read_memorize
from assignments_grades
join assignments
on assignments_grades.assisgnment_id = assignments.assisgnment_id
where assignment_text like 'прочитать%' or assignment_text like 'выучить%'"""

group_analysis = """
select t1.group_id,
group_stud_count,
group_avg,
group_stud_count - submitted_count as group_not_submitted,
group_expired,
group_retry
from
(select group_id, count(student_id) as group_stud_count from students
group by group_id)
natural join
(select group_id, avg(grade) as group_avg, count(distinct students.student_id) as submitted_count
from assignments_grades
natural join students
group by group_id) as t1
left join
(select group_id, count(distinct student_id) as group_expired
from assignments_grades
natural join
(select assisgnment_id, due_date from assignments)
natural join
(select student_id, group_id from students)
where due_date < date
group by group_id) as t2
on t1.group_id = t2.group_id
natural join
(select group_id, count(*) as group_retry
from (select student_id, assisgnment_id, count(*) as group_retry
from assignments_grades
natural join students
group by student_id, assisgnment_id
having group_retry > 1) as temp_t
left join students on temp_t.student_id = students.student_id
group by group_id)"""


with sqlite3.connect("homework.sqlite") as conn:
    c = conn.cursor()
    for i in [hardest_ex, easiest_ex_students, best_st, min_max_avg_expired_ex, read_memorize, group_analysis]:
        for line in c.execute(i):
            print(line)
        print('\n')
