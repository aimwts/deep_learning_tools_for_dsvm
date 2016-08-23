#Downloads the MNIST data
import sys
import os
import zipfile
current_path = os.path.dirname(os.path.abspath(__file__))
root_path = current_path.rsplit('solutions')[0]
sys.path.insert(0,root_path)
from solutions.utils.python_utils import download_file


#MNIST data in ubyte
url_root = 'https://hoaphumanoidstorage2.blob.core.windows.net/public/'
url_ubyte = url_root + 'mnist.zip'
print("Downloading file %s" % url_ubyte)
download_file(url_ubyte)
local_filename = url_ubyte.split('/')[-1]
zfile = zipfile.ZipFile(local_filename)
for name in zfile.namelist():
    zfile.extract(name, current_path)



