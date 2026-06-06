# Contoh exception handling di Python: simpel, medium, dan advanced.

import contextlib
import logging
import time

def simple_example():
	# Contoh sederhana: menangani ZeroDivisionError dan menampilkan else/finally.
	# ZeroDivisionError adalah salah satu built-in exception untuk pembagian dengan nol.
	# built-in exception lainnya: FileNotFoundError, ValueError, KeyError, TypeError, dll.
	print("--- Simple Example ---")
	try:
		a = 10
		b = 0
		result = a / b
	except ZeroDivisionError:
		print("Caught ZeroDivisionError: tidak bisa membagi dengan nol")
	else:
		print("Hasil:", result)
	finally:
		print("Selesai contoh simpel\n")


def _read_number_from_file(path: str) -> int:
	with open(path, "r") as f:
		return int(f.read().strip())


def medium_example():
	# Contoh menengah: file I/O, pengecekan nilai, dan beberapa except berbeda.
	print("--- Medium Example ---")
	path = "data.txt"
	try:
		n = _read_number_from_file(path)
		if n < 0:
			raise ValueError("Nilai harus non-negatif")
		print("Angka dari file:", n)
	except FileNotFoundError:
		print(f"File {path} tidak ditemukan — membuat file contoh.")
		with open(path, "w") as f:
			f.write("42")
		print("File dibuat. Jalankan lagi jika ingin membaca nilainya.")
	except ValueError as e:
		print("Kesalahan nilai:", e)
	except Exception as e:
		print("Kesalahan tidak terduga:", e)
	else:
		print("Sukses membaca dan memvalidasi file.")
	finally:
		print("Selesai contoh medium\n")

class DatabaseConnectionError(Exception):
	pass

def _connect_to_db_sim(retries: int = 3):
	"""
	Simulasi koneksi DB dengan retry. Pada percobaan gagal, melempar ConnectionError.
	Jika semua percobaan gagal, melempar DatabaseConnectionError (raise from untuk chaining).
	"""
	for attempt in range(1, retries + 1):
		try:
			if attempt < retries:
				raise ConnectionError("timeout")
			return "koneksi-terbuka"
		except ConnectionError as e:
			logging.warning("Attempt %d gagal: %s", attempt, e)
			if attempt == retries:
				raise DatabaseConnectionError("Gagal koneksi setelah beberapa percobaan") from e
			time.sleep(0.1)

def advanced_example():
	# Contoh advanced: custom exception, exception chaining, dan contextlib.suppress.
	print("--- Advanced Example ---")
	try:
		conn = _connect_to_db_sim(retries=3)
	except DatabaseConnectionError as e:
		print("Tidak bisa terhubung ke DB:", e)
		if e.__cause__:
			print("Penyebab asli (chained):", repr(e.__cause__))
	else:
		print("Terhubung:", conn)

	# contoh penggunaan contextlib.suppress untuk mengabaikan exception yang diharapkan
	with contextlib.suppress(FileNotFoundError):
		open("no-such-file.txt").close()

	print("Selesai contoh advanced\n")

simple_example()
medium_example()
advanced_example()

