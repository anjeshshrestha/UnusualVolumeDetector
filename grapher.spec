# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['grapher.py'],
             pathex=['C:\\Users\\Home\\Documents\\GitHub\\UnusualVolumeDetector'],
             binaries=[],
             datas=[('C:\\Users\\Home\\Documents\\GitHub\\UnusualVolumeDetector\\matplotlib','matplotlib'), ('C:\\Users\\Home\\Documents\\GitHub\\UnusualVolumeDetector\\matplotlib-3.3.0.dist-info','matplotlib-3.3.0.dist-info')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='grapher',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
