import wave
import csv
import struct

def wav_to_csv(input_wav_file, output_csv_file):
    # Abrir o arquivo WAV para leitura
    with wave.open(input_wav_file, 'rb') as wav_file:
        # Obter os parâmetros do arquivo WAV
        num_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()

        # Ler os dados do arquivo WAV
        frames = wav_file.readframes(num_frames)



        # Converter os dados binários para uma lista de valores
        data = list(struct.unpack_from(f"{num_frames * num_channels}h", frames))

    # Escrever os valores no arquivo CSV
    with open(output_csv_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Escrever os dados
        for i in range(0, num_frames * num_channels, num_channels):
            row_data = data[i:i + num_channels]
            if any(row_data):  # Verifica se pelo menos um valor é diferente de zero
                csv_writer.writerow(row_data)

base_original = 'C:/Users/Vitória Camelo/Documents/sac-dm/files/voice_signals/base/denoised/'
base_csv = 'C:/Users/Vitória Camelo/Documents/sac-dm/files/voice_signals/base/csv/'
caminhos = [
    'audio-f/f01', 'audio-f/f02', 'audio-f/f03', 'audio-f/f04', 'audio-f/f05',
    'audio-m/m01', 'audio-m/m02', 'audio-m/m03', 'audio-m/m04', 'audio-m/m05',
    'audio-sf/sf01', 'audio-sf/sf02', 'audio-sf/sf03', 'audio-sf/sf04', 'audio-sf/sf05',
    'audio-sm/sm01', 'audio-sm/sm02', 'audio-sm/sm03', 'audio-sm/sm04', 'audio-sm/sm05',
]

#input_wav_file = '/home/pesquisador/Documentos/sac-dm/files/voice_signals/sample/original/galvao_ia.wav'
#output_csv_file = '/home/pesquisador/Documentos/sac-dm/files/voice_signals/sample/data/galvao_ia.csv'
for i in range(len(caminhos)):
    wav_to_csv(base_original+caminhos[i]+".wav", base_csv+caminhos[i]+"-denoised"+".csv")

