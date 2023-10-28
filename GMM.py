import os
#防止内存泄露，即已分配的内存没有被释放
os.environ["OMP_NUM_THREADS"] = '1'
import numpy as np
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import StandardScaler

#predition function of channel gain by GMM(3-dimension)
def GMMg(data_g,K):
    size_g = data_g.shape
    n_components_range = range(1, size_g[0]-1)
    aic = []
    #data_g has 3 dimensions, we can not directly use it, we need to do standardisation
    # apply logarithm
    data_log = np.log(data_g)
    # standardize data
    scaler = StandardScaler()
    data_std = scaler.fit_transform(data_log.reshape(-1, 1)).reshape(data_g.shape)
    G = np.reshape(data_std, (size_g[0], size_g[1]*size_g[2]))
    for n in n_components_range:
        gmm = GaussianMixture(n_components=n)
        gmm.fit(G)
        aic.append(gmm.aic(G))

    # Fit GMM model with best number of components
    best_n_components = np.argmin(aic) + 1
    # print(best_n_components)
    gmm_g = GaussianMixture(best_n_components)
    gmm_g.fit(G)

    # predict next one time slot
    future_G = gmm_g.sample(n_samples=K)[0]
    future_G = np.reshape(future_G, (K,size_g[1], size_g[2]))
    future_data_g = np.exp(future_G) * np.mean(data_g)
    return future_data_g



#predict the solar energy of devices by GMM(2-dimension)
def GMMi(data_i,K):
    n=len(data_i)
    # Compute AIC for different number of components
    n_components_range = range(1, n-1)
    aic = []
    for n in n_components_range:
        gmm = GaussianMixture(n_components=n)
        gmm.fit(data_i)
        aic.append(gmm.aic(data_i))

    # Fit GMM model with best number of components
    best_n_components = np.argmin(aic) + 1
    # (best_n_components)
    gmm_ei = GaussianMixture(n_components=best_n_components, random_state=42).fit(data_i)

    # Predict the sloar energy arrival of devices at future one time slot
    future_data_i = gmm_ei.sample(n_samples=K)[0]
    return future_data_i



#predict the solar energy of the server by GMM(1-dimension)
def GMMs(data_s,K):
    n=len(data_s)
    # Compute AIC for different number of components
    n_components_range = range(1, n-1)
    aic = []
    for n in n_components_range:
        gmm = GaussianMixture(n_components=n)
        gmm.fit(data_s)
        aic.append(gmm.aic(data_s))

    # Fit GMM model with best number of components
    best_n_components = np.argmin(aic) + 1
    # print(best_n_components)
    gmm_es = GaussianMixture(n_components=best_n_components, random_state=42).fit(data_s)

    # Predict the sloar energy arrival of devices at future one time slot
    future_data_s = gmm_es.sample(n_samples=K)[0]
    return future_data_s







