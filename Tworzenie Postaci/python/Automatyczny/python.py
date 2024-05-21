import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import ttk

def get_class_description(file_path, selected_class):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().split('\n\n')
            for section in data:
                if selected_class in section:
                    return section
        return "Description not found for this class."
    except FileNotFoundError:
        return "File not found."

def get_race_description(file_path, selected_race):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().split('\n\n')
            for section in data:
                if selected_race in section:
                    return section
        return "Description not found for this race."
    except FileNotFoundError:
        return "File not found."

def get_main_description(file_path, selected_race):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().split('\n\n')
            for section in data:
                if selected_race in section:
                    return section
        return "Description not found for this race."
    except FileNotFoundError:
        return "File not found."

def predict_character():
    selected_race = race_combobox.get()
    selected_class = class_combobox.get()

    if selected_race in race_map and selected_class in class_map:
        race_label_enc = race_map[selected_race]
        class_label_enc = class_map[selected_class]

        selected_race_enc = race_encoder.transform([selected_race])[0]
        selected_class_enc = class_encoder.transform([selected_class])[0]

        prediction = dtree.predict([[selected_race_enc, selected_class_enc]])

        if prediction:
            predicted_character = prediction[0]
            result_label.config(text=f"Wybrana postać: {predicted_character}")
            
            main_description = get_main_description('main_descriptions.txt', predicted_character)
            main_description = main_description.split(':', 1)[-1].strip() if ':' in main_description else main_description
            result_description_label.config(text=main_description)
        else:
            result_label.config(text="Prediction not found in map.")
    else:
        result_label.config(text="Please select a valid race and class.")


df = pd.read_csv("csv.csv", delimiter=';')

race_encoder = LabelEncoder()
class_encoder = LabelEncoder()

df['wybierz_rase_enc'] = race_encoder.fit_transform(df['wybierz_rase'])
df['wybierz_klase_enc'] = class_encoder.fit_transform(df['wybierz_klase'])

race_map = dict(zip(df['wybierz_rase'], df['wybierz_rase_enc']))
class_map = dict(zip(df['wybierz_klase'], df['wybierz_klase_enc']))
inverse_race_map = {v: k for k, v in race_map.items()}

features = ['wybierz_rase_enc', 'wybierz_klase_enc']
X = df[features]
y = df['postac']

dtree = DecisionTreeClassifier()
dtree.fit(X, y)

root = tk.Tk()
root.title("Przewidywanie Postaci")

main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

race_frame = tk.Frame(main_frame)
race_frame.pack()

race_label = tk.Label(race_frame, text="Wybierz rase:")
race_label.pack(side=tk.LEFT, padx=10)

races = list(race_map.keys())
race_combobox = ttk.Combobox(race_frame, values=races, width=30)
race_combobox.pack(side=tk.LEFT)

race_description_label = tk.Label(main_frame, text="", wraplength=400)
race_description_label.pack(pady=5)

class_frame = tk.Frame(main_frame)
class_frame.pack()

class_label = tk.Label(class_frame, text="Wybierz Klase:")
class_label.pack(side=tk.LEFT, padx=10)

classes = list(class_map.keys())
class_combobox = ttk.Combobox(class_frame, values=classes, width=30)
class_combobox.pack(side=tk.LEFT)

class_description_label = tk.Label(main_frame, text="", wraplength=400)
class_description_label.pack(pady=5)

predict_button = tk.Button(main_frame, text="Przewidywany wynik", command=predict_character)
predict_button.pack(pady=10)

result_label = tk.Label(main_frame, text="", font=("Arial", 12))
result_label.pack()

result_description_label = tk.Label(main_frame, text="", wraplength=400)
result_description_label.pack(pady=5)


def update_race_description(event):
    selected_race = race_combobox.get()
    race_description = get_race_description('race_descriptions.txt', selected_race)
    race_description = race_description.split(':', 1)[-1].strip() if ':' in race_description else race_description
    race_description_label.config(text=race_description)


race_combobox.bind("<<ComboboxSelected>>", update_race_description)

def update_class_description(event):
    selected_class = class_combobox.get()
    class_description = get_class_description('class_descriptions.txt', selected_class)
    class_description = class_description.split(':', 1)[-1].strip() if ':' in class_description else class_description
    class_description_label.config(text=class_description)

class_combobox.bind("<<ComboboxSelected>>", update_class_description)

root.mainloop()
