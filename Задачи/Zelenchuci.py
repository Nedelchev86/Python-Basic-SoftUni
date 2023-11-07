import mat
zelenchuci_cena = float(input())
plodove_cena = float(input())
total_zelenchuci = float(input())
total_plodove = float(input())
total = (zelenchuci_cena * total_zelenchuci) + (plodove_cena * total_plodove)
total_evro = total / 1.94
print (F"{total_evro:.2F}")