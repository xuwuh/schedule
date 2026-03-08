import json
from collections  import defaultdict




def validator(schedule_data):
  errors=[]

  teacher_busy=defaultdict(list)
  auditorium_busy=defaultdict(list)
  lecture_group=defaultdict(list)

  for lesson in schedule_data.get("lessons", []):
    auditorium=lesson["аудитория"].strip().lower()
    teacher=lesson["преподаватель"].strip().lower()
    subject=lesson["предмет"].strip().lower()
    subject_type=lesson["тип"].strip().lower()
    day=lesson["день_недели"].strip().lower()
    time=lesson["время"].strip().lower()
    id=lesson["uid"].strip().lower()
    group=lesson["группа"].strip().lower()
    course=lesson["курс"]
    key=(day, time)
    lect_key=(day, time, subject, course)

    if subject_type=="лекция":
      for i_teacher, i_id , i_sibject, i_course in teacher_busy[key]:
        if i_teacher==teacher:
          if i_sibject!=subject or i_course!=course:
            errors.append(f"{teacher} занят в {day}, {time}, группой {group} на {course} на лекции по предмету {subject}")
      teacher_busy[key].append((teacher, id, subject, course))

      for i_auditorium, i_id, i_sibject, i_course in auditorium_busy[key]:
        if i_auditorium==auditorium:
          if i_sibject!=subject or i_course!=course:
            errors.append(f"аудитория {auditorium} занята в {day}, {time}, группой {group} на {course} на лекции по предмету {subject}")
      auditorium_busy[key].append((auditorium, id, subject, course))

    else:
      for i_teacher, i_id, _, _ in teacher_busy[key]:
        if i_teacher==teacher:
          errors.append(f"{teacher} занят в {day}, {time}, группой {group} на {course} на {subject_type} по предмету {subject}")
      teacher_busy[key].append((teacher, id, subject, course))

      for i_auditorium, i_id, _, _ in auditorium_busy[key]:
        if i_auditorium==auditorium:
          errors.append(f"аудитория {auditorium} занята в {day}, {time}, группой {group} на {course} на {subject_type} по предмету {subject}")
      auditorium_busy[key].append((auditorium, id, subject, course))

  return errors


def check_schedule(file_path):
  with open(file_path, "r", encoding='utf-8') as f:
    schedule=json.load(f)

  errors=validator(schedule)

  if errors:
    for error in errors:
      print(error)
  else:
    print("OK")
  print(len(errors))





if __name__=="__main__":
  schedule_path="lessons.json"
  check_schedule(schedule_path)
