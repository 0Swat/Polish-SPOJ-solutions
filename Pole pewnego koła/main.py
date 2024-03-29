def PoleKola(r_in, d_in):
    r2 = (r_in**2) - (0.25*(d_in**2))
    pole = 3.141592654 * r2
    pole = round(pole, 2)

    return float(pole)

r, d = input().split()
print(PoleKola(float(r), float(d)))