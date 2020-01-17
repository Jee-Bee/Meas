import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


def create_sound(f=125, fs=512, T=5):
    t = np.arange(T * fs) / fs
    s = np.sin(2 * np.pi * f * t)
    return (t, s)


def plot_sound(t, s, title="recorded sound"):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
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
    plot_sound(time, sound, title=cust_title)

    play_sound = False
    rec_sound = False
    play_rec = True

    if play_sound == True:
        sd.play(sound, fs)
        sd.wait()

    duration = 10.5  # seconds
    if rec_sound == True:
        print("Play sound now!")
        record = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()

        print(record.shape)
        t_record = np.arange(int(duration * fs)) / fs
        plot_sound(t_record, record.T[0])

    if play_rec == True:
        record = sd.playrec(sound, samplerate=fs, channels=2)
        print(record.shape)
        t_record = np.arange(len(record.T[0])) / fs
        plot_sound(t_record, record.T[0])
