#RO_Pag038_exercici_for.py

n_imparell = int(input("n_imparell = "))
s_imparell = 0

for i in range (1, n_imparell):
    k = (2 * i) - 1
    s_imparell = s_imparell + k
    
if s_imparell == n_imparell ** 2:
    print("verdader")
    
else:
    print("fals")
    
