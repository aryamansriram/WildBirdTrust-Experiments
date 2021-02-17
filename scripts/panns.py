import librosa
import panns_inference
from panns_inference import SoundEventDetection,AudioTagging,labels
import numpy as np

print("PANNs initialised...")
audio_path = "Data/Transfer_02/CPPR-006_20180505_072539.wav"


def print_audio_tagging_result(clipwise_output):
    """Visualization of audio tagging result.
    Args:
      clipwise_output: (classes_num,)
    """
    sorted_indexes = np.argsort(clipwise_output)[::-1]

    # Print audio tagging top probabilities
    for k in range(10):
        print('{}: {:.3f}'.format(np.array(labels)[sorted_indexes[k]],
            clipwise_output[sorted_indexes[k]]))


audio,_ = librosa.load(audio_path,sr=32000,mono=True)


audio = audio[None,:]

at = AudioTagging(checkpoint_path="/home/madlad/panns_data/Cnn14_DecisionLevelMax.pth", device='cuda')
(clipwise_output, embedding) = at.inference(audio)

print_audio_tagging_result(clipwise_output[0])
sed = SoundEventDetection(checkpoint_path="/home/madlad/panns_data/Cnn14_DecisionLevelMax.pth", device='cuda')
framewise_output = sed.inference(audio)
sqz = np.squeeze(framewise_output,axis=0)
classes = np.argmax(sqz,axis=1)
labs= [labels[i] for i in classes]
print(labs)