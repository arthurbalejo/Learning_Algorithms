cidade = str(input("Em qual cidade voce nasceu? "))
cidade = cidade.strip()
cidade = cidade.title()

if (cidade[:5] == "Santo"):
    print("True")
else:
    print("False")