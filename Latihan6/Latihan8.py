from pathos.multiprocessing import ProcessPool
def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)
if __name__ == '__main__':
    # Buat ProcessPool dengan 2 proses
    pool = ProcessPool(2)
    pool.map(worker, range(5))