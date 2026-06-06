import sounddevice as sd

print("Default device:", sd.default.device)
print()

for i, dev in enumerate(sd.query_devices()):
    print(i, dev["name"])