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

    def check_student(self,level, idd):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("school-diary-f3a73-firebase-adminsdk-xvqli-73aadbafa6.json")
                initialize_app(cred, {'databaseURL': 'https://school-diary-f3a73-default-rtdb.firebaseio.com/'})
                ref = db.reference('Diary').child("classes").child(level).child("students").child(idd)
                data = ref.get()
                if idd in data:
                    return data

                elif level not in data:
                    return "Noclass"

                else:
                    return "NO"

