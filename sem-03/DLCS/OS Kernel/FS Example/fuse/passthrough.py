#!/usr/bin/env python
from __future__ import print_function, absolute_import, division

import logging
import os
import sys
import errno
from fuse import FUSE, Operations, FuseOSError

class PassthroughFS(Operations):
    """
    A simple passthrough FUSE filesystem.
    It intercepts calls, logs them, and passes them to the underlying OS.
    """
    
    def __init__(self, root):
        self.root = root

    # --- Helper function ---

    def _full_path(self, partial):
        """Calculate the full path in the underlying filesystem."""
        if partial.startswith("/"):
            partial = partial[1:]
        path = os.path.join(self.root, partial)
        return path

    # --- Filesystem methods ---

    def getattr(self, path, fh=None):
        """
        Called for `ls -l` or any time file attributes are needed.
        """
        # 1. Custom Processing
        print(f"*** INTERCEPT [getattr]: {path}")

        # 2. Get the full path
        full_path = self._full_path(path)

        # 3. Passthrough to default
        try:
            st = os.lstat(full_path)
        except FileNotFoundError:
            raise FuseOSError(errno.ENOENT)

        # FUSE expects a dict, so we convert the os.stat_result
        keys = ('st_atime', 'st_ctime', 'st_gid', 'st_mode', 'st_mtime',
                'st_nlink', 'st_size', 'st_uid')
        return {key: getattr(st, key) for key in keys}

    def readdir(self, path, fh):
        """
        Called for `ls`.
        """
        # 1. Custom Processing
        print(f"*** INTERCEPT [readdir]: {path}")

        # 2. Get the full path
        full_path = self._full_path(path)

        # 3. Passthrough to default
        dirents = ['.', '..']
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        
        # 4. Return results
        for r in dirents:
            yield r

    def open(self, path, flags):
        """
        Called for `cat`, `nano`, etc.
        """
        # 1. Custom Processing
        print(f"*** INTERCEPT [open]: {path}")

        # 2. Get the full path
        full_path = self._full_path(path)

        # 3. Passthrough to default
        # This returns a file handle (an integer)
        return os.open(full_path, flags)

    def read(self, path, size, offset, fh):
        """
        Called when reading an open file.
        `fh` is the file handle returned by open().
        """
        # 1. Custom Processing
        print(f"*** INTERCEPT [read]: {path} (Size: {size}, Offset: {offset})")

        # 2. Passthrough to default
        # We use the file handle 'fh' directly
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, size)

    def release(self, path, fh):
        """
        Called when the file is closed.
        """
        # 1. Custom Processing
        print(f"*** INTERCEPT [release]: {path}")

        # 2. Passthrough to default
        return os.close(fh)
    
    # We should also implement:
    # write, truncate, mkdir, rmdir, etc.
    # but this is enough to show the concept.

# --- Main function to mount the filesystem ---
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {} <root_directory> <mountpoint>'.format(sys.argv[0]))
        sys.exit(1)
    
    root = sys.argv[1]       # The "default" directory to mirror
    mountpoint = sys.argv[2] # The new mount point
    
    # Create the FUSE object
    FUSE(PassthroughFS(root), mountpoint, foreground=True, nothreads=True)
