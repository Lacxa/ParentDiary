from datetime import datetime


class Transfer:
    current_time = str(datetime.now())
    date, time = current_time.strip().split()
    week_day = ""
    day = ""
    point = '1'
    bought = '1'
    loyal = '1'
    orders = '1'
    number = 0
    order_id = '123'

    def check_student(self, level, idd):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("school-diary-f3a73-firebase-adminsdk-xvqli-73aadbafa6.json")
                initialize_app(cred, {'databaseURL': 'https://school-diary-f3a73-default-rtdb.firebaseio.com/'})
                ref = db.reference('Diary').child("classes")
                data = ref.get()

                if level in data:
                    if idd in data[level]["students"]:
                        info = data[level]["students"][idd]
                        return info
                    else:
                        return "No"
                else:
                    return "Noclass"

    def fetch_homework(self, level):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("school-diary-f3a73-firebase-adminsdk-xvqli-73aadbafa6.json")
                initialize_app(cred, {'databaseURL': 'https://school-diary-f3a73-default-rtdb.firebaseio.com/'})
                ref = db.reference('Diary').child("classes").child(level).child("homework").child(self.year()).child(
                    self.month_date())
                data = ref.get()

                one = data["Homework"]
                return one

    def get_attendance(self, level, i):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("school-diary-f3a73-firebase-adminsdk-xvqli-73aadbafa6.json")
                initialize_app(cred, {'databaseURL': 'https://school-diary-f3a73-default-rtdb.firebaseio.com/'})
                ref = db.reference('Diary').child("classes").child(level).child("Attendance").child(self.year()).child(
                    self.month_date())
                data = ref.get()
                if i in data:
                    return "present"

                elif i not in data:
                    return "absent"



    def year(self):
        current_time = str(datetime.now())
        date, time = current_time.strip().split()
        y, m, d = date.strip().split("-")

        return y

    def month_date(self):
        current_time = str(datetime.now())
        date, time = current_time.strip().split()
        y, m, d = date.strip().split("-")

        return f"{m}_{d}"

# Transfer.get_attendance(Transfer(), "class3", "KVKn2u")
# Transfer.fetch_homework(Transfer(), "class3")
