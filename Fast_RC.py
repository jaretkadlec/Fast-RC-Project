import numpy as np
import matplotlib.pyplot as plt


#if q = cA^a B^b where c, m, n are constants, then
def rul4(Q, A, dA, a, B, dB, b):
    dQ = Q * np.sqrt(((a*(dA/A))**2) + (b*(dB/B))**2)
    return dQ

def tau(t_half):
    return t_half/np.log(2)
    

#Experiment 1
#record t1/2 from the scope screen of setup Fig. 3b
t_half = float(input('What was t1/2?'))
#based off of precision of the text box reading
dtau_half = float(input('What is the precision of the text box reading?'))
tau = tau(t_half)
dtau = dtau_half
print('Half time constant is', '{x:.3f}'.format(x=t_half), '+/-', '{y:.3f}'.format(y=dtau_half))
print('Tau is', '{x:.3f}'.format(x=tau), '+/-', '{y:.3f}'.format(y=dtau))

#Experiment 2 - more Parallel!
#record form the scope screen
t_half2 = float(input('What was t1/2?'))
dtau_half2  = float(input('What is the precision of the text box reading?'))
tau2 = tau(t_half2)
dtau2 = dtau_half2
print('Half time constant is', '{x:.3f}'.format(x=t_half2), '+/-', '{y:.3f}'.format(y=dtau_half2))
print('Tau is', '{x:.3f}'.format(x=tau2), '+/-', '{y:.3f}'.format(y=dtau2))

#Experiment 3 - Series
#record t1/2 from the scope screen of setup Fig. 3b
t_half3 = float(input('What was t1/2?'))
#based off of precision of the text box reading
dtau_half3 = float(input('What is the precision of the text box reading?'))
tau3 = tau(t_half3)
dtau3 = dtau_half3
print('Half time constant is', '{x:.3f}'.format(x=t_half3), '+/-', '{y:.3f}'.format(y=dtau_half3))
print('Tau is', '{x:.3f}'.format(x=tau3), '+/-', '{y:.3f}'.format(y=dtau3))

#Experiment 4 - Theoretical Values

#measure resistor using multimeter
r = float(input('What is the resistance of the resistor?'))
dr = float(input('What is the uncertainty of the measuring device for resistance?'))

#measure capacitance using multimeter
c1 = float(input('What is the capacitance of the first capacitor (the one used in experiment 1)?'))
dc1 = float(input('What is the precision of the capacitance measuring device?'))

c2 = float(input('What is the capacitance of the second capacitor?'))
dc2 = dc1

#for each of the three circuits determing the capacitance of the circuits
#Experiment 1
totalc = c
dtotalc = dc1
theorytau = totalc * r
dtheorytau = rul4(theorytau, totalc, dtotalc, 1, r, dr, 1)
print('For the first experiment Tau should be:', '{x:.3f}'.format(x=theorytau), 'While the experimental tau was:', '{y:.3f}'.format(y=tau))
print('The uncertainties; Theoretical:', '{x:.3f}'.format(x=dtheorytau), 'Exerimental:', '{y:.3f}'.format(y=dtau))

#experiment 2
totalc2 = c1 + c2
dtotalc2 = np.sqrt((dc1**2)+(dc2**2))
theorytau2 = totalc2 * r
dtheorytau2 = rul4(theorytau2, totalc2, dtotalc2, 1, r, dr, 1)
print('For the second experiment Tau should be:', '{x:.3f}'.format(x=theorytau2), 'While the experimental tau was:', '{y:.3f}'.format(y=tau2))
print('The uncertainties; Theoretical:', '{x:.3f}'.format(x=dtheorytau2), 'Exerimental:', '{y:.3f}'.format(y=dtau2))


#Experiment 3
totalc3 = 1/(c1**-1 + c2**-1)
dtotalc3 = np.sqrt((dc1**2)+(dc2**2))/totalc3
theorytau = totalc3 * r
dtheorytau3 = rul4(theorytau3, totalc3, dtotalc3, 1, r, dr, 1)
print('For the third experiment Tau should be:', '{x:.3f}'.format(x=theorytau3), 'While the experimental tau was:', '{y:.3f}'.format(y=tau3))
print('The uncertainties; Theoretical:', '{x:.3f}'.format(x=dtheorytau3), 'Exerimental:', '{y:.3f}'.format(y=dtau3))

