import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


def create_sound(f=125, fs=512, T=5):
    t = np.arange(T * fs) / fs
    s = sin(2 * np.pi * f * t)
    return (t, s)


def plot_sound(t, s, title="recorded sound"):
    fig = plt.figure()
    ax = add_subplot(1, 1, 1)
    ax.plot(t, s)
    ax.set_xlabel('time [s]')
    ax.set_ylabel('voltage [mV]')
    ax.set_title(title)
    # plt.grid(On)
    fig.show()


if __name__ == "__main__":
    f = 512
    fs = 44100
    T = 5
    time, sound = create_sound(f, fs, T)
    cust_title = "sinewave of " + str(f) + " Hz, duration is " + str(T) + " seconds."
    plot_sound(time, title=cust_title)

    play_sound = True
    rec_sound = False

    if play_sound == True:
        sd.play(sound, fs)
        sd.wait()

    duration = 10.5  # seconds
    if rec_sound == True:
        record = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()

        print(record.shape)
        t_record = int(duration * fs)
        plot_sound(t_record, record)
