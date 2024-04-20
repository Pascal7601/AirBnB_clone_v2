from test_state import session, Subjects, Student

student1 = Student(name="Pascal")
student2 = Student(name="Fide")

subj1 = Subjects(name="Calculus")
subj2 = Subjects(name="Business")
subj3 = Subjects(name="Math")

student1.subjects.extend([subj1, subj2])
student2.subjects.append(subj3)

session.add(student1)
session.add(student2)
session.commit()

print(f"{student1.subjects= }")
print(f"{student2.subjects= }")
print(f"{subj1.student= }")
