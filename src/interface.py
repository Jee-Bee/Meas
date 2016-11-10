# Test Script for signal generation and recording:

import sys
import numpy as np
import sounddevice as sd
import src.measerror
from src.measwarning import InterfaceWarning


def interfaceIO():
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
    try:
        import sounddevice as sd
        # Signal to soundcard
        # Soundcard information
        devinfo = sd.query_devices()
        # print(devinfo)
    
        IOs = np.zeros((len(devinfo), 3))
        for device in range(len(devinfo)):
            temp = devinfo[device]
            IOs[device][0] = device
            IOs[device][1] = temp['max_input_channels']
            IOs[device][2] = temp['max_output_channels']
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
                raise InterfaceError(str(devopt), 'No full dupplex interfaces are availlable. Create Aggrigate Device or virtual In/Out Device:')
            elif sys.platform.startswith('cygwin'):
                raise InterfaceError(str(devopt), 'No full dupplex interfaces are availlable. Create Aggrigate Device or virtual In/Out Device:')
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
    except ImportError:
        raise ImportError("No module named 'sounddevice'. ")


def advPlayRec(data, samplerate=None, input_channels=None, output_channels=None,
               repeats=None, l0=None, cascade=False, dtype=None, out=None,
               input_mapping=None, output_mapping=None, blocking=False, **kwargs):
    """
    adv PlayRec

    Parameters
    ----------
    data: Audio data to be played back. see python Sounddevice
    repeats: Number of repeats (per channel).
    cascade: If ''False''(the default) measure all output channels at once. If
        ''True'' Solo measurement per channel.
    input_channels, output_channels: Number of input channels. default the 
        number of output channels is obtained from *data.shape*. except by 
        cascading signals
    dtype:  Input data type.
    input_mapping, output_mapping
    blocking: If ``False`` (the default), return immediately, if ``True``, wait
        until playback/recording is finished.

    return
    ------
    The recorded data.

    Other Parameters
    ----------------
    out : Optional see python Sounddevice
    samplerate, **kwargs: All parameters of `Stream` -- exceptions see
        python Sounddevice

    Basic function of Sounddevice playrec() extended to need of repeating and
    avaraging sound signals

    """
    try:
        import sounddevice as sd
        #from scripts.checks import srepeat

        print(sd.get_portaudio_version())
        if repeats is None:
            repeats = 1
        else:
            data = np.tile(data, repeats)

        if (output_mapping is not None) and (cascade is True):
            # chack same dimension
            mapping_length = len(output_mapping)
            recarray = []
            for channel in range(mapping_length):
                chanarray = sd.playrec(data, samplerate, input_channels, dtype, out,
                            input_mapping, output_mapping[channel], blocking, kwargs)
                if channel == 0:
                    recarray = np.append(recarray, chanarray)
                elif recarray.ndim == 1:
                    recarray = np.vstack((recarray, chanarray))
                else:
                    recarray = np.dstack((recarray, chanarray))
            recarray = np.array_split(recarray, repeats, axis=0)
            recarray /= repeats
            return(recarray)
        elif (output_mapping is not None):
            recarray = []
            mapping_length = len(output_mapping)
            data = np.repeat(data, output_channels, axis=1).reshape((len(data), mapping_length))
            singlerec = sd.playrec(data, samplerate, input_channels, dtype, out,
                            input_mapping, output_mapping, blocking, kwargs)
            recarray = np.array_split(recarray, repeats, axis=0)
            recarray /= repeats
            return(recarray)
        elif (output_channels is not None) and (cascade is True):
            # check dimension with signal
            recarray = []
            for channel in range(output_channels):
                chanarray = sd.playrec(data, samplerate, input_channels, dtype, out,
                            input_mapping, channel, blocking, kwargs)
                if channel == 0:
                    recarray = np.append(chanarray, recarray)
                elif recarray.ndim == 1:
                    recarray = np.vstack((recarray, chanarray))
                else:
                    recarray = np.dstack((recarray, chanarray))
            recarray = recarray = np.array_split(recarray, repeats, axis=0)
            recarray /= repeats
            return(recarray)
        elif (output_channels is not None):
            recarray = []
            data = np.repeat(data, output_channels, axis=1).reshape((len(data), output_channels))
            singlerec = sd.playrec(data, samplerate, input_channels, dtype, out,
                input_mapping, output_mapping, blocking, kwargs)
            recarray = recarray = np.array_split(recarray, repeats, axis=0)
            recarray /= repeats
            return(recarray)
        else:
            recarray = []
            for repeat in range(repeats):
                singlerec = sd.playrec(data, samplerate, output_channels)
                recarray += singlerec
            recarray = recarray / repeats
            return(recarray)
    except ImportError:
        raise ("No module named 'sounddevice'. ")


def BufferSampt(Ns):
    print('Sample buffer is ' + Ns + 'Samples')
