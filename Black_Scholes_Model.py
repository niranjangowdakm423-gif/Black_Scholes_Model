import numpy as np
from scipy.stats import norm
from implied_volatility_using_bisection_method import implied_volatility
s=float(input("enter the current price"))
print("\n--- For Implied Volatility Calculation ---")
k_iv   = float(input("Enter strike used to derive IV (nearby market strike): "))
c_mkt  = float(input("Enter market price of that option: "))
t_iv   = int(input("Enter time to expiry for IV strike (in days): "))
r=0.1
sigma=implied_volatility(s,k_iv,t_iv/365,c_mkt) 
def call_option(S,K,t):

    d1=(np.log(S/K)+(r+(sigma**2)/2)*t)/(sigma*t**0.5)
    d2=d1-sigma*t**0.5
    C=S*norm.cdf(d1)-K*np.exp(-r*t)*norm.cdf(d2)
    return C

def put_option(S,K,t):

    d1=(np.log(S/K)+(r+(sigma**2)/2)*t)/(sigma*t**0.5)
    d2=d1-sigma*t**0.5
    P=K*np.exp(-r*t)*norm.cdf(-d2)-S*norm.cdf(-d1)
    return P
print("=== Black-Scholes Option Pricer ===")
g=int(input("enter the 1 to price call option 2 to price put option"))
k=float(input("enter the strike price"))
t=int(input("enter time in days"))
if g==1:
    print(call_option(s,k,t/365))
elif g==2:
    print(put_option(s,k,t/365))
else:
    print("invalid input")



