states = ['x', 'z', 'th']
corrModels = ['M1','M2','M3','M4','M5']

model_data = {}
true_data = {}
pear = {}
RMS = {}

path = './assimilation_log/gp_training/DCE/Fig4_5/'

for corrModel in corrModels:
    for state in states:
        # Load and flatten model data
        model_key = f"{state}_model_{corrModel}"
        model_data[model_key] = np.load(f'{path}{state}_{corrModel}.npy').flatten()
        
        # Load and flatten true data
        true_key = f"{state}_true"
        true_data[true_key] = np.load(f'{path}{state}_true.npy').flatten()
        
        rms_key = f"{state}_{corrModel}"
        # Compute pearson
        pear[rms_key]= stats.pearsonr(model_data[model_key], true_data[true_key])[0]
