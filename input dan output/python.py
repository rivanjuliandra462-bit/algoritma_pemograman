nama = iinput("masukan nama barang: ")
harga = float(input("masukan harga barang: "))
jumlah = int(input("masukan jumlah beli:" ))

total = harga * jumlah 

if total > 100000:
    diskon = total * 0.10
else:
    diskon = 0
    
    total_bayar = total - diskon 
    
    print("\n===== STRUK PEMBELIAN =====")   
    print(f"nama barang  : {nama}")
    print(f"harga satuan : {harga}")
    print(f"jumlah beli  : {jumlah}")
    print(f"total harga  : {total}")
    print(f"diskon       : {diskon}")
    print(f"ottal bayar  : {total_bayar}")
    print("===========================")
    
    