import json
from collections  import defaultdict

def validator(schedule_data):
    errors=[]

    teacher_busy=defaultdict(list)
    auditorium_busy=defaultdict(list)

    for lesson in schedule_data.get("lessons", []):
      auditorium=lesson["аудитория"]
      teacher=lesson["преподаватель"]
      subject=lesson["предмет"]
      subject_type=lesson["тип"]
      day=lesson["день_недели"]
      time=lesson["время"]
      id=lesson["uid"]
      group=lesson["группа"]
      course=lesson["курс"]
      key=(day, time)

      for i_teacher, i_id in teacher_busy[key]:
        if i_teacher==teacher:
          errors.append(f"{teacher} занят в {day}, {time}, курсом {course} на {subject_type}")
      teacher_busy[key].append((teacher, id))

      for i_auditorium, i_id in auditorium_busy[key]:
        if i_auditorium==auditorium:
          errors.append(f"аудитория {auditorium} занята в {day}, {time}")
      auditorium_busy[key].append((auditorium, id))
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

if __name__=="__main__":
  schedule_path="lessons.json"
  check_schedule(schedule_path)
