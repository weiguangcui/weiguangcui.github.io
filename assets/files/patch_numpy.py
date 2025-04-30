# Create a file named patch_numpy.py
def patch_numpy():
    import os
    import sys
    
    # Find the numpy distutils directory
    import numpy
    numpy_dir = os.path.dirname(numpy.__file__)
    distutils_dir = os.path.join(numpy_dir, 'distutils')
    
    # Path to the mingw32ccompiler.py file
    mingw_file = os.path.join(distutils_dir, 'mingw32ccompiler.py')
    
    # Read the content of the file
    with open(mingw_file, 'r') as f:
        content = f.read()
    
    # Modify the import statement to handle the case when msvccompiler is not available
    if 'from distutils.msvccompiler import get_build_version as get_build_msvc_version' in content:
        modified_content = content.replace(
            'from distutils.msvccompiler import get_build_version as get_build_msvc_version',
            'try:\n    from distutils.msvccompiler import get_build_version as get_build_msvc_version\nexcept ImportError:\n    def get_build_msvc_version(): return None'
        )
        
        # Write the modified content back to the file
        with open(mingw_file, 'w') as f:
            f.write(modified_content)
        
        print("Successfully patched numpy.distutils.mingw32ccompiler")
    else:
        print("Could not find the import statement to patch")

if __name__ == "__main__":
    patch_numpy()
