for h in range(24):
    for m in range(60):
        print(F"{h}:{m}")
        if h < 10:
            hours = "0" + str(h)
        else:
            hours = h
        if  m <10:
            minutes = "0" + str(m)
        else:
            minutes = m
        print(F"{hours}:{minutes}")