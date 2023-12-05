# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mbytes = 1.44
disk_size_bytes = disk_size_mbytes * 1024**2
pages = 100
len_string = 50
len_symbol = 25
size_bytes_for_symbol = 4
book_size = pages * len_string * len_symbol * size_bytes_for_symbol
print("Количество книг, помещающихся на дискету:", int(disk_size_bytes//book_size))
