def call_option(S,K,t,sigma):
    import numpy as np
    from scipy.stats import norm
    r=0.1
    d1=(np.log(S/K)+(r+(sigma**2)/2)*t)/(sigma*t**0.5)
    d2=d1-sigma*t**0.5
    C=S*norm.cdf(d1)-K*np.exp(-r*t)*norm.cdf(d2)
    return C

def implied_volatility(s,k,t,C_market,maxiteration=50):
    sigma_low=0.0001
    sigma_high=5
    price_low = call_option(s,k,t, sigma_low)
    price_high = call_option(s,k,t, sigma_high)
    if price_low > C_market or price_high < C_market:
        raise ValueError("Implied volatility not bracketed")

    for i in range(maxiteration):
        if price_low<C_market and price_high>C_market:
            sigma_mid=(sigma_low+sigma_high)/2
            if call_option(s,k,t,sigma_mid)>C_market:
                sigma_high=sigma_mid
            else:
                sigma_low=sigma_mid
    return sigma_mid

        
    
