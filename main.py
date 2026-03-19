import joblib

model = joblib.load("model.pkl")

hours = float(input("Enter study hours: "))

prediction = model.predict([[hours]])

if prediction[0] == 1:
    print("Student will PASS")
else:
    print("Student will FAIL")