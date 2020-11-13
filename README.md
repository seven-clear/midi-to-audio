# midi-to-audio
基于FluidSynth的midi转audio的python脚本


## 前提
- 安装[FluidSynth](https://github.com/FluidSynth/fluidsynth)
- 设备上sound font且知道其路径
- 设备上装了Python3

## 用法
将sound font放置soundfont目录下，或者实例化FluidSynth的时候传入你的sound font路径(建议此方法)

实例化一个FluidSynth并调用midi_to_audio即可


## 其他
脚本在fluidsynth 2.1.5上测通，其他版本未测

sound font可从[此](https://github.com/FluidSynth/fluidsynth/wiki/SoundFont)下载

Windows上若报fluidsynth不是内部或外部命令这类，请将脚本移至fluidsynth.exe所在目录