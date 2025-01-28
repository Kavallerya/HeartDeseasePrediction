# Heart Disease Prediction

## Cel projektu
Celem projektu jest stworzenie modelu uczenia maszynowego do przewidywania obecności chorób serca na podstawie parametrów medycznych pacjenta. Rozwiązanie to może wspierać wczesną diagnostykę i zmniejszać ryzyko dla zdrowia.

---

## Dane
W projekcie wykorzystano zbior danych **Heart Disease Dataset** z 1988 roku, który  łączy cztery bazy danych (Cleveland, Hungary, Switzerland i Long Beach V). Analiza obejmuje podzbior zawierający 14 atrybutów.

### Główne atrybuty:

- **age** - wiek pacjenta (w latach).
- **sex** - płeć pacjenta:
  - `0` - kobieta
  - `1` - mężczyzna
- **cp** - rodzaj bólu w klatce piersiowej:
  - `0` - Brak bólu
  - `1` - Nietypowa dławica piersiowa
  - `2` - Ból niezwiązany z sercem
  - `3` - Typowa dławica piersiowa
- **trestbps** - ciśnienie krwi w spoczynku (mm Hg).
- **chol** - poziom cholesterolu we krwi (mg/dl).
- **fbs** - poziom cukru we krwi na czczo (> 120 mg/dl):
  - `1` - tak
  - `0` - nie
- **restecg** - wyniki elektrokardiogramu:
  - `0` - Normalny
  - `1` - Nieprawidłowości fali ST-T
  - `2` - Przeciążenie lewej komory
- **thalach** - maksymalna częstość akcji serca.
- **exang** - wysiłkowa dławica piersiowa:
  - `1` - tak
  - `0` - nie
- **oldpeak** - obniżenie odcinka ST w porównaniu ze stanem spoczynkowym.
- **nachylenie** - nachylenie odcinka ST podczas szczytowego wysiłku:
  - `0` - rosnące
  - `1` - Płaskie
  - `2` - Nachylenie w dół
- **ca** - liczba głównych naczyń (od 0 do 4) wybarwionych za pomocą fluoroskopii.
- **thal** - status talasemii:
  - `0` - Normalny
  - `1` - Utrwalony defekt




---

## Etapy pracy

### 1. Analiza danych
- Sprawdzono rozkład zmiennej docelowej, aby ocenić równowagę klas.
- Zwizualizowano korelacje między atrybutami przy użyciu macierzy korelacji.

Po przeanalizowaniu macierzy możemy zobaczyć, które klasy mają największy wpływ na
ryzyko chorób serca

### 2. Przygotowanie danych
- Podzielono dane na zbior treningowy (70%) i testowy (30%).
- Przeskalowano dane dla modelu **Logistic Regression**.

### 3. Trenowanie modeli
Zastosowano trzy algorytmy:
- **Random Forest Classifier**;
- **Gradient Boosting Classifier**;
- **Logistic Regression** (z przeskalowanymi danymi).

### 4. Ocena modeli
- Użyto metryk:
    - **Accuracy**,
    - **Precision**,
    - **Recall**,
    - **F1 Score**,
    - **AUC**.
- Stworzono krzywe **ROC** dla każdego modelu.
- Stworzono diagram porównujący wydajność modeli .

### 5. Testowanie
- Zapisano najlepsze modele w formacie `.joblib`.
- Opracowano funkcję przewidującą obecność chorób serca na podstawie nowych danych medycznych pacjenta.

---

## Główne wyniki
- **Random Forest Classifier** osiągnął najwyższy wynik AUC = **0.998**, wykazując najlepsza zdolność do rozróżniania klas.
- **Gradient Boosting Classifier** osiągnął AUC = **0.98**, co zapewnia równowagę między precyzją a czułością.
- **Logistic Regression** uzyskał AUC = **0.925**, co potwierdza jego skuteczność po przeskalowaniu danych.

---

## Wnioski
- **Random Forest Classifier** jest najlepszym wyborem dla precyzyjnego przewidywania.
- **Logistic Regression** zapewnia szybkie działanie oraz łatwą interpretację wyników.

---

## Demonstracja
Model jest zdolny do przewidywania obecności chorób serca na podstawie nowych danych medycznych pacjenta.

