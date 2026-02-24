import time
import random

# Fungsi untuk membuat matrix ukuran n x n
def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# =========================
# SERIAL VERSION
# =========================
# Pada versi serial:
# - Hanya menggunakan 1 core CPU
# - Setiap baris dan kolom dihitung secara berurutan
# - Tidak ada pembagian pekerjaan
# - Proses berjalan satu per satu (sequential)

def multiply_serial(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]

    # Loop pertama: memilih baris dari matrix A
    for i in range(n):
        # Loop kedua: memilih kolom dari matrix B
        for j in range(n):
            # Loop ketiga: menghitung hasil perkalian baris dan kolom
            for k in range(n):
                # Proses perkalian dan penjumlahan dilakukan satu per satu
                result[i][j] += A[i][k] * B[k][j]

    # Semua baris selesai dihitung secara berurutan
    return result


n = 150
A = generate_matrix(n)
B = generate_matrix(n)

start = time.time()

print("=== SERIAL EXECUTION ===")
C = multiply_serial(A, B)

end = time.time()

print("Serial time:", end - start, "seconds")

# PENJELASAN SERIAL:
# Baris 0 dihitung → selesai
# Baris 1 dihitung → selesai
# Baris 2 dihitung → selesai
# Semua dilakukan oleh 1 core CPU secara berurutan