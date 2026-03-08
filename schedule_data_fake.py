import json
import random
from faker import Faker

fake=Faker('ru_RU')

n_auditoriums =10
n_teachers= 10
n_subject= 5
n_groups= 5

#аудитории
aud_campacity=[1,2,3,4]
aud_campasity_prods=[0.5, 0.05, 0.05, 0.4]

auditoriums=[]
for i in range(1, n_auditoriums+1):
  auditoriums.append({
      "id": i,
      "номер": 100+i,
      "вместимость": random.choices(aud_campacity, aud_campasity_prods)[0],
      "тип аудитории": random.choice([0,1]) #1-тех, 0-не тех
  })

#преподаватели
teachers_name=[]
for _ in range(n_teachers):
  teachers_name.append(fake.name())

teachers=[]
for i in range(1, n_teachers+1):
  num_subjects=random.randint(1,3)
  sub_to_teach={subj_id:[] for subj_id in range(1,n_subject+1)}
  analable_subj=[subj_id for subj_id in range(1, n_subject+1) if len (sub_to_teach[subj_id])<3]

  if not analable_subj:
    analable_subj=list(range(1, n_subject+1))
  teachers_subject=random.sample(analable_subj, min(num_subjects, len(analable_subj)))

  teachers.append({
      "id": i,
      "ФИО": teachers_name[i-1],
      "преподает предметы (id)": teachers_subject
  })

for subj_id in range(1, n_subject+1):
  if len(sub_to_teach[subj_id])==0:
    teach_id=random.randint(1, n_teachers)
    sub_to_teach[subj_id].append(teach_id)
    teachers[teach_id-1]["преподает предметы (id)"].append(subj_id)

#предметы
subject=[]
subject_name=[
    "математика", "русский", "литература", "информатика", "естествознание", "экономика", "философия"
]
for i in range(1, n_subject+1):
  sub_name=subject_name[i-1]
  for typ in [1,0]: #1-лекция, 0-семинар
    subject.append({
        "id": len(subject)+1,
        "название": sub_name,
        "часы в неделю": random.randrange(2,8,2),
        "тип занятия": typ
    })

  #группы
  groups=[]
  for i in range(1, n_groups+1):
    groups.append({
        "id": i,
        "номер": random.randint(1, 10),
        "курс": random.randint(1, 3)
    })

  #сборка в один словарь
  data={
      "аудитории": auditoriums,
      "преподаватели": teachers,
      "предметы": subject,
      "группы": groups
  }


#сохранение файла
with open("schedule_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
print("база данных сохранена")
