import multiprocessing

def partial_sum(numbers):
    return sum(numbers)

if __name__ == "__main__":
    n = 5
    numbers = list(range(1, n + 1))

    # Bagi data menjadi 2 bagian
    mid = len(numbers) // 2
    part1 = numbers[:mid]
    part2 = numbers[mid:]

    with multiprocessing.Pool(2) as pool:
        results = pool.map(partial_sum, [part1, part2])

    total = sum(results)

    print("Kompuasi Paralel dimulai...")
    print("Hasil Parsial:", results)
    print("Hasil Paralel pertambahan:", total)