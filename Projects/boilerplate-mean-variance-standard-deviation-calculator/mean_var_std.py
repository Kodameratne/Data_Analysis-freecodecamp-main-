import numpy as np

def calculate(list):
  try:
    a=np.array(list)
    a=a.reshape(3,3)
    flat=a.flatten()
    calculations={
      'mean':[],
      'variance': [],
      'standard deviation': [],
      'max': [],
      'min': [],
      'sum': []
    }

    mean_r = a.mean(axis=0).tolist()
    mean_c =a.mean(axis=1).tolist()
    mean_f = flat.mean()
    mean_list = [mean_r, mean_c, mean_f]
    calculations['mean']=mean_list

    var_r = a.var(axis=0).tolist()
    var_c = a.var(axis=1).tolist()
    var_f = flat.var()
    var_list = [var_r, var_c, var_f]
    calculations['variance']=var_list

    std_r = a.std(axis=0).tolist()
    std_c = a.std(axis=1).tolist()
    std_f = flat.std()
    std_list = [std_r, std_c, std_f]
    calculations['standard deviation']=std_list

    max_r = a.max(axis=0).tolist()
    max_c = a.max(axis=1).tolist()
    max_f = flat.max()
    max_list = [max_r, max_c, max_f]
    calculations['max']=max_list

    min_r =  a.min(axis=0).tolist()
    min_c = a.min(axis=1).tolist()
    min_f = flat.min()
    min_list = [min_r, min_c, min_f]
    calculations['min']=min_list

    sum_r = a.sum(axis=0).tolist()
    sum_c = a.sum(axis=1).tolist()
    sum_f = flat.sum()
    sum_list = [sum_r, sum_c, sum_f]
    calculations['sum']=sum_list
    return calculations
  except ValueError:
    raise ValueError("List must contain nine numbers.")
