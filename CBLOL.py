import math

CBLOL = ['INTZ e-Sports', 'paiN Gaming', 'Los Grandes', 'RED Canids', 'Vivo Keyd Stars', 'Fluxo', 'FURIA Esports', 'Liberty', 'LOUD', 'KaBuM! e-Sports']
Matches = [['LOUD', 'KaBuM! e-Sports', '1 - 0'], ['Vivo Keyd Stars', 'Los Grandes', '1 - 0'], ['Fluxo', 'FURIA Esports', '1 - 0'], ['Liberty', 'INTZ e-Sports', '1 - 0'], ['RED Canids', 'paiN Gaming', '1 - 0'], ['Los Grandes', 'Fluxo', '1 - 0'], ['INTZ e-Sports', 'RED Canids', '1 - 0'], ['KaBuM! e-Sports', 'Vivo Keyd Stars', '1 - 0'], ['FURIA Esports', 'Liberty', '1 - 0'], ['paiN Gaming', 'LOUD', '1 - 0'], ['Fluxo', 'KaBuM! e-Sports', '0 - 1'], ['Vivo Keyd Stars', 'INTZ e-Sports', '1 - 0'], ['paiN Gaming', 'FURIA Esports', '1 - 0'], ['LOUD', 'Liberty', '1 - 0'], ['RED Canids', 'Los Grandes', '1 - 0'], ['FURIA Esports', 'LOUD', '0 - 1'], ['Los Grandes', 'INTZ e-Sports', '1 - 0'], ['Liberty', 'paiN Gaming', '1 - 0'], ['KaBuM! e-Sports', 'RED Canids', '1 - 0'], ['Fluxo', 'Vivo Keyd Stars', '0 - 1'], ['INTZ e-Sports', 'FURIA Esports', '0 - 1'], ['LOUD', 'Fluxo', '1 - 0'], ['paiN Gaming', 'Los Grandes', '1 - 0'], ['Vivo Keyd Stars', 'RED Canids', '0 - 1'], ['Liberty', 'KaBuM! e-Sports', '0 - 1'], ['RED Canids', 'Fluxo', '0 - 1'], ['KaBuM! e-Sports', 'paiN Gaming', '0 - 1'], ['INTZ e-Sports', 'LOUD', '0 - 1'], ['Los Grandes', 'FURIA Esports', '0 - 1'], ['Vivo Keyd Stars', 'Liberty', '1 - 0'], ['Liberty', 'Los Grandes', '0 - 1'], ['Fluxo', 'paiN Gaming', '0 - 1'], ['LOUD', 'RED Canids', '1 - 0'], ['FURIA Esports', 'Vivo Keyd Stars', '0 - 1'], ['KaBuM! e-Sports', 'INTZ e-Sports', '1 - 0'], ['paiN Gaming', 'Vivo Keyd Stars', '1 - 0'], ['FURIA Esports', 'KaBuM! e-Sports', '0 - 1'], ['RED Canids', 'Liberty', '1 - 0'], ['Fluxo', 'INTZ e-Sports', '1 - 0'], ['Los Grandes', 'LOUD', '1 - 0'], ['RED Canids', 'FURIA Esports', '1 - 0'], ['Liberty', 'Fluxo', '1 - 0'], ['Vivo Keyd Stars', 'LOUD', '1 - 0'], ['INTZ e-Sports', 'paiN Gaming', '0 - 1'], ['Los Grandes', 'KaBuM! e-Sports', '0 - 1'], ['INTZ e-Sports', 'Liberty', '0 - 1'], ['FURIA Esports', 'Fluxo', '0 - 1'], ['paiN Gaming', 'RED Canids', '1 - 0'], ['KaBuM! e-Sports', 'LOUD', '1 - 0'], ['Los Grandes', 'Vivo Keyd Stars', '0 - 1'], ['LOUD', 'paiN Gaming', '1 - 0'], ['Vivo Keyd Stars', 'KaBuM! e-Sports', '1 - 0'], ['Fluxo', 'Los Grandes', '0 - 1'], ['RED Canids', 'INTZ e-Sports', '1 - 0'], ['Liberty', 'FURIA Esports', '1 - 0'], ['KaBuM! e-Sports', 'Fluxo', '0 - 1'], ['Los Grandes', 'RED Canids', '0 - 1'], ['INTZ e-Sports', 'Vivo Keyd Stars', '0 - 1'], ['Liberty', 'LOUD', '1 - 0'], ['FURIA Esports', 'paiN Gaming', '0 - 1'], ['INTZ e-Sports', 'Los Grandes', '0 - 1'], ['paiN Gaming', 'Liberty', '0 - 1'], ['RED Canids', 'KaBuM! e-Sports', '1 - 0'], ['Vivo Keyd Stars', 'Fluxo', '1 - 0'], ['LOUD', 'FURIA Esports', '1 - 0'], ['RED Canids', 'Vivo Keyd Stars', '1 - 0'], ['KaBuM! e-Sports', 'Liberty', '0 - 1'], ['FURIA Esports', 'INTZ e-Sports', '1 - 0'], ['Los Grandes', 'paiN Gaming', '0 - 1'], ['Fluxo', 'LOUD', '0 - 1'], ['paiN Gaming', 'KaBuM! e-Sports', '0 - 1'], ['LOUD', 'INTZ e-Sports', '1 - 0'], ['Liberty', 'Vivo Keyd Stars', '1 - 0'], ['FURIA Esports', 'Los Grandes', '0 - 1'], ['Fluxo', 'RED Canids', '0 - 1'], ['Vivo Keyd Stars', 'FURIA Esports', '1 - 0'], ['RED Canids', 'LOUD', '0 - 1'], ['Los Grandes', 'Liberty', '1 - 0'], ['paiN Gaming', 'Fluxo', '0 - 1'], ['INTZ e-Sports', 'KaBuM! e-Sports', '1 - 0'], ['Liberty', 'RED Canids', '0 - 1'], ['LOUD', 'Los Grandes', '1 - 0'], ['KaBuM! e-Sports', 'FURIA Esports', '1 - 0'], ['Vivo Keyd Stars', 'paiN Gaming', '1 - 0'], ['INTZ e-Sports', 'Fluxo', '1 - 0'], ['LOUD', 'Vivo Keyd Stars', '0 - 1'], ['KaBuM! e-Sports', 'Los Grandes', '0 - 1'], ['FURIA Esports', 'RED Canids', '0 - 1'], ['Fluxo', 'Liberty', '1 - 0'], ['paiN Gaming', 'INTZ e-Sports', '1 - 0']]

