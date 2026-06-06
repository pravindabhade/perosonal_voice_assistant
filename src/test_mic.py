import sounddevice as sd

print(sd.query_devices())
print("\nDefault Input Device:")
print(sd.default.device)