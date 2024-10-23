def convert_temperature(value, scale):
    if scale.upper() == 'C':
        return (value * 9/5) + 32
    elif scale.upper() == 'F':
        return (value - 32) * 5/9
    else:
        raise ValueError("Pilihan tidak ada. Pakai 'C' untuk Celsius atau 'F' untuk Fahrenheit KOCAK!!")

try:
    suhu = float(input("Masukkan nilai suhu: "))
    satuan = input("Masukkan satuan suhu ('C' untuk Celsius, 'F' untuk Fahrenheit): ")
    hasil = convert_temperature(suhu, satuan)
    if satuan.upper() == 'C':
        print(f"{suhu}°C = {hasil:.2f}°F")
    else:
        print(f"{suhu}°F = {hasil:.2f}°C")
except ValueError as e:
    print(e)
