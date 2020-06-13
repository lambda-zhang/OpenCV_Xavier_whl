from setuptools import setup
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    """ Forces BinaryDistribution. """
    def has_ext_modules(self):
        return True

    def is_pure(self):
        return False


long_description = ""
with open("../README.md") as f:
    long_description = f.read()


setup(name="opencv-python",
      version="3.4.3",
      url='',
      license='MIT',
      description='opencv-python on armv8',
      long_description=long_description,
      distclass=BinaryDistribution,
      packages=['cv2'],
      include_package_data = True,
      install_requires="numpy>=1.13",
      classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: C++',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Software Development',
        ]
      )
