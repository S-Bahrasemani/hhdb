import os

# ami imports
import pyAMI.client
import pyAMI.atlas.api as AtlasAPI
client = pyAMI.client.Client('atlas')
AtlasAPI.init()

if __name__ == '__main__':

    Ids = []
    for a in open('stupid.txt'):
        b = a.strip().replace('/','')
        if len(b) == 0: 
            continue
        #Take AOD instead of DAOD (not the same original number of events)
        b = b.replace('DAOD_HIGG4D2', 'AOD')
        b = b.replace('_p2419', '')
#        b = b.rstrip(b[-6:])
#        print b
        id = b.split('.')[1]

        if id in Ids:
            continue

        Ids.append(id)

        infos = AtlasAPI.get_dataset_info(client, b)[0]
        xsec = float(infos['crossSection']) * 1000
        filtstr = infos['approx_GenFiltEff']
        if filtstr.find('N/A')>=0:
         #   print 'No filter efficiency available'
          #  print infos
            filt = 1 
        else:
            filt = float(filtstr)
        kfac = 1.0
        nevts = float(infos['totalEvents'])
        lumi = nevts/ 1000. / (xsec * kfac * filt)
            
        print id, '\t', '%s' % int(nevts), '\t', '{0}*{1}*{2}'.format(xsec, kfac, filt), '\t', '{0:1.2f}'.format(lumi),'\t', b
