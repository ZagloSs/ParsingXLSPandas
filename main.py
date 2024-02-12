import pandas as pd
import json
from datetime import date
from openpyxl.workbook import Workbook

employeesJson = open("employees.json")
employeesData = json.load(employeesJson)
validEmployeesForXML = []

def changeCurrency(str):
    strNoDol = str[1::]
    strEur = strNoDol + "€"
    return strEur

def addTenPercent(stri):
    salary = stri[:-1:]
    strSalary = salary.split(",")
    separator = ""
    floatSalary = float(separator.join(strSalary))
    floatSalary *= 1.10
    stringFinal = str(floatSalary) + "€"
    return stringFinal


# Descartar todos los trabajadores del proyecto GRONK
for employee in employeesData:
    if employee['proyect'] != "GRONK":
        validEmployeesForXML.append(employee)

# Cambio todos los salarios por € y sumo el 10% extra a los menores de 30 años
for employee in validEmployeesForXML:
    employee['salary'] = changeCurrency(employee['salary'])
    if employee['age'] < 30:
        employee['salary'] = addTenPercent(employee['salary'])

salary = []
age = []
name = []
gender = []
proyect = []
email = []
for employee in validEmployeesForXML:
    salary.append(employee['salary'])
    age.append(employee['age'])
    name.append(employee['name'])
    gender.append(employee['gender'])
    proyect.append(employee['proyect'])
    email.append(employee['email'])


pf = pd.DataFrame({"Salary": salary, "Age": age, "Name": name, "Gender": gender, "Proyect": proyect, "email": email})
hoy = str(date.today())
fecha = hoy.split("-")


excelName = "pagos-empleados-" + fecha[1] + "-" + fecha[0]+".xlsx"

pf.to_excel(excelName)

