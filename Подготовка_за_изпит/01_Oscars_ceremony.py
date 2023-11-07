rent = int(input())

statue = 0.70 * rent
catering = 0.85 * statue
sound = catering / 2
sum = rent +  statue + catering + sound

print(F"{sum:.2F}")