===============================
Tifffile
===============================

.. image:: https://badge.fury.io/py/tifffile.png
    :target: http://badge.fury.io/py/tifffile

.. image:: https://pypip.in/d/tifffile/badge.png
        :target: https://pypi.python.org/pypi/tifffile


Read and write image data from and to TIFF files.

Image and metadata can be read from TIFF, BigTIFF, OME-TIFF, STK, LSM, NIH,
SGI, ImageJ, MicroManager, FluoView, SEQ and GEL files.
Only a subset of the TIFF specification is supported, mainly uncompressed
and losslessly compressed 2**(0 to 6) bit integer, 16, 32 and 64-bit float,
grayscale and RGB(A) images, which are commonly used in bio-scientific imaging.
Specifically, reading JPEG and CCITT compressed image data or EXIF, IPTC, GPS,
and XMP metadata is not implemented.
Only primary info records are read for STK, FluoView, MicroManager, and
NIH image formats.

TIFF, the Tagged Image File Format, is under the control of Adobe Systems.
BigTIFF allows for files greater than 4 GB. STK, LSM, FluoView, SGI, SEQ, GEL,
and OME-TIFF, are custom extensions defined by Molecular Devices (Universal
Imaging Corporation), Carl Zeiss MicroImaging, Olympus, Silicon Graphics
International, Media Cybernetics, Molecular Dynamics, and the Open Microscopy
Environment consortium respectively.

For command line usage run ``python tifffile.py --help``

:Author:
  `Christoph Gohlke <http://www.lfd.uci.edu/~gohlke/>`_

:Organization:
  Laboratory for Fluorescence Dynamics, University of California, Irvine

:Version: 2014.08.24

Requirements
------------
* `CPython 2.7 or 3.4 <http://www.python.org>`_
* `Numpy 1.8.2 <http://www.numpy.org>`_
* `Matplotlib 1.4 <http://www.matplotlib.org>`_ (optional for plotting)

Notes
-----
This is a mirror of the code at http://www.lfd.uci.edu/~gohlke/code/tifffile.py.html.  For any development concerns, please email Christoph Gohlke at
``cgohlke at uci.edu``.

The API is not stable yet and might change between revisions.

Tested on little-endian platforms only.

Other Python packages and modules for reading bio-scientific TIFF files:

*  `Imread <http://luispedro.org/software/imread>`_
*  `PyLibTiff <http://code.google.com/p/pylibtiff>`_
*  `SimpleITK <http://www.simpleitk.org>`_
*  `PyLSM <https://launchpad.net/pylsm>`_
*  `PyMca.TiffIO.py <http://pymca.sourceforge.net/>`_ (same as fabio.TiffIO)
*  `BioImageXD.Readers <http://www.bioimagexd.net/>`_
*  `Cellcognition.io <http://cellcognition.org/>`_
*  `CellProfiler.bioformats
   <https://github.com/CellProfiler/python-bioformats>`_

Acknowledgements
----------------
*   Egor Zindy, University of Manchester, for cz_lsm_scan_info specifics.
*   Wim Lewis for a bug fix and some read_cz_lsm functions.
*   Hadrien Mary for help on reading MicroManager files.

References
----------
(1)  TIFF 6.0 Specification and Supplements. Adobe Systems Incorporated.
     http://partners.adobe.com/public/developer/tiff/
(2)  TIFF File Format FAQ. http://www.awaresystems.be/imaging/tiff/faq.html
(3)  MetaMorph Stack (STK) Image File Format.
     http://support.meta.moleculardevices.com/docs/t10243.pdf
(4)  Image File Format Description LSM 5/7 Release 6.0 (ZEN 2010).
     Carl Zeiss MicroImaging GmbH. BioSciences. May 10, 2011
(5)  File Format Description - LSM 5xx Release 2.0.
     http://ibb.gsf.de/homepage/karsten.rodenacker/IDL/Lsmfile.doc
(6)  The OME-TIFF format.
     http://www.openmicroscopy.org/site/support/file-formats/ome-tiff
(7)  UltraQuant(r) Version 6.0 for Windows Start-Up Guide.
     http://www.ultralum.com/images%20ultralum/pdf/UQStart%20Up%20Guide.pdf
(8)  Micro-Manager File Formats.
     http://www.micro-manager.org/wiki/Micro-Manager_File_Formats
(9)  Tags for TIFF and Related Specifications. Digital Preservation.
     http://www.digitalpreservation.gov/formats/content/tiff_tags.shtml

Examples
--------

>>> data = numpy.random.rand(5, 301, 219)
>>> imsave('temp.tif', data)

>>> image = imread('temp.tif')
>>> numpy.testing.assert_array_equal(image, data)

>>> with TiffFile('temp.tif') as tif:
...     images = tif.asarray()
...     for page in tif:
...         for tag in page.tags.values():
...             t = tag.name, tag.value
...         image = page.asarray()


Known build errors
------------------
On Windows, the error `Error:unable to find vcvarsall.bat` means that distutils is not correctly configured to use the C compiler. Modify (or create, if not existing) the configuration file `distutils.cfg` (located for example at `C:\\Python27\\Lib\\distutils\\distutils.cfg`) to contain::

  [build]
  compiler=mingw32

