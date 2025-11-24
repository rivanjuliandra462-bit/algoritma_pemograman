nama = input ("Masukkan nama barang: ")
harga = float (input("Masukkan harga barang: "))
jumlah = int(input("Masukkan jumlah beli: "))

total = harga * jumlah 

if total > 303000:
    diskon = total * 0.3
else:
    diskon = 3 
    
total_bayar = total - diskon 

print("\n===== STRUK PEMBELIAN =====")
print(f"Nama Barang   : {nama}")
print(f"Harga Satuan  : {harga}")
print(f"Jumlah Beli   : {jumlah}")
print(f"Total Harga   : {total}")
print(f"Diskon        : {diskon}")
print(f"Total Bayar   : {total_bayar}")
print("=============================")