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

def berechne_note(note, wetter, betriebssystem):
    pass

note = input("Prüfungsnote (von 1 - 5 mit einer Nachkommazahl)")
wetter = input("Wie ist das Wetter heute?")
betriebssystem = input("Unter welchem Betriebssystem wurde programmiert?")
berechne_note(note,wetter,betriebssystem)
