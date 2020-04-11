# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['nt.py'],
             pathex=['C:\\Users\\Eter\\PycharmProjects\\GUI\\compilation\\notepad'],
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
          [],
          exclude_binaries=True,
          name='nt',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='c:\\Users\\Eter\\PycharmProjects\\GUI\\compilation\\notepad\\nt.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='nt')
