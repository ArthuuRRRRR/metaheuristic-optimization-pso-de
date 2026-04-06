def fonction_objectives(valeurs_in):
    x1,x2,x3 = valeurs_in
    return (x1 ** 2)* x2 * (2+x3)

def contraintes_fonction(valeurs_in):
    x1,x2,x3 = valeurs_in
    g1 = 1 - ((x2 ** 3 ) * x3) / (71785 * x1 ** 4) 
    g2 = (4 * (x2 ** 2 ) - x1 * x2) / (12566 * (x2 * (x1 **3) - x1** 4)) + (1/ (5108 * (x1**2))) - 1 
    g3 = 1 -(140.45 * x1 / ((x2 **2) * x3)) 
    g4 = ((x1 + x2 ) /1.5)-1 
    return g1,g2,g3,g4


def verification_contraintes(valeurs_in):
    g1,g2,g3,g4 = contraintes_fonction(valeurs_in)
    if (g1 <= 0) and (g2 <= 0) and (g3 <= 0) and (g4 <= 0):
        return True
    else :
        return False
   

def penaliser_algo(valeurs_in):
    violation_signe = 0
    if verification_contraintes(valeurs_in) is False:
        violation_signe += 100
    f = fonction_objectives(valeurs_in)

    g1, g2, g3, g4 = contraintes_fonction(valeurs_in)

        

    v1 = max(0.0, g1)
    v2 = max(0.0, g2)
    v3 = max(0.0, g3)
    v4 = max(0.0, g4)

    violation_totale = v1*v1 + v2*v2 + v3*v3 + v4*v4 + violation_signe

    coef_penalite = 900 
    penalite = coef_penalite * violation_totale

    return f + penalite
