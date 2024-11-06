import pandas as pd
import random

'''
Aufgabenstellung:
Oft haben Studierende das Gefühl, dass ihre Note in einem Modul gar nicht nur von ihrer Leistung
abhängt - deshalb schreiben wir uns heute ein absichtlich unfaires Benotungsprogramm!
(a) Das Programm bekommt die eigentliche Prüfungsnote, das heutige Wetter (sonnig, wolkig, regnerisch,
stürmisch) als Eingabe, sowie das Betriebssystem, das vom Prüfling genutzt wird
(Windows, Linux, Mac). Je schöner das Wetter, je besser die Prüfungsnote. Wolkiges Wetter
hat dabei keinen Einfluss, sonniges Wetter führt zu 0.3 Punkten Verbesserung, Regen zu 0.3 Punkten
Verschlechterung und Sturm sogar zu 0.6 Punkten Verschlechterung.
Wie jeder weiß sind Informatiker:innen Linux-Fans! Arbeiten die Prüflinge unter Linux, gibt es
dewegen eine ganze Note besser! Für Windows gibt es 0.3 Noten schlechter und für Mac 1.0 Notenpunkte
Abzug.
(b) Für alle Studierenden die Noten einzeln über die Eingabezeile einzugeben ist eigentlich
zu anstrengend. Schreibt das Programm so um, dass es eine csv Datei einliest, in der die
Namen, Noten und das Betriebssystem der Studierenden steht. Beim Programmstart wird also nur noch
nach dem Wetter gefragt.
(c) Die Abgabe der Studierenden an sich zu benoten ist eigentlich auch viel zu viel Arbeit.
Streicht die ursprüngliche Note aus der csv Datei und schreibt das Programm so um,
dass die ursprüngliche Note einfach gewürfelt wird.  Das Wetter und das
Betriebssystem haben weiterhin die gleiche Auswirkung wie bisher.
'''

class Grading:
    def __init__(self, csv_path = None):
        if csv_path:
            self.df = pd.read_csv(csv_path, encoding="utf-8")
        else:
            self.df = pd.DataFrame(columns=["Name", "Note", "Betriebssystem"])

    def overwrite_grades(self):
        grade_list = [0.7, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3, 4.7, 5.0]
        for i in range(len(self.df)):
            self.df.loc[i, "Note"] = random.choice(grade_list)

    def get_values(self):
        name = input("Name des Studierenden:")
        weather = input("Wie ist das Wetter heute?")
        grade = float(input("welche Prüfungsnote (Deutsches Notensystem) wollen Sie geben?"))
        os = input("Welches Betriebssystem wurde verwendet?")
        return name, grade, weather, os

    def calc_grade(self):
        grade_list = [0.7, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3, 4.7, 5.0]
        weather_dict = {"sonnig": -0.3, "wolkig": 0, "regnerisch": 0.3, "stürmisch": 0.6}
        os_dict = {"Windows": 0.3, "Linux": -1, "Mac": 1}

        if self.df.empty:
            while True:
                name, grade, weather, os = self.get_values()
                if weather in weather_dict and os in os_dict and grade in grade_list:
                    grade = grade + weather_dict[weather] + os_dict[os]
                    closest_grade = min(grade_list, key=lambda x: abs(x - grade))
                    self.df = self.df._append({"Name": name, "Note": closest_grade, "Betriebssystem": os}, ignore_index=True)
                    break
                else:
                    print("Falsche Eingabe")
        
        else:
            while True:
                weather = input("Wie ist das Wetter heute?")
                if weather in weather_dict:
                    break
                else:
                    print("Falsche Eingabe")

            for i in range(len(self.df)):
                name = self.df.loc[i, "Name"]
                grade = self.df.loc[i, "Note"]
                os = self.df.loc[i, "Betriebssystem"]

                closest_grade = min(grade_list, key=lambda x: abs(x - grade))

                self.df.loc[i, "Note"] = closest_grade

if __name__ == "__main__":
    # a
    print("a")
    g = Grading()
    g.calc_grade()
    print(g.df)
    # b
    print("\nb")
    path = input("Pfad zur csv Datei:")
    g.calc_grade()
    print(g.df)
    #c
    print("\nc")
    g.overwrite_grades()
    g.calc_grade()
    print(g.df)