import joblib
import pandas as pd

filename = 'finalized_model.sav'
loaded_model = joblib.load(filename)

valtest = [2.909760729608066, 1971.0979494860405, 701.6631206560565, 105.60923058163786, 22.059723953514393, 285.2339273251449, 480.75726038836507, 2437.0199990716437, 214.74787711509032, 90.0, 6.81938553412735, 58.38297644603422]

parameters = ['Соотношение матрица-наполнитель',
 'Плотность, кг/м3',
 'модуль упругости, ГПа',
 'Количество отвердителя, м.%',
 'Содержание эпоксидных групп,%_2',
 'Температура вспышки, С_2',
 'Поверхностная плотность, г/м2',
 'Прочность при растяжении, МПа',
 'Потребление смолы, г/м2',
 'Угол нашивки, град',
 'Шаг нашивки',
 'Плотность нашивки']
range = ['(0.88.....8.5)',
         '(2300......3882)',
         '(4......2391)',
         '(50......291)',
         '(20......48)',
         '(260......636)',
         '(3.....1791)',
         '(2000.....3000)',
         '(90.....590)',
         '(0...173)',
         '(1.....21)',
         '(39....138)']
dftest = pd.DataFrame([valtest], columns=parameters)

val = []
i = 0
print("Модель прогноза- 'Модуль упругости при растяжении,ГПа %' ")
param_value = []
while i < len(parameters):
    line = f" {parameters[i]}{range[i]}: "

    while True:
        try:
            param_val = input(line)
            param_value = float(param_val)
        except:
            print("ОШИБКА! введите числовое значение")
            continue
        break
    val.append(param_value)
    i += 1

df = pd.DataFrame([val], columns=parameters)
test_predictions = loaded_model.predict(df)[0]

print(" Прогнозное значение Модуль упругости при растяжении в ГПа :", str(test_predictions))