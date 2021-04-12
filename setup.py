from distutils.core import setup

setup(name='omsi',
      version='0.1',
      description='Berkeley Analysis and Storage Toolkit (BASTet)',
      author='Oliver Ruebel and Benjamin P. Bowen',
      author_email='oruebel@lbl.gov',
      url='http://openmsi.nersc.gov',
      packages=['omsi' , 'omsi/analysis' , 'omsi/dataformat' , 'omsi/tools'],
      requires=['numpy' , 'h5py'],
      license="See licence.txt.",
      keywords="storage MSI analysis workflow provenance"
     )
