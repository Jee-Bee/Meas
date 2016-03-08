# Test Script for signal generation and recording:

import sys
import numpy as np
import sounddevice as sd

def InterfaceIO():
    # Signal to soundcard
    # Soundcard information
    devinfo = sd.query_devices()
    # print(devinfo)

    IOs = np.zeros((len(devinfo), 3))
    for idx in range(len(devinfo)):
        temp = devinfo[idx]
        IOs[idx][0] = idx
        IOs[idx][1] = temp['max_input_channels']
        IOs[idx][2] = temp['max_output_channels']
    # nonzeroval = IOs[:, [1, 2]]  # filter on arrays!!
    # http://stackoverflow.com/questions/8386675/extracting-specific-columns-in-numpy-array
    nzin = np.nonzero(IOs[:, 1])[0]
    # nzin = np.append(5, nzin)
    nzout = np.nonzero(IOs[:, 2])[0]
    devopt = []
    for idx in range(len(nzin)):
        devopt = np.append(devopt, np.where(nzout == nzin[idx]))

    if len(devopt) != 0:
        print('This are full dupplex interfaces under all circumstances:')
        for idx in devopt:
            temp = devinfo[np.int(idx)]
            print(idx, temp['name'])
    else:
        if sys.platform.startswith('linux'):
            print('No full dupplex interfaces are availlable. Any valid combination of interfaces will work :')
            print('Inputs:')
            for idx in nzin:
                temp = devinfo[np.int(idx)]
                print(idx, temp['name'])
            print('Outputs:')
            for idx in int(nzout):
                temp = devinfo[np.int(idx)]
                print(idx, temp['name'])
            devopt = (nzin, nzout)
        elif sys.platform.startswith('win32'):
            print('No full dupplex interfaces are availlable. Create Aggrigate Device or virtual In/Out Device:')
        elif sys.platform.startswith('cygwin'):
            print('No full dupplex interfaces are availlable. Create Aggrigate Device or virtual In/Out Device:')
        elif sys.platform.startswith('darwin'):
            print('No full dupplex interfaces are availlable. Any valid combination of interfaces will work :')
            print('Inputs:')
            for idx in int(nzin):
                temp = devinfo[np.int(idx)]
                print(idx, temp['name'])
            print('Outputs:')
            for idx in int(nzout):
                temp = devinfo[np.int(idx)]
                print(idx, temp['name'])
            devopt = (nzin, nzout)
    return(devinfo, devopt)


def BufferSampt(Ns):
    print('Sample buffer is ' + Ns + 'Samples')
