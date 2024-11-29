--Schema
data = [[1, 'Alice'], [2, 'Bob'], [13, 'John'], [6, 'Alex']]
students = pd.DataFrame(data, columns=['student_id', 'student_name']).astype({'student_id':'Int64', 'student_name':'object'})
data = [['Math'], ['Physics'], ['Programming']]
subjects = pd.DataFrame(data, columns=['subject_name']).astype({'subject_name':'object'})
data = [[1, 'Math'], [1, 'Physics'], [1, 'Programming'], [2, 'Programming'], [1, 'Physics'], [1, 'Math'], [13, 'Math'], [13, 'Programming'], [13, 'Physics'], [2, 'Math'], [1, 'Math']]
examinations = pd.DataFrame(data, columns=['student_id', 'subject_name']).astype({'student_id':'Int64', 'subject_name':'object'})

--Solution
import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    student_subject_combo = pd.merge(students, subjects, how = 'cross')
    examinations = examinations.groupby(['student_id','subject_name']).agg(attended_exams=('student_id','value_counts')).reset_index()
    result = pd.merge(student_subject_combo, examinations, on = ['student_id','subject_name'], how='left')
    result['attended_exams'] = result['attended_exams'].fillna(0)
    result = result.sort_values(['student_id','subject_name'])
    return result[['student_id','student_name','subject_name','attended_exams']]