class Teams:
    def __init__(self, name, ratings, deviations, volatilities):
        self.name = name
        self.ratings = ratings
        self.deviations = deviations
        self.volatilities = volatilities

ITZ = Teams('INTZ e-Sports', [1500],[350], [0.06])
PNG = Teams('paiN Gaming', [1500],[350], [0.06])
LOS = Teams('Los Grandes', [1500],[350], [0.06])
RED = Teams('RED Canids', [1500],[350], [0.06])
VKS = Teams('Vivo Keyd Stars', [1500],[350], [0.06])
FLX = Teams('Fluxo', [1500],[350], [0.06])
FUR = Teams('FURIA Esports', [1500],[350], [0.06])
LBR = Teams('Liberty', [1500],[350], [0.06])
LLL = Teams('LOUD', [1500],[350], [0.06])
KBM = Teams('KaBuM! e-Sports', [1500],[350], [0.06])

Dic = {ITZ.name:ITZ, PNG.name:PNG, LOS.name:LOS, RED.name:RED, VKS.name:VKS, FLX.name:FLX, FUR.name:FUR, LBR.name:LBR, LLL.name:LLL, KBM.name:KBM}

def predict(obj1, obj2):
    s1 = (obj1.ratings[-1] - 1500)/173.7178
    RD1 = obj1.deviations[-1]/173.7178
    s2 = (obj2.ratings[-1] - 1500)/173.7178
    RD2 = obj2.deviations[-1]/173.7178
    x = math.sqrt(RD1**2 + RD2**2)
    g = 1/math.sqrt(1 + (3*x**2)/math.pi**2)
    A = g * (s2-s1)
    return 1 - 1/(1 + math.exp(-A))

from Glicko2 import Glicko

'''update'''

errors = 0
total = 0
for match in range(len(Matches)):
    obj1 = Dic[Matches[match][0]]
    obj2 = Dic[Matches[match][1]]
    result1 = int(Matches[match][2][0])
    result2 =  int(Matches[match][2][-1])

    output1 = Glicko(obj1,obj2,result1)
    output2 = Glicko(obj2,obj1,result2)

    obj1.ratings.append(output1[0])
    obj1.deviations.append(output1[1])
    obj1.volatilities.append(output1[2])

    obj2.ratings.append(output2[0])
    obj2.deviations.append(output2[1])
    obj2.volatilities.append(output2[2])

    if len(Matches)-1 > match >=5:
        pred = predict(Dic[Matches[match+1][0]],Dic[Matches[match+1][1]])
        #(Dic[Matches[match+1][0]].name, Dic[Matches[match+1][1]].name, pred, Matches[match+1][2][0])
        errors+=abs(pred - int(Matches[match+1][2][0]))
        total += int(Matches[match+1][2][0])

sorted = dict(sorted(Dic.items(), key=lambda item: item[1].ratings[-1]))
for i in sorted:
    print(Dic[i].name, Dic[i].ratings[-1])

print(predict(RED, LOS))

# import pandas as pd
# out = {}
# for i in Dic:
#     out[Dic[i].name] = Dic[i].ratings
# Df = pd.DataFrame(out)
# Df.to_excel('D://out.xlsx')
