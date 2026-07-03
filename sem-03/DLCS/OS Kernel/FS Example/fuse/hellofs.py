#!/usr/bin/env python
from __future__ import print_function, absolute_import, division

import logging
import errno
import os
import stat
from fuse import FUSE, Operations, FuseOSError

class HelloFS(Operations):
    """
    A simple "Hello World" FUSE filesystem.
    It has one directory (/) and one file (hello.txt).
    """
    
    def __init__(self):
        self.hello_str = b'Hello, World!\n'
        self.hello_path = '/hello.txt'
        
        # Define attributes for our virtual file and directory
        self.file_attr = dict(
            st_mode=(stat.S_IFREG | 0o444), # Read-only file
            st_nlink=1,
            st_size=len(self.hello_str),
            st_ctime=0, st_mtime=0, st_atime=0,
            st_uid=os.getuid(),
            st_gid=os.getgid()
        )
        self.dir_attr = dict(
            st_mode=(stat.S_IFDIR | 0o755), # R/W/X for owner, R/X for others
            st_nlink=2, # . and ..
            st_uid=os.getuid(),
            st_gid=os.getgid()
        )

    def getattr(self, path, fh=None):
        """
        Called by the kernel to get file/dir attributes.
        (e.g., when you run `ls -l`)
        """
        if path == '/':
            return self.dir_attr
        
        if path == self.hello_path:
            return self.file_attr
        
        # If file not found
        raise FuseOSError(errno.ENOENT)

    def readdir(self, path, fh):
        """
        Called by the kernel to list directory contents.
        (e.g., when you run `ls`)
        """
        if path == '/':
            # . and .. are special entries for current/parent dir
            return ['.', '..', 'hello.txt']
        
        # No other directories exist
        raise FuseOSError(errno.ENOENT)

    def read(self, path, size, offset, fh):
        """
        Called by the kernel when a process reads from a file.
        (e.g., when you run `cat hello.txt`)
        """
        if path == self.hello_path:
            # Return the requested slice of our string
            return self.hello_str[offset:offset + size]
        
        # File not found
        raise FuseOSError(errno.ENOENT)

# --- Main function to mount the filesystem ---
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: {} <mountpoint>'.format(sys.argv[0]))
        sys.exit(1)

    # logging.basicConfig(level=logging.DEBUG)
    
    # Create the FUSE filesystem
    # foreground=True keeps it running in the terminal
    FUSE(HelloFS(), sys.argv[1], foreground=True)
