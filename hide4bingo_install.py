'''
Created on September 1, 2018

author: Lucas Olivari
'''

import os

######################################################################
#### THIS IS THE SCRIPT WILL MODIFY HIDE SO IT CAN BE USED FOR BINGO
######################################################################

# ==================================================================
# CHOOSE DESTINATION AND WORKING PATHS
# ==================================================================

destination_path = '~/anaconda2/lib/python2.7/site-packages/hide-0.1.0-py2.7.egg/' # change to your destination (the place where your hide package is located within your python repository)

working_path = '/home/lucas/Documentos/work/hidetest/hide/' # change to your working path (the place where your hide stuff are located)

# ==================================================================
# COPYNG STUFF AROUND
# ==================================================================

dfile = 'files/run_hide.py'
os.system('cp ' + dfile + ' ' + working_path)

dfile = 'files/altitude.txt'
os.system('cp ' + dfile + ' ' + working_path)

dfile = 'files/azimuth.txt'
os.system('cp ' + dfile + ' ' + working_path)

dfile = 'files/plot_tod.py'
os.system('cp ' + dfile + ' ' + working_path)

dfile = 'files/bingo.py'
os.system('cp ' + dfile + ' ' + working_path + 'hide/config/')

dfile = 'files/make_fake_bingo_model_1.py'
os.system('cp ' + dfile + ' ' + working_path + 'hide/data/')

dfile = 'files/make_fake_bingo_model_2.py'
os.system('cp ' + dfile + ' ' + working_path + 'hide/data/')

dfile = 'files/hi_sky.py'
os.system('cp ' + dfile + ' ' + destination_path + 'hide/astro/')
os.system('cp ' + dfile + ' ' + working_path + 'hide/astro/')

dfile = 'files/background_noise.py'
os.system('cp ' + dfile + ' ' + destination_path + 'hide/plugins/')
os.system('cp ' + dfile + ' ' + working_path + 'hide/plugins/')

dfile = 'files/clean_up.py'
os.system('cp ' + dfile + ' ' + destination_path + 'hide/plugins/')
os.system('cp ' + dfile + ' ' + working_path + 'hide/plugins/')

dfile = 'files/initialize.py'
os.system('cp ' + dfile + ' ' + destination_path + 'hide/plugins/')
os.system('cp ' + dfile + ' ' + working_path + 'hide/plugins/')

dfile = 'files/write_coords.py'
os.system('cp ' + dfile + ' ' + destination_path + 'hide/plugins/')
os.system('cp ' + dfile + ' ' + working_path + 'hide/plugins/')

dfile = 'files/fake_bingo_spectrometer.py'
os.system('cp ' + dfile + ' ' + destination_path + 'hide/spectrometer/')
os.system('cp ' + dfile + ' ' + working_path + 'hide/spectrometer/')

dfile = 'files/signal.py'
os.system('cp ' + dfile + ' ' + destination_path + 'hide/utils/')
os.system('cp ' + dfile + ' ' + working_path + 'hide/utils/')

dfile = 'files/sphere.py'
os.system('cp ' + dfile + ' ' + destination_path + 'hide/utils/')
os.system('cp ' + dfile + ' ' + working_path + 'hide/utils/')

# ==================================================================
# CREATING DIRECTORIES AROUND
# ==================================================================

directory = 'sky'
os.system('mkdir ' + working_path + 'hide/data/' + directory)

# ==================================================================
# SAVING THE TEST DATA
# ==================================================================

dfile = 'files/maps_foregrounds_test.fits'
os.system('cp ' + dfile + ' ' + working_path + 'hide/data/sky')

dfile = 'files/freqs_foregrounds_test.fits'
os.system('cp ' + dfile + ' ' + working_path + 'hide/data/sky')

