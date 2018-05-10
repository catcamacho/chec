def extract_dicom_info(i,dicom, dicoms_info, volume_name):    
    from pydicom import dcmread
    from pandas import DataFrame
    from nipype import config, logging
    config.enable_debug_mode()
    logging.update_logging(config)
    
    info = dcmread(dicom)
    etl = info[0x18,0x91].value
    te = info[0x18,0x81].value
    fa = info[0x181314].value
    tr = info[0x18, 0x80].value
    pid = info[0x10, 0x20].value
    slice_thick = info[0x18, 0x50].value
    pixel_size = info[0x28, 0x30].value
    acq_matrix = info[0x181310].value
    slice_timing = info[0x191029].value
    acquisition_num = info[0x20, 0x12].value

    dicoms_info.loc[i] = [pid, etl, te, fa, tr, acquisition_num, 
                               slice_thick, pixel_size, acq_matrix, slice_timing, volume_name]
    return(dicoms_info)

def make_nifti(dicom, output_dir, volume_name):
    from pandas import DataFrame
    from os.path import basename
    import shutil
    from nipype.interfaces.freesurfer.preprocess import MRIConvert
    from nipype import config, logging
    config.enable_debug_mode()
    logging.update_logging(config)
    
    temp_path = output_dir + '/' + basename(dicom)
    
    shutil.move(dicom,temp_path)
    mrc = MRIConvert()
    mrc.inputs.in_file = temp_path
    mrc.inputs.out_file = volume_name
    mrc.run()
    shutil.move(temp_path, dicom)
    return()

from glob import glob
from pandas import DataFrame

dicoms_folder = '/home/camachocm2/Analysis/ChEC/fmri_proc/raw/pilot002/chec_movie_PA'
output_dir = '/home/camachocm2/Analysis/ChEC/fmri_proc/raw/pilot002/chec_sort'

files = glob(dicoms_folder + '/*')
files = sorted(files)
dicoms_info = DataFrame(columns = ['PatientID','EchoTrainLength','TE','FlipAngle','TR', 'AcqNumber',
                                   'SliceThickness','PixelSize','AcqMatrix','SliceTiming','VolumeName'])

for volnum in range(0, len(files)):
    volume_name = output_dir + '/vol' + str(volnum).zfill(5) + '.nii.gz'
    
    #dicom_info = extract_dicom_info(volnum, files[volnum], dicoms_info, volume_name)
    make_nifti(files[volnum], output_dir, volume_name)
    
