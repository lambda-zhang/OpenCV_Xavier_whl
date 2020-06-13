### base on
```
https://github.com/jetsonhacks/buildOpenCVXavier.git


commit ca885938823640505cfdca6d6a82f7949c161717 (HEAD -> master, tag: v1.0, origin/master, origin/HEAD)
Author: jetsonhacks <jim@jetsonhacks.com>
Date:   Wed Nov 7 14:21:18 2018 -0800

    remove libjasper-dev install
```


### 编译so
```
# cd buildOpenCVXavier/
# ./buildAndPackageOpenCV.sh
```

### 打包 whl
```
# cd opencv-python
# cp /root/opencv/build/lib/python3/cv2.cpython-36m-aarch64-linux-gnu.so cv2/cv2.cpython-36m-aarch64-linux-gnu.so

# python3 setup.py bdist_wheel

# ls dist/ -lh
total 1.6M
-rw-r--r-- 1 root root 1.6M Jun 13 01:20 opencv_python-3.4.3-cp36-cp36m-linux_aarch64.whl
```
