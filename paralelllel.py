import multiprocessing
import time
import random

def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# =========================
# PARALLEL VERSION
# =========================
# Pada versi parallel:
# - Menggunakan banyak core CPU
# - Setiap baris matrix dihitung secara bersamaan
# - Pekerjaan dibagi ke beberapa proses
# - Proses berjalan simultan (bersamaan)

# Fungsi ini hanya menghitung SATU BARIS hasil matrix
def multiply_row(args):
    A_row, B = args
    n = len(B)
    result_row = []

    # Menghitung satu baris penuh
    for j in range(n):
        total = 0
        for k in range(n):
            total += A_row[k] * B[k][j]
        result_row.append(total)

    return result_row


if __name__ == "__main__":
    n = 150
    A = generate_matrix(n)
    B = generate_matrix(n)

    print("=== PARALLEL EXECUTION ===")

    start = time.time()

    # Pool akan membuat beberapa proses sesuai jumlah core CPU
    # Setiap proses akan mengerjakan satu baris matrix secara bersamaan
    with multiprocessing.Pool() as pool:
        C = pool.map(multiply_row, [(row, B) for row in A])

    end = time.time()

    print("Parallel time:", end - start, "seconds")

# PENJELASAN PARALLEL:
# Baris 0   → dihitung oleh Core 1
# Baris 1   → dihitung oleh Core 2
# Baris 2   → dihitung oleh Core 3
# Baris 3   → dihitung oleh Core 4
# ...
# Semua baris bisa dihitung secara bersamaan
#
# Inilah perbedaan utama:
# SERIAL   → satu baris selesai dulu baru lanjut baris berikutnya
# PARALLEL → banyak baris dihitung secara bersamaan oleh banyak core