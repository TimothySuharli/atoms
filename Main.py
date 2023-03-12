unsur_atom = {1: "Hidrogen", 2: " Helium", 3: "Litium", 4: " Berilium", 5: "Boron", 6: " Karbon", 7: "Nitrogen", 8: "Oksigen", 9: "Florin", 10: "Neon"}

A = int(input("Masukkan massa atom: "))
Z = int(input("Masukkan nomor atom: "))
n = int(input("Masukkan pangkatnya (angka): "))

proton = Z
elektron = proton-n
neutron = A-Z

if Z in unsur_atom : 
    print ("Unsur atom: ", unsur_atom.get(Z)) 

else : 
    print ("Unsur atom tidak diketahui atau belum diupdate")

print ("proton = ", proton)
print ("elektron = ", elektron)
print ("neutron = ", neutron)

if n == 0 : 
    print ("Atomnya netral")
else :
    print ("Atomnya ion")

