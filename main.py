import pandas as pd
import json

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






print(validEmployeesForXML)