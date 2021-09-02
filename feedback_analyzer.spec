# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.building.build_main import *
import sys
import os

path = os.path.abspath(".")
kivymd_repo_path = path.split("demos")[0]
sys.path.insert(0, kivymd_repo_path)

from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Aniket thani\\Desktop\\Feedback Analysis on Cloud'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[kivymd_hooks_path],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,Tree('C:\\Users\\Aniket thani\\Desktop\\Feedback Analysis on Cloud\\'),
          a.binaries,
          a.zipfiles,
          a.datas,  
          *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='feedback_analyzer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
