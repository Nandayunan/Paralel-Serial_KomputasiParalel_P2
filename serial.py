# Sequential / Serial Computing Example

n = 5
total = 0

print("Komputasi Serial dimulai...")

for i in range(1, n + 1):
    total += i
    print(f"Step {i}: total = {total}")

print("Hasil Akhir serial :", total)