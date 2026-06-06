
"""Contoh Input/Output di Python dalam gaya OOP: simple, medium, advanced.

Setiap contoh dibungkus dalam kelas dengan metode `run()` sehingga mudah di-extend
atau diuji.
"""

import contextlib
import json
import gzip
import mmap
from pathlib import Path
from typing import Optional


class IOExample:
	"""Base class untuk contoh I/O."""

	def run(self):  
		raise NotImplementedError()


class SimpleIO(IOExample):
	def __init__(self, out_path: Optional[Path] = None):
		self.out = out_path or Path("simple_output.txt")

	def run(self):
		print("--- Simple I/O (OOP) ---")
		try:
			name = input("Masukkan nama Anda: ")
			with self.out.open("w", encoding="utf-8") as f:
				f.write(f"Halo, {name}!\n")
			print(f"Tersimpan di {self.out}")
		except OSError as e:
			print("Gagal menulis file:", e)
		print()


class MediumIO(IOExample):
	"""Medium: baca/ tulis JSON, tangani FileNotFound dan parsing error."""

	def __init__(self, path: Optional[Path] = None):
		self.path = path or Path("data.json")
		self.sample = {"items": [1, 2, 3], "meta": {"owner": "user"}}

	def ensure_sample(self):
		if not self.path.exists():
			self.path.write_text(json.dumps(self.sample, indent=2), encoding="utf-8")
			print("File contoh data.json dibuat.")

	def run(self):
		print("--- Medium I/O (JSON, OOP) ---")
		try:
			self.ensure_sample()
		except OSError as e:
			print("Gagal membuat file:", e)
			return

		try:
			text = self.path.read_text(encoding="utf-8")
			data = json.loads(text)
			print("Isi data.json:", data)
		except FileNotFoundError:
			print("File tidak ditemukan — seharusnya sudah dibuat di atas.")
		except json.JSONDecodeError as e:
			print("JSON invalid:", e)
		except Exception as e:
			print("Kesalahan saat membaca/ parsing:", e)
		print()


class AdvancedIO(IOExample):
	"""Advanced: tulis file terkompresi gzip lalu baca menggunakan mmap.

	Menunjukkan operasi biner, context managers, dan mmap untuk akses cepat.
	"""

	def __init__(self, gz_path: Optional[Path] = None, tmp_path: Optional[Path] = None):
		self.gz_path = gz_path or Path("big-data.txt.gz")
		self.tmp_path = tmp_path or Path("big-data.txt")

	def write_gzip(self):
		with gzip.open(self.gz_path, "wt", encoding="utf-8") as gz:
			for i in range(100):
				gz.write(f"Line {i}\n")
		print(f"Tertulis {self.gz_path}")

	def uncompress_to_tmp(self):
		with gzip.open(self.gz_path, "rt", encoding="utf-8") as gz, self.tmp_path.open("w", encoding="utf-8") as out:
			out.write(gz.read())

	def read_via_mmap(self):
		with self.tmp_path.open("r+b") as f:
			mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
			try:
				sample = mm.readline().decode("utf-8").strip()
				print("Baris pertama dari mmap:", sample)
			finally:
				mm.close()

	def run(self):
		print("--- Advanced I/O (gzip + mmap, OOP) ---")
		try:
			self.write_gzip()
			self.uncompress_to_tmp()
			self.read_via_mmap()
		except Exception as e:
			print("Kesalahan advanced I/O:", e)
		finally:
			with contextlib.suppress(OSError):
				self.tmp_path.unlink()
		print()


def _make_example(name: str) -> IOExample:
	name = name.lower()
	if name == "simple":
		return SimpleIO()
	if name == "medium":
		return MediumIO()
	if name == "advanced":
		return AdvancedIO()
	raise ValueError("Unknown example")


print("Demo I/O (OOP): pilih contoh yang ingin dijalankan atau tekan Enter untuk semua.")
choice = input("Pilih (simple/medium/advanced/all): ").strip().lower()
if choice in ("", "all"):
    SimpleIO().run()
    MediumIO().run()
    AdvancedIO().run()
else:
    try:
        _make_example(choice).run()
    except ValueError:
        print("Pilihan tidak dikenal. Keluar.")

