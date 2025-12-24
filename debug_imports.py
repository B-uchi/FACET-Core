import yolox
import pkgutil
import os

print(f"YOLOX location: {yolox.__file__}")
print("Submodules in yolox:")
for loader, module_name, is_pkg in pkgutil.walk_packages(yolox.__path__, yolox.__name__ + "."):
    print(f"  {module_name}")

try:
    import bytetrack
    print(f"ByteTrack location: {bytetrack.__file__}")
except ImportError:
    print("bytetrack package not found")
