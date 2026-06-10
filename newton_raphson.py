# ============================================================
#  ESTIMASI TITIK IMPAS USAHA KECIL
#  Metode Newton-Raphson dengan Konvergensi Kuadratik
# ============================================================
#  Kelompok 7 - Metode Numerik (Semester Genap 2024/2025)
#  1. Sami Aji               (C2455201001)
#  2. Harits Akbar Al Madhani (C2455201002)
#  3. Riansyah               (C2455201003)
#  Program Studi : Teknik Informatika
#  Universitas   : STMIK Palangka Raya
# ============================================================

import numpy as np

# ------------------------------------------------------------
# 1. DEFINISI FUNGSI LABA DAN TURUNANNYA
# ------------------------------------------------------------
# Model fungsi laba non-linier:
#   f(x)  = 0.5x^3 - 4x^2 + 8x - 3
#   f'(x) = 1.5x^2 - 8x  + 8
# di mana x = volume produksi/penjualan (satuan unit)
# Titik impas tercapai saat f(x) = 0
# ------------------------------------------------------------

def f(x):
    """Fungsi laba: f(x) = 0.5x^3 - 4x^2 + 8x - 3"""
    return 0.5 * x**3 - 4 * x**2 + 8 * x - 3

def df(x):
    """Turunan pertama: f'(x) = 1.5x^2 - 8x + 8"""
    return 1.5 * x**2 - 8 * x + 8


# ------------------------------------------------------------
# 2. IMPLEMENTASI METODE NEWTON-RAPHSON
# ------------------------------------------------------------

def newton_raphson(x0, tol=0.0001, maks_iterasi=100):
    """
    Mencari akar f(x) = 0 menggunakan metode Newton-Raphson.

    Rumus iterasi:
        x_{n+1} = x_n - f(x_n) / f'(x_n)

    Parameter:
        x0           : tebakan awal
        tol          : batas toleransi error relatif (default 0.0001 = 0.01%)
        maks_iterasi : batas maksimum iterasi (default 100)

    Return:
        akar  : estimasi nilai akar (float)
        tabel : list riwayat setiap iterasi
    """
    x = x0
    tabel = []

    header = f"{'N':>4}  {'x_n':>10}  {'f(x_n)':>12}  {'f\'(x_n)':>12}  {'Error (%)':>10}"
    print("=" * len(header))
    print(header)
    print("=" * len(header))

    for n in range(maks_iterasi):
        fx  = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-12:
            print("Turunan mendekati nol! Metode tidak konvergen.")
            return None, tabel

        x_baru = x - fx / dfx

        # Error relatif (%)
        error = abs((x_baru - x) / x_baru) * 100 if x_baru != 0 else float('inf')

        print(f"{n:>4}  {x:>10.4f}  {fx:>12.6f}  {dfx:>12.6f}  {error:>10.4f}")
        tabel.append(dict(n=n, x=x, fx=fx, dfx=dfx, error=error))

        if error < tol * 100:       # konvergensi tercapai
            x = x_baru
            break

        x = x_baru

    # Tampilkan baris konvergen terakhir
    print(f"{len(tabel):>4}  {x:>10.4f}  {f(x):>12.6f}  {df(x):>12.6f}  {'0.0000 ✓':>10}")
    print("=" * len(header))

    return x, tabel


# ------------------------------------------------------------
# 3. EKSEKUSI & OUTPUT
# ------------------------------------------------------------

if __name__ == "__main__":
    print()
    print("=" * 58)
    print("  ESTIMASI TITIK IMPAS (BREAK-EVEN POINT) USAHA KECIL")
    print("  Metode Newton-Raphson dengan Konvergensi Kuadratik")
    print("=" * 58)
    print()

    X0  = 1.0      # tebakan awal sesuai poster
    TOL = 0.0001   # toleransi

    print(f"  Fungsi  : f(x) = 0.5x³ - 4x² + 8x - 3")
    print(f"  Turunan : f'(x) = 1.5x² - 8x + 8")
    print(f"  Tebakan awal x0 = {X0}")
    print(f"  Toleransi error = {TOL}\n")

    akar, riwayat = newton_raphson(X0, TOL)

    if akar is not None:
        print()
        print(f"  ✅ Titik Impas ditemukan pada  x = {akar:.4f}")
        print(f"     Verifikasi f({akar:.4f}) = {f(akar):.8f}  ≈ 0")
        print(f"     Jumlah iterasi : {len(riwayat)}")
        print(f"     Toleransi      : {TOL}")
        print()
        print("  Interpretasi:")
        print(f"  Usaha mencapai titik impas pada volume produksi/penjualan")
        print(f"  sebesar x ≈ {akar:.4f} unit.")
        print()
