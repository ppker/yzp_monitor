# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['new_monitor.py'],
             pathex=['/usr/local/var/python_code/solo_work/yzp_monitor'],
             binaries=[],
             datas=[],
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
          name='晓夜',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='ui/soom.icns')
app = BUNDLE(exe,
             name='晓夜.app',
             icon='./ui/soom.icns',
             bundle_identifier=None)
