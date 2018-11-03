# -*- mode: python -*-

block_cipher = None


a = Analysis(['mqtt_to_p'],
             pathex=['C:\\Users\\liu\\Desktop\\IOT\\GITHUB\\First1\\B5data'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mqtt_to_p',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
