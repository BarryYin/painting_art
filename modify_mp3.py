from pydub import AudioSegment

def modify_mp3_file(file_name, new_rate = 16000, channels=1):
    # 加载MP3文件
    audio = AudioSegment.from_mp3(file_name)
    new_file_name = 'modified_'+ file_name
    # 设置新的音频参数
    # 注意：pydub中设置采样率的方法是使用set_frame_rate，设置声道数的方法是使用set_channels
    modified_audio = audio.set_frame_rate(new_rate).set_channels(channels)
    
    # 导出修改后的音频到新的文件
    modified_audio.export(new_file_name, format="mp3")
    return new_file_name

# 使用示例：将现有MP3音频修改为16kHz采样率，单声道
#modify_mp3_file('outout1.mp3')