import sys, json
from faster_whisper import WhisperModel
m=WhisperModel(sys.argv[2], device="cpu", compute_type="int8")
from scipy.io import wavfile
import numpy as np
_,a=wavfile.read(sys.argv[1]); a=a.astype(np.float32)/32768
segs,info=m.transcribe(a, word_timestamps=True, vad_filter=True, beam_size=5)
out=[]
for s in segs:
    out.append({"start":s.start,"end":s.end,"text":s.text.strip(),"words":[[w.start,w.end,w.word] for w in s.words]})
    print(f"[{s.start:7.2f}] {s.text.strip()}", flush=True)
json.dump({"lang":info.language,"segments":out},open(sys.argv[3],"w"))
print("LANG",info.language)
