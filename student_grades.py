from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        score = self.scores[index]

        if score in range(90, 101):
            return "A"
        elif score in range(80, 90):
            return "B"
        elif score in range(70, 80):
            return "C"
        elif score in range(60, 70):
            return "D"
        elif score in range(50, 60):
            return "E"
        elif score in range(0, 50):
            return "F"

    def find(self, score):
        indexes = []

        for i in range(len(self.scores)):
            if self.scores[i] == score:
                indexes.append(i)

        return []

    def get_sorted(self):
        arr = self.scores[:]

        for i in range(len(arr) - 1):

            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def average(self):
        return sum(self.scores) / len(self.scores)

    def best(self):
        return max(self.scores)

    def worst(self):
        return min(self.scores)

    def pass_rate(self):
        passed_count = 0

        for score in self.scores:
            if score >= 50:
                passed_count += 1

        return passed_count / len(self.scores)

    def __str__(self):
        return f"StudentsGrades: {self.count()} students, average {self.average():.2f}"

    def __iter__(self):
        return iter(self.scores)

def main():
    results = StudentsGrades(random_numbers(30, 0, 100))
    full_scores_index = []

    print(f"{results.count()} students took the test.")

    for i, result in enumerate(results):
        print(f"Student {i + 1}: {result} points - {results.get_grade(i)}")

        if result == 100:
            full_scores_index.append(i)

    print(f"{len(full_scores_index)} student(s) with 100 points: {full_scores_index}")
    print(f"Sorted scores: {results.get_sorted()}")
    print(f"Average score: {results.average():.2f}")
    print(f"Best score: {results.best()}")
    print(f"Worst score: {results.worst()}")
    print(f"Pass rate: {results.pass_rate():.2f}")

if __name__ == "__main__":
    main()
    main()
    main()