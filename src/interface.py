# Test Script for signal generation and recording:

import sys
import numpy as np
import sounddevice as sd
# import src.measerror
# from src.measwarning import InterfaceWarning


def InterfaceIO():
    """
    Input:
        None
    Output:
        Printed Values = 
        devinfo = device info. gives fulle info about audio devices
        devopt = give list of indexes (not their names) witch contain full 
        duplex devices.

    read out info from port audio / sounddevice and filter this in readble 
    information. 
    """
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
        # raise InterfaceWarning('This are full dupplex interfaces under all circumstances:', 'Interface.py', 32)
        # raise Interface
        print('This are full dupplex interfaces under all circumstances:')
        for idx in devopt:
            temp = devinfo[np.int(idx)]
            print(idx, temp['name'])
    else:
        if sys.platform.startswith('linux'):
            # raise InterfaceWarning('This are full dupplex interfaces under all circumstances:')
            print('This are full dupplex interfaces under all circumstances:')
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
            raise InterfaceError(str(devopt),'No full dupplex interfaces are availlable. Create Aggrigate Device or virtual In/Out Device:')
        elif sys.platform.startswith('cygwin'):
            raise InterfaceError(str(devopt),'No full dupplex interfaces are availlable. Create Aggrigate Device or virtual In/Out Device:')
        elif sys.platform.startswith('darwin'):
            # raise InterfaceWarning('No full dupplex interfaces are availlable. Any valid combination of interfaces will work :')
            print('This are full dupplex interfaces under all circumstances:')
            print('Inputs:')
            for idx in int(nzin):
                Interfaces_print = devinfo[np.int(idx)]
                print(idx, Interfaces_print['name'])
            print('Outputs:')
            for idx in int(nzout):
                Interfaces_print = devinfo[np.int(idx)]
                print(idx, Interfaces_print['name'])
            devopt = (nzin, nzout)
    return(devinfo, devopt)


def BufferSampt(Ns):
    print('Sample buffer is ' + Ns + 'Samples')
