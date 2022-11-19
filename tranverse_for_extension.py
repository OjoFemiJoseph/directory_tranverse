import os,sys

def traverse_for_extension(path,ext):
    """_summary_

    Args:
        path (str): path to traverse
        ext (ext): extension to search for

    Returns:
        filenames_ending_with_ext (list) : list of files with extension
    """
    
    filenames_ending_with_ext = []
    
    for dir,subdir,list_of_subdir_filename in os.walk(path):
        
        for filename in list_of_subdir_filename:
            
            if filename.endswith(ext.replace('*', '')):
                full_path = os.path.join(dir,filename).replace(path, '.')
                filenames_ending_with_ext.append(full_path)
    return filenames_ending_with_ext


if __name__ == '__main__':
    traverse_for_extension(sys.argv[-1],sys.argv[-2])